---
titulo: "Resumen y conclusiones del Módulo 3"
capitulo: "05-Módulo 3 Construí con red Git skills y disciplina"
orden: 11
source: "apuntes/slides/00-raw/05-Módulo 3 Construí con red Git skills y disciplina/11-Resumen y conclusiones del Módulo 3 – MUG.html"
source_sha256: 04fc1f62db29a5cf
extraido: 2026-07-30
---

# Resumen y conclusiones del Módulo 3

Este módulo fue la respuesta a tu lista de dolores de la v1: le pusiste **red, disciplina y superpoderes** a tu vibecoding, y volviste a construir para sentir la diferencia. Antes del quiz, repasemos las ideas que importan. Si algo no te suena, volvé a la lección antes de seguir. 🧠

## 🧷 Git: tu red de seguridad

- **Git es un sistema de save points:** repo = carpeta con memoria, commit = punto guardado, `git diff` = qué cambió, `git restore` = cargar la partida. Con eso entendés el 90% de las conversaciones sobre Git.
- El agente **maneja los comandos por vos** —vos los entendés para dirigirlo bien—. Y GitHub es el respaldo en la nube: tu repo ya vive ahí, y `git push` sube cada avance (los PRs y el trabajo en equipo llegan en el Módulo 9).
- 🛠️ **Ejercicio:** nació el **repo de tu proyecto** — una carpeta **NUEVA** a la que viajaron **solo** `PRD.md`, `AGENTS.md` y `CLAUDE.md` (el código de la v1 se quedó en su carpeta, de testigo), convertida en repo con `git init` y dada de alta en GitHub. Y probaste el botón de pánico rompiendo algo a propósito.

## 🥾 La disciplina de iterar con red

- **Commit-as-checkpoint:** cada vez que algo funciona, foto. Cuanto más seguido, más corta la distancia entre «se rompió» y «estoy sano».
- **Revertir en vez de parchar:** sobre un desastre no se apilan arreglos; se vuelve al último estado bueno y se reintenta limpio.
- **Diffs chicos y revisados**, y saber **cuándo frenar**: si van tres vueltas y se enrosca peor, `git restore` y replanteo. Insistir sobre un rumbo torcido no es perseverancia.

## 🧩 Skills: capacidades empaquetadas

- Un **skill** (`SKILL.md`) empaqueta un workflow que el agente **invoca solo** cuando la tarea encaja. La **`description`** es el trigger: si está vaga, el skill no se enciende nunca. Regla mental: **si se lo explicaste dos veces, es candidato a skill.**
- 🛠️ **Ejercicio:** escribiste **`create-prd`** —tu método completo de PRD: template, checklist y **loop** de auditoría— y lo viste dispararse solo para generar tu `PRD2`, que curaste con lo mejor de tu versión a mano. El recambio quedó commiteado; borraste el viejo sin miedo porque **Git lo recuerda**. Moraleja: **el skill garantiza el piso; tu juicio pone el techo.**
- 🛠️ **Desafío:** construiste **solo** tu segundo skill, **`conventional-commit`** — de acá en más, todos tus commits salen con formato profesional, gratis.

## 🔒 Correctitud y seguridad

- **Test-first prompting:** la prueba se escribe ANTES que el código, para que la IA no se apruebe su propio examen. Vos ponés la **regla de negocio** (eso lo sabés mejor que nadie, vengas de donde vengas); la IA pone la sintaxis; el verde no negocia. La cláusula anti-trampa: *«NO modifiques el test»*.
- El dato que lo justifica: ~**45% del código generado por IA trae alguna vulnerabilidad** (Veracode 2025). Revisar no es opcional: lo que aprobás lleva tu nombre. Los escáneres automáticos llegan en el Módulo 9; la calidad del sistema completo (evals), en el Módulo 10.

## 🏗️ Tu app v2

- 🛠️ **Ejercicio:** **reconstruiste tu app desde tu PRD final**, en el repo nuevo, con el taller completo —plan aprobado antes de la primera línea, pasos chicos, test-first en la lógica clave, revert cuando se enroscó— y el ritmo que te llevás para todo el curso: **funcionalidad lista → commit → push a `main`**. De «una feature cruda» a **las features core del PRD, funcionando y en la nube**.
- La comparación con la v1 es la lección del módulo: misma app, mismo vos, otra forma de trabajar. **Eso es construir con red.**

## 🧱 Los anti-patterns y el muro de los 3 meses

- Los **anti-patterns** comparten una raíz: **delegar el juicio**, no solo el tipeo. El builder delega el tipeo; el juicio se lo queda siempre.
- Aun con red, el vibecoding sin más método acumula deuda: código que cuesta entender, decisiones que nadie tomó, miedo a tocar. Ese **muro no es un argumento contra la IA, sino contra la IA sin método** — y es exactamente el dolor que viene a resolver el **Módulo 4**.

## 🎁 Tu entregable doble

- Tu **PRD final** (regenerado con tu skill `create-prd`, curado por vos) y tu **app v2** corriendo, con su historia en Git — entregados con **la URL de tu repositorio de GitHub** en el ejercicio de la app v2.

## 🎯 La gran conclusión

Construiste tu app **dos veces**: sin red y con red. Ya no hace falta que nadie te explique por qué Git, por qué skills, por qué disciplina — lo sentiste. **Eso es ser builder: método que se gana con las manos.**

Y también sentiste que la red no lo resuelve todo: el muro sigue ahí, esperando a los que vibecodean sin más estructura. En el **Módulo 4** lo atacamos de frente con **Spec-Driven Development**: vas a reconstruir esta misma app desde una spec, y vas a entender por qué el método le gana al vibe. Antes, el **quiz del Módulo 3**. Ahí te espero. 🚀
