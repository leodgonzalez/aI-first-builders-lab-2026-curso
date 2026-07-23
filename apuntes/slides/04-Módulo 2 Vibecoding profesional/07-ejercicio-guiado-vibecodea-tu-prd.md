---
titulo: "Ejercicio guiado: Vibecodeá tu PRD"
capitulo: "04-Módulo 2 Vibecoding profesional"
orden: 7
source: "apuntes/slides/00-raw/04-Módulo 2 Vibecoding profesional/07-Ejercicio guiado_ Vibecodeá tu PRD – MUG.html"
source_sha256: 0e41e51eaa8c7ebc
extraido: 2026-07-16
---

# Ejercicio guiado: Vibecodeá tu PRD

Este es el **segundo ejercicio del módulo** —y sí, otra vez con entregable concreto: tu PRD mejorado—. Arranca donde no lo esperabas: **no con código, con tu PRD.** 🧬 En M1 lo escribiste **a mano, a propósito sin IA**, para entrenar el ojo. Hoy, por primera vez, lo vas a mejorar **dirigiendo a la IA** —tu primer acto de vibecoding, sobre un documento que no se puede romper—. Lo vamos a hacer con **Claude Code**, la herramienta principal del curso, y te voy a llevar de la mano paso por paso.

## 🎯 Por qué el PRD primero (y no el código)

Podría mandarte directo a codear. No lo hago, y por tres razones que valen oro:

- **Es el on-ramp más seguro.** Vibecodear un documento te hace practicar el ciclo *pedir → revisar → refinar* y el músculo de **dirigir y juzgar**, pero sobre algo que no explota. Es como aprender a manejar en un playón vacío antes de salir a la autopista: si la IA propone una macana, la descartás y listo, sin costo.
- **Es estratégico.** El PRD es el **contrato** del que va a nacer tu app. Cada hueco que le tapes hoy es un bug que no vas a tener que cazar mañana, cuando ya esté enterrado bajo mil líneas de código.
- **Te va a sorprender.** Vas a descubrir cuántos huecos tenía tu PRD «terminado». Es normal: ahora tenés un par de ojos frescos ayudándote a mirarlo. Un PRD es un **documento vivo**.

> 🧭 **¿Y los skills? Todavía no.** Un skill sirve para *repetir* un workflow muchas veces; hoy este workflow lo hacés **a mano, en conversación**, para entrenar el ojo. Guardá el dato: **en el próximo módulo** vas a empaquetar exactamente esto en tu **primer skill** (`create-prd`) —y en el **Módulo 5**, skills como ese se orquestan en un pipeline completo—. Primero a mano, como en M1: así después vas a poder juzgar si el skill trabaja bien.

## 🔁 La mentalidad: esto es un loop, no un one-shot

Grabate esto antes de tocar la primera tecla, porque es LA clave del ejercicio: **los pasos que siguen no son una escalera que subís una sola vez; son una vuelta que vas a dar varias veces.** El ciclo *Prompt → Generate → Review → Refine* que viste en la lección de prompting no era teoría decorativa: es exactamente lo que vas a hacer acá, girando sobre tu PRD hasta que quede filoso. Concretamente:

- **La primera auditoría no encuentra todo.** Encuentra los problemas gruesos; cuando los corregís, la segunda pasada encuentra los que estaban tapados debajo. Es normal y es buena señal: significa que el documento está mejorando de verdad.
- **La primera reescritura no queda perfecta.** Vas a leerla y algo no te va a cerrar. Eso no es un fracaso del ejercicio: **es el ejercicio**. Pedís otra vuelta, ajustás, volvés a leer.
- **Volver a arrancar es jugada de profesional, no derrota.** Si la conversación se ensució —el agente arrastra sugerencias que ya rechazaste, mezcla versiones— acordate de la lección anterior: `/clear` y entrás de nuevo, limpio, con el `PRD.md` fresco. No perdés nada: el documento está a salvo en el archivo; lo que soltás es la conversación sucia que lo rodeaba.

Si terminás el ejercicio habiendo dado **una sola pasada**, casi seguro te quedaste corto. El PRD v2 no sale de un prompt genial: sale de varias vueltas de dirigir y juzgar.

