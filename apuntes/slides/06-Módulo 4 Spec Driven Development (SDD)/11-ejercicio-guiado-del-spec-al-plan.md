---
titulo: "Ejercicio guiado: Del spec al plan"
capitulo: "06-Módulo 4 Spec Driven Development (SDD)"
orden: 11
source: "apuntes/slides/00-raw/06-Módulo 4 Spec Driven Development (SDD)/11-Ejercicio guiado_ Del spec al plan – MUG.html"
source_sha256: 0598960086f4b650
extraido: 2026-08-03
---

# Ejercicio guiado: Del spec al plan

Tenés un spec cerrado: sabés *qué* construir y *por qué*, sin ambigüedades. Ahora, por fin, llega el momento de hablar de **cómo** — y para eso está `/speckit.plan`. 🏗️

## ⚙️ Acá sí entra lo técnico

Durante todo el spec te pedí que no metieras stack ni decisiones de arquitectura. El plan es el lugar donde eso vive. Y hay un detalle importante que conviene que sepas antes de correr el comando: `/speckit.plan` **no adivina tu stack solo** —se lo decís vos, como argumento del comando, igual que le pasaste tu feature a `/speckit.specify`—. El agente **elabora** el plan técnico a partir de la dirección que le das: qué lenguaje y framework, cómo se estructura el código, qué piezas se crean, cómo se conectan.

Y acá es donde se cierra el círculo con tu `AGENTS.md`: **vos ya tenés un stack anotado ahí**, en la sección «Stack» que copiaste de tu repo de M2-M3 al preparar este repo. Este es el momento de usarlo: pasale ese mismo stack a `/speckit.plan` como argumento. Por default, **mantené el que ya tenías** —así el plan de esta vuelta usa el mismo stack que tu app de M2-M3, y la comparación entre métodos queda limpia (mismo resultado técnico, proceso distinto)—. Si en algún momento decidís cambiarlo, que sea a propósito, no porque el agente improvisó algo distinto al no decirle nada.

La separación importa: si mezclás el qué y el cómo desde el principio, terminás atando decisiones de producto a decisiones técnicas que capaz cambian. Primero acordás el comportamiento (spec), después elegís cómo materializarlo (plan). Y como el plan sale del spec, queda **trazable**: cada decisión técnica responde a algo que el spec pidió.

## 🚦 Para qué sirve la constitución acá (el «Constitution Check»)

Puede que te preguntes: si el stack se lo digo yo a mano en este comando, ¿entonces para qué escribimos la constitución en la lección anterior? Buena pregunta, y merece una respuesta precisa, no una excusa.

`/speckit.plan` no solo lee tu dirección técnica: **también lee `.specify/memory/constitution.md`**, y arma en el plan una sección obligatoria llamada **«Constitution Check»**. Ahí el agente valida, principio por principio, que el plan que está armando no viole ninguno de los que escribiste — y si algo choca (por ejemplo, tu constitución dice «test-first» y el plan no contempla tests), el gate lo marca como violación y te obliga a justificarla explícitamente o corregir el plan. Y no se chequea una sola vez: se revisa **antes** de arrancar el diseño técnico y **de nuevo después**, por si el diseño terminó pisando algo que al principio parecía cumplirse.

Entonces la respuesta completa es esta: **el stack es un dato que vos le das** (por eso lo repetís, no lo inventa); **la constitución es un filtro que se aplica automáticamente** sobre lo que sea que ese plan termine proponiendo. Uno te dice el qué técnico; el otro audita que ese qué técnico no traicione tus principios. No son la misma cosa disfrazada dos veces — son dos mecanismos distintos, y **los dos actúan en esta misma fase**.

## 👀 Revisá el plan antes de seguir

El plan es un checkpoint clave, así que leelo con atención — y prestale especial atención a la sección «Constitution Check»: si aparece algo marcado como violación sin justificar, no sigas de largo. Y prestá atención a algo que pasa seguido y es **sano**: a veces, al planear, el agente (o vos) descubre que el spec estaba incompleto —»para esto necesito saber X, y el spec no lo dice»—. Cuando pase, **volvé al spec, completalo, y regenerá el plan.** No es retroceder; es el loop de validación funcionando. Mejor descubrir el hueco acá, en palabras, que tres horas después en el código.

> 🏷️ Este ida y vuelta entre spec y plan tiene nombre en la documentación de Spec Kit: es el modelo **«flow-back»** de mantener tus artefactos —cualquiera de los tres (spec, plan, tareas) puede informar a los otros, y vos reconciliás—. No hace falta que te memorices el término, pero si lo cruzás en la documentación de la herramienta, ya sabés que es justo lo que veniste haciendo acá.

## 🛠️ Tu turno: generá y revisá el plan

⏱️ **Tiempo estimado:** ~20 min · 📦 **Entregable:** el plan técnico de tu feature, revisado, con el mismo stack de tu `AGENTS.md` (o el nuevo, si lo cambiaste a propósito) y sin violaciones de constitución sin justificar.

1. Con el spec cerrado, corré **`/speckit.plan`**, pasándole el stack de tu `AGENTS.md` (o el que decidiste usar para esta vuelta).
2. Leé el plan: ¿el stack es el que le pediste?, ¿la estructura es razonable?, ¿cada decisión técnica responde a algo del spec?
3. Revisá la sección **«Constitution Check»**: ¿hay algo marcado como violación? Si lo hay, corregí el plan o entendé por qué se justifica.
4. Si el plan revela que al spec le faltaba algo → volvé al spec, completalo y regenerá el plan.
5. Dejá el plan aprobado antes de avanzar a las tareas.

> ✅ **Lo lograste cuando** tenés un plan técnico que podés defender línea por línea contra el spec, sin huecos, sin violaciones de constitución sin explicar, y sin decisiones «porque sí».

### 🔎 La muestra: el plan de TicketTriage

Para la feature de clasificación, le pasamos a `/speckit.plan` el mismo stack que ya estaba en el `AGENTS.md` de TicketTriage desde M2:

```
/speckit.plan Usá el mismo stack de nuestro AGENTS.md: Python 3.12 + FastAPI, SQLite,
API de Claude (claude-sonnet-4-6). Front mínimo con HTMX.
```

Y el plan aterrizó las decisiones técnicas:

```
## Constitution Check
✓ Aislamiento de IA: la clasificación vive en un módulo dedicado (app/ai.py).
✓ Test-first: se planean tests con pytest antes de la implementación.
✓ Cero secretos: la API key se lee de variable de entorno.
Sin violaciones.

## Plan técnico
- Stack: Python 3.12 + FastAPI, SQLite, API de Claude (claude-sonnet-4-6).
- La clasificación vive en app/ai.py, función clasificar(texto) -> {categoria, prioridad}
  (aislada, como pide la constitución).
- Devuelve un set cerrado de valores; si el modelo no está seguro → "otro"/"baja" + flag de revisión.
- Tests con pytest, mockeando la llamada al modelo (no se pega a la API real en tests).
```

Fijate dos cosas. Primero, el stack —FastAPI, SQLite, Claude— es exactamente el mismo que ya estaba anotado en el `AGENTS.md` desde M2: no es casualidad, es la comparación entre métodos funcionando como tiene que funcionar. Segundo, el **Constitution Check** no es un saludo protocolar: audita, principio por principio, que el diseño que se está por generar no traicione lo que ya acordaste. Los dos mecanismos —tu dato de stack y el filtro de la constitución— trabajaron juntos en este mismo plan.

Con el plan aprobado, lo descomponemos en pasos accionables: **generar las tareas**. ➡️
