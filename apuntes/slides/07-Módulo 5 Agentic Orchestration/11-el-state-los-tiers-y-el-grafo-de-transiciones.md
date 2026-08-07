---
titulo: "El state, los tiers y el grafo de transiciones"
capitulo: "07-Módulo 5 Agentic Orchestration"
orden: 11
source: "apuntes/slides/00-raw/07-Módulo 5 Agentic Orchestration/11-El state, los tiers y el grafo de transiciones – MUG.html"
source_sha256: a1d8fd8d8c8f7b6a
extraido: 2026-08-07
---

# El state, los tiers y el grafo de transiciones

Última pieza técnica antes de que hagas tuya la máquina. Tres cosas que van juntas: **cómo recuerda, cómo se adapta al tamaño del pedido, y dónde están escritas sus reglas de movimiento**. 🎚️

—

# Parte 1 · El state: la memoria

El `.daw-state.json` que viste moverse mientras corría tu feature es un archivo chico —cabe en media pantalla— con toda la verdad del pipeline:

| Campo | Qué guarda | Quién lo lee |
| --- | --- | --- |
| `phase` | En qué fase está la máquina | El orquestador, para enrutar |
| `tier` | Qué clase de pedido es | El orquestador y el grafo |
| `ticket` · `title` | Qué se está trabajando | Los paths, el branch, la línea de estado |
| `tracker` | El ID en tu gestor de tickets, si viene de uno | Las reglas de cierre |
| `block` | Qué bloque del spec se está implementando | La fase CODE, para retomar donde iba |
| `gates` | Qué condiciones ya se cumplieron | **Los hooks**, para dejar pasar o frenar |
| `history` | El log de todas las transiciones | Vos, y cualquier auditoría |

Y ahí está toda la máquina. Nada más.

> 📏 **La regla de diseño, para cuando armes el tuyo:** el state guarda **lo que la máquina necesita para decidir. Nada más.**

Esa regla parece obvia y no lo es, porque la tentación de guardar «por si acaso» es fuerte. El problema de cada campo de más es concreto: es algo que **se puede desincronizar**. Si guardás información que nadie usa para decidir, en algún momento va a decir algo distinto de la realidad, nadie se va a enterar, y el día que alguien la lea va a tomar una decisión con datos viejos. Un state chico es un state que no miente.

## 📜 `history` append-only: la máquina no reescribe su pasado

Cada transición agrega una entrada al final del historial: **cuándo, desde dónde, hacia dónde, por qué, de qué ticket y de qué tier**. Y hay una restricción dura: **las entradas se agregan al final y nunca se modifican, ni se reordenan, ni se borran.**

```
{ "timestamp": "2026-07-28T14:02:11Z", "from": "CODE", "to": "VERIFY",
  "action": "implementación completa", "ticket": "FEAT-001a", "tier": "FEATURE" }
```

👉 **Mirá el `ticket` de esa entrada, que no está de adorno.** Al cerrar, el ticket se resetea a `null` — así que **la entrada es el único lugar donde sobrevive el nombre de lo que se terminó**. Sin eso, el historial diría que hubo transiciones pero no *de qué*, y un registro de movimientos anónimos no puede contestar la única pregunta que vale dentro de seis meses: **qué pasó con este pedazo de trabajo**.

Y tiene una consecuencia práctica que vas a ver: **de ahí sale la lista de sub-tickets pendientes.** Si un PRD se partió en cuatro, DAW compara los PRDs que hay en disco contra los cierres que hay en el historial, y lo que falta te lo nombra al arrancar la sesión. **Sin guardar nada nuevo** — es la resta de dos cosas que ya existían. La regla de arriba en acción: el state guarda lo necesario para decidir, y lo demás se deriva.

Suena a formalismo de contador, pero es lo que convierte al historial en **una auditoría** y no en **una narración**. Si la máquina pudiera reescribir su historia, el historial diría lo que la máquina —o el agente— quiere que diga. Y un registro que se puede editar no es un registro: es un borrador.

Hay un hook que valida esta propiedad en **cada escritura del state**: si detecta que alguien insertó una entrada al principio, o truncó el array, o cambió una fase sin dejar el rastro correspondiente, **bloquea**. No es una convención que se pide en el prompt: es una regla impuesta, con la lógica de la lección 8.

## 🧹 Volver a IDLE resetea el ticket

Un detalle chiquito con una consecuencia grande. Cuando el trabajo termina y la máquina vuelve a IDLE, **`tier` vuelve a `null` y `gates` vuelve a `{}`**. El `history` es la excepción: nunca se limpia, solo crece.

