---
titulo: "Anti-patterns y errores comunes"
capitulo: "05-Módulo 3 Construí con red Git skills y disciplina"
orden: 10
source: "apuntes/slides/00-raw/05-Módulo 3 Construí con red Git skills y disciplina/10-Anti-patterns y errores comunes – MUG.html"
source_sha256: cec4a8ed901a7dd4
extraido: 2026-07-30
---

# Anti-patterns y errores comunes

Acabás de construir tu app y, si te pasó lo que le pasa a todos, sentiste las dos caras del vibecoding: la velocidad embriagante… y ese momento en que algo empezó a doler. Esta lección le pone **nombre** a lo que viviste. Porque vibecodear rápido es fácil —cualquiera le saca velocidad a un agente en cinco minutos—; vibecodear *bien* es lo que separa a un builder del que improvisa. Y la mejor forma de hacerlo bien es reconocer las formas típicas de hacerlo mal, para verlas venir la próxima vez. 🚧

## 🐛 Los anti-patterns clásicos

Hay un puñado de errores que se repiten una y otra vez, sin importar el lenguaje ni la herramienta. Todos comparten una misma raíz que te voy a revelar al final de la lista, pero primero conviene verlos uno por uno, con nombre y apellido, porque lo que se nombra se reconoce:

- **Prompt improvisado.** Pedir vago y esperar magia, en vez de aplicar la anatomía de prompt que vimos en la L3. Un «hacé el login» a secas deja que el agente invente el cómo, el dónde y el con-qué; después te sorprende que la solución no se parezca en nada a lo que tenías en la cabeza. El agente no adivina tu contexto: te devuelve exactamente el promedio de lo que le pediste.
- **Exceso de confianza.** Asumir que si compila, está bien. La IA es experta en producir código que *parece* correcto: nombres prolijos, estructura razonable, cero errores de sintaxis… y una lógica que falla en el segundo caso de uso. Que pase el compilador no dice nada sobre si hace lo que necesitás; solo dice que está bien escrito.
- **Aceptar sin leer.** Apretar «aceptar» en cada diff sin mirarlo. Es el pecado capital del vibecoding, y el más grave de la lista, porque desactiva el único control de calidad que tenés. Acordate del marco de siempre: la IA es un intern poderoso pero no confiable; nadie le firma el trabajo a un intern sin leerlo.
- **Código stale.** Seguir trabajando con contexto viejo y dejar que el agente decida sobre convenciones que ya cambiaron. Es el *context rot* de la L4, ahora en su versión cotidiana: renombraste una función hace media hora, pero el agente sigue usando el nombre anterior porque en su contexto todavía existe. El síntoma clásico es el agente «peleando» contra decisiones que ya tomaste.
- **Hacks frágiles.** Aceptar soluciones que funcionan de milagro y se rompen al primer cambio. Ese `if` raro que arregla el bug hoy pero nadie sabe por qué, ese timeout mágico de 500ms, ese workaround que «por ahora sirve». Funcionan hasta que tocás lo de al lado, y entonces se caen sin dar la cara.

¿Ves el hilo que los une? En todos, el error es el mismo: **delegar el juicio**, no solo el tipeo. Improvisar el prompt, confiar de más, aceptar a ciegas, arrastrar contexto viejo o tapar con hacks son cinco maneras distintas de correr la vista del volante. Y esa es, en una frase, la regla que te mantiene a salvo de los cinco a la vez —el builder delega el tipeo, pero el juicio se queda con él, siempre—.

## 🧱 El «muro de los 3 meses»

Ahora el más importante de todos, porque no es un error puntual sino un patrón de fondo, y conecta con todo el resto del curso. El vibecoding sin disciplina tiene una trayectoria conocida: al principio volás 🚀, todo sale rápido y la sensación es de superpoder. Pero por debajo, sin que lo veas, la **deuda se va acumulando** —código que nadie entiende, cero tests, ninguna estructura—. Y en algún punto, que la gente bautizó como **«el muro de los 3 meses»**, el proyecto se vuelve **inmanejable**: cada cambio rompe dos cosas, tocar algo da miedo, y avanzar pasa de volar a arrastrarse.

Quiero que leas bien esto, porque es la tesis que sostiene el curso entero: ese muro **no es un argumento contra la IA**, es un argumento contra **la IA sin método**. Y es exactamente el problema que viene a resolver el **Spec-Driven Development del Módulo 4**: cuando sentís que el vibe ya no alcanza, *formalizás*. No es casualidad que en M4 reconstruyas tu app con specs —vas a estar resolviendo, con método, justo el dolor que el vibecoding puro te hizo sentir—.

## 📈 Over-building antes de validar

Hay un último clásico que merece su lugar: construir de más antes de saber si la idea sirve. Con la IA la tentación es enorme, porque cada feature «sale gratis y rápido» —le pedís una pantalla más, un botón más, una integración más, y aparecen en minutos—. Pero una feature que nadie pidió es deuda igual que cualquier otra, solo que con la excusa de que fue barata: hay que mantenerla, testearla y arrastrarla en cada cambio futuro, sirva o no. La consigna es vieja y sigue valiendo: **validá primero, construí después.** Por suerte, las reglas de tu proyecto —app chica, una a tres features— ya te protegen bastante de este pozo; respetalas.

## 🧭 Cómo detectarlos a tiempo

La buena noticia es que todos estos errores avisan, si sabés escuchar las señales. La clave está en tener un puñado de preguntas a mano y hacértelas cada tanto, sin esperar a que el problema explote:

- **¿Aceptaste los últimos diffs sin leerlos?** Frená y revisá. Cada diff que entró sin mirarse es código del que no te hacés cargo, y la deuda se paga con intereses.
- **¿Hace rato que no commiteás algo que funcione?** Probablemente estés acumulando deuda sin darte cuenta: el estado «verde» quedó lejos y no tenés a dónde volver si algo se rompe.
- **¿La IA viene proponiendo parches sobre parches?** Es hora de resetear el rumbo, como vimos en *Iterar con red*. Cuando el agente arregla su propio arreglo, la señal no es que le falta un intento más: es que el enfoque se agotó.
- **¿Te encontraste agregando features que no están en el PRD?** Eso es over-building, frená. Si no estaba en el plan, preguntate por qué lo estás construyendo antes de seguir.

Tener estas preguntas como chequeo mental periódico es, en sí mismo, una de las disciplinas más valiosas del builder: no evita que aparezcan las señales, pero hace que las veas cuando todavía son baratas de corregir.

Con los errores identificados y el muro entendido, cerramos el ciclo del vibecoding: dos versiones de tu app, un método cada vez más afilado, y un dolor con nombre que ya sabés a dónde te lleva. Vamos al **repaso del módulo**. ➡️
