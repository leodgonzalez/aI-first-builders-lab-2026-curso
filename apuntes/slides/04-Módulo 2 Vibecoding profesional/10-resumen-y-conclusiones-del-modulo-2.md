---
titulo: "Resumen y conclusiones del Módulo 2"
capitulo: "04-Módulo 2 Vibecoding profesional"
orden: 10
source: "apuntes/slides/00-raw/04-Módulo 2 Vibecoding profesional/10.Resumen y conclusiones del Módulo 2 – MUG.html"
source_sha256: 9cdfa87529c65f0e
extraido: 2026-07-16
---

# Resumen y conclusiones del Módulo 2

Fue el módulo del gran salto: pasaste de la teoría de M1 a **construir tu app por primera vez**, aprendiendo a dirigir a la IA con método. Antes del quiz, repasemos las ideas que importan. Si algo no te suena, volvé a la lección antes de seguir. 🧠

## 🎯 Qué es (y qué no es) el vibecoding

- Vibecoding es **dirigir a la IA hacia un resultado completo** e iterar con ella, no pedir snippets sueltos ni pegar a ciegas lo que sale.
- El builder **dirige y juzga**; el prompter **pide y reza**. La diferencia no está en la herramienta, está en quién mantiene el control.
- Es la herramienta correcta para el **momento correcto**: brilla en prototipos y MVPs; cuando va a producción, le sumás rigor.

## ✍️ Dirigir a la IA

- Un buen prompt es **claridad estructurada**: contexto, objetivo, especificidad, restricciones y ejemplos. De vago a preciso es lo que más mueve la aguja —y no exige saber programar: las piezas son **decisiones de producto**, no sintaxis—.
- Hay **dos familias de prompts**: los que le escribís al agente para construir, y los que viven *adentro* de tu app y corren miles de veces sin nadie mirando. La anatomía es la misma; la precisión, en la segunda, importa todavía más.
- El trabajo es un ciclo: **Prompt → Generate → Review → Refine**. El *review* no es un trámite: es donde entra tu criterio. Y no es un one-shot: se **loopea**.
- El **context engineering** es el corazón del módulo: la ventana es **todo lo que el agente sabe** de tu proyecto en cada momento —lo que no está, no existe—. Las cinco palancas: **selección**, compresión, ordenamiento, aislamiento, formato; de todas, la selección es la que más rinde.

## 🛡️ Equipar al agente: guardrails

- El guardrail vive en **un solo archivo**, `AGENTS.md` (y un `CLAUDE.md` que lo importa con `@AGENTS.md`, para Claude Code). Define **cómo se comporta el agente siempre**. Cortito (~300 líneas tope), solo lo no-inferible, sin reglas de estilo —eso es del linter—. Se **itera** a partir del comportamiento real.
- 🛠️ **Ejercicio:** nació tu proyecto —carpeta + `PRD.md` de M1 + guardrails— y pasaste la prueba de fuego: en una conversación limpia, el agente citó tus reglas **sin que le pases nada**.

## 🧬 El PRD, endurecido dirigiendo

- 🛠️ **Ejercicio:** tu primer acto de vibecoding fue sobre un documento que no se rompe. En **loop** —auditar contra el checklist → juzgar vos → reescribir → volver a auditar— convertiste el PRD de M1 en tu **PRD v2**: verificable, tuyo, defendible línea por línea.
- La actitud quedó grabada: la IA **propone**, vos **exigís rigor**. Todo lo que no pediste va a Fuera de Alcance; todo criterio es binario.

## 🏗️ Construir (sin red, a propósito)

- 🛠️ **Ejercicio:** construiste tu **app v1** —la feature core del PRD, corriendo— con plan en palabras aprobado antes de la primera línea, pasos chicos y probando cada paso.
- Y sentiste el límite: sin puntos de guardado, un error de la IA no tiene vuelta atrás. Esa lista de «dónde dolió» que anotaste es la **materia prima del Módulo 3**.

## 🧰 Y algo para llevarte a cualquier lado

- El **arsenal de prompting profesional** (rol, contexto, formato, few-shot, «pensá paso a paso», partir en pasos, límites, delimitadores, iterar, «preguntame antes»). No depende de esta herramienta ni de este curso: sirve con cualquier IA, para cualquier cosa.
- Y el bonus de Claude Code: **Plan Mode** (Shift+Tab) — el «proponé antes de ejecutar» convertido en feature, con la garantía de que el agente no toca nada hasta que aprobás.

## 🎁 Tu entregable doble

- Tu **PRD v2** y tu **app v1** corriendo. Los dos salieron de los ejercicios del módulo.

## 🎯 La gran conclusión

Ya sabés **dirigir**: pedís con precisión, diseñás lo que el agente ve, fijás reglas permanentes y convertiste tu PRD en software real. **Eso ya es vibecodear con método.**

Pero también —y a propósito— construiste **sin red**, y lo sentiste. En el **Módulo 3** llega el equipamiento completo: una carpeta **nueva** que nace como **repo Git**, la disciplina de iterar, y tus primeros **skills** —y reconstruís tu app ahí, esta vez sin miedo—. Tu PRD y tus guardrails viajan con vos; el código de la v1 queda en su carpeta. Antes, un último paso para fijar lo aprendido: el **quiz del Módulo 2**. Ahí te espero. 🚀
