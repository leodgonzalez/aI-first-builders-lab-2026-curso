#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["beautifulsoup4", "lxml", "markdownify"]
# ///
"""Convierte las lecciones del curso (HTML guardado desde el navegador) a Markdown.

    uv run tools/slides2md.py                 convierte lo que cambió
    uv run tools/slides2md.py <ruta.html>     convierte solo esa lección
    uv run tools/slides2md.py <capítulo/>     convierte solo ese capítulo
    uv run tools/slides2md.py --force         regenera todo
    uv run tools/slides2md.py --check         muestra qué haría, sin escribir
    uv run tools/slides2md.py --audit         compara palabra por palabra origen vs .md

Pasar rutas nunca toca las demás lecciones: las que no se nombran quedan como están.

Entrada:  apuntes/slides/00-raw/<capítulo>/<NN-Título – MUG>.html
Salida:   apuntes/slides/<capítulo>/<NN-titulo-slug>.md
"""

import argparse
import hashlib
import json
import re
import shutil
import sys
import unicodedata
from datetime import date
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

RAW = Path("apuntes/slides/00-raw")
OUT = Path("apuntes/slides")

# La lección vive acá adentro; todo lo de afuera es header, sidebar y footer.
CONTENIDO = "div.llms-lesson-content"

# Chrome de LifterLMS/wpDiscuz que queda DENTRO del contenedor.
CHROME_SELECTORES = [
    '[class*="wpd-"]',          # widget de rating: wpd-not-rated si nadie votó, wpd-rating-wrap si sí
    ".llms-parent-course-link",  # "Volver al curso: ..."
    ".llms-favorite-wrapper",
    ".llms-lesson-button-wrapper",  # "Lección completada"
    "nav.llms-course-navigation",   # anterior/siguiente
    ".llms-focus-comments",         # hilo de comentarios + avatares
    ".clear",
]
CHROME_TAGS = ["script", "style", "noscript", "form", "button", "svg",
               "input", "select", "textarea", "label"]

# Si alguna de estas frases sobrevive, se nos coló chrome: falta un selector.
CHROME_FRASES = [
    "Valora la Publicación", "Volver al curso", "Lección completada",
    "Marcar la lección", "Suscribirse", "Cerrar sesión", "Lección siguiente",
    "Lección anterior", "Has iniciado sesión",
]


def slugify(texto: str) -> str:
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    t = re.sub(r"[^\w\s-]", " ", t).strip().lower()
    return re.sub(r"[\s_-]+", "-", t).strip("-")


class Conversor(MarkdownConverter):
    """Markdownify con las particularidades de este curso."""

    def convert_img(self, el, text, parent_tags=None):
        # WordPress sirve los emoji como <img>; los devolvemos a carácter.
        if "emoji" in (el.get("class") or []):
            return el.get("alt", "")
        return super().convert_img(el, text, parent_tags)


def limpiar(container, html_path: Path, assets_dir: Path, escribir: bool, titulo: str):
    """Saca el chrome, arregla emoji/videos y baja las imágenes reales a assets/."""
    for sel in CHROME_SELECTORES:
        for el in container.select(sel):
            el.decompose()

    # Algunas lecciones repiten el título como <h1>; el nuestro sale del <title>.
    for h1 in container.find_all("h1"):
        if slugify(h1.get_text(" ")) == slugify(titulo):
            h1.decompose()

    # Los videos quedaron como iframe a un archivo local; el ID de Vimeo es el nombre.
    for wrap in container.select(".llms-video-wrapper"):
        iframe = wrap.find("iframe")
        vid = Path(iframe.get("src", "")).stem if iframe else ""
        nuevo = BeautifulSoup("", "lxml").new_tag("p")
        if vid.isdigit():
            nuevo.string = f"[Video de la lección](https://vimeo.com/{vid})"
        else:
            nuevo.string = "[Video de la lección]"
        wrap.replace_with(nuevo)

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
            destino = assets_dir / origen.name
            if escribir:
                assets_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(origen, destino)
            im["src"] = f"assets/{origen.name}"
            imagenes.append(origen.name)
        elif origen and (assets_dir / origen.name).exists():
            # La carpeta <lección>_files se borró (pesa ~4 MB y es basura del
            # navegador), pero la captura ya vive en assets/ de una corrida previa.
            # Sin esto, un --force dejaría el link apuntando al _files inexistente.
            im["src"] = f"assets/{origen.name}"
            imagenes.append(origen.name)
    return imagenes


def palabras(texto: str) -> list[str]:
    return re.findall(r"[0-9A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+", texto.lower())


