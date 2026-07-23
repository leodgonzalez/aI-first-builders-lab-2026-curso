---
titulo: "Context engineering: el corazón del vibecoding"
capitulo: "04-Módulo 2 Vibecoding profesional"
orden: 4
source: "apuntes/slides/00-raw/04-Módulo 2 Vibecoding profesional/04-Context engineering_ el corazón del vibecoding – MUG.html"
source_sha256: f1564599cdcafb16
extraido: 2026-07-16
---

# Context engineering: el corazón del vibecoding

Si tuviera que elegir **una sola** habilidad de todo el módulo para que te lleves, sería esta, sin dudarlo. Y arranco conectando con algo que ya traés: en M1, en *Gestión de contexto y costos*, conociste el **kit de supervivencia** —la ventana finita, el context rot, los comandos `/context`, `/compact`, `/clear`, `/usage`— para no quemar la cuota ni confundir al agente. Eso era el equipo de primeros auxilios. Acá venimos a lo que te prometí allá: la **disciplina profunda** que hay detrás. 🧠

## 🪟 Antes de la disciplina, lo esencial: qué es «el contexto»

Frenemos un segundo, porque en esta lección voy a decir «contexto» doscientas veces y necesito que todos —vengas de donde vengas— tengamos la misma imagen mental. Va sin tecnicismos:

Un modelo de IA no «sabe» nada de vos ni de tu proyecto, y **no recuerda nada entre conversaciones**. Cada vez que le pedís algo, lo único que existe para él es **lo que tiene delante en ese preciso momento**: tu pedido, los archivos que le pasaste, lo que se habló antes en esa misma conversación. Ese «todo lo que tiene delante» es la **ventana de contexto**.

La mejor imagen que conozco: un colaborador brillante —el mejor que contrataste en tu vida— pero con **amnesia total**, que solo puede leer los papeles que hay sobre su mesa. Con lo que está en los papeles, trabaja de maravilla. Y de ahí salen las dos consecuencias que quiero que sientas en el cuerpo:

- **Lo que no está sobre la mesa, para él NO EXISTE.** Ni tu proyecto, ni las decisiones de ayer, ni el archivo que te olvidaste de pasarle. No es que «le cueste recordarlo»: no existe.
- **Si le falta un dato, no te dice «no sé».** Rellena el hueco **inventando, con total confianza y muy buena prosa**. En una charla casual es una anécdota graciosa; cuando está escribiendo el código que va a manejar los datos de tus usuarios, es un problema serio.

¿Y cuánto entra en esa mesa? Depende del modelo, y acá van dos datos que importan:

- **La ventana se mide en tokens** (pedacitos de texto; una palabra suelen ser 1-2 tokens) y **cada modelo tiene un tamaño distinto**: algunos andan por los ~200.000 tokens —unas 300 páginas—, otros llegan al millón. Suena enorme… hasta que caés en que un proyecto de software real puede medir **millones** de tokens: tu proyecto entero **nunca entra**. Siempre hay alguien decidiendo qué entra y qué queda afuera; si no decidís vos, decide el azar.
- **Más grande no es mejor.** Esta es la parte contraintuitiva: los modelos rinden mejor con la mesa **enfocada** que con la mesa llena. A medida que la ventana se carga de cosas irrelevantes, la calidad **se degrada**: el modelo se distrae, mezcla, y lo importante queda enterrado en el medio, donde menos atención recibe.

Ahora juntá las piezas y vas a entender por qué digo que esta es *la* habilidad del módulo: cuando desarrollás software con IA, esa ventana es **el 100% de lo que el agente sabe de tu proyecto** en el momento exacto en que escribe código. La sesión mágica que te resolvió todo en diez minutos y la sesión desastrosa que «alucinó» un archivo inexistente **corrían el mismo modelo**: la diferencia estuvo en qué había —y qué faltaba, y qué sobraba— sobre la mesa. **Quien controla la ventana, controla el resultado.** De eso se trata todo lo que sigue.

## 📐 Qué es, con precisión

Vale la pena una definición firme, porque el término se usa mucho y se entiende poco:

> **Context engineering** es la disciplina de decidir, a propósito, **qué información entra en la ventana de contexto del agente en cada momento —y qué se queda afuera—** para que produzca el mejor resultado posible.

Desarmemos los términos, porque cada uno importa:

