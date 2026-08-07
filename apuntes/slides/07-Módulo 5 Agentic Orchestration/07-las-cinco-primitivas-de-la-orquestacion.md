---
titulo: "Las cinco primitivas de la orquestación"
capitulo: "07-Módulo 5 Agentic Orchestration"
orden: 7
source: "apuntes/slides/00-raw/07-Módulo 5 Agentic Orchestration/07-Las cinco primitivas de la orquestación – MUG.html"
source_sha256: f0f3cd69b37f65fa
extraido: 2026-08-07
---

# Las cinco primitivas de la orquestación

Tenés DAW corriendo en tu repo. Ahora vamos a abrirlo y ver **de qué está hecho**. 🧩

Y quiero empezar por una afirmación que a esta altura te va a servir mucho: cualquier pipeline agéntico —el de DAW, el que arme un equipo de Google, el que salga el año que viene con otro nombre— se construye con **las mismas cinco piezas**. No cinco parecidas: las mismas. Lo que cambia entre herramientas es **cómo se llama cada una y con qué sintaxis se escribe**, no qué hace ni para qué sirve.

Por eso las vemos en concepto y no como «features de Claude Code». Es lo que te va a permitir, en los Módulos 6 y 7, portar tu pipeline a otra herramienta **sin volver a aprender nada conceptual** — y es también lo que te va a permitir mirar cualquier producto agéntico del mercado y entender en treinta segundos de qué está hecho.

## 1️⃣ Skill — el *qué hace*

Una **capacidad empaquetada** que el agente invoca cuando corresponde. Ya las venís escribiendo desde el Módulo 3: tu `create-prd` fue la primera.

En un pipeline, los skills son **las acciones de cada fase**: `daw-create-spec` genera el spec, `daw-test` corre y valida la suite, `daw-security-sast` audita el código, `daw-commit` arma el commit con la convención. Están en `.claude/skills/` de tu instalación: son los dieciséis que trae DAW, escritos para encajar en las fases del pipeline. Los tuyos del M3 no los copiaste, y estuvo bien: DAW ya trae lo que el pipeline necesita. Nada te impide sumar uno propio más adelante — y fijate que el prefijo `daw-` de todos ellos está justamente para que el tuyo no tenga que pelear por un nombre.

Ahora, la pregunta interesante: **¿por qué empaquetar la acción en vez de escribirla en el prompt cada vez?** Tres razones, y las tres se sienten con el tiempo:

- **Se versiona.** El skill es un archivo en el repo. Si cambiás el criterio de cómo se arma un PRD, ese cambio queda en un commit, con fecha y con vos como autor. Un prompt que escribiste a mano el martes no deja rastro de por qué el jueves lo escribiste distinto.
- **Se repite idéntico.** El paso 4 del skill se ejecuta igual siempre. Y esto no es obsesión por el orden: es lo único que te permite **comparar**. Si el resultado cambia entre dos corridas, sabés que fue por el input, no porque escribiste el pedido con otras palabras.
- **Se audita.** Podés leer qué hace tu pipeline en cada fase abriendo cinco archivos, sin tener que reconstruirlo de conversaciones viejas.

## 2️⃣ Subagent — el *especialista con contexto limpio*

Un agente con **su propio system prompt y su propio contexto aislado**, que se spawnea para una tarea puntual y devuelve un resultado. En DAW son los cinco que están en `.claude/agents/`: tres auditores —`daw-arch-auditor` (¿respeta la arquitectura?), `daw-sec-auditor` (¿hay riesgos de seguridad?) y `daw-module-verifier` (¿lo construido cumple el spec?)—, más `daw-impact-scanner` (¿qué más toca este cambio en el codebase real?) y `daw-implementer` (el que escribe un bloque).

Lo interesante no es que sea «otro agente» —eso es un detalle de implementación—. Lo interesante es **por qué conviene aislarlo**, y hay dos razones. La primera es la esperable; la segunda es la que importa.

**Primera: es context engineering, del Módulo 2.** Un subagent que revisa código no necesita —ni le conviene tener— los sesenta mensajes previos de la sesión principal en la cabeza. Arranca limpio, enfocado en una sola pregunta, y devuelve su veredicto sin llenar de ruido el contexto de arriba. Es eficiente en las dos direcciones.

