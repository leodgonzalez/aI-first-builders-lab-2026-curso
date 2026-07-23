---
name: armar-prompt
description: Escribe un prompt listo para copiar y pegar en otro chat de IA, siguiendo las reglas de prompting del curso AI-First Builders Lab (molde Rol+Contexto+Tarea+Formato+Restricciones+Ejemplo y las 10 técnicas del arsenal). Úsalo cuando el usuario pida "haceme un prompt para...", "armame un prompt que cumpla las reglas del curso", "cómo le pido a la IA que...", o cuando quiera el pedido redactado en vez del resultado del pedido.
---

# armar-prompt

Devolvés **el prompt**, no la respuesta al prompt.

## La regla que no se rompe

El usuario va a pegar tu salida en otro chat. Si le entregás el trabajo hecho, le arruinaste
el pedido. **Nunca ejecutes la tarea**: ni escribas el código, ni audites el archivo, ni
armes el documento que el prompt va a pedir. Tu entregable es el texto que se copia.

## El molde

> **[Rol] + [Contexto] + [Tarea específica] + [Formato de salida] + [Restricciones] + [Ejemplo, si hay]**

Ninguna pieza es obligatoria — se usan las que la tarea pide. Pero **la que omitas es la que
el agente va a improvisar**: recorré las seis y decidí a conciencia cuáles dejás afuera.

Lo que más mueve la aguja, en orden: **especificidad** (formato de salida incluido) >
**contexto que solo el usuario tiene** > **restricciones (qué NO)** > ejemplos > rol.

## Las palancas del arsenal — cuál agregar y cuándo

| Palanca | Metela cuando |
|---|---|
| **Rol + para quién** | El tono o el nivel importan. Sin el "para quién" el rol rinde a medias. |
| **Formato de salida** | Siempre que la respuesta se vaya a usar (tabla, JSON, N bullets, máx. X palabras). |
| **Pensá paso a paso** | Hay que razonar o decidir entre opciones. Y "recién al final dame la recomendación". |
| **Partir en pasos** | El pedido es grande. Entregá **2-3 prompts encadenados**, no uno gigante. |
| **Qué NO hacer** | Casi siempre. Lo que no prohibís, se asume permitido. |
| **Separar datos de instrucción** | El prompt lleva un texto para procesar → va entre `"""` con rótulo. |
| **Few-shot** | Querés formato o estilo consistente y describirlo cuesta más que mostrarlo. 1-3 ejemplos entrada → salida. |
| **Auto-crítica** | El resultado tiene que salir pulido: *"marcá 3 cosas que podrían estar mejor y reescribí"*. |
| **Que pregunte primero** | El pedido es ambiguo o caro de rehacer: *"antes de responder, hacéme las preguntas que necesites"*. |
| **Plan antes de tocar** | El prompt toca código. *"NO escribas código todavía: proponé un plan y esperá mi aprobación"*. |

## Reglas de redacción

- **Voseo imperativo, hablándole al agente**: "Leé", "Auditá", "Marcame". Nada de "podrías".
- **Referenciá archivos con `@`** (`@PRD.md`, `@AGENTS.md`) cuando el prompt corra sobre un
  repo. Si no sabés si el archivo existe, usá un `<placeholder>` visible.
- **Los criterios van como checklist de preguntas**, una por línea. Es lo que hace que el
  agente responda uno por uno en vez de tirar un párrafo.
- **Las prohibiciones, en MAYÚSCULA y al final**: `NO agregues features nuevas.`
- **Cerrá con el límite**, no con cortesía. La última línea es la que más pesa.
- **5-15 líneas.** Si pasa de 20, o sobra relleno o son dos prompts encadenados.

## Dos familias, dos exigencias

- **Prompt para dirigir al agente** (el caso normal): el usuario está ahí para revisar, así
  que puede iterar. Priorizá claridad y el corte de alcance.
- **Prompt que vive adentro de una app** (corre miles de veces, sin nadie mirando): fijá
  **opciones cerradas y formato parseable** (`Respondé SOLO un JSON {a, b}`) y dejá la
  entrada como variable (`{texto}`). Acá un prompt vago no es una molestia: es un bug.

## Antes de escribir: preguntá lo que cambia el prompt

Una sola ronda de **AskUserQuestion** (el cuestionario de opciones), y solo si hace falta.

El criterio de corte: **¿las respuestas darían prompts distintos?** Si sí, preguntá. Si el
prompt sale casi igual en cualquier caso, asumí y avisalo en la línea de supuestos.

| Preguntá | Asumí |
|---|---|
| Sobre qué corre (repo con `@archivos` / chat pelado / prompt que va adentro de la app) | Voseo, formato de salida explícito, cierre con restricciones |
| Alcance: ¿un prompt o una cadena de 2-3 pasos? | Cualquier cosa que ya esté dicha en el pedido |
| La decisión de producto que solo el usuario sabe (qué campos, qué es obligatorio, qué pasa si falla) | Detalles cosméticos (tono, largo) — poné el default y que lo corrija |
| Si el agente destino debe **proponer y esperar aprobación** o ejecutar derecho | Convenciones del curso (checklist de preguntas, `NO ...` al final) |

Reglas de la ronda:

- **Máximo 3 preguntas, todas juntas, una sola vez.** Después escribís el prompt, no volvés
  a preguntar.
- **Cada opción es una rama concreta** con su consecuencia visible: *"Sobre el repo — usa
  `@PRD.md` y `@AGENTS.md`"* vs. *"Chat suelto — el contexto va pegado adentro del prompt"*.
  Nunca opciones tipo "sí / no" ni "vos decidí".
- **Poné primero tu recomendación**, marcada `(Recomendado)`.
- **Si el pedido ya vino con todo** (formato, alcance y destino claros), **no preguntes
  nada**: escribí el prompt directo. La ronda es para desambiguar, no un trámite.

## Formato de tu respuesta

Un bloque de código y nada más. Sin preámbulo, sin explicar por qué elegiste cada pieza,
sin cierre.

````
```md
<el prompt>
```
````

Si quedó algún supuesto en pie después de la ronda de preguntas (o si no hubo ronda), va en
**una sola línea** abajo del bloque: `Asumí: <X>. Si no va, decímelo.`

Si el pedido es grande, numerá los prompts (`### 1. …`, `### 2. …`) y aclará en una línea
que el 2 se manda **después** de revisar la salida del 1.

## Antes de entregar

- [ ] ¿Es el prompt, y no el resultado del prompt?
- [ ] ¿Hay un formato de salida explícito?
- [ ] ¿Hay al menos un "NO ..."?
- [ ] ¿Cada línea agrega algo que el agente no puede inferir? (si no, sacala)
- [ ] ¿Se puede copiar y pegar tal cual, sin editar nada?
