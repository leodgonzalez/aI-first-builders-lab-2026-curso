---
titulo: "Ejercicio guiado: Escribí los guardrails de tu proyecto"
capitulo: "04-Módulo 2 Vibecoding profesional"
orden: 6
source: "apuntes/slides/00-raw/04-Módulo 2 Vibecoding profesional/06-Ejercicio guiado_ Escribí los guardrails de tu proyecto – MUG.html"
source_sha256: e6a55544dd2817ca
extraido: 2026-07-16
---

# Ejercicio guiado: Escribí los guardrails de tu proyecto

Teoría fresca, manos a la obra: acabás de ver qué lleva un buen guardrail, y **ahora lo escribís para tu proyecto** —no un ejemplo de juguete, el de verdad—. 🧱 Y este ejercicio tiene un plus: acá **nace la carpeta de tu proyecto**, la que te va a acompañar todo este módulo. La creás, le ponés adentro el PRD que escribiste en M1, y la equipás con sus guardrails. Al terminar, tu agente va a saber de qué va tu proyecto y qué tiene prohibido hacer **antes de que vos escribas el primer prompt de cada sesión**.

¿Por qué esto antes de escribir la app? Porque un agente que abre una carpeta pelada es como un compañero nuevo al que no le pasaste el onboarding: talentoso, pero perdido. No sabe qué construís, con qué stack, ni qué tiene prohibido tocar; cada sesión empieza explicándole lo mismo, y cada explicación sale un poco distinta. El guardrail invierte eso: **el contexto queda escrito en la carpeta** y el agente lo lee solo, siempre. Preparás una vez y cosechás en cada sesión.

## 🎯 Qué vas a dejar armado

Dos archivos, nada más —y ya sabés de la lección anterior por qué son dos—:

- Un **`AGENTS.md`** — el guardrail: *cómo comportarse* (propósito, stack, cómo correr) + *qué NO hacer* (las prohibiciones), en un solo archivo.
- Un **`CLAUDE.md`** de una sola línea —`@AGENTS.md`— para que **Claude Code** lo importe. Una fuente de verdad, cero copias que se contradigan.

## 🛠️ Tu turno: paso a paso con Claude Code

⏱️ **Tiempo estimado:** ~25 min · 📦 **Entregable:** la carpeta de tu proyecto creada, con `PRD.md` + `AGENTS.md` + `CLAUDE.md`, y la prueba de que el agente los lee solo.

**1. Creá la carpeta de tu proyecto y ponele tu PRD.** El nombre que quieras. Adentro, guardá tu PRD de M1 como **`PRD.md`** —si lo tenés en Google Docs o Word, copiá el texto y pegalo en ese archivo `.md`; el contenido es lo que importa, no el formato—.

**2. Abrí Claude Code en esa carpeta.** Desde la terminal, parado en la carpeta:

```
claude
```

**3. Drafteá el guardrail en `AGENTS.md`.** Dejá que Claude Code te arme el borrador a partir del PRD —pero primero que te pregunte lo que no sabe—. Copiá y pegá:

```
Leé @PRD.md. Vamos a escribir un AGENTS.md corto (menos de 40 líneas) para este proyecto,
con exactamente estos bloques y nada más:
- Propósito (2 líneas: qué es la app)
- Stack (las versiones que importan)
- Cómo correr (los comandos exactos de instalar / levantar / correr tests)
- Qué NO hacer (2-3 prohibiciones reales que salgan del PRD)

Antes de escribir nada, hacéme TODAS las preguntas que necesites sobre cada uno de esos
puntos —sobre todo el stack y los comandos, que quizás no estén en el PRD—. Yo te respondo,
y recién con mis respuestas armás el borrador. NADA de reglas de estilo ni obviedades.
Después guardalo como AGENTS.md.
```

