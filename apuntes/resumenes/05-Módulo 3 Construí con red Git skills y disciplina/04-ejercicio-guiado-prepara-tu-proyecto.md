---
titulo: "Ejercicio guiado: Prepará tu proyecto"
capitulo: "05-Módulo 3 Construí con red Git skills y disciplina"
orden: 4
leccion: "apuntes/slides/05-Módulo 3 Construí con red Git skills y disciplina/04-ejercicio-guiado-prepara-tu-proyecto.md"
---

# Ejercicio guiado: Prepará tu proyecto

## De qué trata

Primer ejercicio del módulo (~25 min). Nace el **hogar definitivo del proyecto**:
una carpeta **nueva**, repo Git desde el día cero, publicada en GitHub.

> ⚠️ **La v1 no se toca.** Queda de testigo de cómo se trabaja sin red. A la carpeta
> nueva viajan **solo tres archivos**: `PRD.md`, `AGENTS.md`, `CLAUDE.md`.
> **El código NO se copia** — la v2 se reconstruye desde el PRD. Los documentos
> (contrato + reglas) son lo que vale oro; el código sale mejor rehecho.

## Los siete pasos

| # | Paso | Comando |
|---|---|---|
| 1 | Carpeta nueva + copiar los tres archivos | — |
| 2 | Convertirla en repo | `git init` · `git branch -M main` |
| 3 | Primer save point (foto liviana, sin código) | `git add .` · `git commit -m "estado inicial: PRD + guardrails"` · verificar con `git log --oneline` |
| 4 | Alta en GitHub — **New repository**, mismo nombre, Private, **sin** README ni .gitignore | `git remote add origin <url>` · `git push -u origin main` |
| 5 | Editar una línea del PRD y mirar el diff antes de guardar | `git diff` → segundo commit |
| 6 | Romper `AGENTS.md` a propósito y apretar el botón de pánico | `git restore .` |
| 7 | **Dirigir, no tipear**: pedirle el commit + push a Claude Code | «Commiteá este cambio con un mensaje claro y pushealo a main.» |

La URL `https://github.com/<usuario>/<repo>` es **la entrega del módulo**, con la
app v2 adentro.

## ✅ Lo lograste cuando

- Repo con **≥ 2 commits** y **solo los tres archivos** (nada de código viejo).
- **Publicado en GitHub**: la URL abre y muestra los archivos.
- **Sentiste el alivio** de deshacer un desastre con `git restore`.
- El **agente** hizo un commit + push dirigido por vos, verificado en `git log` y
  en la nube.

## El ritmo que queda instalado

> **Funcionalidad lista → commit → push a `main`.** Vos dirigís, la IA ejecuta.

Ese es el ritmo del resto del curso. El punto: **el agente maneja los comandos, vos
entendés lo que pasa** — por eso los cinco comandos vinieron primero
([[02-git-para-builders-desde-cero]]) y la disciplina después
([[03-iterar-con-red-la-disciplina-del-builder]]).

**Atajo visual:** `code .` → pestaña de control de versiones: diffs coloreados e
historial clickeable. Mismo dato, sin terminal.

## El cierre

El proyecto queda con las cuatro piezas: **contrato** (`PRD.md`), **reglas**
(`AGENTS.md`), **red** (Git) y **espejo** (GitHub). Lo que falta es lo que más te
separa de un prompter: **skills** — capacidades que el agente invoca solo cuando
hacen falta. El primero va a empaquetar un workflow que ya hiciste a mano.
