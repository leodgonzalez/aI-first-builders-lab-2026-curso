---
titulo: "El flujo SDD de un vistazo"
capitulo: "06-Módulo 4 Spec Driven Development (SDD)"
orden: 6
source: "apuntes/slides/00-raw/06-Módulo 4 Spec Driven Development (SDD)/06-El flujo SDD de un vistazo – MUG.html"
source_sha256: bf4d44a180b19693
extraido: 2026-07-31
---

# El flujo SDD de un vistazo

Ya tenés el repo con Spec Kit listo y los comandos `/speckit.*` a mano. Antes de meternos fase por fase, quiero que veas **el mapa completo** —a dónde vamos y en qué orden—, porque entender el viaje entero hace que cada paso tenga sentido. Si arrancás a ciegas, comando por comando, sin saber para qué sirve el siguiente, el flujo se siente como una serie de trámites; si tenés el mapa, se siente como un camino con lógica. 🗺️

## 🛤️ Las ocho fases

El flujo de Spec Kit es una secuencia, y cada comando deja un **artefacto** —un archivo concreto, guardado en tu repo— que alimenta al siguiente. Nada se pierde en el aire de una conversación: todo queda escrito.

1. **`/speckit.constitution`** — escribís los **principios del proyecto**: las reglas que valen siempre, en toda feature que construyas de acá en adelante. Es lo primero porque después va a actuar como filtro de todo lo demás.
2. **`/speckit.specify`** — generás el **spec**: el qué y el porqué de lo que vas a construir, alimentado por tu PRD2. Todavía sin una palabra de tecnología.
3. **`/speckit.clarify`** — el agente te **interroga** sobre lo ambiguo y completa el spec con tus respuestas. Es la conversación que en vibecoding nunca tenías a tiempo.
4. **`/speckit.checklist`** — valida que el spec esté **completo y sin agujeros**, como un test unitario pero para el español que escribiste.
5. **`/speckit.plan`** — recién acá entra el **stack y las decisiones técnicas**: el cómo. Y acá el spec se contrasta contra la constitución, para asegurarse de que el cómo no viole ninguno de tus principios.
6. **`/speckit.tasks`** — descompone el plan en **tareas chicas y verificables**, cada una del tamaño justo para revisarla de un vistazo.
7. **`/speckit.analyze`** — chequea que **spec, plan y tareas sean consistentes** entre sí, antes de que se escriba una sola línea de código real.
8. **`/speckit.implement`** — el agente **construye** siguiendo las tareas, en orden, validando contra lo que el spec prometió.

> [!WARNING]
> **Nota de corrección (agregada al apunte, no está en la lección original).**
>
> Las fases 1-3 y 5-8 coinciden con la herramienta. **La fase 4 va a contramano:**
> `/speckit.checklist` es el único comando de validación que **exige `plan.md`**, así que
> corriéndolo antes del plan aborta. Los scripts de Spec Kit `0.12.4.dev0`:
>
> | Comando | Lo que invoca | Qué implica |
> |---|---|---|
> | `clarify` | `check-prerequisites.sh --json --paths-only` | No valida nada → corre sin plan. Fase 3 ✅ |
> | `checklist` | `check-prerequisites.sh --json` | Valida y **corta**: `ERROR: plan.md not found… Run /speckit-plan first` (`check-prerequisites.sh:127`) |
> | `tasks` | `setup-tasks.sh` | Mismo corte si falta `plan.md` → tasks va después de plan ✅ |
> | `analyze` | `check-prerequisites.sh --json --require-tasks --include-tasks` | Exige `tasks.md`. Fase 7 ✅ |
> | `implement` | ídem `analyze` | Fase 8 ✅ |
>
> **El flujo tal como lo espera la herramienta:**
>
> `constitution` → `specify` → `clarify` → **`plan`** → **`checklist`** → `tasks` → `analyze` → `implement`
>
> El README de `github/spec-kit` lo respalda: marca `clarify` como *«recommended before
> `/speckit.plan`»* y `analyze` como *«run after `/speckit.tasks`, before
> `/speckit.implement`»*, pero a `checklist` no le asigna posición fija — su lugar lo fija
> el script, que pide el plan.
>
> **Si querés seguir el orden de la lección** (validar el spec antes de planear, que
> conceptualmente tiene sentido: el checklist son «tests unitarios del español» y no
> necesita el stack), hay que forzarlo: correr el chequeo con `--paths-only` para saltear
> la validación. Funciona, pero estás usando el comando fuera de su camino previsto.
>
> **Aparte:** las fases son ocho en la lección, pero la herramienta tiene un noveno comando
> —`/speckit.converge`, después de `implement`— que el README describe como *«assess the
> codebase against spec/plan/tasks and append remaining work»*.

## 🧍 Dónde entrás vos

Acá está la clave que separa al SDD del «dale, construí todo»: **cada fase es un checkpoint tuyo.** El agente propone, vos revisás y aprobás antes de avanzar. No es que escribís un comando y volvés en una hora a ver qué salió: leés el spec antes de planear, leés el plan antes de generar tareas, leés las tareas antes de implementar. Dirigís en cada escalón, con la misma actitud crítica que ya practicaste en M2-M3 —la diferencia es que acá cada decisión queda anotada en un artefacto, no solo en tu cabeza—.

Y el flujo **no siempre es una línea recta**. Si en el plan descubrís que el spec estaba incompleto, volvés al spec y lo arreglás —ese loop de *validar → replanear* es sano, no un error—. Vas a ver también unos marcadores **`[NEEDS CLARIFICATION]`**: son las cosas que el agente detecta como ambiguas y deja señaladas para que las resuelvas (de eso se encarga `/speckit.clarify`). Mientras queden marcadores pendientes, el spec no está listo, y avanzar igual sería repetir el error del vibecoding sin método: construir sobre una suposición que nadie confirmó.

## 💡 Para aplicar

Mirá la lista de las ocho fases y ubicá mentalmente dónde está hoy tu proyecto: tenés el PRD2 (copiado de M3) y tu guardrail con el stack de siempre, así que estás parado justo antes de `/speckit.constitution`. Tener el mapa claro te va a evitar perderte cuando entremos en cada fase — cada vez que abras una lección nueva, volvé un segundo a esta lista y ubicate en ella.

Empecemos por la primera piedra del flujo: **la constitución del proyecto**. ➡️
