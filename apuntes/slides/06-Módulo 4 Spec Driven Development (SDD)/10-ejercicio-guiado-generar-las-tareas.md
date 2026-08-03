---
titulo: "Ejercicio guiado: Generar las tareas"
capitulo: "06-Módulo 4 Spec Driven Development (SDD)"
orden: 10
source: "apuntes/slides/00-raw/06-Módulo 4 Spec Driven Development (SDD)/10-Ejercicio guiado_ Generar las tareas – MUG.html"
source_sha256: 611250f12cfd7818
extraido: 2026-08-03
---

# Ejercicio guiado: Generar las tareas

Tenés el plan técnico aprobado. Pero un plan todavía es una vista de pájaro: para construir sin perderte, necesitás bajarlo a **pasos chicos y accionables**. Eso hace `/speckit.tasks`. ✅

## 🧩 De la vista de pájaro al paso a paso

`/speckit.tasks` toma tu plan y lo descompone en una **lista de tareas concretas y verificables**: cada una es un pedazo de trabajo que el agente puede hacer y que vos podés chequear. La clave es que sean **chicas** —una tarea no es «construí la clasificación», es «creá la función `clasificar()` en `app/ai.py`«—. Tareas grandes esconden problemas; tareas chicas se revisan de un vistazo, y si algo sale mal, sabés exactamente en cuál. El comando también respeta el orden que importa: agrupa las tareas en fases (setup, tests, núcleo, integración, pulido) y marca cuáles pueden hacerse en paralelo y cuáles dependen de otras.

Esto, en el fondo, es el **plan-first que viste en M2, pero formalizado**. Allá le pedías al agente que propusiera un plan antes de tocar código, en una conversación suelta; acá el flujo te lo da estructurado, trazable hasta el spec, y como un checklist que se va completando y que queda escrito en `tasks.md`, no en el scroll de un chat que se pierde. La misma disciplina, ahora como parte del método — y con un beneficio extra: en la próxima lección, cada tarea que se completa la vas a poder cerrar con un commit prolijo, usando el skill `conventional-commit` que armaste en M3 y que ya copiaste a este repo.

## 🛠️ Tu turno: descomponé tu plan en tareas

⏱️ **Tiempo estimado:** ~15 min · 📦 **Entregable:** la lista de tareas de tu feature, chicas y verificables.

1. Con el plan aprobado, corré **`/speckit.tasks`**.
2. Revisá la lista: ¿cada tarea es lo bastante chica como para revisarla sola?, ¿se entiende qué la da por terminada?
3. Si ves una tarea gigante, pedile al agente que la parta en dos.

> ✅ **Lo lograste cuando** tenés una lista donde cada tarea es un paso concreto y verificable, no un «construí media app».

### 🔎 La muestra: las tareas de TicketTriage

Del plan de clasificación salió una lista así:

```
- [ ] T1: crear el modelo Ticket (asunto, descripción, estado, categoría, prioridad) en models.py
- [ ] T2: escribir el test de clasificación (test-first) en tests/test_clasificacion.py
- [ ] T3: implementar clasificar(texto) en app/ai.py que pase el test
- [ ] T4: endpoint POST /tickets que cree el ticket y lo clasifique al vuelo
- [ ] T5: manejar el caso ininteligible/vacío → "otro"/"baja" + flag de revisión
```

Cada tarea toca poco, dice qué archivo, y se sabe cuándo está hecha. Fijate que T2 (el test) va **antes** que T3 (la implementación) — la constitución test-first, hecha tarea. (El modelo `Ticket` arranca con lo de la clasificación; el dueño/socio se le suma cuando construyas la feature de auth — RF-01.)

Con las tareas listas, llegó el momento que esperabas: **analizar e implementar**. ➡️
