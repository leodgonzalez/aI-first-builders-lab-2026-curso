---
titulo: "Escribir guardrails efectivos"
capitulo: "04-Módulo 2 Vibecoding profesional"
orden: 5
source: "apuntes/slides/00-raw/04-Módulo 2 Vibecoding profesional/05-Escribir guardrails efectivos – MUG.html"
source_sha256: 971dda84430ff32f
extraido: 2026-07-16
---

# Escribir guardrails efectivos

En el Módulo 1 vimos los guardrails **en concepto**: qué son los archivos de contexto, por qué el agente los lee siempre, la regla de oro de documentar solo lo no-inferible. Bien, llegó la hora de pasar de la teoría a la tinta. En esta lección vas a aprender a **escribir uno bueno de verdad** —qué lleva, qué NO, cómo se afila— porque apenas termines, **en la lección que sigue**, vas a escribir el de **tu** proyecto y no un ejemplo de juguete. ✍️

## 🧱 Qué lleva el guardrail de un builder individual

Un buen archivo de contexto para tu proyecto no es una plantilla rellenada: es un retrato útil de lo que el agente necesita saber para no equivocarse. Pensalo como el papelito que le dejarías a alguien que arranca a laburar en tu repo mañana a la mañana y no tiene a quién preguntarle. En general cubre estos bloques:

- **Propósito** — qué es esto, en dos líneas. Que el agente entienda de entrada de qué va el proyecto antes de tocar una sola línea.
- **Stack** — las versiones que realmente importan. No listes todo lo que tenés instalado; solo lo que cambia cómo se escribe el código (esa versión de framework que rompe compatibilidad, ese runtime específico).
- **Estructura** — dónde vive cada cosa, pero solo si no es obvia. Si tu layout es el estándar del framework, no lo repitas; si tenés una carpeta rara con una convención propia, ahí sí vale la pena.
- **Cómo correr** — los comandos exactos de build, tests y entorno de desarrollo. Escritos tal cual se tipean, no descritos «más o menos».
- **Qué sí y qué no** — las convenciones y prohibiciones propias del proyecto: eso que en tu equipo se da por sentado pero que un recién llegado (o un agente) no tiene forma de saber.

Pero la lista es lo de menos. La clave, la que de verdad hace la diferencia, es la que ya conocés de M1 y que repito porque es *el* criterio: escribí únicamente **lo que el agente no puede adivinar mirando el código**. El nombre del framework lo deduce solo leyendo un `import`; el comando raro de build con el que arrancás los tests, no. Ahí está el valor: en la información que no está escrita en ningún lado más que en tu cabeza.

## 📏 El nivel de detalle correcto (donde casi todos la pifian)

El error más común con los guardrails es contraintuitivo: no es escribir poco, es escribir **de más**. La gente arma archivos enormes pensando que «más instrucciones = mejor agente», y consigue exactamente lo contrario: un archivo gordo y genérico **empeora** el resultado, porque llena el contexto de ruido y le hace perder foco. Es la misma lógica de una reunión donde alguien habla veinte minutos para decir algo que entraba en una frase: cuanto más texto irrelevante metés, más difícil es que lo importante se escuche.

Dos reglas para no caer en eso:

- **Mantenelo corto.** Apuntá a menos de 300 líneas, e idealmente mucho menos. Cada línea que agregás compite por la atención del agente con todas las demás; si algo no se está ganando el lugar, sacalo.
- **No metas reglas de estilo** —indentación, comillas, dónde va la llave—. Eso es trabajo del **linter**, una herramienta determinista, instantánea y gratis. Ponerle esas reglas a un LLM es malgastar contexto (caro y lento) en algo que un `prettier` resuelve sin pensar y sin margen de error. Dejá que cada herramienta haga lo que hace bien.

Un guardrail gordo y genérico es ruido; uno corto y específico es oro puro.

## 🗂️ Un archivo, dos roles (y cómo lo lee cada herramienta)

Acá conviene despejar una confusión común: tu guardrail vive en **un solo archivo**, no en varios. Ese archivo cumple dos roles a la vez, y ayuda tenerlos separados en la cabeza:

- **Cómo comportarse** (lo que sí): el contexto positivo del proyecto, el «así trabajamos acá».
- **Qué NO hacer** (lo que no): las prohibiciones duras, el «esto no se toca».

Los dos van en el **mismo archivo**, como dos secciones. ¿Y cómo se llama ese archivo? Usá **`AGENTS.md`**: es el estándar que entienden todas las herramientas (lo viste en M1). Como en el curso trabajás con **Claude Code**, que lee `CLAUDE.md`, el truco para no duplicar es tener un `CLAUDE.md` de una sola línea que **importe** al otro: `@AGENTS.md`. Una sola fuente de verdad, y todos los agentes leen exactamente lo mismo.

