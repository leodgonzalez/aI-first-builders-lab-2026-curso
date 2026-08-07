#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["beautifulsoup4", "lxml", "markdownify"]
# ///
"""Convierte las calificaciones del curso (HTML guardado) a Markdown.

    uv run tools/calificaciones2md.py                 convierte lo que cambió
    uv run tools/calificaciones2md.py <ruta.html>     convierte solo esa
    uv run tools/calificaciones2md.py --force         regenera todo
    uv run tools/calificaciones2md.py --check         muestra qué haría, sin escribir
    uv run tools/calificaciones2md.py --audit         compara palabra por palabra origen vs .md

Entrada:  calificaciones/00-raw/<lo que sea>.html
Salida:   calificaciones/m<N>-entrega-<titulo-slug>.md
          calificaciones/m<N>-quiz-intento-<K>.md

Hay dos tipos de página y la tool los distingue sola por su contenido:

- ENTREGA (assignment)  lo que importa es la NOTA y la DEVOLUCIÓN del instructor.
- QUIZ                  lo que importa es la NOTA, qué preguntas se erraron y en qué intento.

Nada sale del nombre del archivo: el módulo, el tipo y el número de intento se deducen del
HTML, así que 00-raw puede quedar tal como lo escupe el navegador.
"""

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import unicodedata
from collections import defaultdict
from datetime import date
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

RAW = Path("calificaciones/00-raw")
OUT = Path("calificaciones")
SLIDES = Path("apuntes/slides")  # donde viven los enunciados
SRC = Path("../src")             # los proyectos de cada módulo, hermanos de curso/

# La página vive acá adentro; el resto es header, sidebar y footer.
CONTENIDO = "div.llms-lesson-content"
# Lo que decide de qué tipo de página se trata.
ENTREGA = "section.llms-assignment-content"    # el essay que se entregó
QUIZ = "div.llms-quiz-results"                 # el intento corregido
RESULTADOS = "section.llms-assignment-submission-results"  # existe si ya la corrigieron
REMARKS = "div.llms-assignment-remarks"                    # el feedback del instructor

# Chrome de LifterLMS que queda DENTRO del contenedor.
CHROME_SELECTORES = [
    '[class*="wpd-"]',                  # widget de rating
    ".llms-return",                     # "Return to Lesson"
    ".llms-assignment-footer",          # "Next Lesson"
    ".llms-assignments-results-title",  # "Grade & Instructor Remarks", ya va al frontmatter
    ".llms-quiz-buttons",               # "Volver al curso" / "Reintentar"
    ".llms-parent-course-link",
    ".llms-favorite-wrapper",
    ".llms-focus-comments",
    ".clear",
]
CHROME_TAGS = ["script", "style", "noscript", "form", "button", "svg",
               "input", "select", "textarea", "label"]

# Si alguna de estas frases sobrevive, se nos coló chrome: falta un selector.
CHROME_FRASES = [
    "Return to Lesson", "Next Lesson", "Grade & Instructor Remarks",
    "Valora la Publicación", "Volver al curso", "Suscribirse", "Cerrar sesión",
    "Reintentar el examen",
]

MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
         "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


def slugify(texto: str) -> str:
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    t = re.sub(r"[^\w\s-]", " ", t).strip().lower()
    return re.sub(r"[\s_-]+", "-", t).strip("-")


def palabras(texto: str) -> list[str]:
    return re.findall(r"[0-9A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+", texto.lower())


def yaml(v):
    return json.dumps(v, ensure_ascii=False) if v else "null"


def numero(txt: str) -> str:
    """El donut trae 80 o 93.33; que no quede el .0 de más."""
    f = float(txt)
    return str(int(f)) if f == int(f) else str(f)


class Conversor(MarkdownConverter):
    """Markdownify con las particularidades de este curso."""

    def convert_img(self, el, text, parent_tags=None):
        # WordPress sirve los emoji como <img>; los devolvemos a carácter.
        if "emoji" in (el.get("class") or []):
            return el.get("alt", "")
        return super().convert_img(el, text, parent_tags)