- La **ventana de contexto** es todo lo que el modelo «tiene a la vista» cuando responde: tu pedido, los archivos que le pasaste, la conversación previa, los resultados de las herramientas que corrió. Se mide en **tokens** (pedacitos de texto) y tiene un **tope**: no es infinita.
- «**A propósito**» es la palabra clave. Todo el mundo *tiene* un contexto cuando trabaja con un agente; pocos lo *diseñan*. La diferencia entre una sesión que vuela y una que alucina rara vez está en el prompt: está en qué había en esa ventana en el momento de trabajar.

No es un truco ni una moda: es el **oficio central del builder profesional**, y la industria ya lo reconoce como disciplina propia. La propia Anthropic lo describe como *«la progresión natural del prompt engineering»*.

## 🔄 De «prompt engineering» a «context engineering»

Durante un tiempo todo el mundo hablaba de «prompt engineering», como si el secreto estuviera en encontrar la frase mágica. Esa etapa quedó atrás. La disciplina maduró y la subsumió. Ojo, el prompt no desapareció —sigue siendo la base—, pero el juego se corrió de lugar: ya no se trata de tener el prompt más ingenioso, sino de lograr que el agente tenga **la información justa, en el momento justo, sin ruido alrededor**.

¿Por qué este cambio de foco? Por la razón que ya tocaste en M1: el contexto de un modelo es **finito y caro**. No es un balde sin fondo. Si lo llenás de archivos irrelevantes, de conversación vieja, de detalles que no vienen al caso, el resultado se degrada —el agente se distrae, mezcla cosas, pierde el hilo—. Pensalo como un escritorio de trabajo: si lo tapás con todas las carpetas de la oficina, no encontrás la que necesitás; si dejás arriba solo las dos hojas del problema de hoy, trabajás enfocado. La novedad de esta lección es que vamos a dejar de *reaccionar* a ese límite y a empezar a *trabajarlo*.

## 🎛️ Las cinco palancas

Diseñar el contexto, en la práctica, es trabajar cinco palancas. Conviene tenerlas claras como un set de herramientas —no son reglas abstractas, son las perillas que vas a estar girando todo el tiempo mientras construís—:

- **Selección** — qué archivos e información le das al agente y —tan importante como eso— cuáles le ocultás. Es la decisión de fondo: elegir las dos o tres piezas que importan para la tarea de hoy, y dejar el resto afuera.
- **Compresión** — resumir lo largo para que entre lo que de verdad importa. En vez de pegar un log de 300 líneas, le das las 5 que muestran el error; en vez del hilo entero, un resumen de las decisiones que quedaron firmes.
- **Ordenamiento** — poner lo más relevante donde sea más accesible, porque no todo pesa igual. Lo que va primero y lo que va último marca más que lo que queda enterrado en el medio; ubicá ahí lo que no querés que se pierda.
- **Aislamiento** — separar tareas para que no se contaminen entre sí. Terminaste el login y arrancás el checkout: no dejes que la conversación de uno se filtre en el otro y lo ensucie.
- **Formato** — estructurar la información de modo que el agente la procese fácil. Una lista con viñetas, una tabla o bloques de código bien marcados se leen mejor que un párrafo corrido con todo mezclado.

De las cinco, la que más rinde al principio es la **selección**, así que apoyate ahí primero: la mayoría de las sesiones que se descarrilan no es porque les faltó contexto, sino porque les sobró.

## 🧰 De los comandos al hábito deliberado

Los comandos ya los conocés de M1, así que no los reintroduzco: lo que cambia acá es **cómo los usás**. En M1 eran higiene para no fundirte la cuota; ahora son decisiones de diseño del contexto. El mismo comando, otra intención. Repasemos qué hace cada uno y cómo lo usa un builder:

- **`/context`** — te muestra **cuánto de la ventana estás ocupando y con qué**. Tenelo a la vista no solo para no saturarte, sino para *leer* qué cargó el agente y preguntarte si de verdad hace falta. Es tu radar.
- **`/compact`** — **comprime** la conversación: conserva lo importante y descarta el relleno. Usalo **a propósito** cuando pasás el ~60% de la ventana —antes de que se sature, no después—, en vez de dejar que la auto-compactación decida por vos, que es opaca y a veces te tira justo lo que necesitabas.
- **`/clear`** — **borra el contexto y arranca de cero**. No es solo para «ordenar»: es la palanca de **aislamiento** en acción. Cerraste un tema, limpiás, entrás fresco al siguiente sin arrastrar lo anterior.

Y sumá un hábito que es puro context engineering: trabajá por *chunks* —por función, por clase, por módulo— en lugar de meterle el repo entero de una. Darle todo no es darle más ayuda, es darle más ruido.

