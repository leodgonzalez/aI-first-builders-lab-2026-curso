---
titulo: "Intro al módulo 3: Construí con red"
capitulo: "05-Módulo 3 Construí con red Git skills y disciplina"
orden: 1
source: "apuntes/slides/00-raw/05-Módulo 3 Construí con red Git skills y disciplina/01-Intro al módulo 3_ Construí con red – MUG.html"
source_sha256: e36b58cb013635c3
extraido: 2026-07-17
---

# Intro al módulo 3: Construí con red

Bienvenido al Módulo 3, Builder. Antes de contarte qué vamos a hacer, sacá esa lista que te pedí que anotaras al final de tu app v1 —la de «dónde dolió»—. 📝 ¿La tenés? Seguro dice cosas como estas:

- La IA rompió algo que andaba, y no hubo forma de volver atrás.
- Rehiciste trabajo que ya estaba hecho.
- Le explicaste lo mismo dos y tres veces, en sesiones distintas.
- Terminaste con miedito de pedir cambios, por lo que se podía romper.

Buenas noticias: **este módulo es la respuesta a esa lista, punto por punto.** Nada de lo que viene es teoría suelta: cada herramienta llega justo después de que sentiste el problema que resuelve. Ese era el plan desde el principio —por eso te mandé a construir sin red—.

## 📁 Lo primero que tenés que saber: acá arrancamos con una carpeta NUEVA

Prestale atención a esto porque ordena todo el módulo y evita el error más fácil de cometer:

> ⚠️ **En este módulo NO seguimos trabajando en la carpeta de la v1.** Vamos a crear un **directorio nuevo** —una carpeta desde cero— que se va a **convertir en un repositorio Git** (con su espejo en GitHub). A esa carpeta nueva viajan **solo tres archivos** de la anterior: tu `PRD.md`, tu `AGENTS.md` y tu `CLAUDE.md`. **El código de la v1 NO viaja**: se queda en su carpeta, de testigo. La app se reconstruye acá, con red desde el primer minuto.

¿Por qué así? Porque la v1 nació sin red a propósito, y ponerle Git *encima* a algo ya construido es empezar la historia por la mitad. Tu proyecto de verdad —el que va a crecer durante todo el curso— merece nacer bien: versionado desde el día cero, con cada paso registrado. Los documentos (contrato y reglas) son lo que vale la pena llevarse; el código, con todo lo que aprendiste, sale mejor si lo reconstruís.

## 🧰 Qué te llevás de este módulo

- **Git, tu red de seguridad** (desde cero, aunque nunca lo hayas tocado): puntos de guardado, deshacer, historia. El «no hay vuelta atrás» se termina acá. → 🛠️ nace el **repo de tu proyecto**: la carpeta nueva, con Git desde el día cero y publicada en **GitHub**.
- **La disciplina de iterar con red**: commit cuando funciona, revertir en vez de parchar, diffs chicos, saber cuándo frenar.
- **Skills: capacidades empaquetadas** que el agente invoca solo. Se acabó el «explicarle lo mismo tres veces». → 🛠️ escribís tu primer skill (`create-prd`, que empaqueta TU método de PRD y lo corre en loop) y 🛠️ un desafío: el segundo (`conventional-commit`), esta vez solo.
- **Correctitud y seguridad**: el test antes que el código —para que la IA no se corrija su propio examen— y por qué revisar no es opcional (~45% del código generado trae alguna vulnerabilidad).
- Y el gran final: → 🛠️ **reconstruís tu app** desde tu PRD final, ahora con todo el equipamiento, y la llevás a su **v2** —más completa, más sólida y, sobre todo, construida sin miedo, con **cada funcionalidad commiteada y pusheada a `main`**—.

¿Notaste el patrón? Es el mismo del módulo pasado: **teoría → práctica inmediata**, sobre tu proyecto real. Y el viaje de tu app sigue su filosofía de loops: la construiste sin red (v1), la vas a reconstruir con red (v2), y en el próximo módulo la volvés a hacer con **Spec-Driven Development**. Cada vuelta, la misma app, mejor método.

## 🎁 Lo que entregás al final

El entregable de este módulo es **doble**:

1. Tu **PRD final** — regenerado con tu propio skill `create-prd` y curado por vos (el anterior se elimina: Git lo recuerda).
2. Tu **app v2** corriendo — reconstruida desde ese PRD, con su historia completa en Git y publicada en GitHub.

¿Y cómo se entrega? Con **una sola cosa: la URL de tu repositorio de GitHub**, en el ejercicio final del módulo. Ahí adentro va a estar todo: PRD, guardrails, skills, la app y su historia commit a commit.

Arranquemos por la herramienta que le pone fin al dolor más grande de tu lista: **Git, desde cero** —tranquilo, aunque no vengas del mundo técnico—. ➡️