def a_markdown(nodo) -> str:
    if nodo is None:
        return ""
    md = Conversor(
        heading_style="ATX",
        bullets="-",
        escape_asterisks=False,
        escape_underscores=False,
        escape_misc=False,
        code_language="",
    ).convert_soup(nodo)
    return re.sub(r"\n{3,}", "\n\n", md).strip()


def buscar_enunciado(titulo: str) -> str | None:
    """El enunciado de cada entregable (y cada quiz) es la lección homónima."""
    objetivo = slugify(titulo)
    hallados = [p for p in sorted(SLIDES.glob("*/*.md"))
                if re.sub(r"^\d+-", "", p.stem) == objetivo]
    return str(hallados[0]).replace("\\", "/") if len(hallados) == 1 else None


def deducir_modulo(titulo: str, enunciado: str | None, html_path: Path) -> int:
    """Del capítulo del enunciado ('05-Módulo 3 …'), o del título, o del nombre del archivo."""
    for candidato in (enunciado or "", titulo, html_path.stem):
        m = re.search(r"módulo\s*(\d+)", candidato, re.I)
        if m:
            return int(m.group(1))
    m = re.match(r"M(\d+)", html_path.stem, re.I)
    return int(m.group(1)) if m else 0


def repo_entregado(texto: str) -> str | None:
    """Casi todas las entregas son la URL de un repo público de GitHub."""
    m = re.search(r"https?://github\.com/[\w.-]+/[\w.-]+", texto)
    return re.sub(r"\.git$", "", m.group(0).rstrip(".,);")) if m else None


def repo_normalizado(url: str) -> str:
    """owner/repo en minúsculas, venga como URL https o como remote SSH."""
    u = re.sub(r"\.git$", "", url.strip())
    m = re.search(r"[:/]([\w.-]+/[\w.-]+)$", u)
    return m.group(1).lower() if m else u.lower()


def proyecto_local(modulo: int) -> tuple[str | None, str | None]:
    """La ruta del proyecto de ese módulo y el remote de su repo, si existen."""
    d = SRC / f"modulo-{modulo}"
    if not d.is_dir():
        return None, None
    remote = None
    try:
        p = subprocess.run(["git", "-C", str(d), "remote", "get-url", "origin"],
                           capture_output=True, text=True, timeout=15)
        if p.returncode == 0:
            remote = p.stdout.strip() or None
    except (OSError, subprocess.SubprocessError):
        pass
    return str(d).replace("\\", "/"), remote


def limpiar(container, html_path: Path, assets_dir: Path, escribir: bool):
    """Saca el chrome y baja las imágenes reales a assets/."""
    for sel in CHROME_SELECTORES:
        for el in container.select(sel):
            el.decompose()
    for tag in CHROME_TAGS:
        for el in container.find_all(tag):
            el.decompose()

    imagenes = []
    for im in container.find_all("img"):
        clases = im.get("class") or []
        if "emoji" in clases:
            continue
        if any(c.startswith("avatar") for c in clases):
            im.decompose()
            continue
        src = im.get("src", "")
        origen = (html_path.parent / src).resolve() if not src.startswith("http") else None
        if origen and origen.exists():
            if escribir:
                assets_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(origen, assets_dir / origen.name)
            im["src"] = f"assets/{origen.name}"
            imagenes.append(origen.name)
        elif origen and (assets_dir / origen.name).exists():
            # La carpeta <página>_files ya se borró, pero la captura sigue en assets/.
            im["src"] = f"assets/{origen.name}"
            imagenes.append(origen.name)
    return imagenes


# ---------------------------------------------------------------- entregas


