---
name: slides-a-md
description: Convierte las lecciones del curso AI-First Builders Lab de HTML guardado a Markdown, respetando la estructura de capítulos. Úsalo cuando el usuario libere/agregue lecciones nuevas, mencione "pasar las slides a md", "convertir las lecciones", "actualizar los apuntes del curso", o cuando aparezcan .html nuevos en apuntes/slides/00-raw/.
---

# Convertir las lecciones del curso a Markdown

La conversión la hace una tool determinística. **No conviertas HTML a mano ni leas los .html
para transcribirlos**: es lento, gasta tokens y sale peor. Tu trabajo es correr la tool,
leer su auditoría y arreglar la tool si algo falla.

## Cómo funciona

```
apuntes/slides/00-raw/<capítulo>/<NN-Título – MUG>.html   ← fuente, no se edita a mano
                    ↓  uv run tools/slides2md.py
apuntes/slides/<capítulo>/<NN-titulo-slug>.md              ← salida, no se edita a mano
```

Cada `.md` se regenera desde su `.html`. Si editás un `.md` a mano, la próxima corrida con
`--force` te lo pisa. Lo que hay que arreglar es la tool o el HTML de origen.

## Uso

```bash
uv run tools/slides2md.py           # convierte solo lo que cambió (por hash del origen)
uv run tools/slides2md.py --check   # muestra qué haría, sin escribir
uv run tools/slides2md.py --force   # regenera todo
uv run tools/slides2md.py --audit   # detalla las palabras perdidas, si hubiera

# Una lección puntual, cuando el usuario pasa la ruta (lo demás queda intacto):
uv run tools/slides2md.py "apuntes/slides/00-raw/<capítulo>/<NN-Título – MUG>.html"
uv run tools/slides2md.py "<capítulo>"   # o el capítulo entero
```

La ruta acepta backslashes de Windows y formas cortas (relativa a `00-raw`, o al capítulo).
Tiene que colgar de `00-raw/`: el capítulo se deduce del nombre de la carpeta contenedora.

Se corre **desde la raíz del proyecto**. `uv` resuelve las dependencias solo (están
declaradas inline en el script, PEP 723): no hay venv que activar ni `pip install`.

Salida esperada: una línea por lección y `34 lecciones · 0 con observaciones`.

- `✓` convertida y auditada
- `·` sin cambios desde la última corrida
- `⚠` **bug de la tool, arreglalo** (ver más abajo). Son dos chequeos distintos:
  - *N palabras perdidas* → se cayó contenido real
  - *chrome sin filtrar* → se coló texto de la plataforma
- `✗` no apareció el contenedor `div.llms-lesson-content` → la plataforma cambió el DOM

## Cómo se capturan las lecciones nuevas

Las hace el usuario a mano, desde su navegador logueado (el curso es privado; no se puede
scrapear sin sesión). Los pasos, en Edge:

1. Abrir la lección y **scrollear hasta el final** (si no, lo que carga en diferido no se guarda).
2. `Ctrl + S`.
3. Guardar en `apuntes/slides/00-raw/<capítulo>/`, con el número de orden adelante: `04-Guardrails I`.
4. En el desplegable **Tipo**, elegir **"Página web, solo HTML"**.

Detalle importante: si elige **"Página web, completa"** queda una carpeta `<lección>_files`
de ~4 MB al lado. La tool la ignora, pero conviene borrarlas después de convertir:

```bash
find apuntes/slides/00-raw -type d -name '*_files' -exec rm -rf {} +
```

Ojo: si la lección tiene **capturas de pantalla**, esas viven dentro de `_files`. Corré la
tool ANTES de borrarlas — se copian solas a `<capítulo>/assets/`. Verificá antes de borrar:

```bash
for f in apuntes/slides/*/*.md; do d=$(dirname "$f")
  for i in $(grep -ho 'assets/[^)]*' "$f"); do [ -f "$d/$i" ] || echo "FALTA: $d/$i"; done
done
```

