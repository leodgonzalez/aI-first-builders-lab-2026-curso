---
titulo: "Capstone: el diseño de tu pipeline"
capitulo: "07-Módulo 5 Agentic Orchestration"
orden: 13
source: "apuntes/slides/00-raw/07-Módulo 5 Agentic Orchestration/13-Capstone_ el diseño de tu pipeline – MUG.html"
source_sha256: e9c494d6dc503315
extraido: 2026-08-07
---

# Capstone: el diseño de tu pipeline

Última parada del módulo, y la que cuenta. Ya conocés DAW por dentro, lo corriste con tu app y **le metiste mano**. Ahora escribís **cómo va a ser el tuyo** — y ese documento es el que te va a permitir repetir el ejercicio con OpenCode y con Copilot. 📐

## ⚖️ Primero, el criterio: ¿tu proyecto necesita todo esto?

Antes de diseñar nada, la pregunta que casi nadie se hace y que separa a un profesional de alguien que aplica recetas.

Un pipeline con fases y gates **cuesta**. Cuesta montarlo, cuesta mantenerlo cuando el proyecto cambia, y cuesta cada vez que te frena en el medio de algo. Ese costo se paga solo cuando el trabajo es **repetible y el resultado importa**:

| Vale la pena cuando… | Es overkill cuando… |
| --- | --- |
| Lo vas a repetir muchas veces | Es un prototipo que tirás el viernes |
| Otra persona va a leer o mantener el código | Estás explorando si una idea es viable |
| Va a producción, con usuarios reales | Estás aprendiendo una API que no conocés |
| Trabajás en equipo | Sos vos solo, en algo de una sola vez |
| Hay datos sensibles o plata de por medio | El error no tiene consecuencias |

Volvé a la escalera de la primera lección: **la madurez no es usar siempre lo más pesado, es saber en qué escalón parar.** Para un prototipo descartable, el prompt suelto sigue siendo la respuesta correcta, y montar todo esto sería gastar más tiempo en la ceremonia que en el trabajo.

Elegir un pipeline recortado también es una decisión profesional. Lo que **no** lo es, es no haberlo pensado — y ése es exactamente el trabajo que se te pide acá.

## 🛤️ Los tres caminos

Con ese criterio en la cabeza, elegí uno. **Los tres son válidos** y los tres entregan el mismo documento:

### 🅰️ Usar DAW tal cual

**Para quién:** para quien tiene un proyecto que encaja razonablemente con el flujo completo, o para quien quiere que su energía vaya a **su app** y no al andamiaje. Es una elección de foco, y es perfectamente respetable.

**Qué entregás:** el mapeo de las seis fases a **tu** proyecto — qué produce cada una en tu caso concreto, qué gate aplica, y **cuáles no aplican y por qué**.

👉 Ojo con eso último, porque es donde está el trabajo real de este camino: **justificar una exclusión es más difícil que hacer un cambio**. Si decís que la fase de release no te aplica, tenés que explicar qué hacés en su lugar y **qué garantía perdés**.

### 🅱️ Personalizarlo

**El camino más común**, y la continuación natural de la lección anterior — donde ya hiciste los tres cambios.

**Para quién:** para quien, corriéndolo, vio fases o gates que le sobran o le faltan. Si en la reflexión del ejercicio anotaste *«esto para mi proyecto sobra»*, este camino es el tuyo.

**Qué entregás:** el **diff conceptual** respecto de DAW:

- Qué fases **sacás, agregás o fusionás**.
- Qué gates **agregás o sacás**, aplicando la pregunta de la lección 8: si esto se saltea, ¿rompe el sistema, es un riesgo de seguridad, o solo molesta? Lo que solo molesta no es un gate: es una instrucción en el contexto.
- Qué **skill propio** sumás y en qué fase.
- **El porqué de cada cambio.** Una línea por decisión — sin el porqué es una lista de preferencias, no un diseño.

### 🅲 Diseñar el tuyo desde cero

**Para quién:** para quien ya tiene un flujo de trabajo propio y fuerte que no se parece a DAW, o para quien quiere hacer el ejercicio completo por convicción.

**Qué entregás:** el diseño completo, usando las siete preguntas de la lección 9 para cada fase. DAW te queda como **referencia**, no como base.

👉 **Aviso honesto:** es el camino más caro, y éste es el módulo evaluado del bloque. Elegilo **por convicción, no por orgullo** — que sea el camino más difícil no lo hace el mejor, lo hace el más difícil.

> Una decisión bien fundamentada de *«lo uso tal cual»* vale **exactamente lo mismo** que una de *«lo rehago»*. Acá se evalúa el **criterio**, no el volumen de trabajo.

## 🛠️ Tu turno

⏱️ **Tiempo estimado:** ~40 min · 📦 **Entregable:** `daw-design.md` en tu repositorio de M5.