def armar_entrega(container, titulo: str, html_path: Path) -> dict:
    """Assignment corregido: nota, devolución del instructor y lo que se entregó."""
    nota, resultado = None, None
    res = container.select_one(RESULTADOS)
    if res is not None:
        donut = res.select_one("[data-perc]")
        if donut is not None:
            nota = numero(donut["data-perc"])
            # El caption de las entregas viene en inglés ("Pass") y el de los quizzes en
            # español: se lee la clase en los dos, así el dataset queda homogéneo.
            clases = " ".join(donut.get("class") or [])
            resultado = "Aprobado" if "pass" in clases else "Fallado" if "fail" in clases else None

    nodo_remarks = container.select_one(REMARKS)
    nodo_entrega = container.select_one(ENTREGA)
    # La consigna son los <p> sueltos que la plataforma deja como hijos directos.
    nodos_consigna = [p for p in container.find_all("p", recursive=False) if p.get_text(strip=True)]

    consigna = " ".join(a_markdown(p) for p in nodos_consigna).strip().strip("'\"“”").strip()
    remarks_md, entrega_md = a_markdown(nodo_remarks), a_markdown(nodo_entrega)

    enunciado = buscar_enunciado(titulo)
    modulo = deducir_modulo(titulo, enunciado, html_path)
    repo = repo_entregado(entrega_md)
    proyecto, remote = proyecto_local(modulo)
    # Si lo entregado y lo que hay local no son el mismo repo, alguno de los dos miente.
    desalineado = bool(repo and remote and repo_normalizado(repo) != repo_normalizado(remote))

    campos = [
        "tipo: entrega",
        f"titulo: {json.dumps(titulo, ensure_ascii=False)}",
        f"modulo: {modulo}",
        f"nota: {nota if nota is not None else 'null'}",
        f"resultado: {yaml(resultado)}",
        f"enunciado: {yaml(enunciado)}",
        f"repo: {yaml(repo)}",
        f"proyecto: {yaml(proyecto)}",
        f"consigna: {json.dumps(consigna, ensure_ascii=False)}",
    ]
    partes = [f"# {titulo}"]
    if nota is not None:
        partes.append(f"**Nota: {nota}%**" + (f" — {resultado}" if resultado else ""))
    if remarks_md:
        partes.append(f"## Devolución del instructor\n\n{remarks_md}")
    if entrega_md:
        partes.append(f"## Lo entregado\n\n{entrega_md}")

    auditar = [*nodos_consigna, nodo_remarks, nodo_entrega]
    return {
        "nombre": f"m{modulo}-entrega-{slugify(titulo)}.md",
        "campos": campos, "partes": partes, "auditar": auditar,
        "nota": nota, "resultado": resultado, "enunciado": enunciado,
        "proyecto": proyecto, "desalineado": desalineado, "modulo": modulo,
        "extra_avisos": [], "detalle": None,
    }


# ------------------------------------------------------------------- quiz


def segundos(txt: str) -> int | None:
    """'11 minutos, 51 segundos' -> 711. Sirve para comparar intentos."""
    total, visto = 0, False
    for cant, unidad in re.findall(r"(\d+)\s*(hora|minuto|segundo)", txt, re.I):
        total += int(cant) * {"hora": 3600, "minuto": 60, "segundo": 1}[unidad.lower()]
        visto = True
    return total if visto else None


def fecha_iso(txt: str) -> str | None:
    """'5 de julio de 2026 11:28' -> '2026-07-05 11:28'."""
    m = re.search(r"(\d{1,2})\s+de\s+(\w+)\s+de\s+(\d{4})(?:\s+(\d{1,2}:\d{2}))?", txt, re.I)
    if not m:
        return None
    dia, mes, anio, hora = m.groups()
    mes = unicodedata.normalize("NFKD", mes.lower()).encode("ascii", "ignore").decode()
    if mes not in MESES:
        return None
    iso = f"{anio}-{MESES.index(mes) + 1:02d}-{int(dia):02d}"
    return f"{iso} {hora}" if hora else iso