Parece una prolijidad y no lo es. Si los gates quedaran ahí, el **ticket siguiente los heredaría** — arrancaría con `tests`, `sast` y `verify` ya en `true`, pagados por un trabajo que no tiene nada que ver, y podría recorrer el pipeline entero sin ganarse ni uno. Con todos los candados puestos y ninguno cerrado.

> 🧠 **Para tu diseño:** cuando algo termina, preguntate **qué tiene que volver a cero**. Un state que arrastra datos del trabajo anterior es peor que no tener state, porque miente con formato de verdad.

—

# Parte 2 · Los tiers: el pipeline se adapta al pedido

## 😤 El problema, antes que la solución

Imaginate esta escena. Encontrás un typo en un mensaje de log —una palabra, cuatro letras—, se lo pedís al agente, y la máquina te contesta:

> *«🔍 Clasificando pedido… Tier propuesto: FEATURE. ¿Confirmás? Perfecto, pasemos a DEFINE: voy a generar el PRD para este cambio.»*

**Abandonarías el pipeline esa misma semana.** Y tendrías toda la razón.

Un pipeline que no distingue el tamaño del trabajo no es riguroso: es **inutilizable**. Corregir un typo no puede costar un PRD, un spec y un threat model. Y ojo con la consecuencia, que es peor de lo que parece: si el proceso cuesta más que el trabajo, la gente **lo saltea**. Y un proceso que se saltea es **peor que no tener proceso**, porque genera la ilusión de que hay control donde ya no lo hay.

Por eso CLASSIFY asigna un **tier**, y el tier **elige qué pipeline se activa**.

## 🎚️ Los cinco tiers de DAW

**Sin state — se resuelve y listo:**

- **💬 QUERY** — una pregunta informativa: *«¿cómo está estructurado el módulo de pagos?»*. Se responde, es de solo lectura y **ni toca el state**: no abre fase, no escribe `tier`, no queda en el historial.

Que este tier exista es más importante de lo que parece: es el que evita que el pipeline **se meta donde no lo llamaron**. Sin él, cada pregunta que hicieras dispararía una clasificación, y en dos días estarías puteando. Y hay un caso todavía más de fondo: un pedido que **no tiene nada que ver con el código del repo** ni siquiera se clasifica. DAW gobierna lo que le pasa al código, no todo lo que le pedís al agente.

**Con pipeline corto:**

- **⚡ QUICK-FIX** — el arreglo mínimo. Recorre `CLASSIFY → DEFINE → CODE → RELEASE`: **saltea planificación y verificación**. En DEFINE no escribe un PRD sino un *brief* de cuatro líneas. Es el carril rápido para lo genuinamente chico — y ojo, **el SAST sigue bloqueando**: el atajo te ahorra ceremonia, no seguridad.

**Con pipeline completo:**

- **🔧 FIX** — un defecto en algo que ya existe, **incluido uno ardiendo en producción**. Además del recorrido completo pide tres cosas propias: **análisis de causa raíz**, un **test de regresión** que reproduzca el bug, y un **plan de rollback**.
- **✨ FEATURE** — funcionalidad nueva. El caso canónico, el que corriste.

**Con su propio flujo:**

- **📝 DISCOVERY** — ideación libre: explorar una idea, definir funcionalidades, generar PRDs sin implementar nada. **No recorre las fases estrictas** y no toca tu código fuente.

> 🎭 Fijate que DISCOVERY es exactamente lo que anticipamos en la lección 2: **el lugar donde el workflow deja suelto al agente a propósito**. No es una inconsistencia ni un pedazo sin terminar — es el diseño reconociendo que **la exploración no se gatea**, porque su valor está justamente en no tener el resultado predefinido. Y es, de paso, el carril por el que entra al pipeline gente que no escribe código: un PRD bien pensado es un entregable tan legítimo como una feature.

## 🚨 El tier que DAW decidió NO tener

Acá hay una historia de diseño que te va a servir más que la lista de arriba, porque es una decisión que se tomó **sacando** algo.

DAW tenía un tier `INCIDENT`, separado de `FIX`, para lo que se rompe en producción: mismo pipeline completo, más severidad y post-mortem obligatorio. Sonaba correcto. **Se eliminó.**

El argumento en contra fue éste: el problema real de producción no es que falte un tier, es que **la gente apurada clasifica mal a propósito para ir más rápido**. Un tier extra «de emergencia» no arregla eso — le pone nombre oficial. Y peor: multiplica las conversaciones sobre *en qué carril va esto*, que es tiempo que nadie tiene a las tres de la mañana.

La solución fue plegar el caso adentro de `FIX`, que ya pide causa raíz y rollback, que es exactamente lo que necesitás cuando algo está ardiendo.

