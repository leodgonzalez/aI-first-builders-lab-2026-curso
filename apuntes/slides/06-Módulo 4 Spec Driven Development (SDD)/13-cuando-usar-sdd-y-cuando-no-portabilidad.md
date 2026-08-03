---
titulo: "Cuándo usar SDD (y cuándo no) + portabilidad"
capitulo: "06-Módulo 4 Spec Driven Development (SDD)"
orden: 13
source: "apuntes/slides/00-raw/06-Módulo 4 Spec Driven Development (SDD)/13-Cuándo usar SDD (y cuándo no) + portabilidad – MUG.html"
source_sha256: b21b9911c06d875c
extraido: 2026-08-03
---

# Cuándo usar SDD (y cuándo no) + portabilidad

Ya recorriste el flujo completo y construiste una feature dirigida por spec. Ahora el criterio, que es lo que te hace profesional: **saber cuándo SDD vale la pena y cuándo es matar una mosca a cañonazos.** ⚖️

## 🎯 SDD sí, SDD no

SDD tiene un costo: escribir y clarificar un spec lleva tiempo. Ese costo se paga solo cuando hay algo que proteger. Conviene cuando el trabajo es **complejo**, cuando trabajás **en equipo** (el spec es el acuerdo común — reemplaza el «che, ¿vos entendiste que había que hacer esto así?» por un documento que todos leyeron), o cuando va a **producción** y los errores duelen de verdad (plata, usuarios reales, reputación). Ahí, la disciplina del spec te ahorra retrabajo, malentendidos e incidentes — el mismo tipo de dolor que sentiste en el muro de los 3 meses, pero evitado antes de que ocurra.

¿Y cuándo no? Cuando estás **prototipando o explorando una idea** para ver si pisa: ahí el vibecoding (M2-M3) es tu amigo, porque la velocidad importa más que el contrato y el costo de equivocarse es bajo — si el prototipo no sirve, lo tirás, y no perdiste tiempo especificando algo que nunca iba a sobrevivir. No es «SDD bueno, vibe malo» —son dos herramientas para dos momentos—. El builder maduro elige según el riesgo: vibe para tantear, SDD para construir en serio. Un ingeniero senior no usa SDD para un script descartable de una tarde, ni vibecodea a ciegas el sistema de facturación de su empresa.

Un caso que vale la pena nombrar: **SDD sobre código legacy**. Cuando entrás a un sistema que ya existe y nadie entiende del todo, escribir el spec de un cambio *antes* de tocarlo es una de las mejores formas de no romper nada — te obliga a entender y acordar qué tiene que pasar antes de meter mano, en vez de improvisar sobre un sistema que ya de por sí es frágil.

## 🔁 La portabilidad: el puente a lo que viene

Acá hay una propiedad del SDD que es clave para el resto del curso. Como el spec describe el *qué* (no está atado a una herramienta), **el mismo spec lo puede ejecutar cualquier agente.** El spec que escribiste para Claude Code lo podés correr en Copilot o en OpenCode y obtener la misma feature. El spec es portable; el agente es intercambiable. Esto es exactamente lo contrario de lo que pasaba con tus prompts de vibecoding en M2-M3: esos vivían pegados a la conversación con un agente puntual; el spec, en cambio, es un documento que cualquier agente puede leer y ejecutar.

Esa idea es, justamente, el puente a los **Módulos 5, 6 y 7**: ahí vas a llevar tu forma de construir de una herramienta a otra. Y un deslinde para que no te confundas: en este módulo usaste SDD **como método**, con Spec Kit, una herramienta ya hecha. En **M5** das el salto a un **pipeline agéntico propio** —tu Dilux Agentic Workflow, que orquesta skills, hooks y subagents en una máquina de estados— y construís tu app pasándola por él con Claude Code. En **M6 y M7** (opcionales) repetís el ejercicio con OpenCode y con Copilot. Acá *usaste* una máquina de SDD ya hecha; allá vas a *entender la tuya por dentro y personalizarla*.

## 💡 Para aplicar

Pensá en dos cosas que tengas pendientes: una idea que querés tantear rápido y un cambio serio sobre algo que ya funciona. Asignale a cada una su método —vibe para una, SDD para la otra— y, sobre todo, escribí *por qué*. Ese «por qué» es el criterio que te llevás del módulo, y es la pregunta que te vas a hacer cada vez que arranques algo nuevo de acá en adelante.

Cerramos con el integrador: aplicar todo esto al **spec de tu proyecto final**. ➡️