def armar_quiz(container, titulo: str, html_path: Path) -> dict:
    """Intento de quiz corregido: nota, tiempo y qué se erró."""
    quiz = container.select_one(QUIZ)
    titulo = re.sub(r"^Quiz\s*[—–-]\s*", "", titulo).strip()  # "Quiz — Quiz Módulo 1"

    h2 = quiz.select_one(".llms-quiz-results-title")
    m = re.search(r"#\s*(\d+)", h2.get_text(" ", strip=True) if h2 else "")
    intento = int(m.group(1)) if m else 1

    donut = quiz.select_one("[data-perc]")
    nota = numero(donut["data-perc"]) if donut else None
    clases = " ".join(donut.get("class") or []) if donut else ""
    # El texto del donut es "Fallar" (mala traducción de LifterLMS); vamos por la clase.
    resultado = "Aprobado" if "passing" in clases else "Fallado" if "failing" in clases else None

    meta = {}
    nodos_meta = quiz.select("li.llms-quiz-meta-item")
    for li in nodos_meta:
        t = li.get_text(" ", strip=True)
        if ":" in t:
            k, v = t.split(":", 1)
            meta[slugify(k)] = v.strip()
    correctas = total = None
    if (mc := re.search(r"(\d+)\s*/\s*(\d+)", meta.get("respuestas-correctas", ""))):
        correctas, total = int(mc.group(1)), int(mc.group(2))
    fecha = fecha_iso(meta.get("completado", ""))
    tiempo = meta.get("tiempo-total")

    preguntas, erradas, lineas = quiz.select("li.llms-quiz-attempt-question"), [], []
    auditar_q = []
    for i, q in enumerate(preguntas, 1):
        cl = q.get("class") or []
        ok = "correct" in cl and "incorrect" not in cl
        if not ok:
            erradas.append(i)
        nodo_titulo = q.select_one(".llms-question-title")
        if nodo_titulo is not None:
            # Viene como <h3>: si lo convertimos tal cual, mete otro "###" adentro del nuestro.
            nodo_titulo.name = "span"
        enunciado_q = a_markdown(nodo_titulo) or "(sin enunciado)"
        header = q.select_one(".llms-quiz-attempt-question-header")
        pts = re.search(r"(\d+)\s*/\s*(\d+)\s*punto", header.get_text(" ", strip=True) if header else "")
        # Las de opción traen <li> por opción elegida, pero las de completar (type--blank)
        # traen la oración entera con la respuesta adentro: hay que tomar la sección completa.
        sec = q.select_one(".llms-quiz-attempt-answer-section.llms-student-answer")
        if sec is not None:
            for lbl in sec.select("p.llms-quiz-results-label"):
                lbl.decompose()  # "Respuesta seleccionada": lo decimos nosotros
        respuesta = a_markdown(sec)
        # A las preguntas borradas por el profe LifterLMS las cuenta como incorrectas.
        borrada = "type--deleted" in cl
        auditar_q += [n for n in (nodo_titulo, sec) if n is not None]

        lineas.append(f"### {i}. {'✓' if ok else '✗'} {enunciado_q}")
        detalle = []
        if pts:
            detalle.append(f"{pts.group(1)}/{pts.group(2)} punto" + ("s" if pts.group(2) != "1" else ""))
        if borrada:
            detalle.append("pregunta borrada por el instructor")
        if detalle:
            lineas.append(f"*{' · '.join(detalle)}*")
        if respuesta:
            # Las listas necesitan su propia línea; una respuesta de una sola frase no.
            lineas.append(f"Respondí:\n\n{respuesta}" if respuesta.lstrip().startswith("-")
                          else f"Respondí: {respuesta}")

    enunciado = buscar_enunciado(titulo)
    modulo = deducir_modulo(titulo, enunciado, html_path)

    campos = [
        "tipo: quiz",
        f"titulo: {json.dumps(titulo, ensure_ascii=False)}",
        f"modulo: {modulo}",
        f"intento: {intento}",
        f"nota: {nota if nota is not None else 'null'}",
        f"resultado: {yaml(resultado)}",
        f"correctas: {correctas if correctas is not None else 'null'}",
        f"preguntas: {total if total is not None else len(preguntas)}",
        f"erradas: [{', '.join(str(e) for e in erradas)}]",
        f"fecha: {yaml(fecha)}",
        f"tiempo: {yaml(tiempo)}",
        f"tiempo_segundos: {segundos(tiempo or '') or 'null'}",
        f"enunciado: {yaml(enunciado)}",
    ]
    resumen = [f"**Nota: {nota}%**" + (f" — {resultado}" if resultado else "")]
    if correctas is not None:
        resumen.append(f"{correctas}/{total} correctas")
    if tiempo:
        resumen.append(tiempo)
    partes = [
        f"# {titulo} — intento {intento}",
        " · ".join(resumen),
        "## Preguntas\n\n" + "\n\n".join(lineas),
    ]
    # La meta no se audita palabra por palabra porque va normalizada al frontmatter
    # (fecha ISO, segundos); lo que sí se chequea es que se haya podido parsear.
    sin_parsear = [n for n, v in [("respuestas correctas", correctas),
                                  ("fecha", fecha), ("tiempo", tiempo)] if v is None]
    return {
        "nombre": f"m{modulo}-quiz-intento-{intento}.md",
        "campos": campos, "partes": partes, "auditar": auditar_q,
        "nota": nota, "resultado": resultado, "enunciado": enunciado,
        "proyecto": None, "desalineado": False, "modulo": modulo,
        "extra_avisos": [f"no pude leer del quiz: {', '.join(sin_parsear)}"] if sin_parsear else [],
        "detalle": f"intento {intento} · {len(erradas)} errada" + ("s" if len(erradas) != 1 else ""),
    }