> 🧠 **Para tu diseño, y esto rinde muchísimo:** antes de agregar un tier, preguntate si el que ya tenés no cubre el caso con un modificador. **Cada tier que agregás es una decisión más que alguien tiene que tomar bien, en el peor momento posible.** Un pipeline con nueve carriles no es más expresivo que uno con cuatro: es más fácil de usar mal.

## 🛡️ La salvaguarda: diseñá también el abuso de tus atajos

Acá hay una decisión que muestra madurez de diseño, y te recomiendo copiarla tal cual.

QUICK-FIX es un atajo. Y **todo atajo se abusa** — no por mala fe, sino porque *«esto es chiquito»* es la mentira más fácil de contarse a uno mismo. Empezás con un typo, ves algo al lado que te molesta, terminás refactorizando tres archivos. Y todo eso pasó **sin spec, sin threat model y sin verificación**, porque el tier decía «rápido» y nadie volvió a preguntar.

La solución de DAW: un hook vigila mientras el tier es QUICK-FIX y **bloquea** si el trabajo toca rutas sensibles o si el diff acumulado supera las diez líneas. Y cuando bloquea no te deja colgado: **te manda a reclasificar**, con el pipeline completo.

Hay dos detalles finos de ese guard que valen oro para cuando escribas el tuyo, porque los dos fueron bugs reales:

- **El guard mide contra tu rama base, y la busca — no la asume.** La primera versión comparaba contra `main` a secas. En cualquier repo cuyo tronco se llame `master` (o `develop`, o `trunk`), el `git` fallaba, la cuenta de líneas daba **cero**, y el guard dejaba pasar cualquier cosa. Un control que falla **abierto** es peor que no tener control: no protege y encima te hace creer que sí.
- **No cuenta los artefactos del propio pipeline.** Como cada fase commitea lo suyo, el *brief* de cuatro líneas que escribe DEFINE aparecía en el diff acumulado y **se comía el presupuesto de diez líneas** antes de que escribieras una sola línea de código. El presupuesto es para **código**; lo que vive en `docs/daw/` no cuenta.

> 🧠 **Para tu diseño:** cuando pongas un carril rápido, **diseñá también qué pasa cuando alguien lo usa mal** — incluido vos, sobre todo vos. Y después preguntate lo segundo, que es lo que casi nadie se pregunta: **si mi control se rompe, ¿falla cerrado o falla abierto?** Un control que ante un error deja pasar es un control que un día se rompe en silencio y nadie se entera por meses.

—

# Parte 3 · El grafo de transiciones

Ésta es, para mí, **la pieza más elegante de DAW**, y la que más conviene que copies aunque no copies nada más.

Las transiciones legales **no están escritas en el prompt del agente**. Están en un archivo de datos: `.daw/rules/transition-graph.json`. Abrilo: son unas treinta y pico de líneas, y **ahí adentro está toda la ley de movimiento de la máquina**. Declara, **por cada tier**, qué transición es legal y qué gates exige:

| Transición (FEATURE) | Gates que exige |
| --- | --- |
| `CLASSIFY → DEFINE` | — |
| `DEFINE → PLAN` | `define` |
| `PLAN → CODE` | `spec` + `threat` |
| `CODE → VERIFY` | `tests` + `sast` |
| `VERIFY → RELEASE` | `verify` |
| `RELEASE → IDLE` | `commit` + `pr` |

Y declara también las dos flechas hacia atrás —`PLAN → DEFINE` y `VERIFY → CODE`— sin gates, porque **volver nunca cuesta**: lo que cuesta es avanzar. Un pipeline que te castiga por retroceder es un pipeline que te empuja a seguir de largo con algo que sabés que está mal.

Para **QUICK-FIX** el mismo archivo declara otro recorrido: `DEFINE → CODE` directo, sin PLAN ni VERIFY. Si con ese tier la máquina intentara ir a PLAN, **esa transición simplemente no existe en el grafo** y queda bloqueada.

**Por qué esto es tan bueno**, en tres puntos:

- **Las reglas están en datos, no en prosa.** Un archivo declarativo que un script lee y aplica. No hay interpretación posible, no hay matices, no hay «bueno, en este caso…».
- **Es la forma más pura de lo que viste en la lección 8:** mover un control crítico del prompt al código. El *«no avances sin spec»* dejó de ser una frase que el modelo tiene que recordar entre otras cuarenta, y pasó a ser **una fila en una tabla que un `if` consulta**.
- **Se cambia sin tocar el pipeline.** ¿Querés agregarle un gate a una transición? Editás el JSON y listo. No reescribís instrucciones, no reentrenás a nadie, no rezás para que el modelo lo respete. Es, de hecho, lo que vas a hacer en la próxima lección.