1. **Tu camino**, y en dos renglones **por qué**. Es parte del entregable, no un preámbulo.
2. **Las fases:** el diagrama de tu pipeline, con el trabajo de cada una en una línea.
3. **La tabla de gates**, con las columnas de la lección 9:

| Gate | Condición **verificable** | Quién valida | Qué marca en el state |
| --- | --- | --- | --- |

Fijate que **no hay una columna «¿hook o chequeo?»**, y es a propósito. Después de la lección 8 esa pregunta ya no se hace por gate: **todo lo que entra en esta tabla está impuesto**. La pregunta que sí se hace es la anterior — *¿esto merece ser un gate?* —, y lo que no pasa ese filtro no va acá: va a tu guardrail, como instrucción.

Y el recordatorio que más falta hace: **si la condición no la puede evaluar un script o un checklist cerrado, no es un gate — es una sensación.**

1. **El state:** los campos, con un ejemplo a mitad de camino. Acordate de la regla — lo que la máquina necesita para decidir, nada más.
2. **Las primitivas:** qué skill mueve cada fase, qué subagent aparece (si aparece), y **dónde va el hook**.
3. **Seguridad:** dónde caen el threat modeling y el SAST en tu flujo. Si decidís sacarlos, **escribí por qué** — es una decisión válida para un proyecto personal descartable, pero tiene que ser **una decisión**, no un olvido.
4. **El test final del documento.** Releelo y preguntate: *¿alguien podría construir esta máquina leyendo **solo** esto?* Si la respuesta es no, le falta algo — y ese algo es exactamente lo que te va a trabar cuando lo repitas con otra herramienta.

> ✅ **Lo lograste cuando** tenés un `daw-design.md` que describe tu pipeline entero —fases, gates, state, primitivas y seguridad— con **el porqué de cada decisión escrito**.

## 🔎 La muestra: el `daw-design.md` de TicketTriage

> ⚠️ **Leelo como lo que es: UN EJEMPLO DE PERSONALIZACIÓN, no el modelo a copiar.** Esto **no es DAW**, y no es «la versión correcta» de nada. Es **el pipeline propio** de la app de ejemplo, que eligió el **camino B** y por lo tanto **se apartó de DAW a propósito**: le cambió los nombres a las fases, sacó dos, y decidió sus propios gates. Si tu diseño no se parece en nada a éste, **puede estar perfecto**. Lo que sí tenés que copiar de acá **no es el contenido: es la forma de razonar**. Fijate que cada desvío respecto de DAW viene con **qué se pierde** y **por qué se asume**. Ése es el entregable. Un documento que dice *«saqué RELEASE»* sin más es una lista de preferencias; uno que dice *«saqué RELEASE, pierdo la trazabilidad de cierre, vuelve en el M8»* es un diseño.

Así quedó el de la app de ejemplo. Eligió el **camino B**:

```
# Pipeline de TicketTriage — diseño

## Camino: B (personalizar DAW)
El flujo me sirve, pero trabajo solo y todavía no tengo proceso de PRs.
Dos cosas sobran tal como están.

## Fases
DEFINE ─[A]→ SPEC ─[B]→ BUILD ─[C]→ VERIFY ─[D]→ listo

Cambios respecto de DAW:
- CLASSIFY se saca: trabajo un solo tipo de pedido (features de mi app).
  Pierdo los tiers y el carril rápido; asumido, todavía no me hacen falta.
- RELEASE se saca: no tengo flujo de PRs. Vuelve en el M8, cuando monte CI.
  Pierdo el commit con convención y la trazabilidad de cierre. Asumido.
- El resto queda igual.

## Gates
Los cuatro impuestos por hook: los cuatro tienen condición verificable, así que
ninguno se queda en promesa. Lo que cambia entre ellos es QUIÉN la verifica.

| Gate | Condición verificable | Quién valida | State |
|---|---|---|---|
| A | El PRD pasa el checklist de validación | skill `daw-validate-prd` + yo | gates.define |
| B | Existe docs/daw/specs/spec-{ticket}.md y la validación pasa | skill `daw-validate-spec` + yo | gates.spec |
| C | Suite en verde + SAST sin hallazgos críticos | skills `daw-test` y `daw-security-sast` | gates.tests, gates.sast |
| D | Cumple todos los criterios de aceptación del spec | subagent `daw-module-verifier` (no escribió el código) | gates.verify |

## State (.daw-state.json)
{ "ticket", "title", "phase": "DEFINE|SPEC|BUILD|VERIFY",
  "gates": { define, spec, tests, sast, verify }, "history": [] }

A mitad de camino:
{ "ticket": "FEAT-001", "title": "Clasificación de tickets con IA",
  "phase": "BUILD",
  "gates": { "define": true, "spec": true, "tests": false, "sast": false, "verify": false } }

## Primitivas por fase
- DEFINE: skill `daw-validate-prd`
- SPEC:   skill `daw-create-spec` + mi skill `create-prd-propio` del M3
- BUILD:  implementación + el hook del gate B vigilando cada escritura
- VERIFY: subagent `daw-module-verifier` (contexto limpio) + skill `daw-test`

## Seguridad
- Threat modeling: se queda en SPEC. La app procesa texto de usuarios y lo
  clasifica: hay superficie de prompt injection que quiero pensar antes.
- SAST: gate de BUILD (gate C). No negociable.
- DAST: no es gate de este pipeline. Necesita la app levantada y yo no tengo
  ambiente todavía, así que sería un gate que se marca cumplido sin cumplirse.
  Vuelve en el M8, corriendo en CI, que es donde sí se puede.
```

