---
titulo: "Gestión de contexto y costos"
capitulo: "03-Módulo 1 AI-First Development mindset y PRD del proyecto"
orden: 7
source: "apuntes/slides/00-raw/03-Módulo 1 AI-First Development mindset y PRD del proyecto/07-Gestión de contexto y costos – MUG.html"
source_sha256: 4d6848303ea46e9e
extraido: 2026-07-16
---

# Gestión de contexto y costos

Esta es de las lecciones más prácticas para tu bolsillo y tu paciencia, aunque no escribas una línea de código. Un agente mal manejado es perfectamente capaz de **fundirte la cuota Pro en una sola clase** —no es exageración, pasa todo el tiempo— y, peor todavía, de **volverse más tonto** a medida que la conversación se alarga. Las dos cosas tienen la misma raíz: el **contexto**. Entender qué es y cómo manejarlo es lo que separa a quien le saca jugo al agente de quien se frustra y abandona. 💸

## 🧠 Qué es la ventana de contexto

Pensá en el contexto como la **memoria de trabajo** del agente: todo lo que «tiene presente» en este momento para responderte. Ahí entra tu mensaje, las instrucciones de sistema, los archivos que abrió, los resultados de las herramientas que usó y **toda la conversación previa**. Esa memoria se mide en **tokens** (pedacitos de texto: una palabra es, más o menos, uno o dos tokens) y tiene un **tamaño máximo**: la *ventana de contexto*.

Dos consecuencias que hay que tener clarísimas:

- **La ventana es finita.** Por grande que sea, se llena. Cuando se llena, algo se tiene que ir —y si no lo manejás vos, lo maneja la herramienta por su cuenta, no siempre como querrías—.
- **Todo lo que entra, se procesa cada vez.** El modelo no «recuerda» gratis lo de antes: en cada turno vuelve a leer el contexto entero. Más contexto = más trabajo en cada respuesta.

## 🗑️ Contexto viejo es peor que poco contexto

Acá hay algo contraintuitivo que conviene grabarse, porque es la causa #1 de que un agente «se ponga raro». **Más contexto no es mejor.** Cuando arrastrás una conversación larga —con tareas viejas, archivos que ya no importan, intentos fallidos que quedaron dando vueltas— el agente tiene que repartir su atención entre lo relevante y la basura acumulada. El resultado: se confunde, mezcla cosas, retoma decisiones que ya habías descartado.

A este fenómeno se lo suele llamar **«context rot»**: la calidad de las respuestas se degrada a medida que el contexto se ensucia. La moraleja es fuerte y vale para todo el curso: **cuando empezás una tarea nueva, arrancá con el contexto limpio.** Un agente con poco contexto bien curado le gana siempre a uno con mucho contexto sucio.

## 💰 Por qué esto es plata (y tiempo)

Cada token que el agente procesa **cuesta** —en tu cuota Pro o en dinero, según el plan—. Y como en cada turno se re-procesa todo el contexto, una conversación inflada no solo confunde: **multiplica el costo de cada interacción**. Una sesión larga y desprolija puede quemar en una hora lo que una sesión enfocada gasta en un día. Por eso manejar el contexto no es manía de ordenado: es administrar un recurso que se agota.

## 🧰 El kit de supervivencia: cuatro comandos

La buena noticia es que controlarlo es fácil una vez que conocés el equipo básico. En Claude Code son cuatro comandos, y conviene que los incorpores como reflejo:

- **`/context`** — te muestra **cuánto contexto estás usando ahora mismo**. Es tu tablero: tenelo a la vista para saber si estás holgado o al límite.
- **`/compact`** — **comprime** la conversación cuando se hizo larga: conserva lo importante y tira el relleno. Ideal cuando venís bien pero la charla ya pesa.
- **`/clear`** — **arranca de cero**. Es más útil de lo que parece: cuando empezás algo nuevo, limpiá y empezá fresco en vez de arrastrar lo anterior. Combate directo al *context rot*.
- **`/usage`** — te deja **chequear cuánto llevás consumido** de tu cuota. El termómetro para no llevarte sorpresas.

> 💡 **La regla práctica que resume todo:** trabajá en **sesiones enfocadas** (una tarea por sesión), **limpiá seguido** (`/clear` al cambiar de tema) y **comprimí cuando se alargue** (`/compact`). Mirá el tablero (`/context`) cada tanto y el termómetro (`/usage`) cuando dudes.

## 🛠️ Tu turno: tomale el pulso a tu contexto

⏱️ **Tiempo estimado:** ~5 min · 📦 **Entregable:** haber visto tu consumo real al menos una vez.

1. En una sesión de Claude Code, comenzá a chatear diciendole que querés hacer consultas de **[esta publicación](https://mug.org.ar/el-diferencial-es-entender-el-dominio/)** (copiá y pegá la URL) y preguntale cosas como la conclusión general, un resumen, etc.
2. Luego de unos chats, corré **`/context`** y mirá cuánto estás usando.
3. Corré **`/usage`** para ver tu consumo de cuota.
4. La próxima vez que cambies de tarea, en vez de seguir en la misma charla, hacé **`/clear`** y notá la diferencia: el agente arranca más enfocado.

> ✅ **Lo lograste cuando** sabés leer tu tablero de contexto y tenés el reflejo de limpiar al cambiar de tema.

## 🔭 Esto es solo el equipo de primeros auxilios

Ojo con una cosa: lo de hoy es **manejo de contexto** —el kit básico para no quemarte la cuota ni confundir al agente—. El **context engineering** en serio —*curar* deliberadamente qué información ve el agente y cuándo, para sacarle el máximo provecho— es una disciplina más profunda, y la vas a ver en el **Módulo 2**. Por ahora, con estos reflejos llegás entero y con cuota a la próxima etapa.

Con MCP entendido y el contexto bajo control, te queda lo más importante del módulo: **decidir qué vas a construir**. En las próximas lecciones le ponemos nombre a esa pieza —el **PRD**—: primero qué es y cómo se arma, y después escribís el de tu proyecto. ➡️
