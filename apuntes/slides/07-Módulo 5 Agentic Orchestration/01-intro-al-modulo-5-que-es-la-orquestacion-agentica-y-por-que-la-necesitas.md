---
titulo: "Intro al módulo 5: qué es la orquestación agéntica y por qué la necesitás"
capitulo: "07-Módulo 5 Agentic Orchestration"
orden: 1
source: "apuntes/slides/00-raw/07-Módulo 5 Agentic Orchestration/01-Intro al módulo 5_ qué es la orquestación agéntica y por qué la necesitás – MUG.html"
source_sha256: 15e36d1e47460ca1
extraido: 2026-08-03
---

# Intro al módulo 5: qué es la orquestación agéntica y por qué la necesitás

En el Módulo 4 usaste Spec Kit y funcionó. Escribiste un spec antes del código, tuviste un contrato del que derivar todo, y probablemente fue la vez que más ordenado te sentiste construyendo con IA en todo el curso.

Pero si prestaste atención, algo quedó picando.

Corriste `/speckit.specify`, después `/speckit.plan`, después `/speckit.implement` — **a mano, uno por uno, cada vez**. Vos te acordabas del orden. Vos disparabas cada paso. Vos llevabas la cuenta de en qué punto ibas cuando volvías al otro día. Y si un martes cualquiera te salteabas la clarificación porque el cambio parecía chico, **no pasaba absolutamente nada**: la herramienta no se enteraba, el agente no protestaba, y el código salía igual.

Dicho de otro modo: **el proceso existía porque vos lo sostenías**. Funciona perfecto mientras estés concentrado y con tiempo. El día que estés cansado, apurado o con tres cosas encima, el proceso se cae — porque el proceso, en realidad, era tu memoria.

Eso es lo que arreglamos en este módulo. 🎼

## 🎼 Qué es Agentic Orchestration

**Orquestar es sacar el proceso de tu cabeza y ponerlo en el sistema.**

En vez de que vos decidas el orden, recuerdes el estado y vigiles que no se saltee ningún paso, eso lo hace una máquina: un pipeline con **fases** definidas, con **memoria que vive en disco**, y con **condiciones que no se pueden esquivar** porque las impone código y no la buena voluntad del modelo.

En el mercado, la disciplina se llama **Agentic Orchestration** y lo que se construye se llama **agentic workflow**. Vale la pena que te quedes con los nombres, porque no es un tema de nicho ni una moda de este curso: es la diferencia entre **usar IA para escribir código** y **tener un proceso de desarrollo asistido por IA**. La primera la tiene cualquiera con una suscripción. La segunda es lo que distingue a un equipo que puede confiar en lo que produce.

## 🧗 La escalera que venís subiendo

Y acá viene lo lindo: esto no aparece de la nada. Es **el escalón siguiente de una escalera que venís subiendo desde el Módulo 2**, aunque no te lo hayamos dicho con estas palabras.

Mirala completa, porque cuando la ves de lejos aparece un patrón muy claro — **cada escalón te dio más determinismo a cambio de menos improvisación**:

| Escalón | Qué ganaste | Qué quedó sin resolver |
| --- | --- | --- |
| **Prompt suelto** (M2) | Velocidad brutal para arrancar | Nada persiste; el resultado depende de cómo lo pediste ese día |
| **Guardrail** (M2) | Las reglas dejaron de repetirse en cada prompt | Es **contexto, no ley**: el modelo puede ignorarlo, y cuanto más largo, más lo diluye |
| **Skill** (M3) | El *cómo* de una tarea, escrito una vez y repetible | El skill sabe hacer lo suyo, pero **nadie decide cuándo ni en qué orden** se usan |
| **SDD con Spec Kit** (M4) | Un orden y un contrato: el spec como fuente de verdad | **Vos sos el motor**, y las fases son una convención, no una restricción |
| **Pipeline orquestado** (M5) | El orden, la memoria y los límites viven en el sistema | ⬅️ **estás acá** |

