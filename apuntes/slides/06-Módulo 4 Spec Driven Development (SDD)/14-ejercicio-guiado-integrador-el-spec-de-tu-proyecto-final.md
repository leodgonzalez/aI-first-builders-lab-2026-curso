---
titulo: "Ejercicio guiado: Integrador — el spec de tu proyecto final"
capitulo: "06-Módulo 4 Spec Driven Development (SDD)"
orden: 14
source: "apuntes/slides/00-raw/06-Módulo 4 Spec Driven Development (SDD)/14-Ejercicio guiado_ Integrador — el spec de tu proyecto final – MUG.html"
source_sha256: c7412a912db0b64d
extraido: 2026-08-03
---

# Ejercicio guiado: Integrador — el spec de tu proyecto final

Llegaste al final de M4, y este es el momento de juntar todo. Recorriste cada fase del flujo de Spec Kit por separado; ahora lo aplicás **de punta a punta a tu proyecto**, en una sola pasada, encadenando lo que hasta acá viste lección por lección. Es tu entrega del módulo y una pieza concreta del proyecto final. 🏗️

## 🎯 Qué vas a lograr

Vas a salir de esta lección con **el spec de tu proyecto y la primera parte construida desde él**, en el repo de M4. No es un ejercicio de juguete: es tu app real, ahora dirigida por spec, lista para que en M5 la lleves a tu propio pipeline. La misma app que vibecodeaste en M2-M3, reconstruida con método — y vas a sentir la diferencia en el cuerpo: menos vueltas, menos sorpresas, más criterio en cada decisión.

## 🛠️ Tu turno: el flujo completo sobre tu proyecto

⏱️ **Tiempo estimado:** ~1-2 h (es el integrador) · 📦 **Entregable:** constitución + spec de tu proyecto + plan + tareas + la primera parte construida, commiteada y validada.

Corré el flujo entero, revisando en cada checkpoint:

1. **Constitución** — `/speckit.constitution` con los principios de tu proyecto (los que ya definiste).
2. **Spec** — `/speckit.specify` alimentado con tu **PRD2** (el que copiaste de M3). Que capture historias y criterios de aceptación.
3. **Clarificar + validar** — `/speckit.clarify` hasta que no queden `[NEEDS CLARIFICATION]`, después `/speckit.checklist`.
4. **Plan** — `/speckit.plan`, pasándole el stack de tu `AGENTS.md`: las decisiones técnicas, revisadas contra el spec y contra la constitución (el «Constitution Check»).
5. **Tareas** — `/speckit.tasks`: chicas y verificables.
6. **Analizar + implementar** — `/speckit.analyze` → `/speckit.implement` la **primera parte** (el core de una feature), commiteando cada tarea con tu skill `conventional-commit`.
7. **Validá** contra los criterios de aceptación.

> ✅ **Lo lograste cuando** tenés el spec de tu proyecto completo y validado, y al menos una feature core construida a través del flujo (con su historial de commits prolijo), con sus criterios de aceptación pasando. Guardá todo en el repo de M4: es la pieza de este módulo para tu proyecto final.

### 🔎 La muestra: TicketTriage, de punta a punta

A lo largo del módulo armamos justamente esto sobre TicketTriage: constitución (IA aislada, test-first, grounded en KB) → spec de la clasificación desde el `PRD2.md` (copiado del repo de M3) → clarify (casos borde resueltos) → plan (FastAPI + SQLite + Claude, el mismo Stack del `AGENTS.md` copiado, Constitution Check sin violaciones) → tareas T1-T5 → implement con un commit por tarea → validación contra los criterios. El resultado: la feature de clasificación andando, **trazable desde el PRD hasta el test, y desde el test hasta el commit**. Esa cadena —PRD2 → spec → plan → tareas → código → commit → criterios— es lo que se llevás de M4.

## 🎯 Cierre del Módulo 4

Reconstruiste tu app con método. Donde en M2 improvisabas y rezabas —y en M3 ya tenías red, pero no contrato—, ahora dirigís desde un contrato que vos acordaste, con cada decisión trazable y cada criterio verificable. Sentiste por qué, cuando algo es serio, el spec no es burocracia: es lo que te deja ir rápido *sin* chocar contra el muro.

En el **Módulo 5 (Agentic Orchestration)** das el salto más grande del curso: vas a dejar de *usar* máquinas de otros y vas a **diseñar tu propio pipeline agéntico** —tu **Dilux Agentic Workflow**—, para construirlo a partir del Módulo 5 (empezando con Claude). Nos vemos ahí. 🚀