Y ahora sí, **lo que hay que copiar de esta muestra**: no el pipeline, sino estas cuatro maneras de decidir.

- **Toda exclusión dice qué garantía se pierde.** *«RELEASE se saca»* a secas es un olvido; *«se saca, pierdo trazabilidad de cierre, vuelve en el M8»* es una decisión. La diferencia es enorme y se nota al leerlo.
- **Ningún gate queda a medias.** El que no se podía verificar de verdad no quedó como «gate flojo» con una nota al pie: **quedó afuera de la tabla**, con su motivo escrito. Es la regla de la lección 8 aplicada — si no lo podés imponer, no lo llames gate.
- **Se apartó de DAW donde le convenía, y no donde no.** Cambió las fases, porque su trabajo es de un solo tipo. Pero **no le cambió el nombre a los skills ni movió las carpetas**: eso no le resolvía ningún problema y le costaba compatibilidad con todo lo que viene instalado. Renombrar por renombrar es trabajo que no rinde — personalizar es sacar lo que te estorba, no repintar lo que ya funciona.
- **La seguridad se pensó, no se copió.** Mantiene el threat modeling **con un motivo concreto** (procesa texto de usuarios) y deja el DAST afuera **con un motivo concreto** (no tiene cómo correrlo honestamente). Las dos decisiones son defendibles porque tienen un porqué atado a esa app y no a una regla general.

—

## 🎯 Cierre del Módulo 5

Arrancaste este módulo con el picorcito que te dejó Spec Kit: un proceso que existía porque vos lo sostenías, y que se caía el día que estabas cansado. Elegiste **workflow con gates** —y no por moda, sino porque el resultado importa y se repite—, y entendiste que son rieles y no correa corta.

Después conociste **DAW**, creaste el repo de tu app con pipeline, te trajiste el PRD, los guardrails y los skills que ya tenías validados, y **pasaste tu primera feature de punta a punta**. Provocaste un bloqueo a propósito y viste con tus ojos la diferencia entre pedir y imponer.

Con la máquina andando la abriste por dentro: las cinco primitivas y su coreografía, promesa vs enforcement con sus límites honestos, cómo se diseña una fase como contrato, por qué la seguridad va adentro del pipeline, y cómo la máquina recuerda y se autolimita. Y terminaste **modificándola**: sacaste una fase, moviste un gate a hook y metiste un skill tuyo adentro del flujo.

> 🧠 **Lo que realmente te llevás:** ya no mirás un agente, **mirás un sistema** — y entendés de qué piezas está hecho. Podés agarrar cualquier herramienta agéntica que salga el año que viene, abrirla, y decir *«esto es el orquestador, esto es el state, y acá no hay enforcement real, solo un prompt que pide por favor»*.

## 🔨 Lo que viene

Con esto cerrás el módulo **evaluado** del bloque agéntico: tenés tu app construida por un pipeline, con Claude, y el diseño de cómo querés que sea ese pipeline.

Lo que sigue es la parte que hace que todo esto valga de verdad. En el **Módulo 6** repetís el ejercicio con **OpenCode**, y en el **Módulo 7** con **Copilot CLI**: **el mismo método, la misma app, otra herramienta**. Los dos son cortos y van directo al grano —la teoría de orquestación ya la tenés—, y su valor está en algo que no se puede explicar, solo experimentar: **sentir en las manos qué cambia y qué no** cuando movés el pipeline de una herramienta a otra.

Ahí la tabla de primitivas de la lección 7 se vuelve oro. Vas a descubrir que el método —las fases, los gates, el state, el grafo— **no se toca**, y que lo único que cambia es el enchufe. Que es exactamente la conclusión que queremos que te lleves: **lo que aprendiste no depende de la herramienta**.

Y después, con la versión que más te guste, seguís endureciéndola: **Módulo 8** (CI y code review), **Módulo 9** (evals), **Módulo 10** (deploy y monitoreo), hasta el Demo Day.

Llegás con el repo armado, la máquina conocida y tu diseño escrito. **Nos vemos en el Módulo 6.** 🚀