Fijate especialmente en una cosa: hasta el Módulo 4, **el que recordaba y vigilaba eras vos**. Todos los escalones anteriores sacaron *conocimiento* de tu cabeza y lo pusieron en el repo — las reglas en el guardrail, el procedimiento en el skill, el contrato en el spec. Ninguno sacó **el control**. Ése es el que falta, y es el de este módulo.

Y una aclaración de criterio, para que no leas mal la escalera: **subir no invalida los escalones de abajo**. Para un prototipo que vas a tirar el viernes, el prompt suelto sigue siendo la respuesta correcta, y montar un pipeline con fases y gates sería gastar más tiempo en la ceremonia que en el trabajo. La madurez profesional no es usar siempre lo más pesado — es **saber en qué escalón parar para cada tarea**. A ese criterio volvemos al cerrar el módulo, cuando decidas cómo va a ser tu pipeline.

## 🩹 Los tres agujeros que tapa

Un agente trabajando sobre código falla **siempre de las mismas tres formas**. No es mala suerte ni un modelo malo: son consecuencias estructurales de trabajar sin proceso. Y lo interesante es que **cada una tiene su antídoto**, con nombre propio, dentro de un pipeline:

- **Salta pasos** — va directo a escribir sin entender el requerimiento. Pasa porque el modelo está optimizado para *responder*, y escribir código **parece** responder: un archivo lleno de líneas se ve como progreso, preguntarte «¿qué querés decir con login?» se ve como demora. *Antídoto:* una **máquina de estados**, donde en la fase de planificación escribir código no es «algo que no conviene», es algo que **no se puede**.
- **Pierde contexto** — en sesiones largas olvida decisiones tomadas cuarenta mensajes atrás y en qué punto del trabajo estaba. Pasa porque la ventana de contexto es finita y, cuando se llena, el sistema compacta — y compactar es resumir, y resumir es perder. Lo que se pierde no lo elegís vos. *Antídoto:* **el state en disco**, que sobrevive a que cierres la sesión, te vayas de vacaciones y vuelvas.
- **Se sobrecarga** — si le das cuarenta reglas juntas, cumple las que le quedaron más a mano. Es el mismo fenómeno que trabajaste en *context engineering* en el M2, y acá se ve en su versión más frustrante: vos **sí** escribiste la regla, y aun así no se cumplió. *Antídoto:* **cargar solo las reglas de la fase actual**, para que ninguna instrucción compita con otras treinta y nueve.

> 🧠 Ninguno de los tres se arregla escribiendo un prompt mejor. Lo intentaste y sabés hasta dónde llega. Son problemas **estructurales**, y los problemas estructurales se resuelven con **estructura**.

## 🗺️ Qué vas a hacer en este módulo

En orden, y sin vueltas:

1. **Definís qué clase de máquina** querés —workflow con rieles, no agente suelto— y por qué. Es una decisión de cinco minutos que condiciona todo lo demás.
2. **Conocés DAW — Dilux Agentic Workflow**: el pipeline con el que vas a trabajar de acá hasta el Módulo 7. Es open source y vive en [github.com/soydiloreto/dilux-agentic-workflow](https://github.com/soydiloreto/dilux-agentic-workflow). Vas a ver sus fases, sus gates y de qué está hecho.
3. **Creás el repo de este módulo, lo instalás y lo corrés.** Te traés el PRD —lo único que viaja, porque el instrumental te lo da el pipeline— y pasás la primera feature de tu app por las seis fases. A partir de ahí, todo lo que leas lo vas a poder mirar en tu propia terminal.
4. **Lo abrís por dentro**: las cinco primitivas, por qué un gate impuesto vale más que uno prometido, cómo se diseña una fase, y por qué la seguridad va adentro del pipeline y no al costado.
5. **Lo personalizás** para tu proyecto y entregás el diseño de **tu** pipeline.

Al final tenés tres cosas concretas: **el repo de tu app construida con un pipeline agéntico**, **DAW corriendo y adaptado a vos**, y un **`daw-design.md`** que dice cómo va a ser el tuyo. Ese documento es el registro de tus decisiones, y lo que te va a permitir reconstruir el mismo pipeline con OpenCode (M6) y con Copilot (M7).

Antes de mirar ninguna máquina, hay **una sola decisión de fondo** que tomar. ➡️