### 🧬 Dos detalles del archivo que conviene robarse

Cuando lo abras vas a encontrar dos cosas que no son obvias y que resuelven problemas reales:

**`extends`, para no duplicar un recorrido.** El tier `FIX` recorre exactamente el mismo camino que `FEATURE`, así que en vez de copiar las seis filas dice `{ "extends": "FEATURE" }`. Parece cosmético hasta que agregás un gate: con la copia tenés que acordarte de tocar los dos lugares, y el día que te olvides de uno vas a tener **dos tiers que dicen la misma regla de forma distinta** sin que nadie se entere. Lo que se duplica, se desincroniza.

**`no_walkaway`, la lista de fases de las que no te podés bajar.** Ya la viste en acción: hoy contiene solo `RELEASE`. Está en el **archivo de datos** y no adentro de la lógica, y eso es a propósito — si vos decidís que de tu fase de despliegue tampoco se puede salir, la agregás a la lista. La regla la ejecuta el código; **cuáles son las reglas lo declara el JSON**. Esa línea es la que hace que el pipeline sea tuyo y no del que lo escribió.

## 🔄 Cómo conversan las tres partes

Cerremos el círculo con el caso concreto. Estás en PLAN, con el spec escrito y el threat model hecho, y pedís avanzar:

1. La máquina propone la transición `PLAN → CODE` y **te pide confirmación**.
2. Confirmás. Se escribe el state: `phase` pasa a `CODE`, se marcan `gates.spec` y `gates.threat`, y se agrega la entrada al `history`. **Todo en una sola escritura** — si se partiera en dos, existiría un instante con el state incoherente, y ese instante es justo donde se cuelan los bugs raros.
3. El **hook** intercepta esa escritura, consulta el **grafo**, verifica que `PLAN → CODE` existe para tu tier y que los dos gates están presentes → **deja pasar**.
4. El **orquestador** lee el state nuevo, ve `CODE`, y carga solo las reglas de esa fase.

Si en el paso 2 faltara `gates.threat`, el paso 3 devuelve un bloqueo con el motivo y la máquina no avanza. **No porque se acordó de la regla: porque no pudo.**

### ⚠️ El agujero que esconde «todo en una sola escritura»

Fijate el paso 2 de nuevo, porque tiene una trampa hermosa que costó descubrir.

«Todo en una sola escritura» es la regla correcta para que el state nunca quede a medio camino. Pero si el hook solo valida **el resultado**, esa misma regla se convierte en la puerta de salida: nada impide que **una única escritura** deje el state diciendo `phase: RELEASE` con los cinco gates en `true` de golpe. El archivo final es perfectamente coherente. Cada gate está donde debe estar. Y el pipeline entero **no se recorrió**.

Lo que faltaba era obvio recién después de verlo: el hook no tiene que validar solo que el state resultante sea válido, tiene que validar que **el salto sea de a uno**. Una escritura, una transición, y los gates que se agregan son exactamente los que esa transición pide — ni uno más.

> 🧠 **Para tu diseño, y es de las lecciones que más se pagan:** un control que valida **el estado final** siempre se puede satisfacer escribiendo el estado final. Lo que hay que validar es **el movimiento**, no la foto. La pregunta correcta no es *«¿esto es válido?»* sino *«¿se puede llegar acá desde donde estabas, en un paso?»*.

## 🛠️ Micro-ejercicio (10 min)

Sobre tu repo:

1. **Abrí tu `.daw-state.json` y leé el `history` de punta a punta.** Reconstruí tu propia corrida solo con eso: ¿en qué orden pasaron las cosas, cuánto tardó cada fase, hubo alguna vuelta atrás? Eso es lo que te da un historial append-only, y es exactamente lo que no tenías en el Módulo 4.
2. **Abrí `.daw/rules/transition-graph.json`** y ubicá la entrada de tu tier. Mirá qué transiciones tenías permitidas y probablemente no sabías.
3. **Empezá a bocetar el state de tu pipeline**: qué campos necesitás para decidir. Arrancá con `phase`, `ticket` y `gates` — con esos tres ya tenés casi todo, y agregá solo lo que puedas justificar.

> ✅ Tu state está bien diseñado cuando podés responder, **leyendo solo el archivo**: ¿en qué fase estoy? ¿qué gates cumplí? ¿qué estoy construyendo? Si necesitás mirar otra cosa para contestar alguna, te falta un campo. Si hay campos que no contestan ninguna, te sobran.

Ya conocés la máquina entera, de punta a punta. **Ahora hacela tuya.** ➡️
