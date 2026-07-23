---
titulo: "Skills: empaquetá tus workflows reutilizables"
capitulo: "05-Módulo 3 Construí con red Git skills y disciplina"
orden: 5
source: "apuntes/slides/00-raw/05-Módulo 3 Construí con red Git skills y disciplina/05-Skills_ empaquetá tus workflows reutilizables – MUG.html"
source_sha256: 22ceaf89215f3785
extraido: 2026-07-18
---

# Skills: empaquetá tus workflows reutilizables

Acordate del ejercicio *Vibecodeá tu PRD*, en el módulo pasado: para auditar tu PRD tuviste que pasarle al agente el template completo, el checklist de calidad punto por punto, las advertencias de «no inventes features»… varios prompts largos, cuidadosamente armados. Salió bien. Ahora la pregunta incómoda: ¿y la próxima vez? 🔁 Porque va a haber una próxima vez —en este curso reconstruís tu app varias veces, y en la vida real los PRDs se escriben seguido—. ¿Vas a volver a tipear todo eso, esperando acordarte de cada punto? Cada vez gastás tiempo (y tokens) reexplicando algo que ya sabés que querés siempre igual; y peor, cada explicación sale un poco distinta, así que el resultado nunca es consistente.

Hay una forma mejor: **empaquetar ese workflow una sola vez** y que el agente lo invoque solo cuando hace falta. Eso es un **skill**. Y dominarlo es, posiblemente, lo que más te separa de alguien que solo «tira prompts»: en vez de pedir mejor, **equipás** a tu agente con capacidades que antes no tenía.

En esta lección vas a entender **qué es un skill** y en qué se diferencia de las otras formas de configurar al agente, y vas a ver **cómo es uno por dentro** 🔬. Tu **primer skill propio** lo vas a escribir en la próxima lección —y va a ser exactamente ese: el que empaqueta tu workflow de PRD—; acá te doy todo lo que necesitás para que salga bien y, sobre todo, una forma nueva de pensar tu trabajo con la IA. 🎯

## 🧩 Qué es un skill

Un **skill** es una carpeta con un archivo `SKILL.md`: un markdown con instrucciones que el agente carga **cuando detecta que la tarea lo amerita**. La mejor analogía es una **recetita que le dejás al chef** 👨‍🍳. El chef ya sabe cocinar (el modelo ya sabe programar) → la receta le dice exactamente *cómo querés vos ese plato*, sin que tengas que pararte al lado a explicárselo cada vez.

¿La diferencia con tirar un prompt largo cada vez? Que el skill **vive en tu proyecto**. Y eso, que suena chico, cambia todo:

- **Es reutilizable.** Lo escribís una vez y lo usás siempre; no reescribís las instrucciones en cada conversación.
- **Es versionable.** Entra en Git como cualquier archivo: evoluciona con tu proyecto, queda en el historial y podés mejorarlo con el tiempo.
- **Se dispara automáticamente.** No tenés que acordarte de invocarlo — el agente lo saca cuando la tarea encaja.
- **Se comparte.** Si trabajás en equipo, todos arrancan con las mismas capacidades cargadas, sin depender de que cada uno tenga el prompt mágico guardado en un bloc de notas.

## 🆚 Skill vs guardrail vs command (no los confundas)

Hay tres cosas que se parecen mucho pero **no son lo mismo**, y mezclarlas es el error más común al arrancar. Te las pongo lado a lado:

|  | Qué es | Cuándo actúa |
| --- | --- | --- |
| **Guardrail** (`CLAUDE.md`) | Contexto **siempre-on**: cómo comportarse en TODO el proyecto | Siempre, en cada turno |
| **Custom command** | Un **prompt guardado** que disparás a mano (`/loquesea`) | Cuando vos lo invocás |
| **Skill** | Una **capacidad empaquetada** que el agente invoca solo | Cuando la tarea lo amerita (automático) |

La regla mental para no marearte: el **guardrail** es *cómo te comportás siempre*, el **command** es *un atajo que vos apretás*, y el **skill** es *una habilidad que el agente saca de la galera justo cuando la necesita* 🎩. Esa última parte — que se active solo, sin que vos lo pidas — es lo que lo hace tan potente: no es una herramienta que tenés que recordar usar, es una capacidad que el agente ya tiene incorporada y aplica en el momento justo.

## 🔬 Anatomía de un skill

Un `SKILL.md` tiene dos partes: el **frontmatter** (configura) y el **cuerpo** (instruye). Veamos uno real —y no uno cualquiera: **`create-prd`**, el que empaqueta el workflow de PRD que hiciste a mano en el primer ejercicio—:

```
---
name: create-prd
description: Crea o audita un PRD siguiendo el template y el checklist de calidad del curso. Se usa cuando el usuario pide crear, revisar o endurecer un PRD.
---

# Create PRD

Cuando el usuario pida crear o auditar un PRD:

1. Usá el template: Contexto y Problema, Objetivos, RF (RF-01…), RNF (RNF-01…),
   Criterios de Aceptación (Dado/Cuando/Entonces), Fuera de Alcance, Riesgos y Dependencias.
2. Aplicá el checklist de calidad, punto por punto:
   - cada RF es atómico (una sola acción) y dice "debe";
   - cada RNF tiene un número concreto (no "rápido" → "< 3 s p95");
   - cada RF tiene al menos un AC binario, en formato Dado/Cuando/Entonces;
   - hay un AC de control de acceso;
   - el "Fuera de Alcance" es explícito.
3. Antes de inventar cualquier requerimiento, PREGUNTALE al usuario.
4. NO agregues features que el usuario no pidió.
```

