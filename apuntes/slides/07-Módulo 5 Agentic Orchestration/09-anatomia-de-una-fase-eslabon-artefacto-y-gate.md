---
titulo: "Anatomía de una fase: eslabón, artefacto y gate"
capitulo: "07-Módulo 5 Agentic Orchestration"
orden: 9
source: "apuntes/slides/00-raw/07-Módulo 5 Agentic Orchestration/09-Anatomía de una fase_ eslabón, artefacto y gate – MUG.html"
source_sha256: f9506d08562c75f9
extraido: 2026-08-07
---

# Anatomía de una fase: eslabón, artefacto y gate

Ya viste seis fases funcionando en tu propio repo. Ahora vamos a lo que realmente te va a servir: **cómo se diseña una**. Porque en tres lecciones vas a estar diseñando las tuyas, y la diferencia entre hacerlo bien y hacerlo por intuición está enteramente en esta lección. 🔗

Arranco con la definición que ordena todo, y que conviene tomarse en serio:

> **Una fase no es «un momento del trabajo». Una fase es un contrato.**

Si tus fases son «primero pensamos, después hacemos, después revisamos», no tenés un pipeline: tenés una intención, que es lo mismo que tenías antes de empezar el módulo. Un pipeline aparece cuando **cada fase responde, sin ambigüedad, siempre las mismas preguntas**. Ésa es la diferencia entre un proceso y una costumbre.

## 📋 Las siete preguntas

Ésta es la herramienta central del módulo. Para **cada** fase que diseñes, respondé estas siete. Si alguna se queda sin respuesta, la fase está mal definida — y créeme que es infinitamente más barato descubrirlo en un documento que a mitad de un build.

**1. Propósito — ¿qué problema resuelve esta fase, en una frase?**

Una sola. Si necesitás dos, casi siempre es porque la fase está haciendo dos cosas y hay que partirla.

Y esto no es prolijidad: las fases que hacen dos cosas producen **gates ambiguos**. Cuando llegue el momento de preguntar «¿está lista?», la respuesta va a ser «bueno, la mitad sí» — y esa ambigüedad es exactamente por donde te vas a colar para avanzar sin estar listo. Un gate que admite un «más o menos» no es un gate.

**2. Entrada — ¿qué artefacto necesita ya existente para arrancar?**

Una fase sin entrada definida es una fase que **arranca con lo que haya**. Y «lo que haya», en la práctica, suele ser la memoria del agente sobre la conversación — que ya sabemos cuánto dura y con qué fidelidad.

Si tu fase de especificación arranca del PRD, entonces **sin PRD no arranca**. Punto. Definir la entrada es lo que convierte a la cadena en una cadena: cada eslabón necesita al anterior.

**3. Trabajo — ¿qué se hace acá, y con qué primitiva?**

Concretamente: ¿lo hace un skill? ¿cuál? ¿hace falta spawnear un subagent? Esto conecta el diseño con las cinco piezas de la lección 6, y es lo que evita que tus fases queden como cajas vacías con un nombre lindo adentro. Una fase que no podés mapear a una primitiva concreta es una fase que todavía no diseñaste.

**4. Artefacto de salida — ¿qué queda escrito en disco al terminar?**

La más subestimada de las siete, así que la digo fuerte:

> 📦 **Si una fase no produce un artefacto, no es una fase — es una charla.**

Lo que no queda escrito, se perdió. Se perdió para la fase siguiente, que va a tener que reconstruirlo de memoria y lo va a reconstruir un poco distinto. Se perdió para vos dentro de tres semanas. Y —lo más importante— **se perdió para el gate**, porque no se puede verificar lo que no existe.

Es también la razón por la que un pipeline te deja, casi sin querer, la documentación que nunca escribiste: el rastro no es un trabajo extra, es un subproducto obligatorio del diseño.

**5. Bloqueado — ¿qué está prohibido hacer en esta fase?**

Definir lo prohibido es **tan importante como definir lo permitido**, y es lo que casi nadie hace cuando diseña su primer pipeline.

Es lo que impide que el agente «aproveche el viaje»: que mientras planifica escriba tres archivos para ir adelantando, o que mientras verifica arregle lo que fue encontrando. Las dos cosas parecen eficientes en el momento y las dos rompen el sistema — la primera saltea el gate del spec, la segunda saltea los gates de CODE.

Sin prohibiciones explícitas, las fases **se contaminan entre sí** y en pocas semanas el pipeline es decoración: los nombres siguen ahí pero el trabajo real pasa donde quiere.

**6. Condición de salida (el gate) — ¿qué tiene que ser *verificable* para poder avanzar?**

Subrayá **verificable**, que es donde se cae la mayoría de los diseños. La diferencia, con ejemplos:

- ❌ *«El spec está bueno»* — **no es una condición.** No hay forma de que dos personas contesten eso igual, y mucho menos un script.
- ✅ *«Existe el archivo `docs/daw/specs/spec-FEAT-001.md` y la validación del spec pasó sin errores críticos»* — **eso sí**. Es verdadero o falso, y cualquiera llega al mismo veredicto.

La regla práctica: **si tu condición no la puede evaluar un script o un checklist cerrado, no es un gate — es una sensación.** Y las sensaciones no se pueden imponer, que es justamente lo que necesitás.

**7. Quién valida y qué se marca — ¿quién dice que se cumplió, y qué pasa en el state?**

