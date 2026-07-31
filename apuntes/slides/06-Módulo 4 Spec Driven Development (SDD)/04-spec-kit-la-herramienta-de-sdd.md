---
titulo: "Spec Kit: la herramienta de SDD"
capitulo: "06-Módulo 4 Spec Driven Development (SDD)"
orden: 4
source: "apuntes/slides/00-raw/06-Módulo 4 Spec Driven Development (SDD)/04-Spec Kit_ la herramienta de SDD – MUG.html"
source_sha256: 04b627e91ac47433
extraido: 2026-07-31
---

# Spec Kit: la herramienta de SDD

Ya sabés qué es el SDD, por qué importa y de dónde viene. Pero «escribí un spec y dirigí desde él» puede sonar abstracto: ¿cómo se hace eso en la práctica, sin inventar un proceso propio cada vez? Acá entra **Spec Kit**, la herramienta que vamos a usar todo el módulo. 🧰

## 🐙 Qué es Spec Kit

**Spec Kit** es un **toolkit open-source de GitHub** que toma el flujo del Spec-Driven Development y lo convierte en una secuencia de **comandos concretos**. En vez de que vos inventes cómo escribir un spec, cómo clarificarlo, cómo pasar de ahí a un plan y a tareas, Spec Kit te da ese camino ya trazado: una serie de comandos `/speckit.*` que recorrés en orden. Nació dentro de GitHub como un experimento interno para poner en práctica las ideas de SDD que veníamos viendo en la lección anterior, y se liberó como open-source porque el problema que resuelve —cómo hacer que el spec no se desincronice del código— no es exclusivo de GitHub: le pasa a cualquier equipo que construye con agentes.

Y acá está lo más importante de entender, porque es lo que lo hace encajar con todo lo que venís usando: **Spec Kit siempre corre dentro de un agente de IA.** No es una app aparte ni una web; son comandos `/speckit.` *que ejecutás* adentro* del agente. No existe un «Spec Kit suelto» sin agente —su trabajo es, justamente, dirigir a un agente por el flujo SDD—. Así que usarlo dentro de tu agente no es una limitación: **es lo que Spec Kit es.**

Y es **agnóstico**: anda con **más de 30 agentes** (Claude Code, Copilot, OpenCode, Cursor, Gemini, Codex…). Vos elegís cuál. En este módulo vamos a usar **Claude Code** como ejemplo —es el tool principal del curso—, pero todo lo que veas funciona igual con el agente que prefieras: solo cambia un valor al inicializar. Esa portabilidad, de hecho, es una de las gracias del SDD, y la vamos a aprovechar en M5-M8, cuando lleves tu forma de construir de una herramienta a otra.

(No es la única herramienta del mercado —Amazon tiene **Kiro**, que apunta a algo parecido—, pero Spec Kit es open-source, agnóstico y vive donde ya trabajás, sin atarte a un único proveedor de nube ni de modelo. Por eso en «Prepará tu entorno» instalaste su CLI: ya lo tenés listo.)

## 🪄 Qué problema te saca de encima

Pensá qué pasaría sin una herramienta así: tendrías que acordarte de escribir todas las secciones del spec, de no saltearte la clarificación de ambigüedades, de generar un plan técnico antes de codear, de descomponer en tareas… y hacerlo igual cada vez, a mano, con tu propia disciplina como único sostén. Es justo el tipo de proceso que se abandona apenas hay apuro —y el apuro, en un proyecto real, aparece siempre—.

Spec Kit te saca esa carga: **te da la estructura y la disciplina como comandos**, así no dependés de tu memoria ni de tu fuerza de voluntad un martes a las 7 de la tarde. Seguís el flujo, comando por comando, y cada paso deja un artefacto concreto (el spec, el plan, las tareas) que podés revisar antes de avanzar y que queda guardado, versionado, junto con tu código. La disciplina deja de ser un esfuerzo heroico y pasa a ser el camino por defecto. Y como es una herramienta activa y de código abierto, se sigue actualizando semana a semana con lo que la comunidad va aprendiendo sobre cómo dirigir mejor a los agentes — no es un estándar cerrado, es una disciplina en evolución.

## 💡 Para aplicar

Antes de seguir, abrí tu agente y confirmá que tenés Spec Kit a mano (lo instalaste en «Prepará tu entorno»). En la próxima lección vamos a inicializarlo en un repo nuevo y vas a ver aparecer los comandos `/speckit.*` —tener el CLI andando ahora te evita frenar después—.

Con la herramienta presentada, pasemos a las manos: vamos a **crear el repo de M4 e inicializar Spec Kit**. ➡️