**Segunda: nadie se corrige bien a sí mismo.** Y ésta es la razón de fondo. El agente que escribió el código **arrastra las mismas suposiciones con las que lo escribió**. Si al implementar dio por hecho que el input venía validado más arriba en la cadena, al revisar va a dar por hecho exactamente lo mismo — y no va a ver el agujero. No porque sea tonto ni descuidado: porque **para él eso no es una suposición, es un hecho de la conversación**. Está tan adentro del contexto que ya no lo ve como una decisión revisable.

Un subagent arranca sin esa conversación. Mira el código como lo miraría alguien que llega de afuera — que es exactamente lo que querés de un revisor, y exactamente lo que a los humanos nos cuesta tanto conseguir cuando revisamos nuestro propio trabajo.

## 3️⃣ Hook — el *sí o sí*

**Código que el harness ejecuta automáticamente** en momentos definidos: antes de que el agente escriba un archivo, al abrir la sesión, después de una acción. En tu instalación están en `.claude/hooks/`.

(Cuando digo «harness» me refiero al runtime que corre al agente: Claude Code, OpenCode, la extensión de Copilot. La pieza de software que está *alrededor* del modelo y decide qué se ejecuta y cuándo.)

La diferencia con el skill es **estructural**, y es la que sostiene todo lo demás:

- El **skill** lo invoca **el agente**, cuando le parece que corresponde.
- El **hook** lo corre **el harness**, siempre, **fuera del control del LLM**.

Leelo dos veces, porque en esa diferencia está todo. Un skill es una capacidad que el modelo *puede* usar. Un hook es una condición que el sistema *impone*. Uno depende de una decisión; el otro, no.

Es la primitiva que produjo el bloqueo que provocaste a propósito en el ejercicio anterior — y le dedicamos la próxima lección entera, porque es la idea más importante del módulo.

## 4️⃣ State — la *memoria*

Un archivo que **persiste en el repo** y guarda dónde está parada la máquina: en qué fase, qué gates ya se cumplieron, qué se está trabajando. Es el `.daw-state.json` que viste moverse mientras corría tu feature.

La pregunta que vale la pena hacerse acá es **por qué en disco y no «en la conversación»**, que sería lo natural. Y la respuesta es directa: porque la conversación **se compacta, se corta y se pierde**. Es el segundo modo de falla de la lección 1. Un archivo, no. Cerrás la sesión, se cae internet, te vas el fin de semana: el archivo sigue diciendo exactamente lo mismo.

Eso tiene dos consecuencias que conviene tener presentes:

- **Es la fuente de verdad del pipeline.** Si el state dice `CODE`, estamos en CODE — no importa qué recuerde el agente ni qué te parezca a vos. Cuando hay discrepancia, gana el archivo.
- **Es lo que consultan los hooks para decidir.** Y esto no es un detalle: un hook **no puede preguntarle al modelo** en qué fase estamos, porque eso sería confiar la decisión a la parte impredecible del sistema. Lee el archivo. Un dato, no una opinión.

## 5️⃣ Orquestador — el *director*

El que **lee el state, detecta la fase y enruta**: carga las reglas de esa fase **y solo esa**, habilita sus acciones y bloquea el resto. Es el `.daw/orchestrator.md` que se importa desde tu `CLAUDE.md`.

Acá vive el tercer antídoto de la lección 1: el **lazy loading**. El agente nunca ve las cuarenta reglas del pipeline juntas — ve las seis que aplican a la fase en la que está. Y no porque las otras no importen, sino por algo que ya sufriste en carne propia con tus guardrails: **una instrucción que no compite con otras treinta y nueve se cumple muchísimo mejor**.

## 🔗 La coreografía: donde está el valor real

Las cinco piezas por separado son útiles. Juntas son otra cosa. Seguí un turno completo:

