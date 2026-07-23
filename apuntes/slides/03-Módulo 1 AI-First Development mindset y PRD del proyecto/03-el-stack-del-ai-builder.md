---
titulo: "El stack del AI Builder"
capitulo: "03-Módulo 1 AI-First Development mindset y PRD del proyecto"
orden: 3
source: "apuntes/slides/00-raw/03-Módulo 1 AI-First Development mindset y PRD del proyecto/03-El stack del AI Builder – MUG.html"
source_sha256: 19d0d9a326c1a5b7
extraido: 2026-07-16
---

# El stack del AI Builder

Ya tenés la cabeza en su lugar: sabés que tu trabajo ahora es dirigir, revisar y juzgar. La pregunta natural que sigue es *¿dirigir con qué?*. En esta lección abrimos la caja de herramientas y miramos el equipo con el que vas a trabajar todo el curso. 🗺️

Pero antes una aclaración, porque marca el espíritu de la lección: no vengo a venderte cuál es «la mejor». Vengo a darte **el mapa** para que no te pierdas, y para que entiendas que cada herramienta es buenísima *para algo*. El detalle profundo de cada una llega en los módulos 4, 5 y 6, donde las vas a usar a fondo. Hoy lo que necesito es que les agarres la fisonomía y, sobre todo, que entiendas el eje que confunde a casi todo el mundo cuando arranca.

## 🧰 El equipo de trabajo

Son cuatro piezas, y conviene que las distingas bien. **Claude Code** es un agente que vive en la **terminal** —una TUI, una interfaz de texto— y es la herramienta principal del curso: potente, directa, sin la distracción del editor de por medio. **GitHub Copilot** nació **dentro de VS Code** (su *agent mode*, pegado a tu cursor), pero también tiene un **CLI de terminal** — y en este curso lo vamos a usar por **CLI**, igual que a los otros dos, para que la experiencia sea pareja entre las tres herramientas. **OpenCode** es el tercer agente, también de **terminal**, pero con dos particularidades que lo hacen especial: es **open-source** y **agnóstico de modelo**, o sea que le podés enchufar el proveedor de IA que quieras en lugar de quedar atado a uno. Y por debajo de todo está **VS Code**, que funciona como el **hub** donde estas piezas se encuentran.

## 🖥️ El eje que conviene entender: terminal/CLI vs IDE

En el ecosistema, un agente puede vivir en dos lados: en la **terminal** (una interfaz de texto, una TUI/CLI —como Claude Code y OpenCode—) o **dentro del editor** (como el *agent mode* de Copilot en VS Code). Copilot nació en el IDE, pero —como casi todas estas herramientas hoy— también tiene su CLI.

Si venís de pasar el 100% de tu vida adentro de un IDE, trabajar con un agente de **terminal** te va a chocar un poco al principio, y está bien: es otro paradigma. Pensalo así: el agente de terminal opera sobre tu proyecto como un colaborador con acceso a la consola —corre comandos, lee y escribe archivos, ejecuta tus tests— sin una interfaz gráfica de por medio. **En este curso vamos a usar los tres por terminal/CLI**, justamente para que la experiencia sea pareja y te concentres en el método, no en la herramienta. El día de mañana, con el criterio formado, elegís dónde te sentís más cómodo.

## ⚖️ Con qué lente compararlas

Cuando llegue el momento de elegir, no lo vas a hacer por moda sino por criterio. Te dejo de antemano los ejes que de verdad importan, para que mientras las uses las vayas mirando con esta lente: si la herramienta apenas **autocompleta** líneas o si realmente **ejecuta tareas completas** de forma agéntica; si está **atada a un proveedor** o es **agnóstica** y te deja cambiar de modelo; cómo es su **pricing y sus cuotas** (y cuán fácil es quemarlas); y, sobre todo, **para qué brilla** cada una. No memorices un ranking: aprendé a leer estas dimensiones, que es lo que te va a servir cuando salga la próxima herramienta el mes que viene.

## ❓ «¿Y cuál uso?» — la respuesta llega al final, a propósito

Sé que la pregunta te quema, pero te la voy a responder recién al terminar el **Módulo 7**, y no por capricho. Para entonces vas a haber construido **la misma app con las tres**, y esa respuesta no te la va a dar mi opinión: te la va a dar tu propia experiencia. Por ahora resistí la tentación de coronar una favorita antes de probarlas en serio. Te doy el mapa; el veredicto lo escribís vos.

## 🧩 Un adelanto que conviene tener en el radar

Para cerrar, sacate una idea de la cabeza: estos agentes **no son una cajita de chat**. Son plataformas que se extienden con piezas reutilizables —**skills** (workflows que empaquetás una vez y el agente invoca solo), subagents, hooks y MCP—. Hoy solo te los nombro para que el término no te suene a chino más adelante. Los **skills los vas a practicar en el Módulo 3** y la **orquestación de todas esas piezas en una máquina de estados, en el Módulo 5**. Es el corazón de la parte avanzada del curso.

## 💡 Para aplicar

Hacé una predicción y guardala: de Claude Code, Copilot y OpenCode, ¿cuál creés que vas a preferir, y por qué? Anotalo en una línea. Al terminar el Módulo 7 —cuando hayas construido lo mismo con las tres— volvé a leerla y fijate si le pegaste. Vas a aprender tanto de tu acierto como de tu error.

Con el mapa de herramientas claro, lo que sigue es aprender a **dirigirlas y a ponerles límites**: los guardrails. Empezamos por el primero y más amable, los archivos de contexto. ➡️
