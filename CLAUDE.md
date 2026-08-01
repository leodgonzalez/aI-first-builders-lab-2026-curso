# AI-First Builders Lab 2026

Repo personal de Leonardo Gonzalez para cursar el **AI-First Builders Lab 2026** (MUG, el
Microsoft User Group de Argentina). Junta los apuntes del curso y los proyectos que se
construyen a lo largo de los módulos.

No es un producto: es material de estudio más código de práctica. El curso enseña a
construir software dirigiendo agentes de IA — PRD, guardrails, vibecoding, spec-driven
development, orquestación de agentes.

## Para qué es este repo (leer esto primero)

**El objetivo es estudiar.** Lo que se espera de vos, en orden de importancia:

1. **Ayudar a entender el material** — explicar lecciones, responder dudas, conectar
   conceptos entre módulos, tomar examen si hace falta.
2. **Hacer resúmenes reutilizables** — que sirvan para repasar y para consultar mucho
   después de que el curso termine. Ese material que queda es el producto real de este repo.
3. **Acompañar los proyectos** de cada módulo (`src/`), aplicando lo que el curso enseña.

**La importación de las lecciones es importante pero secundaria**: es la infraestructura que
hace posible lo de arriba, no el fin. Ya está resuelta y automatizada (`tools/slides2md.py`
+ skill `slides-a-md`) justamente para que no consuma tiempo ni tokens. Si el usuario pide
convertir lecciones nuevas, corré la tool y volvé a lo importante.

### Los resúmenes

Van en `apuntes/resumenes/<capítulo>/<mismo-nombre-que-la-lección>.md`, con un campo
`leccion:` en el frontmatter que apunta a la fuente. **Nunca dentro de `apuntes/slides/`**:
eso es salida de la tool y la próxima corrida con `--force` lo pisa.

Apuntá a que sirvan **dentro de un año, sin el curso a mano**: esquemáticos, con los
conceptos y el porqué, no transcripciones. El material fuente ya está completo en
`apuntes/slides/` — el resumen agrega valor solo si **destila**. Estructura que viene
funcionando: de qué trata (la tesis en una línea) → los puntos en tabla → la receta o
regla accionable → el cierre.

## Estructura

| Carpeta | Qué hay |
|---|---|
| `apuntes/slides/00-raw/` | **Fuente inmutable.** Las lecciones tal como se guardan del navegador (`.html`), una carpeta por capítulo. No se edita a mano. |
| `apuntes/slides/<capítulo>/` | Las mismas lecciones en Markdown, **generadas** por la tool. No se editan a mano: se regeneran. |
| `apuntes/resumenes/<capítulo>/` | **Los resúmenes de estudio.** Escritos a mano, mismo nombre que la lección que resumen. Esto es lo que queda del curso: acá sí se edita. |
| `apuntes/prompts.md` | Prompts del curso que vale la pena guardar. |
| `tools/slides2md.py` | Convierte las lecciones de HTML a Markdown. |
| `src/modulo-N/` | Los proyectos que se van construyendo en cada módulo. |
| `resource-management/`, `seguimiento-tareas/` | PRDs y redacción de los proyectos propios. |

Los capítulos van numerados (`01-`, `02-`, …) para que ordenen igual que el curso. Los
nombres de capítulo replican los del curso, con acentos y todo; los archivos `.md` usan slug
limpio.

## Los apuntes se generan, no se escriben

`apuntes/slides/` es **salida de una tool**, no contenido a mano. Cuando se liberan lecciones
nuevas del curso, el flujo es: el usuario las guarda como `.html` en `00-raw/` desde su
navegador (el curso es privado, con login), y después:

```bash
uv run tools/slides2md.py
```

Está la skill **`slides-a-md`** con el detalle completo: cómo capturar en Edge, cómo correr
la tool, cómo verificar y qué hacer si la plataforma cambia el DOM. **Usala en vez de
convertir HTML a mano** — transcribir a ojo es lento, caro y sale peor.

Dos cosas aprendidas a la mala, que conviene no repetir:

- **Nada de PDFs.** El primer intento fue imprimir las lecciones a PDF. La plataforma
  renderiza la lección en un contenedor con scroll, así que el PDF captura solo el primer
  viewport: se perdía el 87% del texto. Si aparece un `.pdf` en `00-raw/`, está truncado.
- **La plataforma es WordPress + LifterLMS.** La lección entera vive en
  `div.llms-lesson-content`. Todo lo demás de la página es chrome.

## Convenciones

- Todo en **español rioplatense** (voseo), igual que el curso.
- Las tools son Python + `uv` con dependencias inline (PEP 723): se corren con
  `uv run <script>` desde la raíz, sin venv ni `pip install`.
- Los PRDs siguen el template del curso (RF/RNF/AC trazables por ID) — está la skill
  `create-prd`.
- Cuando el usuario pide **un prompt** para llevarse a otro chat («haceme un prompt para…»),
  lo que quiere es el texto listo para copiar, no que resuelvas vos el pedido. Ojo con ese
  reflejo.
