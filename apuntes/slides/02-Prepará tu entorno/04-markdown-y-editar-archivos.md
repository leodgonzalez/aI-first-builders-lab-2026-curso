---
titulo: "Markdown y editar archivos"
capitulo: "02-Prepará tu entorno"
orden: 4
source: "apuntes/slides/00-raw/02-Prepará tu entorno/04-Markdown y editar archivos – MUG.html"
source_sha256: 096fdb363ece9420
extraido: 2026-07-16
---

# Markdown y editar archivos

Ya tenés la terminal y las herramientas instaladas. Antes de seguir con los agentes, paremos un segundo en algo que vas a usar **en cada lección del curso** y que casi nadie te explica: **cómo se escribe y se edita un archivo de texto** —y por qué muchos de ellos terminan en `.md`—. Si venís del mundo dev, esto te va a sonar obvio; si no, esta lección es la que te saca el «¿y esto cómo lo abro?» de encima. No hay nada que instalar: usamos el **VS Code** que ya pusiste. 📝

## 🤔 ¿Qué es Markdown?

**Markdown** es una forma de escribir texto con formato usando solo **el teclado y unos pocos símbolos** —sin botones, sin barras de herramientas—. La idea es simple: escribís texto normal y, cuando querés un título o una negrita, ponés un símbolo que lo indica.

¿Por qué se usa tanto? Porque es **texto plano**: se abre en cualquier lado, no depende de ningún programa caro, pesa nada y se lleva bien con el control de versiones (Git). Por eso el mundo del software lo adoptó para todo lo que es documentación: los `CLAUDE.md`, los specs, los README de los proyectos… **todos son Markdown**. Los archivos Markdown terminan en **`.md`**.

## 🔤 Los símbolos que vas a usar (son poquitos)

No necesitás aprenderlos todos. Con estos cinco te alcanza para el 95% de lo que vas a escribir en el curso:

| Querés… | Escribís… | Se ve… |
| --- | --- | --- |
| Título principal | `# Mi título` | un título grande |
| Subtítulo | `## Mi subtítulo` | un título más chico |
| Sub-subtítulo | `### …` | más chico todavía |
| Negrita | `importante` | **importante** |
| Lista | `- primer ítem` (uno por línea) | viñetas |

La clave de los `#`: **marcan la jerarquía de los títulos**. Uno solo (`#`) es el título de más arriba; cada `#` que agregás lo hace un nivel más profundo (`##`, `###`). Es la forma de darle estructura a un documento sin tocar el mouse. Y los  **van** pegados** al texto que querés en negrita, uno antes y otro después.

> 💡 Hay más símbolos (links, tablas, citas, bloques de código), pero no te hacen falta para arrancar. Los vas a ir reconociendo solos a medida que los veas en las lecciones.

## 💻 Editar un archivo en VS Code

VS Code es el **editor de texto** donde vas a escribir y modificar archivos durante el curso. Veamos cómo abrir uno. La diferencia importante es si estás en Windows (con WSL) o no:

- 🍎 **Mac** / 🐧 **Linux:** abrí VS Code normalmente (en Mac, `Cmd+Espacio` → *Visual Studio Code*). Listo.
- 🪟 **Windows con WSL:** acá hay un paso que confunde a todos, así que prestá atención. Tu código vive **adentro de Ubuntu (WSL)**, no en Windows, y VS Code tiene que **conectarse ahí**:

1. Abrí VS Code una vez e instalá la extensión **WSL** (ícono de extensiones a la izquierda → buscá `WSL` → *Install*). Se hace una sola vez.
2. De ahí en más, lo más cómodo es abrir VS Code **desde la terminal de Ubuntu**: parate en la carpeta donde estés y escribí:

```
code .
```

(Ese punto significa «la carpeta actual».) La primera vez instala un componente solo; después VS Code abre **ya conectado a WSL** —lo ves abajo a la izquierda, en verde, dice *WSL: Ubuntu*—.

> ⚠️ **Por qué importa:** si en Windows abrís tus archivos de WSL «a mano» desde el explorador en vez de con `code .`, te vas a marear con rutas raras y permisos. Regla simple: **en WSL, abrí siempre con `code .` desde la terminal de Ubuntu.**

## 🛠️ Probémoslo (2 minutos)

Nada como hacerlo una vez. Desde tu terminal, creá un archivo de prueba y abrilo:

```
echo "# Hola Builder" > prueba.md
code prueba.md
```

En VS Code, debajo del título escribí un par de líneas usando lo que viste —un `## subtítulo`, una palabra en `negrita`, una `- lista`—. Para **ver cómo queda renderizado** (con los títulos en grande y las negritas aplicadas), abrí la **vista previa**:

- Apretá `Ctrl+Shift+V` (en Mac, `Cmd+Shift+V`), o tocá el ícono de lupa/preview arriba a la derecha.

Vas a ver tu texto plano transformado en un documento con formato. **Eso** es Markdown: lo escribís simple, se ve prolijo.

> ✅ **Lo lograste cuando** creaste un `.md`, le pusiste un título y una negrita, y los viste aplicados en la vista previa.

## 🧭 ¿Y si no quiero saber nada de esto?

Tranquilo. Para varios entregables del curso (como el PRD del Módulo 1) **el formato es libre**: si te sentís más cómodo, podés usar **Google Docs o Word** con sus títulos y negritas de siempre. Markdown no es obligatorio en *todo*.

Pero sí conviene perderle el miedo, porque hay archivos que **sí o sí** son Markdown —el `CLAUDE.md` que guía a tu agente, los specs, la documentación del repo— y los vas a tocar desde el Módulo 2. Con lo de esta lección ya estás listo para todos.

## 🆘 Si algo no sale

- En **WSL**, si `code .` no hace nada: cerrá y reabrí la terminal de Ubuntu (a veces el comando se «activa» recién ahí) y probá de nuevo.
- Si no aparece la vista previa, revisá que el archivo termine en **`.md`** (VS Code reconoce Markdown por la extensión).
- Cualquier error, **pegalo en los comentarios de esta lección** contando en qué paso estabas. 🙌

Con esto ya sabés leer y escribir los archivos del curso. Ahora sí, vamos a instalar el primero de los agentes: **Claude Code**. 🤖