# --------------------------------------------------------------- el motor


def procesar(html_path: Path, args) -> dict:
    raw_html = html_path.read_text(encoding="utf-8", errors="replace")
    sha = hashlib.sha256(raw_html.encode("utf-8", "replace")).hexdigest()[:16]

    soup = BeautifulSoup(raw_html, "lxml")
    container = soup.select_one(CONTENIDO)
    if container is None:
        return {"file": html_path.name, "estado": "SIN CONTENEDOR"}

    es_quiz = container.select_one(QUIZ) is not None
    if not es_quiz and container.select_one(ENTREGA) is None:
        # Es la página de la lección, no la de la entrega: se guardó la URL equivocada.
        return {"file": html_path.name, "estado": "NO ES UNA CALIFICACIÓN"}

    titulo = (soup.title.string or "").strip() if soup.title else html_path.stem
    titulo = re.sub(r"\s*[–-]\s*MUG\s*$", "", titulo).strip()
    titulo = re.sub(r"\s+Assignment$", "", titulo).strip()

    escribir = not args.check
    limpiar(container, html_path, OUT / "assets", escribir)
    d = armar_quiz(container, titulo, html_path) if es_quiz \
        else armar_entrega(container, titulo, html_path)

    md_path = OUT / d["nombre"]
    if md_path.exists() and not args.force:
        if f"source_sha256: {sha}" in md_path.read_text(encoding="utf-8"):
            return {"file": md_path.name, "estado": "sin cambios", "md": md_path}

    extraido = date.fromtimestamp(html_path.stat().st_mtime).isoformat()
    fm = "\n".join(["---", *d["campos"],
                    f"source: {json.dumps(str(html_path).replace(chr(92), '/'), ensure_ascii=False)}",
                    f"source_sha256: {sha}",
                    f"extraido: {extraido}",
                    "---"])
    doc = "\n\n".join([fm, *d["partes"]]) + "\n"

    # Auditoría: ninguna palabra de las partes útiles debería faltar en el .md...
    origen_w = palabras(" ".join(n.get_text(" ") for n in d["auditar"] if n is not None))
    salida_w = set(palabras(doc))
    faltan = [w for w in origen_w if w not in salida_w]
    # ...y nada de la plataforma debería sobrar.
    chrome = [f for f in CHROME_FRASES if f in doc]

    if escribir:
        OUT.mkdir(parents=True, exist_ok=True)
        md_path.write_text(doc, encoding="utf-8")

    return {**d, "file": md_path.name, "md": md_path,
            "estado": "convertido" if escribir else "convertiría",
            "palabras": len(origen_w), "faltan": faltan, "chrome": chrome,
            "tipo": "quiz" if es_quiz else "entrega"}


