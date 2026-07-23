---
titulo: "Ejercicio guiado: Construí tu app v1 (sin red)"
capitulo: "04-Módulo 2 Vibecoding profesional"
orden: 8
source: "apuntes/slides/00-raw/04-Módulo 2 Vibecoding profesional/08-Ejercicio guiado_ Construí tu app v1 (sin red) – MUG.html"
source_sha256: 03b31a255563e656
extraido: 2026-07-16
---

# Ejercicio guiado: Construí tu app v1 (sin red)

Llegó el momento que veníamos prometiendo desde el primer día: **vas a construir tu app.** 🏗️ Con todo lo que ya tenés —tu `PRD.md` v2 como contrato, tus guardrails como reglas de la casa, el prompting y el context engineering como oficio— vas a dirigir a la IA hasta tener **una primera versión que corre**. Hoy, acá, en este ejercicio.

Y una advertencia honesta antes de arrancar, porque es parte del diseño del curso: **vas a construir sin red de seguridad.** Sin control de versiones, sin botón de deshacer, sin puntos de guardado. Si la IA te reescribe mal un archivo que andaba, no hay vuelta atrás. ¿Por qué te mando así? Porque en el próximo módulo te doy la red completa —y quiero que cuando te la dé, sepas *exactamente* qué te estuvo faltando—. Las herramientas se aprecian de verdad cuando ya sentiste el problema que resuelven.

## 🎯 Qué vas a lograr (y qué NO)

Por lo mismo de arriba, el alcance es **deliberadamente chico**:

- **Una sola feature: el corazón de tu PRD.** La que demuestra la idea. No el login, no la pantalla linda: *la* funcionalidad por la que tu app existe. Mirá tus RF y elegí el que duele.
- **Cruda.** Sin pulir, sin casos borde, sin diseño. Un esqueleto que respira.
- **Que corra.** Que la puedas ejecutar y mostrar. «Casi anda» no cuenta.

> ⚠️ **Esta versión es una picadura, no una fractura.** Si en algún momento la IA te rompe algo feo y no lo podés recuperar, **no pasa nada**: esta v1 es corta a propósito. En el próximo módulo vas a crear una carpeta **nueva** que nace como **repo Git** y vas a **reconstruir la app ahí, mejor y con red abajo** — de esta carpeta solo van a viajar tus documentos (el PRD y los guardrails); la v1 queda acá, de testigo. Así que no inviertas horas de pulido que no vas a poder proteger.

## 🛠️ Tu turno: paso a paso con Claude Code

⏱️ **Tiempo estimado:** ~1 a 2 hs · 📦 **Entregable:** tu app v1 corriendo, mostrando la feature core del PRD, en tu carpeta de proyecto.

**1. Abrí Claude Code en tu carpeta de proyecto** (la que tiene `PRD.md` y guardrails). El contexto ya está servido: el agente lee tus reglas solo.

**2. Pedile el plan ANTES de que toque nada.** No lo largues a codear de una. Copiá y pegá:

```
Leé @PRD.md. NO escribas código todavía. Quiero construir SOLO la feature central
del PRD: <tu feature core>. Proponeme un plan corto, en pasos chicos y en orden,
y esperá mi aprobación antes de tocar nada.
```

Leé el plan **de verdad**. Es el checkpoint más barato que existe: un plan son palabras y se corrige en segundos; el código ya generado cuesta mucho más. Si encaró mal algo, decíselo ahí.

**3. Avanzá un paso por vez.** Con el plan aprobado, un pedido por paso:

```
Dale, arranquemos por el paso 1. Cuando termines, mostrame qué hiciste
y cómo lo pruebo. No sigas al paso 2 hasta que te lo confirme.
```

Y mientras avanzás, los hábitos del módulo, vivos:

- **Probá después de cada paso.** ¿Corre? ¿Hace lo que el paso prometía? Recién ahí seguís. Si apilás cinco pasos sin probar ninguno, cuando algo falle no vas a saber ni por dónde empezar.
- **Revisá antes de aceptar.** Si no entendés qué hizo, pedile que te lo explique en criollo. Aceptar a ciegas es apostar.
- **Cuidá el contexto:** `/context` cada tanto, y si la conversación se ensució o cambiás de tema, `/clear` y entrás fresco con los archivos que importan.

**4. Si se enrosca… respirá.** En algún momento el agente se va a trabar: un arreglo que rompe otra cosa, un error que «corrige» tres veces sin corregir. Sin red, tus opciones son limitadas —pedirle que lo intente distinto, achicar el pedido, `/clear` y replantear— y quizás pierdas un rato rehaciendo algo que ya andaba. **Prestale atención a esa sensación.** No es un accidente del ejercicio: es *el* aprendizaje del ejercicio.

**5. Cerrá contra el PRD.** ¿Arranca? ¿La feature core funciona de punta a punta, aunque sea fea? Listo: **construiste tu primera app dirigiendo a una IA.** Frase que hace un mes te hubiera sonado a ciencia ficción.

> ✅ **Lo lograste cuando** tu app corre y demuestra la feature central del PRD, el plan lo aprobaste vos antes de la primera línea, y anotaste al menos **una** situación donde extrañaste poder «volver atrás».

## 🪞 La reflexión (no la saltees: alimenta el próximo módulo)

Antes de cerrar, escribí dos respuestas honestas en cualquier papel:

- **¿Qué te voló la cabeza?** La velocidad, seguramente: la distancia entre «tengo un PRD» y «tengo una app que corre» se achicó a horas.
- **¿Dónde sufriste?** Sé específico: ¿la IA te rompió algo que andaba? ¿Rehiciste trabajo? ¿Te dio miedo pedirle un cambio grande por lo que podía romper? ¿Terminaste con miedo de tocar tu propia app?

Guardá esas notas. El próximo módulo arranca **exactamente ahí**: cada dolor que anotaste tiene una herramienta con nombre y apellido esperándote.

### 🔎 La muestra: la v1 de TicketTriage

La primera versión de **TicketTriage** salió de este mismo ejercicio: una sola feature —**crear un ticket y que la IA lo clasifique** (categoría + prioridad)— corriendo en una página mínima. Sin login, sin listados, sin borrador de respuesta: eso quedó para después. ¿Y el dolor? Apareció clarito: al pedir un retoque en la clasificación, el agente reescribió el archivo entero y rompió la validación del asunto que ya andaba… y no había forma de volver. Quince minutos rehaciéndola. **Anotado.** 📝

Tu app existe y la construiste vos, dirigiendo. Antes del repaso, te tengo un regalo para el bolsillo: el **arsenal de prompting profesional** —las técnicas que sirven con cualquier IA, para cualquier cosa, dentro y fuera del código—. ➡️
