---
titulo: "Resumen y conclusiones del Módulo 2"
capitulo: "04-Módulo 2 Vibecoding profesional"
orden: 10
leccion: "apuntes/slides/04-Módulo 2 Vibecoding profesional/10-resumen-y-conclusiones-del-modulo-2.md"
---

# Resumen y conclusiones del Módulo 2

## De qué trata

El módulo donde se pasa de la teoría a **construir**. La tesis: **vibecodear es dirigir, no
pedir.** El que dirige mantiene el control aunque no escriba una línea; el que pide, delega
el criterio.

Y una decisión de diseño del curso que conviene entender: **este módulo se construye sin
red, a propósito.** El dolor de no poder volver atrás es lo que motiva el Módulo 3.

## Los puntos

| Tema | La clave |
|---|---|
| **Qué es vibecoding** | Dirigir a la IA hacia un **resultado completo** e iterar, no juntar snippets. Builder = dirige y juzga; prompter = pide y reza. La diferencia no es la herramienta. |
| **Cuándo sirve** | Brilla en prototipos y MVPs. Para producción no se descarta: se le suma rigor. |
| **Anatomía del prompt** | Contexto + objetivo + especificidad + restricciones + ejemplos. Todas son **decisiones de producto**, no sintaxis — por eso no hace falta saber programar. |
| **Dos familias de prompts** | Los que le escribís al agente, y los que viven **dentro de tu app** y corren miles de veces sin nadie mirando. Misma anatomía; en la segunda, la precisión pesa más. |
| **El ciclo** | Prompt → Generate → **Review** → Refine, en loop. El review es donde entra tu criterio: sacarlo es dejar de dirigir. |
| **Context engineering** | El corazón del módulo. La ventana es **todo lo que el agente sabe**: lo que no está, no existe. Cinco palancas — **selección**, compresión, ordenamiento, aislamiento, formato — y la selección es la que más rinde. |
| **Guardrails** | Un solo archivo: `AGENTS.md` (+ `CLAUDE.md` que lo importa con `@AGENTS.md`). Define el comportamiento **permanente**. ~300 líneas tope, solo lo no-inferible, sin reglas de estilo (eso es del linter). Se itera contra el comportamiento real. |
| **Arsenal de prompting** | Las 10 técnicas portables a cualquier IA, y **Plan Mode** (`Shift+Tab`) como el «proponé antes de ejecutar» convertido en garantía. Ver [[09-prompting-profesional-tu-arsenal-para-cualquier-ia]]. |

## Los ejercicios y qué probaron

| Ejercicio | Lo que quedó |
|---|---|
| **Guardrails del proyecto** | Carpeta + `PRD.md` de M1 + guardrails. La prueba de fuego: en una conversación **limpia**, el agente cita tus reglas sin que le pases nada. Si no las cita, no existen. |
| **Vibecodear el PRD** | En loop —auditar contra checklist → **juzgar vos** → reescribir → reauditar— el PRD de M1 se vuelve **PRD v2**: verificable y defendible línea por línea. La actitud: la IA propone, vos exigís rigor. |
| **App v1 (sin red)** | La feature core corriendo. Plan en palabras **aprobado antes de la primera línea**, pasos chicos, probar cada paso. |

**Entregable doble:** PRD v2 + app v1 corriendo.

## La regla accionable

> **Plan aprobado antes de la primera línea. Pasos chicos. Probar cada paso. Y el review nunca se saltea.**

Y la que sostiene todo lo demás: **si no está en la ventana, no existe.** Antes de culpar al
modelo por una respuesta floja, revisá qué le faltaba ver.

## El cierre

M2 enseña a **dirigir**: pedir con precisión, diseñar lo que el agente ve, fijar reglas
permanentes, convertir un PRD en software real. Eso ya es vibecodear con método.

Lo que falta es la **red**. En M3 la app se reconstruye en una carpeta nueva que nace como
repo Git, con disciplina de iteración y los primeros skills. El PRD y los guardrails viajan;
el código de la v1 se queda donde está.

## Nota propia

La lista de «dónde dolió» al construir sin red no es un ejercicio de catarsis: es la
**materia prima explícita del Módulo 3**. Si no la anotaste mientras dolía, M3 llega como
teoría en vez de como alivio.