> ⚠️ **Ojo con la trampa de «muchos archivos».** Podés, si querés, separar las prohibiciones en un `GUARDRAILS.md` aparte. Pero cuidado: **el agente no lee solo un archivo con ese nombre** —solo lee su archivo de contexto (`AGENTS.md` / `CLAUDE.md`)—. Para que un `GUARDRAILS.md` tenga efecto, tenés que **importarlo** igual (`@GUARDRAILS.md`) desde el principal. Por eso, para empezar, **un archivo alcanza y sobra**: no te compliques con dos.

## 🔁 El secreto: el mejor guardrail se itera, no se adivina

Acá va el cambio de enfoque que más te va a servir: **no intentes escribir el guardrail perfecto de una sentada.** Es imposible, y perseguirlo es perder el tiempo —no podés anticipar todas las formas en que el agente va a interpretar (o malinterpretar) tu proyecto—. El método de los que saben es otro, y es casi un ciclo de observación:

- Empezás con una versión mínima, apenas lo esencial.
- Después **mirás cómo se comporta el agente de verdad** trabajando: no en teoría, en tareas reales de tu app.
- ¿Hizo algo que no querías —usó una librería que no va, ignoró una convención—? Agregás una línea al guardrail que lo corrija.
- Y repetís.

La regla práctica que lo resume: cada vez que te encontrás corrigiendo al agente **dos veces por lo mismo**, esa corrección va al archivo. La primera vez puede ser un descuido; la segunda ya es un patrón, y los patrones se documentan. Así el guardrail crece a partir del comportamiento real, no de tus suposiciones, y termina siendo exactamente lo que tu proyecto necesita, ni más ni menos.

### 🔎 La muestra: el `AGENTS.md` de TicketTriage

Para que no arranques de cero, te muestro cómo quedó este mismo entregable en **TicketTriage**, la app de ejemplo que vamos construyendo a lo largo del curso (una mesa de ayuda donde la IA clasifica tickets y sugiere respuestas). Usalo de molde —y si te trabás con el tuyo, volvé acá a ver la forma—:

```
# TicketTriage
Mesa de ayuda donde la IA clasifica tickets (categoría + prioridad) y redacta un borrador de respuesta apoyado en la KB (kb.md).

## Stack
- Python 3.12 + FastAPI · SQLite · API de Claude (claude-sonnet-4-6)
- Front mínimo con HTMX. Deps con uv.

## Cómo correr
- Instalar deps: `uv sync`
- Levantar en dev: `uvicorn app.main:app --reload`
- Tests: `pytest -q`

## Qué NO hacer
- El borrador NUNCA afirma algo que no esté en `kb.md`: si no está, deriva a un humano (no inventa).
- NO hardcodear la API key: va en `.env` como ANTHROPIC_API_KEY.
- NO llamar a la API de Claude desde los tests: usar el mock de `tests/fakes.py`.
- NO agregar features fuera del PRD (CRUD de tickets + clasificación + borrador de respuesta).
```

Fijate qué tiene y qué no: es corto (entra en una pantalla) y solo dice **lo que el agente no puede adivinar** —los comandos exactos, que los tests no toquen la API real, las tres prohibiciones concretas del proyecto—. No hay reglas de estilo ni obviedades: nada de «usá 4 espacios de indentación» o «el código va en `app/`«, porque eso el agente ya lo ve. Ese es el nivel al que apuntás con el tuyo.

Y al lado de ese `AGENTS.md`, en la raíz del repo, un `CLAUDE.md` de **una sola línea** —`@AGENTS.md`— para que Claude Code lo lea. Una fuente de verdad, cero copias que se contradigan.

## 🚧 Un deslinde para que no mezcles capas

Antes de cerrar, dos fronteras importantes.

- **El uso agéntico profundo va después.** Combinar estos archivos con skills, hooks, subagents, MCP y comandos custom es territorio de los módulos 4 a 6. Acá escribís el guardrail base, que ya es muchísimo: es el cimiento sobre el que todo eso se apoya después.
- **La spec del Módulo 3 no es un guardrail.** Esta confunde a mucha gente, así que fijate bien: son capas distintas. El guardrail dice *cómo se comporta el agente siempre*, en cualquier tarea; la spec dice *qué construir esta vez*, para un trabajo puntual. Uno es permanente y transversal, la otra es específica y descartable. Tenerlas separadas en la cabeza te va a ahorrar varios enredos más adelante.

Ya sabés qué lleva un guardrail bueno, qué le sobra y cómo se afila. Ahora nada de quedarse en la teoría: **en la próxima lección nace tu proyecto** —creás su carpeta, le ponés adentro el PRD que escribiste en M1 y le escribís sus guardrails (`AGENTS.md` + `CLAUDE.md`)—. Manos a la obra. ➡️