def procesar(html_path: Path, args) -> dict:
    raw_html = html_path.read_text(encoding="utf-8", errors="replace")
    sha = hashlib.sha256(raw_html.encode("utf-8", "replace")).hexdigest()[:16]

    soup = BeautifulSoup(raw_html, "lxml")
    container = soup.select_one(CONTENIDO)
    if container is None:
        return {"file": html_path.name, "estado": "SIN CONTENEDOR"}

    titulo = (soup.title.string or "").strip() if soup.title else html_path.stem
    titulo = re.sub(r"\s*[–-]\s*MUG\s*$", "", titulo).strip()

    capitulo = html_path.parent.name
    m = re.match(r"(\d+)", html_path.stem)
    orden = int(m.group(1)) if m else 0
    destino_dir = OUT / capitulo
    md_path = destino_dir / f"{orden:02d}-{slugify(titulo)}.md"

    if md_path.exists() and not args.force:
        previo = md_path.read_text(encoding="utf-8")
        if f"source_sha256: {sha}" in previo:
            return {"file": md_path.name, "estado": "sin cambios"}

    escribir = not args.check
    imgs = limpiar(container, html_path, destino_dir / "assets", escribir, titulo)

    cuerpo = Conversor(
        heading_style="ATX",
        bullets="-",
        escape_asterisks=False,
        escape_underscores=False,
        escape_misc=False,
        code_language="",
    ).convert_soup(container)
    cuerpo = re.sub(r"\n{3,}", "\n\n", cuerpo).strip()

    extraido = date.fromtimestamp(html_path.stat().st_mtime).isoformat()
    fm = "\n".join([
        "---",
        f"titulo: {json.dumps(titulo, ensure_ascii=False)}",
        f"capitulo: {json.dumps(capitulo, ensure_ascii=False)}",
        f"orden: {orden}",
        f"source: {json.dumps(str(html_path).replace(chr(92), '/'), ensure_ascii=False)}",
        f"source_sha256: {sha}",
        f"extraido: {extraido}",
        "---",
    ])
    doc = f"{fm}\n\n# {titulo}\n\n{cuerpo}\n"

    # Auditoría: ninguna palabra del original debería faltar en el .md...
    origen_w = palabras(container.get_text(" "))
    salida_w = set(palabras(doc))
    faltan = [w for w in origen_w if w not in salida_w]
    # ...y nada de la plataforma debería sobrar.
    chrome = [f for f in CHROME_FRASES if f in doc]

    if escribir:
        destino_dir.mkdir(parents=True, exist_ok=True)
        md_path.write_text(doc, encoding="utf-8")

    return {
        "file": md_path.name,
        "estado": "convertido" if escribir else "convertiría",
        "palabras": len(origen_w),
        "faltan": faltan,
        "chrome": chrome,
        "imgs": imgs,
        "md": md_path,
    }


def resolver(rutas: list[str]) -> list[Path]:
    """Convierte lo que se pasó por línea de comandos en una lista de .html de 00-raw."""
    fuentes, errores = [], []
    for r in rutas:
        # Windows: las rutas copiadas del explorador vienen con backslash.
        p = Path(r.replace("\\", "/"))
        if not p.exists():
            # Puede venir relativa al capítulo o sin el prefijo apuntes/slides/00-raw.
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

    # Todo tiene que colgar de 00-raw: el capítulo se deduce del nombre de la carpeta.
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
    ap = argparse.ArgumentParser(description="Lecciones HTML del curso -> Markdown")
    ap.add_argument("rutas", nargs="*", metavar="RUTA",
                    help="lección .html o capítulo a convertir (default: todo 00-raw)")
    ap.add_argument("--force", action="store_true", help="regenera aunque no haya cambios")
    ap.add_argument("--check", action="store_true", help="no escribe nada")
    ap.add_argument("--audit", action="store_true", help="detalla palabras perdidas")
    args = ap.parse_args()

    if not RAW.is_dir():
        sys.exit(f"No encuentro {RAW} — corré esto desde la raíz del proyecto.")

    if args.rutas:
        fuentes = resolver(args.rutas)
    else:
        # Solo los .html sueltos del capítulo; lo de <lección>_files/ es basura del navegador.
        fuentes = sorted(p for p in RAW.glob("*/*.html") if not p.parent.name.endswith("_files"))
        if not fuentes:
            sys.exit(f"No hay .html en {RAW}/<capítulo>/")

    problemas = 0
    for f in fuentes:
        r = procesar(f, args)
        est = r["estado"]
        if est == "sin cambios":
            print(f"  ·  {r['file']}")
            continue
        if est == "SIN CONTENEDOR":
            print(f"  ✗  {r['file']}  — no encontré {CONTENIDO}")
            problemas += 1
            continue
        faltan, chrome = r["faltan"], r["chrome"]
        marca = "✓" if not faltan and not chrome else "⚠"
        extra = f"  [{len(r['imgs'])} img]" if r["imgs"] else ""
        avisos = []
        if faltan:
            avisos.append(f"{len(faltan)} palabras perdidas")
        if chrome:
            avisos.append(f"chrome sin filtrar: {', '.join(chrome)}")
        aviso = f"  — {' · '.join(avisos)}" if avisos else ""
        print(f"  {marca}  {r['file']}  ({r['palabras']} palabras){extra}{aviso}")
        if faltan or chrome:
            problemas += 1
            if args.audit and faltan:
                print(f"       perdidas: {faltan[:25]}")

    print(f"\n{len(fuentes)} lecciones · {problemas} con observaciones")


if __name__ == "__main__":
    main()
