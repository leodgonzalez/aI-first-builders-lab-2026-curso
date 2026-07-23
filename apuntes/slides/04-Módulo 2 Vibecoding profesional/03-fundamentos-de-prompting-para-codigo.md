---
titulo: "Fundamentos de prompting para código"
capitulo: "04-Módulo 2 Vibecoding profesional"
orden: 3
source: "apuntes/slides/00-raw/04-Módulo 2 Vibecoding profesional/03-Fundamentos de prompting para código – MUG.html"
source_sha256: 9910fdc1c1d7e4ac
extraido: 2026-07-16
---

# Fundamentos de prompting para código

Si el vibecoding es dirigir a la IA, el prompting es el idioma con el que la dirigís. Es la habilidad base de todo lo que viene, y la buena noticia es que no tiene nada de mágico: no hay frases secretas ni fórmulas ocultas. Un buen prompt es, simplemente, **claridad estructurada**. En esta lección vemos cómo se arma uno para tareas de código, y vas a notar que es más sentido común ordenado que truco. ✍️

## 🧱 La anatomía de un buen prompt

Pensá un prompt efectivo como una pequeña sesión de instrucciones a un colaborador muy capaz pero que no te conoce. Cuanto más completes el cuadro, mejor sale el trabajo. No siempre necesitás todas las piezas —según la tarea, algunas sobran—, pero vale tenerlas en la cabeza para saber cuál te está faltando cuando el resultado no sale como esperabas. Estas son:

- **Contexto** — dónde encaja esto: el proyecto, el archivo que vas a tocar, la convención que seguís. Es lo que el colaborador nuevo no puede adivinar porque no vivió en tu código.
- **Objetivo** — qué querés lograr, concreto y sin vaguedades. Si vos no sabés bien qué pedís, el agente tampoco lo va a saber.
- **Especificidad** — los detalles que importan: formato de salida, casos borde, qué pasa cuando algo falla. Acá se juega la diferencia entre «más o menos lo que quería» y «exactamente lo que quería».
- **Rol** (opcional) — un *«actuá como experto en X»* que enfoca al modelo y lo pone en el registro adecuado para la tarea.
- **Restricciones** — qué stack usar, qué *no* hacer, los límites que no querés que cruce. Decir lo que está prohibido suele ahorrar tanto como decir lo que querés.
- **Ejemplos** — la pieza más subestimada. Un ejemplo de entrada y salida vale más que diez líneas de explicación: le mostrás el resultado en vez de describirlo.

Mejor que enumerarlo es verlo en acción. Comparemos el mismo pedido, flojo y filoso:

❌ *«hacé un login»* → deja todo librado al azar: el agente adivina el stack, el formato, el manejo de errores.

✅ *«agregá un endpoint POST /login que reciba email y password, valide contra la tabla users, devuelva un JWT si es correcto y un 401 si no; seguí el patrón de los otros endpoints en `routes/`«*

El segundo no le deja margen para inventar. Esa es toda la diferencia, y se nota en el resultado.

## 🧩 ¿Y si no venís de programar? Esto también es para vos

Una aclaración importante antes de seguir, porque «prompting **para código**» suena a algo que exige saber programar, y es exactamente al revés: **las piezas de un buen prompt son decisiones de producto, no de sintaxis**. Fijate en el ejemplo del login: lo que marcó la diferencia no fue ninguna palabra técnica rara, fue saber *qué* recibe (email y contraseña), *qué* pasa si está bien y *qué* pasa si está mal. Eso lo sabe cualquiera que entienda el problema —y muchas veces lo sabe *mejor* quien viene del lado del negocio o del producto que quien viene del lado del código—.

Dos ejemplos más, sin una sola línea de código, para que lo veas:

❌ *«hacé una pantalla para cargar gastos»* → el agente inventa los campos, cuáles son obligatorios y qué pasa si te olvidás de algo.

✅ *«hacé una pantalla para cargar gastos con: fecha (por defecto hoy), monto en pesos (obligatorio), categoría elegida de una lista fija [comida, transporte, servicios, otros] y una nota opcional. Si falta el monto, mostrá un aviso en rojo y no guardes.»*

❌ *«la app tiene un error, arreglalo»* → ¿cuál error? ¿dónde aparece? ¿cómo lo reproduzco?

✅ *«cuando guardo un gasto sin elegir categoría, la app se cierra. Debería avisarme ‘elegí una categoría’ y dejarme completar. Para reproducirlo: pantalla de gastos → completar solo el monto → tocar Guardar.»*

Releé los ✅: no hay nada técnico. Hay **conocimiento del problema** —qué campos importan, qué es obligatorio, qué debería pasar cuando algo sale mal—. Eso es exactamente lo que el agente no puede adivinar y vos sí sabés. Y ahí está el porqué de estos fundamentos: la anatomía de arriba es, en el fondo, un **checklist para sacarte de la cabeza lo que ya sabés del problema** y ponerlo por escrito, antes de que el agente lo rellene adivinando —y adivine mal—.

## 🔁 El ciclo Prompt → Generate → Review → Refine

Acá es donde el prompting deja de ser «una frase» y se vuelve un método de trabajo, porque la mentalidad de iteración que viste en M1 se hace concreta. Quiero que te saques de la cabeza la fantasía del prompt perfecto que devuelve el resultado perfecto a la primera: no pasa, y no hace falta que pase. Nadie escribe un pedido impecable de una sola vez; lo que sí podés hacer es cerrar el círculo rápido y aprender de cada vuelta.