¿Lo chequea un skill de validación? ¿un subagent con contexto limpio? ¿un hook? ¿lo confirmás vos? Y cuando se cumple: **qué campo del state se actualiza**.

Esa última parte se olvida siempre y es la que cierra el circuito. Sin marcar nada en el state, el gate no deja rastro, la máquina no puede usarlo para decidir después, y el hook de la fase siguiente no tiene qué leer.

## 🚦 Un gate tiene tres partes, siempre

Los gates se piensan mal porque se piensan como una sola cosa. Son **tres**, y separarlas mentalmente te ordena el diseño de una manera que sorprende:

- **(a) La condición** — *qué* se verifica. Tiene que ser objetiva.
- **(b) El verificador** — *quién* lo verifica: código (un hook), un skill de validación, un subagent, o vos.
- **(c) El efecto** — *qué se marca* en el state y *qué se desbloquea* como consecuencia.

Mirá cómo mejora un gate cuando lo pasás por las tres:

| ❌ Mal formulado | ✅ Bien formulado |
| --- | --- |
| «El PRD está aprobado» | **(a)** el checklist de validación pasa sin errores críticos · **(b)** lo corre el skill `daw-validate-prd` + lo confirmás vos · **(c)** `gates.define = true`, se habilita la fase de especificación |
| «El código está listo» | **(a)** la suite de tests pasa completa y el análisis estático no reporta hallazgos críticos · **(b)** los skills `daw-test` y `daw-security-sast` · **(c)** `gates.tests = true`, `gates.sast = true` |
| «Se verificó» | **(a)** lo construido cumple todos los criterios de aceptación del spec · **(b)** un subagent verificador, que no escribió el código · **(c)** `gates.verify = true`, se habilita el cierre |

Fijate lo que pasó: los de la izquierda **no se pueden evaluar**, y por eso no se pueden imponer. Los de la derecha sí, y por eso pueden llegar a ser un candado.

## 📐 Tres reglas de diseño (con su porqué)

**Regla 1: toda fase produce un artefacto.** Sin artefacto no hay trazabilidad ni forma de verificar el gate. Es la más simple de aplicar y la que más rápido detecta una fase mal pensada: si no sabés qué archivo deja, probablemente esa fase no debería existir.

Y es una regla que hay que aplicarse a uno mismo, no solo a los demás. DAW la incumplía: **VERIFY no dejaba nada escrito** — su veredicto vivía en `gates.verify` y en un resumen que se iba con la terminal. Justamente la fase que dictamina si lo que se construyó es lo que se había pedido era la única que no se podía leer después. Hoy escribe su reporte, como todas. La moraleja no es sobre DAW: es que **la fase que más te vas a olvidar de hacer que escriba es la de revisión**, porque mientras la mirás en pantalla se siente completa.

**Regla 2: todo gate lo verifica alguien que no hizo el trabajo.** Si el único que puede decir «está listo» es el que lo hizo, no es un gate: es una autoevaluación. El verificador puede ser código, un subagent con contexto limpio, o vos — pero no el mismo agente con el mismo contexto y las mismas suposiciones. Es la idea de la lección 6, ahora como regla de diseño.

**Regla 3: toda transición se registra.** Sin historial no podés responder la única pregunta que importa cuando algo sale mal: *¿por qué la máquina está donde está?* Un pipeline que no deja registro te obliga a hacer arqueología cada vez que hay un problema.

## 🙋 Dónde va el humano

Una tentación muy frecuente cuando diseñás tu primer pipeline es **automatizar todo**: que las fases avancen solas apenas los checks pasan, sin que vos tengas que confirmar nada. Suena a la versión evolucionada del sistema.

Resistila, al menos al principio, porque la confirmación explícita cumple dos funciones que no son obvias:

- **Te mantiene informado.** Ves la máquina avanzar y podés cortar cuando algo no cierra. Un pipeline que corre solo de punta a punta es un pipeline del que te enterás **al final**, cuando ya no hay nada que corregir barato.
- **Te obliga a leer el artefacto.** Y ésta es la importante. El momento en que confirmás es el momento en que efectivamente mirás el spec, el PRD, el reporte. Si sacás ese momento, el artefacto se vuelve decorativo en dos semanas: se genera, nadie lo lee, y el pipeline pasa a producir papeles en vez de garantías.

Con el tiempo vas a poder aflojar en las transiciones que ya te merecen confianza. Pero eso **se gana**, no se asume de entrada.

## 🛠️ Micro-ejercicio (10 min)

Éste rinde mucho, hacelo aunque tengas poco tiempo.

**Primero**, tomá **una fase de DAW** que hayas visto correr —PLAN es la más rica— y completá las siete preguntas mirando su archivo en `.daw/rules/`. Vas a ver que todas tienen respuesta, y que están escritas casi con estas mismas categorías.

**Después**, hacé lo mismo con **el flujo de Spec Kit del Módulo 4**: agarrá el paso de especificar y contestá las siete.

Te adelanto lo que va a pasar, porque es el punto del ejercicio: **la 5 y la 6 no van a tener respuesta**. No estaba prohibido nada —nada te impedía implementar— y no había una condición verificable — había una convención y tu buena voluntad.

Ese hueco no es un defecto de Spec Kit: es exactamente **el hueco que un pipeline llena**. Y ahora tenés la plantilla para llenarlo en el tuyo.

Falta una familia de gates que no puede quedar afuera de ningún pipeline serio. ➡️