## 🕵️ La actitud: dirigir y juzgar

Antes de los pasos, la clave del ejercicio. La IA es **buenísima** encontrando huecos en un PRD, pero tiene dos vicios que tenés que atajar sí o sí:

- **Infla el scope.** Le pedís que mejore el PRD y te mete features que nadie pidió, «porque quedan bien». Cortala: *todo lo que no excluís, se asume incluido*. Un requerimiento que no resuelve un dolor real **no entra** —va a «Fuera de Alcance»—.
- **Suaviza los criterios.** Tiende a escribir criterios de aceptación con «correctamente» o «adecuado» adentro, palabras que suenan bien pero no se pueden testear. No los aceptes: cada criterio es **binario** (pasa / no pasa), o no sirve.

La regla es la de siempre: la IA **propone**, vos **exigís rigor**. El PRD que sale de acá tiene que ser uno que **entendés y defendés línea por línea**.

## 🛠️ Tu turno: paso a paso con Claude Code

⏱️ **Tiempo estimado:** ~30-45 min (contando las vueltas del loop — no lo apures) · 📦 **Entregable:** tu **PRD evolucionado** (`PRD.md`, v2), más filoso que el de M1. Es el **primer artefacto de tu entregable doble** (el otro, la app, sale al final del módulo).

Seguí estos pasos tal cual. No hace falta que sepas nada nuevo de Claude Code: con esto alcanza.

**1. Parate en tu carpeta de proyecto.** Es la del ejercicio anterior: ya tiene tu **`PRD.md`** (el de M1) y tus guardrails. Bonus que te ganaste recién: el agente va a entrar **leyendo tus reglas**, sin que se las repitas.

**2. Abrí Claude Code en esa carpeta.** Desde la terminal, parado en la carpeta, escribí:

```
claude
```

**3. Primer prompt — normalizá y validá la estructura.** Antes de auditar el *contenido*, asegurate de que el PRD tenga el molde que definimos en M1 (en la lección *PRD: qué es y cómo se arma*). Este prompt lo pasa a Markdown limpio y valida que estén todas las secciones. Copiá y pegá:

```
Leé @PRD.md. Es el PRD de mi proyecto; si no está en Markdown limpio, pasalo a Markdown.
Validá que respete esta estructura (el template del curso) y decime qué secciones faltan
o están fuera de lugar. Si falta alguna, agregá el encabezado vacío para dejar el molde
completo, pero NO inventes requerimientos ni criterios:

# PRD-001: <nombre del proyecto> — <una línea de qué es>
## Contexto y Problema
## Objetivos
## Requerimientos Funcionales       (RF-01, RF-02, …)
## Requerimientos No Funcionales    (RNF-01, …)
## Criterios de Aceptación          (AC-01 (RF-01): Dado / Cuando / Entonces)
## Fuera de Alcance
## Riesgos y Dependencias
```

Si el agente te marca que falta una sección, buena señal: la vas a completar en los pasos que siguen. Revisá que no haya inventado nada —solo tiene que ordenar y señalar, no rellenar—.

**4. Segundo prompt — la auditoría de calidad.** Con la estructura en orden, ahora sí pedile que audite el *contenido* pieza por pieza. Le damos SOLO el PRD (esto es *selección*, de la lección anterior). Copiá y pegá este prompt, sin cambiar nada:

```
Leé @PRD.md de nuevo. Auditá su contenido, sin reescribir todavía,
contra este checklist y marcame los problemas UNO POR UNO:
- ¿Cada RF es atómico (una sola acción) y dice "debe"?
- ¿Cada RNF tiene un número concreto? (no "rápido" → "< 3 s p95")
- ¿Cada RF tiene al menos un AC que lo verifique?
- ¿Cada AC es binario (pasa/no pasa) y está en formato Dado/Cuando/Entonces?
- ¿El "Fuera de Alcance" está explícito?
- ¿Hay un AC de control de acceso (que un usuario no vea datos de otro)?
Para cada problema, decime dónde está y por qué. NO agregues features nuevas.
```

**5. Leé la auditoría y JUZGÁ cada hallazgo.** Este es el corazón del ejercicio, no lo apures. Aceptá los hallazgos reales, **rechazá el humo** y, sobre todo, **frená cualquier feature nueva** que se le haya colado. Respondele en la misma conversación: *«El punto 1 y el 3 son válidos, corregilos. El punto 4 no: eso queda fuera de alcance.»*

