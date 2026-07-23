---
titulo: "Git para builders (desde cero)"
capitulo: "05-Módulo 3 Construí con red Git skills y disciplina"
orden: 2
leccion: "apuntes/slides/05-Módulo 3 Construí con red Git skills y disciplina/02-git-para-builders-desde-cero.md"
---

# Git para builders (desde cero)

## De qué trata

Git explicado como **save points de videojuego**: fotos del proyecto a las que siempre
podés volver. La tesis: cuando dirigís a una IA, el control de versiones deja de ser
higiene profesional y pasa a ser **imprescindible** — la IA va a romper algo, y la
diferencia entre un susto de treinta segundos y una tarde perdida es tener red abajo.

El curso enseña **cinco comandos**, no cien. Lo que importa es la idea, no el arsenal.

## Los tres nombres

| Nombre | Qué es |
|---|---|
| **Repositorio (repo)** | Tu carpeta de proyecto, **pero con memoria**. Git recuerda toda su historia desde el día uno. |
| **Commit** | Un **punto guardado**: foto del proyecto + mensaje que explica qué había ahí. |
| **GitHub** | La **copia en la nube**. Respaldo + lugar para compartir. Git vive en tu máquina; GitHub, en internet. |

## Los cinco comandos

| Comando | Para qué | Cuándo |
|---|---|---|
| `git init` | La carpeta pasa a ser repo | **Una sola vez**, al principio |
| `git add .` + `git commit -m "..."` | El **save point** (van siempre juntos) | Cada vez que algo funciona |
| `git diff` / `git status` | Ver **qué cambió** desde el último commit | Antes de guardar, siempre |
| `git restore .` | **Cargar la partida**: descarta cambios y vuelve al último commit | Cuando la IA rompe algo |
| `git push` | Sube los commits a GitHub | Después de cada commit |

> ⚠️ `git restore .` solo actúa sobre archivos **ya versionados**. Lo que nunca entró a un
> commit no tiene a dónde volver.

## La receta

> **Funcionalidad lista → `commit` → `push` directo a `main`.**

Ese es el ritmo de todo el módulo. Sin ramas, sin PRs: el proyecto es tuyo y la simplicidad
gana. Y la regla que lo sostiene: **nunca guardes a ciegas** — `git diff` antes del commit.

## Lo que hace builder a esto

**El agente maneja Git por vos.** Le decís «commiteá esto con un mensaje claro» o «volvé al
último commit que funcionaba» y lo hace. Pero necesitás **entender qué está pasando** para
dirigirlo bien y saber cuándo pedírselo. Entender Git es lo que te deja *dirigir* el proceso
en vez de rezar — el mismo principio de [[../04-Módulo 2 Vibecoding profesional/10-resumen-y-conclusiones-del-modulo-2]].

**Atajo visual:** `code .` (literal: `code`, espacio, punto — «la carpeta actual») abre el
proyecto en VS Code. La pestaña de control de versiones muestra el `git diff` en verde y
rojo, clickeable, con botón de commit. No reemplaza entender los comandos; los vuelve
fáciles de *ver*.

## El detalle que no es casual

El primer commit del repo es **liviano a propósito**: solo `PRD.md`, `AGENTS.md` y
`CLAUDE.md`, ni una línea de código. La carpeta es **nueva** — la app se reconstruye ahí
adentro, y cada paso de la v2 nace ya versionado. Eso es exactamente lo que la v1 nunca tuvo.

## El cierre

Los comandos ya están. Lo que falta es el **método** con el que un builder los usa mientras
dirige a la IA: **iterar con red** (lección siguiente). Después llega *Prepará tu proyecto*,
donde esto se aplica sobre el repo propio — y la entrega del módulo es la **URL de tu repo**.