## ⚠️ Context rot, ahora en la mesa de trabajo

El context rot ya lo nombraste en M1 —**el contexto viejo (stale) es PEOR que no tener contexto**—. Acá quiero que lo veas con las manos en el código, porque cuando estás construyendo pega distinto. Uno tiende a pensar que más información siempre suma. Falso. Si el agente arrastra convenciones o decisiones que ya cambiaron mientras vos seguías iterando la feature, no se queda dudando —produce errores con absoluta confianza, apoyándose en algo que dejó de ser cierto—. Es como pedirle a alguien que siga un mapa de una ciudad que ya cambió sus calles: no se detiene a preguntar, dobla seguro por donde antes había paso y hoy es pared.

Por eso, en pleno build, `/clear` es tu mejor amigo más seguido de lo que creés: muchas veces, después de tres o cuatro vueltas sobre una feature, la jugada más inteligente no es agregar contexto, es **borrar el que ya no aplica** y volver a entrar limpio con solo los archivos que importan ahora. No es perder lo hecho —el código ya está en el repo—; es soltar la conversación sucia que lo rodea.

## 🧭 Dos técnicas que suman y casi nadie aprovecha

Te dejo dos técnicas que te van a poner por delante de la media. Las dos atacan un problema distinto:

- **Instrucciones negativas explícitas** — decir *«NO uses la librería X»* es muchísimo más confiable que esperar que el agente lo deduzca por omisión. El silencio no es una instrucción: si no le decís que evite algo, va a asumir que está permitido y lo va a usar en el peor momento. Lo explícito le gana a lo implícito; si hay algo que no querés, escribilo. Eso sí, con criterio: reservalas para lo que de verdad importa, porque una lista interminable de «NO hagas esto» también satura el contexto y termina jugando en contra.
- **Verificación de rumbo** (algunos la llaman *checkpoint injection*) — intercalar chequeos mientras el agente avanza. Sirve para un problema sutil y traicionero: que resuelva *bien* un subproblema pero en la **dirección equivocada**, alejándose prolijamente de lo que querías. Cada tanto frenás y confirmás el rumbo antes de dejarlo seguir —como un piloto que corrige el curso cada varios kilómetros en vez de descubrir al final que aterrizó en otro país—.

### 🔎 La muestra: selección de contexto en TicketTriage

Cierro con una historia en **TicketTriage** —la app que venimos siguiendo desde M1—, porque esta palanca se entiende mejor vivida que explicada. La tarea del día: mejorar el **borrador de respuesta** que la IA arma para cada ticket, que está saliendo demasiado genérico. El código del proyecto, como el de cualquier proyecto real, tiene varias partes:

- la lógica de IA,
- los modelos de datos,
- las plantillas de la interfaz,
- los tests.

**Primera sesión —la que haría cualquiera antes de esta lección—:** abrís el agente y le das el proyecto entero, «total, cuanta más información tenga, mejor me va a ayudar». ¿El resultado? El agente te propone retocar una plantilla de la interfaz, sugiere renombrar un campo del modelo de datos «ya que estamos»… y el borrador sigue igual de genérico. No es que el modelo sea malo: le tapaste la mesa con carpetas que no tenían nada que ver con la tarea, y se puso a trabajar sobre lo que vio.

**Segunda sesión:** `/clear`, y esta vez entrás con la pregunta de context engineering hecha de antemano: *¿qué necesita el agente para ESTA tarea, y nada más?* La respuesta es **solo dos piezas**: el archivo donde vive la **lógica de IA** (ahí se arma el borrador) y la **base de conocimiento** (esa `kb.md` que ya viste en el PRD de TicketTriage en M1, de donde el borrador saca la información). Los modelos, las plantillas y los tests no tienen nada que ver con redactar mejor: afuera. Ahora sí, el agente va derecho al punto: detecta que el borrador no está citando la información concreta de la `kb.md` y lo corrige.

Mismo modelo, mismo pedido, **otra mesa**. La decisión que más mejoró el resultado no fue ningún prompt genial: fue elegir esas dos piezas y dejar el resto afuera. Eso **es** la palanca de *selección* en acción.

Con esto ya no solo *manejás* el contexto: lo **diseñás**. Y antes de ponerlo a trabajar sobre algo tuyo, te falta una sola pieza del equipamiento: las **instrucciones permanentes** que el agente lee solo, en cada sesión, sin que se las repitas —los **guardrails**—. Con esa pieza puesta, todo lo que hagas en los ejercicios del módulo arranca con ventaja. ➡️