El trabajo gira en cuatro tiempos:

- **Prompt** — pedís, lo más claro que puedas, con las piezas de la anatomía que la tarea necesite.
- **Generate** — la IA produce. Este es el paso barato: dejala trabajar.
- **Review** — mirás de verdad lo que vino. Y subrayo *de verdad*, porque acá es donde la mayoría afloja y acepta a ciegas; acordate del intern poderoso pero no confiable.
- **Refine** — ajustás el prompt o pedís correcciones puntuales, y volvés a arrancar la rueda.

Cada vuelta te acerca a lo que querías. Y prestá atención a esto: el paso de review no es un trámite, es el momento exacto en el que vos —tu criterio, tu experiencia— entrás a la ecuación. Es lo que te separa de alguien que solo copia y pega respuestas. Sin ese paso no estás vibecodeando, estás apostando.

## 🎚️ De vago a preciso: la técnica que más mueve la aguja

Si hay una sola práctica de prompting que te va a hacer mejor rápido, es aprender a reescribir un pedido flojo en uno filoso:

❌ *«mejorá esta función»* → no dice nada: ¿mejorar qué, la performance, la legibilidad, el manejo de errores? El agente elige por vos, y casi nunca lo que tenías en la cabeza.

✅ *«refactorizá esta función para que sea más legible: separá la validación en una función aparte y poné nombres descriptivos. No cambies el comportamiento.»*

Especificaste el qué, el cómo y hasta el límite («no cambies el comportamiento»). Cuanto más preciso el pedido, menos sorpresas en la respuesta —y menos vueltas de refinamiento—.

Pensalo como pedir un café: *«un café»* te puede traer cualquier cosa, pero *«un flat white con leche descremada, para llevar»* te trae exactamente lo que querías, sin negociar. En código pasa igual: cada detalle que agregás es una decisión que le sacás de las manos al agente y te quedás vos. Con la práctica, ese pase de vago a preciso lo vas a hacer casi sin pensar, mientras escribís.

### 🔎 La muestra: el prompt de clasificación de TicketTriage

Para que lo veas aterrizado, un ejemplo real con **TicketTriage** —la app que venimos siguiendo desde M1—. Pero antes, una distinción que vale la pena tener clarísima, porque en la vida de un builder hay **dos familias de prompts**:

- Los prompts que **vos le escribís al agente para construir** el software —como el del login de más arriba—. Viven en el desarrollo: los escribís, mirás lo que sale y, si salió mal, lo corregís en la próxima vuelta del ciclo.
- Los prompts que **tu software le manda al modelo cada vez que alguien lo usa**. Viven *adentro* de la app: se escriben una vez y se ejecutan miles de veces —de madrugada, un domingo, sin ningún humano mirando la respuesta—.

El que sigue es de la **segunda familia**: no es un prompt para *desarrollar* TicketTriage, es el prompt que TicketTriage dispara **durante su uso**, cada vez que entra un ticket nuevo, para clasificarlo solo. Fijate cómo también acá cambia todo de vago a preciso:

❌ *«clasificá este ticket»* → le deja tres preguntas abiertas: ¿en qué categorías?, ¿con qué prioridad?, ¿en qué formato me lo devolvés?

✅ *«Clasificá este ticket de soporte. Categoría: una de [facturación, técnico, cuenta, otro]. Prioridad: una de [baja, media, alta]. Respondé SOLO un JSON {categoria, prioridad}. Ticket: ‘{texto}'»*

El segundo fija las opciones y el formato de salida, y por eso la respuesta es **parseable y consistente** —siempre el mismo formato, listo para que tu código lo use—, no una sorpresa distinta cada vez. Ese es exactamente el salto de vago a preciso, sobre un caso concreto.

Y notá por qué en esta familia la precisión importa **todavía más**: cuando le pedís algo al agente mientras desarrollás, vos estás ahí para revisar y corregir; el prompt que vive adentro de la app **tiene que salir bien solo, todas las veces**, porque nadie va a estar mirando cada respuesta. Un prompt vago acá no es una molestia, es un bug que tus usuarios van a sufrir. La buena noticia: la anatomía es **la misma** para las dos familias —contexto, objetivo, especificidad, restricciones, ejemplos—. Por eso esto se llama *fundamentos*: lo que aprendés hoy te sirve para dirigir al agente que construye tu app **y** para diseñar los prompts que tu app va a llevar adentro.

## 🌐 Lo mejor: vale para cualquier herramienta

Una tranquilidad antes de cerrar: todo esto es transversal. Estos fundamentos rinden igual en **Claude Code, en Copilot o en OpenCode**, porque el arte de pedir bien no depende de la herramienta. Cambia la interfaz, cambian los comandos y los atajos, pero la anatomía del buen prompt y el ciclo de iteración son los mismos en todas. Por eso es una habilidad que rinde a interés compuesto: no la estás invirtiendo en una tool que mañana queda vieja, sino en una forma de pensar el trabajo con IA. Lo que aprendas hoy te va a servir también con la herramienta que todavía no salió.

Y no te preocupes por «practicarlo» ahora en abstracto: todo esto lo vas a poner a trabajar en serio en el **primer ejercicio del módulo**, que viene enseguida —ahí vas a dirigir a la IA con estas piezas sobre algo tuyo—. El prompting es pedir bien; pero hay algo todavía más determinante que cómo pedís: **qué información tiene el agente a la vista cuando trabaja**. Eso es el context engineering, y es —para mí— el corazón de todo el módulo. Vamos. ➡️