def resolver(rutas: list[str]) -> list[Path]:
    fuentes, errores = [], []
    for r in rutas:
        p = Path(r.replace("\\", "/"))  # Windows: las rutas del explorador vienen con backslash
        if not p.exists():
            for base in (RAW, OUT, Path(".")):
                if (base / p).exists():
                    p = base / p
                    break
        if not p.exists():
            errores.append(f"no existe: {r}")
            continue
        if p.is_dir():
            hallados = sorted(q for q in p.glob("*.html") if not q.parent.name.endswith("_files"))
            if not hallados:
                errores.append(f"no hay .html en: {p}")
            fuentes += hallados
            continue
        if p.suffix.lower() != ".html":
            errores.append(f"no es un .html: {p}")
            continue
        fuentes.append(p)

    dentro = []
    for f in fuentes:
        try:
            f.resolve().relative_to(RAW.resolve())
        except ValueError:
            errores.append(f"fuera de {RAW}: {f}")
            continue
        dentro.append(f)

    if errores:
        sys.exit("\n".join(f"  ✗  {e}" for e in errores))
    return sorted(set(dentro))


def main():
    ap = argparse.ArgumentParser(description="Calificaciones del curso -> Markdown")
    ap.add_argument("rutas", nargs="*", metavar="RUTA",
                    help="entrega o quiz .html a convertir (default: todo 00-raw)")
    ap.add_argument("--force", action="store_true", help="regenera aunque no haya cambios")
    ap.add_argument("--check", action="store_true", help="no escribe nada")
    ap.add_argument("--audit", action="store_true", help="detalla palabras perdidas")
    args = ap.parse_args()

    if not RAW.is_dir():
        sys.exit(f"No encuentro {RAW} — corré esto desde la raíz del proyecto.")

    if args.rutas:
        fuentes = resolver(args.rutas)
    else:
        fuentes = sorted(p for p in RAW.glob("*.html") if not p.parent.name.endswith("_files"))
        if not fuentes:
            sys.exit(f"No hay .html en {RAW}/")

    problemas = 0
    destinos = defaultdict(list)
    for f in fuentes:
        r = procesar(f, args)
        est = r["estado"]
        if "md" in r:
            destinos[r["md"]].append(f.name)
        if est == "sin cambios":
            print(f"  ·  {r['file']}")
            continue
        if est == "SIN CONTENEDOR":
            print(f"  ✗  {r['file']}  — no encontré {CONTENIDO}")
            problemas += 1
            continue
        if est == "NO ES UNA CALIFICACIÓN":
            print(f"  ✗  {r['file']}  — no tiene ni entrega ni quiz corregido: "
                  f"se guardó la lección, no la calificación")
            problemas += 1
            continue

        avisos = []
        if r["faltan"]:
            avisos.append(f"{len(r['faltan'])} palabras perdidas")
        if r["chrome"]:
            avisos.append(f"chrome sin filtrar: {', '.join(r['chrome'])}")
        if r["nota"] is None:
            avisos.append("sin corregir todavía")
        if r["enunciado"] is None:
            avisos.append("no encontré el enunciado en apuntes/slides")
        if r["desalineado"]:
            avisos.append(f"el repo entregado no es el remote de {r['proyecto']}")
        avisos += r["extra_avisos"]
        marca = "✓" if not avisos else "⚠"
        nota = f"  [{r['nota']}% {r['resultado']}]" if r["nota"] is not None else ""
        det = f"  {r['detalle']}" if r["detalle"] else ""
        aviso = f"  — {' · '.join(avisos)}" if avisos else ""
        print(f"  {marca}  {r['file']}  ({r['palabras']} palabras){nota}{det}{aviso}")
        if avisos:
            problemas += 1
            if args.audit and r["faltan"]:
                print(f"       perdidas: {r['faltan'][:25]}")

    # Dos fuentes que escriben el mismo .md se pisan en silencio: hay que avisar.
    for md, orig in destinos.items():
        if len(orig) > 1:
            print(f"  ✗  {md.name}  — lo escriben {len(orig)} fuentes: {', '.join(orig)}")
            problemas += 1

    print(f"\n{len(fuentes)} calificaciones · {problemas} con observaciones")


if __name__ == "__main__":
    main()