¿Te suena? Es **exactamente** lo que le dictaste al agente, prompt a prompt, cuando vibecodeaste tu PRD. La diferencia es que ahora vive en un archivo: lo escribís una vez y no lo volvés a tipear nunca.

Fijate en las dos partes. El **frontmatter** (lo que va entre los `---`) es la ficha del skill: su `name` y, sobre todo, su `description` — la línea que el agente lee para decidir si lo usa. El **cuerpo** (todo lo de abajo) son las instrucciones que sigue una vez que decidió activarlo: acá es donde le dictás tu workflow, paso a paso.

Eso es todo: un archivo de texto, sin magia. Fijate que no hay nada «técnico» raro — el valor no está en la sintaxis, está en **lo claro y específico que seas** al describir el workflow. Cuanto mejor capturás *cómo lo hacés vos*, mejor lo replica el agente.

> 📁 **¿Dónde vive?** En `.claude/skills/<nombre>/SKILL.md` si es del proyecto (se versiona y lo comparte el equipo), o en `~/.claude/skills/` si es tuyo personal y lo querés en todos tus proyectos.

## 🎯 La `description` es lo más importante

Acá va el secreto que casi nadie te cuenta: si tu skill **no se dispara**, el problema casi nunca son las instrucciones del cuerpo → es la **`description`**.

¿Por qué? Porque el agente decide si usar un skill leyendo justamente esa línea. Antes de ejecutar nada, escanea las `description` de todos tus skills y elige cuál encaja con lo que le pediste — como quien mira los títulos de los libros en un estante sin abrirlos. Si esa línea está vaga, no lo invoca nunca y tu skill queda ahí, juntando polvo 🧹. Por eso conviene cuidarla más que ninguna otra parte:

- Escribila **en tercera persona** y aclará **cuándo** usarlo: *«Se usa cuando el usuario pide crear, revisar o endurecer un PRD»* funciona mucho mejor que *«ayuda con PRDs»*.
- Sé explícito con los disparadores: nombrá las situaciones concretas donde aplica, así el agente las reconoce.

Una buena `description` es, literalmente, la diferencia entre un skill que te cambia la forma de trabajar y uno que nunca se enciende.

## ✅ Buenas prácticas

Una vez que tenés la idea, hay un puñado de prácticas que separan un skill que funciona de uno que estorba. Te las dejo con el porqué de cada una, para que las incorpores desde el primer skill que escribas:

- **Una responsabilidad por skill.** Si tu skill hace tres cosas, en realidad son tres skills. Mantener cada uno enfocado los hace más fáciles de disparar, de entender y de mantener.
- **`SKILL.md` corto** → apuntá a menos de ~500 líneas. El detalle pesado va en archivos aparte que el skill referencia *cuando los necesita*. Esto se llama **progressive disclosure**: no le metés todo el contexto en la cara de una, sino que lo cargás a demanda. Tu agente (y tu cuota de tokens) lo agradecen. 🪙
- **Código determinista para trabajo determinista.** Si algo se resuelve con un script, metelo como script. No le pidas al LLM que «calcule» lo que un `for` resuelve gratis, instantáneo y sin equivocarse nunca.
- **Ejemplos concretos > reglas abstractas.** Un ejemplo bien elegido le enseña al agente más que diez bullets de teoría. Mostrale el resultado que querés, no se lo describas en abstracto.

### 🔎 La muestra: `create-prd` en acción

El skill que viste en la Anatomía es justo el que vas a escribir en el próximo ejercicio. Lo interesante es **cómo se activa**: no lo invocás vos. Escribís algo tan simple como *«armame el PRD de una app para gestionar los turnos del club»*, y el agente **lee la `description`** del skill (*«Se usa cuando el usuario pide crear… un PRD»*), la matchea con tu pedido y lo **dispara solo**: te hace las preguntas del workflow, aplica el template, corre el checklist —todo lo que en el primer ejercicio le dictaste a mano, ahora sin que se lo pidas—.

Esa es toda la magia, y por eso insistí tanto con la `description`: una línea bien escrita es lo que hace que la capacidad aparezca exactamente cuando la necesitás. Tu método de PRD —el que te costó aprender— queda cableado en el agente.

## 🚀 Por qué esto importa

Esto no es un truco más para sumar a la lista. En 2026, los builders que de verdad la rompen **equipan a su agente con skills** en vez de re-explicar todo a cada rato. Es, literalmente, el salto de *prompter* a *builder*: dejás de pedir mejor y empezás a construir el entorno en el que tu agente trabaja.

Y ojo con esto, porque es el hilo que vamos a tirar más adelante: acá aprendiste a **escribir** skills. En el **Módulo 5** los vamos a **orquestar** — combinarlos con hooks, subagents y un estado persistente para armar tu propio pipeline de desarrollo. Pero todo arranca con esta pieza fundamental: la recetita. 🧩

Y ahora sí, a las manos: en el **próximo ejercicio** escribís `create-prd`, lo usás para generar tu PRD de nuevo —esta vez con un solo comando— y lo comparás con el que vibecodeaste, para ver con tus propios ojos qué gana (y qué no) al empaquetar el workflow. Como tu proyecto ya está bajo Git, el recambio queda commiteado como corresponde. ➡️