Ese *«preguntame primero»* es la clave del ejercicio: el agente **no adivina** tu stack ni tus comandos, te los pregunta. Así el borrador sale a tu medida —no un genérico— y vos quedás con cero dudas de por qué dice lo que dice. Respondé cada pregunta con calma; ese ida y vuelta *es* el vibecoding. Y si algún comando todavía no lo decidiste (es normal: la app no existe aún), dejalo escrito como intención y lo firmás cuando construyas.

**4. Conectá Claude Code al guardrail.** Para que Claude Code lea ese `AGENTS.md`, creá el `CLAUDE.md` que lo importa:

```
Creá un CLAUDE.md que en una sola línea importe el guardrail: @AGENTS.md
```

**5. Revisá y hacelo tuyo.** Acá entra tu criterio (dirigir y juzgar): leé el `AGENTS.md` línea por línea y podalo con el checklist de la lección anterior. ¿Cada línea dice algo que el agente **no puede adivinar** mirando el código? ¿Se coló alguna regla de estilo (afuera: eso es del linter)? ¿Las prohibiciones son las **reales** de tu proyecto o relleno que suena bien? Menos es más: si una línea no se gana el lugar, sacala.

**6. La prueba de fuego.** Ahora verificá que el agente de verdad lo lee **solo**. Limpiá el contexto con `/clear` (conversación nueva, de cero) y preguntale, sin pasarle ningún archivo:

```
¿De qué se trata este proyecto y qué tenés prohibido hacer acá?
```

Si te responde con **tu** propósito y **tus** prohibiciones —sin que le hayas pasado nada en esta conversación—, es porque leyó el guardrail por su cuenta: `CLAUDE.md` → `@AGENTS.md`, automático, en cada sesión. Eso es exactamente lo que queríamos: instrucciones permanentes que no dependen de tu memoria.

> ✅ **Lo lograste cuando** tu `AGENTS.md` tiene menos de 40 líneas y todo lo que dice es no-inferible, el `CLAUDE.md` lo importa con `@AGENTS.md`, y la **prueba de fuego** pasó: el agente citó tu propósito y tus prohibiciones en una conversación limpia, sin ayuda.

### 🔎 La muestra: TicketTriage pasa la prueba de fuego

Así quedó la carpeta de **TicketTriage** después de este ejercicio —fijate que todavía no hay una sola línea de código—:

```
tickettriage/
├── PRD.md        # el contrato: qué construir (el de M1 — lo endurecés en el próximo ejercicio)
├── AGENTS.md     # el guardrail: cómo comportarse + qué NO hacer
└── CLAUDE.md     # una línea: @AGENTS.md
```

Y la prueba de fuego, tal cual pasó: `/clear`, pregunta limpia, y el agente respondió *«Es una mesa de ayuda donde la IA clasifica tickets y sugiere respuestas apoyadas en `kb.md`. Tengo prohibido afirmar cosas que no estén en la KB, hardcodear la API key y agregar features fuera del PRD»*. Nadie le pasó nada en esa conversación: lo sacó del guardrail, solo. 🎯

Un último recordatorio de la teoría: este archivo **recién nace**. La versión buena no la vas a escribir hoy, la vas a **iterar** —cada vez que corrijas al agente dos veces por lo mismo, esa corrección se vuelve una línea nueva—. Dejalo vivo. Y un dato para más adelante: estos tres archivos (`PRD.md`, `AGENTS.md`, `CLAUDE.md`) son **los que van a viajar con vos** cuando en el Módulo 3 tu proyecto estrene carpeta nueva con Git — el esfuerzo que pongas acá se amortiza durante todo el curso.

Tu agente ya tiene su manual de comportamiento, y tu proyecto ya existe. Ahora sí, lo que veníamos preparando: tu **primer acto de vibecoding**. En el próximo ejercicio dirigís a la IA para endurecer ese `PRD.md` que trajiste de M1 —con la ventaja de que el agente ya entra leyendo tus reglas—. ➡️
