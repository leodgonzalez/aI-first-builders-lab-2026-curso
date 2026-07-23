---
titulo: "Qué es Vibecoding (y qué no)"
capitulo: "04-Módulo 2 Vibecoding profesional"
orden: 2
source: "apuntes/slides/00-raw/04-Módulo 2 Vibecoding profesional/02-Qué es Vibecoding (y qué no) – MUG.html"
source_sha256: 0591f065589488d2
extraido: 2026-07-16
---

# Qué es Vibecoding (y qué no)

El término «vibecoding» se puso de moda, y como toda palabra de moda, se entiende mal. Para muchos es sinónimo de «tirarle prompts a un chat y pegar lo que sale», y esa confusión es justo la que te puede arruinar el módulo entero. Así que antes de practicarlo, dejemos clarísimo qué es y, sobre todo, qué *no* es —porque en esa diferencia se juega todo lo que separa a un builder de alguien que solo improvisa—. 🎯

## 📜 De dónde viene el término

Conviene arrancar por el origen, porque explica media confusión. El término es nuevo: lo acuñó **Andrej Karpathy** —cofundador de OpenAI y ex director de IA de Tesla, una de las figuras más respetadas del campo— en **febrero de 2025**, en un posteo que se volvió viral en cuestión de días. Su definición original era casi una provocación:

> *«Hay una nueva forma de programar que llamo ‘vibe coding’, donde te entregás del todo a las vibras, abrazás los exponenciales y te olvidás de que el código siquiera existe.»*

Vale la pena detenerse ahí, porque es la clave de toda la lección. En su versión original, el vibe coding era **exactamente lo que en un minuto te voy a decir que NO hagas**: aceptar todo sin leer, no entender lo que corre, dejarse llevar por la corriente. Y ojo: para lo que Karpathy describía —un experimento de fin de semana, un jueguito descartable, un prototipo que si explota no pasa nada— está perfecto. El problema vino después: el término explotó, y mucha gente lo adoptó como forma de trabajar **en serio**, en proyectos reales, arrastrando todas las consecuencias que vamos a ver en este módulo (el famoso «muro de los 3 meses»).

Lo que hacemos en este curso es la **evolución madura** de esa idea. Tomamos la velocidad que Karpathy celebraba y le devolvemos el control que su versión original tiraba por la borda. A eso le llamamos **vibecoding profesional**. Por eso la distinción de qué es y qué no es no es un detalle de vocabulario: es, literalmente, la diferencia entre el término de moda y el oficio que vas a aprender acá.

## 💡 Qué es realmente

Vibecoding es **dirigir a la IA hacia un resultado**, iterando con ella, en lugar de pedir pedacitos de código sueltos y armarlos vos a mano. Le das contexto, le marcás un objetivo y vas guiando el camino: pedís, mirás lo que vino, corregís el rumbo, seguís. Vos sos el director de la película; la IA es la que teclea.

La distinción fina, la que de verdad importa, es esta: el vibecoder **mantiene el control del resultado completo** —la feature funcionando, el comportamiento correcto— y no de líneas aisladas. Pensás el qué y el cómo a alto nivel, tomás las decisiones que importan, y delegás la parte mecánica de escribir. No es que te desentendés; es que trabajás un escalón más arriba.

Pensalo como pedir un plato en un restaurante en lugar de recitar la receta paso a paso. No le dictás a la cocina cada movimiento del cuchillo; le decís qué querés comer, con qué punto, qué te gusta y qué no, probás lo que sale y ajustás. La cocina hace el trabajo fino, pero el criterio de qué está bien y qué vuelve a la parrilla sigue siendo tuyo. Eso es dirigir: no ejecutás cada tarea, pero sos dueño del resultado.

## 🚫 Qué no es (y acá está la trampa)

Por contraste se entiende todavía mejor. Vibecoding **no es** ninguna de estas tres cosas:

- **No es copiar y pegar respuestas de un chat sin entender qué hacen.** Eso es simplemente acumular código ajeno en tu proyecto: funciona hoy por casualidad y el día que se rompe no tenés idea de por dónde empezar, porque nunca fue tuyo.
- **No es aceptar a ciegas todo lo que la IA propone**, apretando «ok» en cada diff sin leerlo. Cada cambio que dejás pasar sin mirar es un problema que firmaste sin leer; la IA se equivoca, alucina APIs que no existen y toma atajos que vos no habrías tomado.
- **No es, bajo ningún concepto, un reemplazo de tu criterio.** Seguís siendo vos quien decide la arquitectura, la intención y el estándar de calidad. La IA propone; vos disponés.

Lo resumo con una imagen que se queda pegada: el **builder dirige y juzga**; el **prompter pide y reza** 🙏. La diferencia no está en la herramienta ni en lo ingenioso del prompt, está en quién mantiene el control. Este módulo entero está diseñado para que salgas siendo lo primero.

## ⚖️ El enfoque híbrido: cuándo sí y cuándo no

Ahora, seamos honestos, porque el vibecoding no es la respuesta para todo y conviene que lo sepas desde hoy. Empecemos por el dato de adopción: según la Stack Overflow Developer Survey 2024, alrededor del **62% de los desarrolladores ya usa herramientas de IA**. Pero ese número mide *cuántos las usan*, no *cuánto les creen* —y ahí está la clave—: la confianza es mucho más baja, y en la práctica el uso es **híbrido y selectivo**. La mayoría no acepta el output a ciegas: lo revisa y lo edita antes de mandarlo a cualquier lado serio.

Esa estadística esconde la regla práctica que quiero que adoptes. El vibecoding brilla cuando el costo de equivocarse es bajo y la velocidad lo es todo:

- Cuando **prototipás** o armás un MVP para validar una idea rápido.
- Cuando construís una **herramienta interna** que van a usar cuatro personas de confianza.
- Cuando **explorás** un enfoque nuevo solo para ver si pisa antes de comprometerte.

Pero cuando el código va camino a producción —donde lo tocan usuarios reales y un bug cuesta plata o reputación— le sumás rigor: specs, tests, code review. No es «vibe para todo» ni «vibe nunca». Es **la herramienta correcta para el momento correcto**, y parte de tu madurez como builder es saber en cuál de los dos estás parado.

## 🔭 Un deslinde que vas a agradecer más adelante

Es muy probable que ya te estés preguntando: *«¿y esto en qué se diferencia del Spec-Driven Development?»*. Excelente pregunta, y la respuesta completa es del **Módulo 4**, así que no te la voy a robar acá. Pero te dejo la semilla para que la tengas presente:

- el vibecoding **improvisa hacia el resultado**, ajustando sobre la marcha;
- el SDD **parte de un spec que manda** y guía la construcción desde un contrato escrito.

Uno descubre el camino caminándolo; el otro lo dibuja antes de dar el primer paso. Son dos herramientas distintas para dos momentos distintos. En este módulo nos dedicamos a dominar la primera a fondo.

Con la definición clara y la trampa desactivada, vamos a la habilidad base que hace que todo lo demás funcione: **el prompting para código**. ➡️