**No usar PDF.** Se probó: al imprimir, la plataforma renderiza la lección dentro de un
contenedor con scroll y el PDF captura solo el primer viewport. Se pierde ~87% del texto y
no hay forma de recuperarlo. Si aparecen `.pdf` en `00-raw/`, están truncados: ignoralos.

## Cómo está hecha la tool

`tools/slides2md.py`. La plataforma es **WordPress + LifterLMS** (tema Astra, comentarios
wpDiscuz), así que el HTML es semántico y la conversión es directa:

1. Toma `div.llms-lesson-content` — ahí vive la lección y nada más (sin header, sidebar ni footer).
2. Descarta el chrome que quedó adentro: rating, "Volver al curso", favoritos, botón de
   lección completada, navegación anterior/siguiente y el hilo de comentarios.
3. Los emoji vienen como `<img class="emoji">`; los devuelve a carácter leyendo el `alt`.
4. Los avatares se tiran; las capturas reales se copian a `<capítulo>/assets/`.
5. Los videos son un iframe cuyo nombre de archivo es el ID de Vimeo → queda un link.
6. Convierte con `markdownify` y escribe frontmatter con `source_sha256` (de ahí sale el
   "sin cambios" de la próxima corrida).

**El filtro es por lista negra, a propósito.** Solo algunas lecciones usan clases
`wp-block-*`; la mayoría tiene `<p>` y `<h2>` pelados. Si filtráramos por lista blanca, un
bloque nuevo se perdería en silencio. Sacamos el chrome que conocemos y conservamos el resto.

## Si algo falla

**`⚠ N palabras perdidas`** — la auditoría compara palabra por palabra el original contra el
`.md`. Si marca pérdidas, hay contenido cayéndose. Corré `--audit` para ver cuáles, buscalas
en el `.html` y fijate qué elemento las contiene: casi seguro un selector de `CHROME_SELECTORES`
o de `CHROME_TAGS` se está comiendo contenido real. Nunca "arregles" el `.md` a mano.

**`✗ no encontré div.llms-lesson-content`** — la plataforma cambió el DOM o el archivo no es
una lección. Verificá el contenedor real:

```bash
uv run --quiet --with beautifulsoup4 --with lxml python -c "
from bs4 import BeautifulSoup
s = BeautifulSoup(open('RUTA.html', encoding='utf-8', errors='replace').read(), 'lxml')
for t in s(['script','style']): t.decompose()
for el in s.find_all(['div','main','article']):
    tx = el.get_text(strip=True)
    if 1000 < len(tx) < 20000: print(el.name, el.get('class'), len(tx))
"
```

**`⚠ chrome sin filtrar`** — se coló texto de la plataforma. Buscá la frase en el `.html`,
mirá qué clase tiene el elemento que la contiene y agregá el selector a `CHROME_SELECTORES`.
Ojo con las variantes: el widget de rating es `wpd-not-rated` si nadie votó pero
`wpd-rating-wrap` si tiene votos — por eso el selector es `[class*="wpd-"]` y no la clase
exacta. Si aparece una frase de chrome nueva, sumala también a `CHROME_FRASES` para que el
chequeo la agarre sola la próxima vez.

## Cómo verificar una conversión

Después de convertir, mirá una lección con contenido variado (tabla, código, imagen). Se
espera: un solo `# ` de título, tablas como tablas Markdown, código en fences, emoji como
caracteres, cero rastros de la plataforma.

```bash
# H1 reales (fuera de bloques de código): debe dar 1 por lección
uv run --quiet python -c "
import pathlib, re
for f in sorted(pathlib.Path('apuntes/slides').glob('*/*.md')):
    fuera = re.sub(r'\`\`\`.*?\`\`\`', '', f.read_text(encoding='utf-8'), flags=re.S)
    n = len(re.findall(r'^# ', fuera, flags=re.M))
    if n != 1: print(f'{n} → {f.name}')
"
```
