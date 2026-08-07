---
titulo: "DAW: el template de flujo del curso"
capitulo: "07-Módulo 5 Agentic Orchestration"
orden: 3
source: "apuntes/slides/00-raw/07-Módulo 5 Agentic Orchestration/03-DAW_ el template de flujo del curso – MUG.html"
source_sha256: c0a783122a0a4cce
extraido: 2026-08-07
---

# DAW: el template de flujo del curso

Ya decidiste que querés un **workflow con gates**. Ahora la pregunta práctica: ¿lo armás vos desde cero, o arrancás de algo que ya funciona?

En este curso arrancamos de algo que ya funciona. Y no por atajo: porque construir un pipeline desde la nada, sin haber usado uno nunca, es la mejor forma de terminar reinventando —mal— decisiones que ya están resueltas. Es mucho más formativo **agarrar una máquina que anda, abrirla, entender por qué cada pieza está donde está, y recién ahí decidir qué le cambiarías**. 📦

Te presento **DAW — Dilux Agentic Workflow**. Es un pipeline de desarrollo guiado por agente que arranca solo cuando pedís un cambio de código. Éste es su mapa completo:

![DAW — Dilux Agentic Workflow: seis fases y los gates entre ellas](assets/aifbl26-daw-pipeline-v2.png)

Tomate un minuto largo con el gráfico, porque tiene condensado todo lo que importa:

- **Seis fases en línea**, cada una con un trabajo acotado, que salen de **IDLE** (la máquina en reposo, esperando) y vuelven ahí al terminar.
- **Un gate entre cada par de fases**: una condición que se tiene que cumplir para poder avanzar. **Los naranjas con candado los impone un hook** — código que corre afuera del modelo, lee el state y rechaza. No son promesas: sin spec aprobado, escribir código no es «algo que no conviene», es literalmente **imposible**. El verde con tilde es el único que no lleva candado, y por un motivo interesante: no exige ninguna condición verificable, **te exige a vos** — es tu confirmación, y una confirmación no se puede meter en un `if`. A esa distinción le dedicamos una lección entera.
- **Cada fase deja un artefacto en el repo**, abajo de cada caja. No hay ninguna fase que termine en una conversación: **todas terminan en un archivo**. Cuando lleguemos a diseñar tu propio pipeline vas a ver que ésa es una de las reglas de oro.

## 🎁 Qué es DAW en este curso: un template, no un dogma

Esto es lo más importante de la lección, así que va sin vueltas y en grande:

> **DAW es un template de flujo. Es la base con la que vas a trabajar en los Módulos 5, 6 y 7 — y podés usarlo tal cual o personalizarlo. Las dos cosas están bien.**

Me interesa que esto quede clarísimo porque condiciona cómo leés todo lo que sigue. No te estoy dando una herramienta para que la admires ni un ejercicio para que la reconstruyas por obligación. Te estoy dando **una base de trabajo**, y lo que hagas con ella es una decisión tuya:

- **Si tu proyecto encaja con el flujo completo**, lo instalás y trabajás. No tenés que justificar nada, no tenés que construir nada. Agarrás la herramienta y hacés tu app. **Es una opción perfectamente válida** y va a ser la de mucha gente — sobre todo la de quienes quieren que su energía vaya al producto y no al andamiaje.
- **Si te sobran o te faltan fases**, lo abrís y lo cambiás. Todo DAW son archivos de texto adentro de tu repo: sacás una fase, movés un gate, agregás un skill tuyo de los que ya venís escribiendo. No hay API de extensión ni permisos que pedir — **editás el archivo**. En la anteúltima lección del módulo vas a hacer exactamente eso, guiado.
- **Si tenés un flujo de trabajo propio y fuerte**, DAW te queda como referencia y armás el tuyo desde cero.

Lo que **no** es una opción es no haberlo pensado. El entregable del módulo es justamente la decisión, escrita y fundamentada.

## 🗓️ Cómo lo vamos a usar de acá en adelante

Para que sepas dónde estás parado en el viaje:

- **En este módulo (M5)** vas a crear **un repo nuevo** —el de tu app construida con DAW—, instalarlo ahí, traerte tu PRD, pasar tu app por el pipeline con **Claude**, y después personalizarlo. Es el módulo **evaluado** del bloque.
- **En el M6 y el M7** hacés lo mismo con **OpenCode** y con **Copilot CLI**: mismo método, misma app, otra herramienta — para ver con tus manos qué cambia y qué no.

Y ya que estamos con las herramientas: DAW soporta **seis**, no tres. Éstas son, con el identificador que vas a usar al instalarlo:

| Herramienta | `--target` | Dónde busca los skills | Qué archivo de contexto lee |
| --- | --- | --- | --- |
| **Claude Code** | `claude` | `.claude/skills` | `CLAUDE.md` |
| **OpenAI Codex CLI** | `codex` | `.agents/skills` | `AGENTS.md` |
| **GitHub Copilot CLI** | `copilot` | `.github/skills` | `AGENTS.md` |
| **Cursor** | `cursor` | `.cursor/skills` | `AGENTS.md` |
| **Google Gemini CLI** | `gemini` | `.gemini/skills` | `GEMINI.md` |
| **OpenCode** | `opencode` | `.opencode/skills` | `AGENTS.md` |

👉 **Fijate la última columna, que explica una decisión de diseño.** Cuatro de las seis leen `AGENTS.md`, que es un [estándar abierto](https://agents.md/) donado a la Linux Foundation. Claude y Gemini leen el suyo. Por eso **las instrucciones de DAW viven siempre en `AGENTS.md`** — el único archivo que todas comparten — y `CLAUDE.md` y `GEMINI.md` quedan reducidos a cuatro líneas que lo importan. Nada duplicado, nada que se pueda desincronizar, y **el día que portás el pipeline no se mueve un archivo**.

El curso recorre tres —Claude en M5, OpenCode en M6, Copilot en M7— porque con tres ya se entiende el punto y hacer seis sería repetir el mismo ejercicio. Pero si trabajás con Cursor, con Gemini o con Codex, **no te quedás afuera**: el método es el mismo archivo y el instalador te arma el cableado igual. Y si mañana aparece una séptima herramienta, agregarla es escribir una receta, no traducir el framework — eso lo vas a ver en detalle en dos secciones más.

O sea: **DAW no es un paseo de una clase**. Es la herramienta con la que vas a trabajar las próximas tres. Por eso conviene conocerla bien ahora.

## 🏭 De dónde sale

DAW es un **framework de desarrollo asistido por IA creado por Pablo Di Loreto** para usar en tus proyectos de creación de software de todos los días, y una gran base para usar en equipos de producción. Por supuesto se puede **personalizar** —y eso es justamente lo que vas a aprender a hacer en este curso—. También lo podés **usar tal cual, sin problemas**.

Lo digo explícito porque cambia cómo conviene leerlo. **No es un ejemplo de curso hecho para el curso**: es una herramienta de producción, desacoplada para que entre en cualquier repositorio. Y eso tiene dos caras que quiero poner sobre la mesa desde el principio:

- **Lo bueno:** lo que vas a ver **funciona en serio**. Las reglas que te parezcan exageradas o demasiado específicas suelen ser cicatrices: alguien se comió el problema y la regla nació para que no vuelva a pasar. Cuando encuentres una de esas, vale la pena preguntarse qué habrá pasado.
- **Lo honesto:** es **más grande de lo que necesitás para empezar**, y va a haber partes que a tu proyecto no le apliquen. Eso está previsto y no es un defecto que haya que disimular — la última parte del módulo es precisamente decidir qué te sirve y qué no.

## 📦 Dónde vive DAW: hoy, adentro de tu repo

Todo DAW vive **dentro de tu repositorio**: se copia adentro del proyecto y listo. A eso se lo llama un **drop-in**.

Y quiero ser claro con esto, porque es fácil confundirlo con una virtud: **es una decisión técnica, no una medalla.** DAW podría perfectamente estar empaquetado de otra forma.

De hecho, **podría ser un plugin**. Claude Code soporta plugins, y tienen ventajas reales: los instalás una vez y los usás en **todos** tus repos, se actualizan de forma centralizada —arreglás algo y lo tenés en todos lados—, y no te mezclan sus archivos con los de tu proyecto.

Un ejemplo concreto que quizás conozcas: **Superpowers**, una colección de skills y metodología de desarrollo para Claude Code, se distribuye exactamente así. Se instala con dos comandos —agregás su marketplace y después el plugin— y a partir de ahí está activo en cada sesión, en cualquier repositorio. Mismo tipo de idea que DAW, empaquetada de la otra forma.

**Empaquetar DAW como plugin queda fuera del alcance de este curso**, pero es bueno que sepas que la opción existe y que, si algún día querés distribuir tu pipeline a un equipo entero, es muy probable que quieras ir por ahí. De hecho **es lo que sigue en la hoja de ruta de DAW**: versiones empaquetadas para las plataformas que lo soportan, para que instalar sea un comando y actualizar sea automático. El método de abajo no cambia — cambia cómo llega.

Entonces, ¿por qué hoy lo trabajamos como drop-in? Por tres razones bien concretas, y todas tienen que ver con **aprender**:

- **Lo podés leer entero.** ¿Querés saber qué hace exactamente en la fase de planificación? Abrís el archivo y lo leés. No hay comportamiento escondido en ningún lado, ni una capa de abstracción entre vos y el proceso.
- **Lo modificás sin ceremonia.** No hay que forkear un proyecto ajeno, ni buscar un punto de extensión, ni esperar que alguien acepte un pull request. Editás el archivo y ya.
- **Se versiona con tu proyecto.** Cambiaste una regla, queda en el commit, y dentro de tres meses ves qué cambiaste y por qué.

Para un curso donde el objetivo no es que sepas *usar* un pipeline sino que puedas **construir el tuyo**, esas tres cosas valen más que la comodidad de instalarlo una sola vez. La contra es real y hay que decirla: **mezcla archivos con los de tu proyecto** y, si lo tenés en varios repos, actualizarlo es copiar de nuevo.

### 🔮 Cómo se distribuiría como plugin (para cuando lo quieras)

Por si te queda la curiosidad, la receta existe y es más simple de lo que parece, porque **ya está la separación que la hace posible**:

- El plugin traería **el método** (`.daw/`) y **el cableado** (hooks, skills, subagents) empaquetados juntos, y se instalaría con dos comandos.
- La regla que lo salva todo: **si tu repo tiene su propio `.daw/`, ése gana.** El plugin aporta el default; tu repo manda.
- Y para pasar de «lo uso» a «lo edito» alcanzaría con un comando que **copie el método del plugin a tu repo**. De ahí en adelante lo tocás como cualquier archivo tuyo.

Es el mismo patrón de un montón de herramientas que ya usás: un default razonable distribuido de forma central, la posibilidad de pisarlo localmente, y una salida de escape para personalizar.

**Por qué en el curso no vamos por ahí:** porque acá el objetivo **es** editarlo. Si arrancáramos con el plugin, la primera instrucción del ejercicio de personalización sería *«sacá el método del plugin para poder tocarlo»* — un rodeo que agrega un concepto y no enseña nada de orquestación. Y en los Módulos 6 y 7 el port se convertiría en «instalá el plugin de la otra herramienta», que esconde justamente lo que queremos que veas.

> 🧠 **Lo importante:** el empaquetado y el método son cosas separadas. Las fases, los gates y el enforcement son los mismos sea un drop-in, un plugin o lo que venga después. Lo que aprendés acá no caduca cuando cambie la forma de distribuirlo.

## 🗂️ Cómo está compuesto (y por qué está partido en dos)

Acá hay una decisión de arquitectura que conviene mirar con atención, porque es la que hace posible el trabajo de los Módulos 6 y 7. DAW se instala en **dos carpetas separadas**, y la separación no es cosmética:

```
.daw/                      ← EL MÉTODO (no depende de ninguna herramienta)
├── orchestrator.md          la máquina de estados y el router de fases
├── rules/                   las instrucciones POR FASE
│   ├── classify · define · plan · code · verify · release
│   ├── testing · commits · security · branches · tracker
│   └── transition-graph.json   ← las transiciones legales, en datos
└── scripts/                 el validador de transiciones y el gate compartido

.claude/                   ← EL CABLEADO de Claude Code
├── settings.json            qué hooks corren y cuándo
├── agents/                  los auditores: arch-auditor, sec-auditor, module-verifier
├── skills/                  las acciones: create-spec, test, security-sast, commit…
└── hooks/                   los scripts de enforcement

AGENTS.md                  ← el contexto de TU proyecto (stack, arquitectura, dominio)
CLAUDE.md                  → importa @AGENTS.md y @.daw/orchestrator.md
docs/daw/                  ← todo lo que produce el pipeline, commiteado
.daw-state.json            ← la memoria del pipeline (gitignoreada: es tuya)
```

Leelo así: **`.daw/` es el método, `.claude/` es cómo se enchufa el método a una herramienta concreta, y `AGENTS.md` es tu proyecto.** Tres cosas distintas, tres lugares distintos — y por eso el instalador te deja un `AGENTS.md` con placeholders para que lo completes: DAW sabe de proceso, pero de **tu** proyecto sabés vos.

El grafo de transiciones, las reglas de cada fase y el orquestador **no saben nada de Claude Code**: son texto y datos que describen un proceso de desarrollo. Lo que sabe de Claude Code es el cableado — el formato del `settings.json`, dónde van los subagentes, cómo se escriben los hooks.

Fijate también que **todo lo que el pipeline produce vive junto, abajo de `docs/daw/`**. Es una decisión chica con un efecto grande: los artefactos del proceso no se mezclan con la documentación que escribís vos. Podés borrar `docs/daw/` entero y no te llevaste puesto nada tuyo, y cuando alguien abre el repo ve de un vistazo qué salió del pipeline y qué no. La única excepción son los **ADR**, que van a `docs/adr/` a propósito: una decisión de arquitectura es de tu proyecto, no de la herramienta que la registró — el día que saques DAW, los ADR se quedan.

¿Por qué importa la separación? Porque cuando en el Módulo 6 portes esto a OpenCode, **`.daw/` no se toca — es byte por byte el mismo archivo**. Escribís cableado nuevo apuntando al mismo método. Si todo viviera mezclado, portar sería «copiá la carpeta y renombrá cosas» — que no enseña nada. Así, portar es lo que realmente es: **el método se queda, el enchufe cambia.**

Y esa separación es lo que hace que soportar una herramienta nueva sea barato. Cada herramienta soportada es una **receta** (`adapters/<id>/adapter.json`) que declara tres cosas: dónde busca los skills, dónde busca los subagentes y en qué formato quiere sus hooks. Ninguna receta contiene lógica del pipeline — si la contuviera, un bug habría que arreglarlo seis veces. El gate que decide si una transición es legal es **uno solo**, compartido por las seis.

## 🔌 Instalar = activar

```
bash install.sh /ruta/a/tu/repo --target claude
```

Si no le pasás `--target`, te pregunta con qué herramienta vas a trabajar. Podés pasarle varias separadas por coma, o `all`.

Es **idempotente**: lo podés correr las veces que quieras sin romper nada. Copia el método a `.daw/`, copia el cableado a `.claude/` **sin pisar lo que ya tengas ahí**, agrega el bloque de activación y manda el archivo de state al `.gitignore`.

**Y actualizar es el mismo comando.** No hay un `update` aparte que puedas olvidarte de correr: si el repo ya tiene DAW, el instalador lo detecta, te dice para qué herramientas está cableado y te ofrece refrescarlas o sumar otra. Reemplaza lo suyo y deja lo tuyo — y si uno de tus skills se llama igual que uno de DAW, te avisa y deja el tuyo tranquilo.

> 🔖 **Lo único que administra dentro de tus archivos de contexto es un bloque marcado** — entre `<!-- BEGIN DAW -->` y `<!-- END DAW -->`. Todo lo que escribas afuera de esos marcadores es tuyo para siempre y no se toca; lo de adentro se reemplaza en cada actualización, así que no lo edites. Es la clase de detalle aburrido que te ahorra una tarde el día que actualices.

Y también se **desinstala**: `uninstall.sh` saca el método, el runtime y el cableado de cada herramienta, sin llevarse por delante lo tuyo — lee el manifiesto de lo que instaló en vez de adivinar por nombre de carpeta. **`docs/` no lo toca nunca**: los PRDs, specs y reportes son el registro de lo que se decidió, y sacar la herramienta no es motivo para perderlo.

Y fijate que no hay ningún paso de «activar», que es la parte que hace clic:

> 🔑 El `CLAUDE.md` **importa** al orquestador, y el `CLAUDE.md` se carga solo al abrir la sesión. Por eso, apenas abrís el agente parado en el repo, **la máquina ya está corriendo**. Instalar *es* activar.

Ese mecanismo —una línea de importación en el archivo de contexto— es lo que convierte un montón de archivos sueltos en un sistema vivo. Cuando diseñes el tuyo, es la pieza que vas a necesitar entender bien.

## 🚫 Qué NO hace DAW, dicho de frente

Para que no te lleves expectativas equivocadas, que es la forma más rápida de frustrarse con una herramienta:

- **No usa MCP.** Se mantiene simple a propósito: no necesita servidores externos ni credenciales de nada.
- **No te elige el stack.** Detecta el que ya tenga tu repositorio y trabaja con eso, sea lo que sea.
- **No está casado con ninguna herramienta de gestión.** Si usás un gestor de tickets (Jira, Linear, GitHub Issues, el que sea) lo aprovecha; si no usás ninguno, genera sus propios identificadores y el pipeline corre igual de completo.
- **No reemplaza tu criterio.** Impone que los gates se cumplan, no que tu trabajo sea bueno. La diferencia entre esas dos cosas es sutil y es importante — le dedicamos una lección.
- **No es infalible, y lo dice en su propia documentación.** El hook cubre las herramientas de escritura; un `cat > archivo.py` desde la shell llega al disco igual. DAW no intenta atajarlo parseando tu shell —cada variante que no anticipara fallaría hacia abierto— pero **te avisa** cuando aparece código en una fase que no escribe código. Los límites están enumerados en `docs/RATIONALE.md`, cada uno con su motivo. **Un framework que te enumera sus agujeros es más confiable que uno que no los menciona**, y esa idea va a volver en la lección de promesa vs enforcement.

## 📥 Conseguilo

DAW es open source, con **licencia Apache 2.0** — usalo, forkealo y adaptalo a cómo trabaja tu equipo, que es justamente para lo que está:

```
git clone https://github.com/soydiloreto/dilux-agentic-workflow.git
```

👉 **https://github.com/soydiloreto/dilux-agentic-workflow**

Cloná el repo y date **cinco minutos** de paseo, sin instalar nada todavía. Te sugiero este recorrido, que es el que más rápido te arma el mapa mental:

- **`README.md`** — qué es y qué promete, en dos minutos de lectura.
- **`daw/rules/`** — mirá los nombres de los archivos. Vas a reconocer las seis fases del gráfico, una por archivo. Abrí `plan.instructions.md` entero: es la fase más rica y te muestra la forma que tienen todas.
- **`daw/rules/transition-graph.json`** — abrilo aunque no lo entiendas del todo. Son treinta y pico de líneas y **ahí adentro están todas las reglas de movimiento de la máquina**. Que quepan en una pantalla es el punto.
- **`adapters/`** — seis carpetas, una por herramienta. Fijate lo chiquitas que son comparadas con `daw/`.
- **`docs/RATIONALE.md`** — el que más te va a servir para el capstone. Es **por qué el método decide lo que decide**: una entrada por cada decisión que razonablemente podría haber ido para el otro lado, con en qué se apoya y **qué te cuesta**. Vas a encontrar ahí, escritas, varias de las preguntas que te vas a hacer cuando diseñes el tuyo.
- **`docs/AGENTS-MD.md`** — qué parte de ese archivo es tuya, cuál administra DAW, y qué títulos busca el método por nombre. Un título que falta **no rompe nada**: la búsqueda no encuentra y la fase sigue. Ése es el único modo de falla silencioso del framework, y por eso tiene su propia página.

**Todavía no lo instales en ningún lado.** Primero conviene entender qué hace cada fase —que es exactamente lo que sigue— y recién después lo instalamos donde va: en el repo nuevo de tu proyecto. ➡️
