---
titulo: "Ejercicio guiado: Analizar e implementar"
capitulo: "06-Módulo 4 Spec Driven Development (SDD)"
orden: 12
source: "apuntes/slides/00-raw/06-Módulo 4 Spec Driven Development (SDD)/12-Ejercicio guiado_ Analizar e implementar – MUG.html"
source_sha256: 3eab0b559fac7102
extraido: 2026-08-03
---

# Ejercicio guiado: Analizar e implementar

Llegó el momento que venías esperando: construir. Pero en SDD no saltamos directo a `implement` —primero un último chequeo de consistencia, y después sí, el agente construye dirigido por todo lo que armaste—. 🚀

## 🔎 `/speckit.analyze`: que todo cierre

Antes de escribir código, `/speckit.analyze` revisa que **spec, plan y tareas sean consistentes entre sí**: que no haya una tarea que contradiga el plan, ni un criterio del spec que ninguna tarea cubra. Es un control barato que evita construir sobre una inconsistencia — la misma lógica del `/speckit.checklist` de la Lección 9, pero mirando los tres documentos juntos en vez de uno solo. Si encuentra algo, lo arreglás antes de seguir.

## 🛠️ `/speckit.implement`: el agente construye

Con todo consistente, `/speckit.implement` pone al agente a **construir siguiendo las tareas, en orden**. No es vibecoding: el agente no improvisa, ejecuta el plan que vos aprobaste, tarea por tarea, respetando las dependencias que marcó `/speckit.tasks` (secuenciales primero, las que pueden ir en paralelo, en paralelo). Antes de tocar código, incluso, verifica que tengas un `.gitignore` acorde a tu stack — un detalle chico, pero que muestra que el flujo asume que estás trabajando dentro de un repo Git real, con higiene.

Vos seguís revisando —cada tarea completada es un checkpoint—, pero la dirección ya está fijada por el spec.

## 📝 Cerrá cada tarea con un commit (esto es una práctica del curso, no algo que Spec Kit haga solo)

Acá va una aclaración importante, para que no te lleves una idea equivocada: `/speckit.implement` marca las tareas como completadas dentro de `tasks.md`, pero **no hace commits de Git por vos** — eso no viene incluido en la herramienta. Y sin embargo, es exactamente el momento perfecto para usar el segundo skill que armaste en M3: **`conventional-commit`**.

La razón es simple: ya tenés tareas chicas y verificables (T1, T2, T3…), cada una es un cambio acotado y con sentido propio — es *justo* el tamaño de commit que un buen historial de Git necesita. Así que la práctica que te propongo, y que vas a usar de acá en más, es: cada vez que el agente termina una tarea y la marca `[X]`, pedile que la commitee usando tu skill `conventional-commit` antes de pasar a la siguiente. Por ejemplo:

```
Terminaste la tarea T3. Commiteala con el skill conventional-commit antes
de seguir con T4.
```

El resultado es un historial de Git donde cada commit corresponde a una tarea del plan, con un mensaje prolijo (`feat: implementar clasificar() en app/ai.py`) — y ahí es donde de verdad se cierra el círculo con M3: el skill que armaste para disciplinarte a vos mismo ahora te sirve para disciplinar al flujo de Spec Kit.

## ✅ Validá contra los criterios de aceptación

Y acá se cierra el círculo del módulo entero: cuando termina, **validás contra los criterios de aceptación del spec**. ¿El ticket de cobro duplicado se clasifica como facturación con prioridad alta? El criterio lo decía; el test lo comprueba. Si algo no cumple, entrás en el **loop de replan**: ajustás lo que haga falta (a veces el spec, a veces el plan) y volvés a implementar. Ese ida y vuelta es lo que mantiene el **código y el spec alineados** — y evita el *drift*, esa deriva silenciosa en la que el código termina haciendo algo distinto de lo que el spec prometía.

## 🛠️ Tu turno: construí tu feature desde el spec

⏱️ **Tiempo estimado:** ~30-40 min · 📦 **Entregable:** la feature construida a través del flujo, commiteada tarea por tarea, y validada contra los criterios de aceptación.

1. Corré **`/speckit.analyze`** y resolvé cualquier inconsistencia que marque.
2. Corré **`/speckit.implement`** y dejá que el agente construya tarea por tarea, revisando cada paso.
3. Después de cada tarea completada, pedile al agente que la **commitee con tu skill `conventional-commit`** antes de seguir.
4. **Validá contra los criterios de aceptación** de tu spec, uno por uno.
5. ¿Algo no cumple? Ajustá (spec o plan) y volvé a implementar — el loop de replan.

> ✅ **Lo lograste cuando** la feature corre, **cada criterio de aceptación de tu spec pasa**, y tu historial de Git tiene un commit prolijo por tarea. Esa es tu entrega de esta lección.

### 🔎 La muestra: TicketTriage implementado

Corrimos `/speckit.analyze` (todo consistente) y después `/speckit.implement`. El agente fue completando las tareas T1→T5, commiteando cada una con `conventional-commit` antes de pasar a la siguiente:

```
feat: crear modelo Ticket (asunto, descripción, estado, categoría, prioridad)
test: agregar test de clasificación (test-first)
feat: implementar clasificar() en app/ai.py
feat: endpoint POST /tickets con clasificación al vuelo
fix: manejar caso ininteligible/vacío en la clasificación
```

Y al final, validamos contra el spec:

```
✓ AC: ticket de cobro duplicado → categoría "facturación", prioridad "alta"   (pasa)
✓ AC: ticket ininteligible → "otro"/"baja" + flag de revisión                 (pasa)
✓ test_clasificacion.py en verde
```

El criterio que escribimos en el spec terminó siendo el test que prueba que el código hace lo prometido. Del PRD al spec, del spec al test, del test al código, del código al commit: **una cadena sin huecos.**

Ya construiste una feature dirigida por spec, de punta a punta. Antes de cerrar, hablemos de **cuándo conviene SDD (y cuándo no)**. ➡️