1. El **orquestador** lee el **state** y determina: *«estamos en CODE»*.
2. Carga **solo** las reglas de CODE y habilita **solo** los skills de esa fase.
3. Si el flujo lo pide, spawnea un **subagent** para una revisión con ojos frescos.
4. Mientras el agente trabaja, los **hooks** vigilan cada escritura y frenan lo que no corresponde a la fase.
5. Cumplido el gate, se actualiza el **state** —fase nueva, gate marcado, entrada en el historial— y la máquina **transiciona**.

**Esa coreografía es el pipeline.** No es ninguna de las cinco piezas: es cómo conversan entre ellas. Y notá que **el state está en el centro de todo** — lo lee el orquestador para enrutar, lo leen los hooks para decidir, y se actualiza en cada transición. Cuando diseñes el tuyo, empezá por ahí.

## 🌐 Cómo se llama cada cosa en cada herramienta

| Primitiva | Claude Code | OpenCode | GitHub Copilot |
| --- | --- | --- | --- |
| **Skill** | Skill / slash command | Command | Prompt file / chat mode |
| **Subagent** | Subagent | Agent | Agent / chat participant |
| **Hook** | Hook (`settings.json`) | Hook en un plugin TS | Hook (puede bloquear) |
| **State** | Archivo en el repo | Archivo en el repo | Archivo en el repo |
| **Orquestador** | `CLAUDE.md` + agente | `AGENTS.md` + agente | `copilot-instructions.md` |

Guardá esta tabla, porque es la que hace posible el trabajo de los Módulos 6 y 7.

Y mirá con atención la fila del **hook**: las tres herramientas pueden interceptar y **bloquear** — que es lo que hace posible el enforcement determinista. Pero se escriben distinto: en Claude Code es un script declarado en `settings.json`, en OpenCode un módulo TypeScript que exporta hooks, y en Copilot CLI su propio mecanismo de eventos. **Misma garantía, tres sintaxis.**

Ahí está la gracia real del port de los Módulos 6 y 7: no alcanza con traducir palabra por palabra. Cada herramienta tiene sus límites y sus mañas, y en algún punto vas a tener que decidir **qué reemplaza a qué y qué garantía estás dispuesto a perder**. Ése es uno de los ejercicios más formativos del curso, y rinde mucho más si llegás con esta tabla entendida.

Fijate también en la fila del **state**: es la única que dice lo mismo en las tres columnas. No es casualidad — un archivo en el repo no depende de ninguna herramienta. Por eso en DAW el state vive en la raíz del repo (`.daw-state.json`) y no adentro de `.claude/`: **es del método, no del harness**.

> 📖 **Dónde está esta tabla, en serio.** La versión de arriba es la didáctica, con las tres herramientas del curso. La versión operativa vive en el repo de DAW: cada herramienta soportada tiene un `adapters/<id>/adapter.json` que declara exactamente eso — dónde busca los skills, dónde los subagentes, en qué formato quiere sus hooks. Son las mismas cinco filas, escritas como datos en vez de como prosa. Si trabajás con **Cursor, Gemini CLI o Codex CLI**, ahí está tu columna; y si querés soportar una herramienta que no está, ahí está el molde. Es exactamente lo mismo que hace `transition-graph.json` con las transiciones: **lo que se puede declarar, no se programa**.

## 🛠️ Micro-ejercicio (5 min)

Sobre tu propia instalación, abrí un archivo de cada primitiva. No los estudies — solo miralos para que dejen de ser un diagrama:

1. Un **skill** de `.claude/skills/` — leé su primera pantalla y fijate qué forma tiene.
2. Un **subagent** de `.claude/agents/` — fijate qué pregunta responde y con qué criterio.
3. Un **hook** de `.claude/hooks/` — todavía no hace falta que lo entiendas; mirá el tamaño (son cortos, y eso ya dice algo).
4. Tu **`.daw-state.json`** — ¿en qué fase quedó tu corrida?
5. El **orquestador** `.daw/orchestrator.md` — buscá la sección «Router de Fases» y mirá cómo cambia lo permitido según dónde esté la máquina.

Cinco archivos, cinco piezas. Ahora ya no es un concepto: es tu repo.

Ahora sí, la lección que explica **por qué todo esto es confiable** y no un castillo de buenas intenciones. ➡️