**6. Pedile la reescritura de lo que aceptaste.** Por ejemplo:

```
Reescribí solo los RF, RNF y AC que marcamos como débiles, aplicando las
correcciones que te aprobé. Mantené el resto igual. Devolveme el PRD completo actualizado.
```

**7. Revisá el resultado… y dale otra vuelta.** Releé el PRD actualizado entero. ¿Algo no te cierra? No lo aceptes «porque ya está»: decíselo y pedí el ajuste. Y aunque te cierre, **volvé al paso 4** y corré la auditoría de nuevo sobre esta versión: lo normal es que la segunda pasada encuentre cosas que la primera no vio (estaban tapadas por los problemas gruesos). Repetí el loop 4 → 7 hasta que la auditoría venga limpia o solo traiga humo que ya sabés rechazar.

**8. ¿La conversación se ensució? Arrancá de nuevo, sin miedo.** Si después de varias vueltas el agente empieza a mezclar versiones o a reflotar sugerencias que ya rechazaste, es el context rot de la lección anterior en vivo. La jugada profesional: `/clear`, y volvés a entrar fresco con el `PRD.md` actual. No estás tirando trabajo —el documento quedó guardado—; estás tirando el ruido.

**9. Guardalo como tu PRD v2.** Cuando el loop ya no trae hallazgos reales, releelo una última vez: tiene que seguir siendo **verificable y tuyo**. Guardá el `PRD.md` actualizado —ese es tu entregable—.

> ✅ **Lo lograste cuando** tu PRD v2 tapó al menos un hueco real que el de M1 tenía, **diste más de una vuelta de auditoría** (si fue una sola, volvé al paso 4), **rechazaste al menos una sugerencia** de la IA, y podés defender cada línea. Guardalo: es la mitad de tu **entregable doble** y el plano desde el que vas a construir la app.

### 🔎 La muestra: el PRD de TicketTriage, endurecido

Cuando pasamos el PRD de **TicketTriage** (el que viste completo en M1) por este ejercicio, la IA cazó un hueco real. El original tenía:

❌ *RF-02: El agente debe poder listar todos los tickets; el socio solo debe ver los suyos.*

La auditoría marcó: *«el socio ve solo los suyos» es una regla de acceso sin ningún criterio que la verifique — ¿qué pasa si el socio B pide el ticket del socio A?*. Buena pregunta: la regla estaba escrita, pero nada la ponía a prueba, y **una regla que no se testea es una regla que no existe**. Aceptamos el hallazgo y sumamos el criterio que faltaba:

✅ *AC-08 (RF-02): Dado el socio A dueño de un ticket y el socio B autenticado, cuando B intenta ver ese ticket, entonces responde HTTP 403 y no lo muestra. (control de acceso)*

Un hueco de seguridad, tapado en el contrato **antes** de escribir una línea. Y ojo: cuando la IA propuso además «un dashboard de métricas de soporte», lo mandamos derecho a **Fuera de Alcance** —no estaba en el dolor original—. Dirigir y juzgar, en acción: aceptamos lo que sumaba, frenamos lo que sobraba.

## 🪜 El peldaño del medio

Para que lo ubiques en el viaje: el PRD lo hiciste **a mano en M1**, lo **evolucionaste dirigiendo la IA hoy**, **en el próximo módulo** vas a empaquetar este mismo workflow en tu **primer skill** (`create-prd`) para correrlo con un solo comando, y en el **Módulo 5** skills como ese se orquestan en un pipeline que corre auditorías **automáticamente**. Cada peldaño existe porque subiste el anterior: como hoy la auditoría la corriste con tus manos, cuando un skill la corra por vos vas a saber leer si hizo un buen trabajo o te metió humo.

Con tu PRD v2 en la mano, llegó el momento que veníamos preparando desde M1: **convertirlo en software**. En el próximo ejercicio construís la primera versión de tu app —vibecodeando, rápido y, ojo, **todavía sin red de seguridad**: eso también es a propósito, y lo vas a entender cuando duela—. ➡️
