---
titulo: "Guardrails I: Archivos de contexto"
capitulo: "03-Módulo 1 AI-First Development mindset y PRD del proyecto"
orden: 4
source: "apuntes/slides/00-raw/03-Módulo 1 AI-First Development mindset y PRD del proyecto/04-Guardrails I_ Archivos de contexto – MUG.html"
source_sha256: 909b6ecb60932ba8
extraido: 2026-07-16
---

# Guardrails I: Archivos de contexto

Ya sabés dirigir con la cabeza y ya conocés el equipo de herramientas. Pero hay un problema práctico que aparece apenas empezás a trabajar en serio con un agente: **¿cómo le decís cómo trabajar en tu proyecto sin tener que repetírselo cada vez que abrís una sesión?** La respuesta son los **guardrails**, y en esta lección vemos el primero de los dos tipos: los **archivos de contexto**. 🧭

## 🧠 Primero, cómo «recuerda» la IA (spoiler: no recuerda)

Hay un malentendido que conviene desarmar antes de seguir, porque si no, nada de esto tiene sentido: el modelo **no recuerda nada entre una sesión y otra por sí solo**. Cero. Cada vez que arrancás, empieza con amnesia.

Lo que parece «memoria» en realidad son dos cosas distintas.

- Por un lado está el **contexto de sesión**: todo lo que charlaron en la conversación actual. Es útil, pero es efímero —cuando cerrás, se evapora—.
- Por otro lado están las **instrucciones persistentes**: archivos que viven en tu proyecto y que el agente **lee siempre, al arrancar cada sesión**. Eso último es un guardrail.

La definición, entonces, es simple y vale la pena retenerla: un guardrail es un conjunto de instrucciones persistentes que condicionan al agente, que le dicen *cómo comportarse en este proyecto, siempre*. No le explicás de nuevo tus convenciones cada mañana; las dejás escritas una vez y el agente las respeta.

## 📄 El panorama: un archivo por agente, la misma idea

Acá viene una pequeña complicación del ecosistema: cada herramienta lee su propio archivo, aunque el concepto sea idéntico. Te dejo el mapa para que no te confundas:

| Archivo | Lo lee |
| --- | --- |
| `CLAUDE.md` | Claude Code (es su máxima autoridad) |
| `AGENTS.md` | estándar emergente — OpenCode y varios más |
| `copilot-instructions.md` (en `.github/`) | GitHub Copilot |

Quiero detenerme un segundo en **`AGENTS.md`**, porque no es el capricho de una herramienta más: es la convergencia hacia un estándar. Lo creó OpenAI en agosto de 2025, y desde diciembre de ese año quedó bajo el paraguas de la **Linux Foundation** (a través de la Agentic AI Foundation), con más de **60.000 proyectos** que ya lo adoptaron. Cuando una pieza junta esa cantidad de adopción y respaldo institucional, deja de ser una moda: pasa a ser *el* lugar donde le decís a cualquier agente cómo comportarse.

## 🔗 El patrón profesional: una sola fuente de verdad

Te habrás dado cuenta del problema que asoma: si usás las tres herramientas, ¿vas a mantener tres archivos casi iguales, sincronizados a mano? Eso es un infierno garantizado —terminan divergiendo y cada agente se comporta distinto—.

El truco que usan los equipos es elegante por lo simple: **un solo archivo, compartido con un symlink** entre herramientas (por ejemplo, que `CLAUDE.md` apunte a `AGENTS.md`). Escribís las reglas una vez, en un único lado, y todos los agentes leen exactamente lo mismo. Una fuente de verdad, sin copias que se pelean entre sí.

## 🥇 La regla de oro (la que separa un guardrail útil de uno dañino)

Y acá está lo más importante de la lección, porque mucha gente la pifia justo en este punto y termina **empeorando** el resultado de su agente sin darse cuenta:

> **Documentá solo lo que el agente NO puede inferir del código.** Comandos exactos, versiones puntuales, tooling no estándar, patrones contraintuitivos de tu proyecto. Nada de obviedades.

¿Por qué tan tajante? Porque el contexto no es gratis ni infinito. Un archivo lleno de cosas que el agente ya sabe —»usamos funciones», «el código va en `src/`«— es puro ruido: le llena la cabeza de obviedades y le hace perder foco sobre lo que de verdad importa. Por eso los archivos autogenerados y sin curar suelen ser *peores* que no tener nada. La consigna es mantenerlo **corto y filoso** —como tope, ~300 líneas, y cuanto más corto mejor—, con pura señal.

> 📝 Tranquilo, que la **autoría profunda** de estos archivos —cómo escribir uno realmente bueno— la vas a practicar a fondo en el Módulo 2. Por ahora quedate con el concepto bien claro: el guardrail es *cómo se comporta el agente, siempre*.

## 💡 Para aplicar

Pensá en un proyecto tuyo y listá **3 cosas que el agente NO podría adivinar leyendo el código**: un comando raro de build, una convención contraintuitiva, una versión puntual que importa. Esas tres líneas son, literalmente, el corazón de tu futuro `CLAUDE.md` —lo vas a escribir en serio en el Módulo 2—. Si te cuesta encontrar tres, buena señal: tu guardrail va a ser corto y filoso.

Ya sabés cómo darle a tu agente sus instrucciones persistentes. Pero hay un segundo tipo de guardrail, más duro y más urgente, que no se ocupa de *cómo* se comporta sino de *qué le permitís hacer*. Eso es lo que viene. ➡️
