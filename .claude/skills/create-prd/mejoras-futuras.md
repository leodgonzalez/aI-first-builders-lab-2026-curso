# create-prd — Observaciones para evolución futura

> ⚠️ **Este documento NO se aplica en la versión actual del skill.**
> La regla de oro vigente es `referencia-regla-de-oro.md` (la lección del curso) y las reglas de `SKILL.md`.
> Lo de acá abajo son notas para futuras evoluciones del skill, no criterios a usar hoy.
> El PRD se sigue evaluando y construyendo **solo** contra `referencia-regla-de-oro.md` + `SKILL.md`.

## De dónde salen estas notas

Auditoría del skill y de `referencia-regla-de-oro.md` contra las escuelas que fundan este formato:

- **Ingeniería de Requisitos** — IEEE 830 / ISO/IEC/IEEE 29148 · Karl Wiegers, *Software Requirements* · Robertson (Volere), *Mastering the Requirements Process*.
- **BDD / Specification by Example** — Dan North · Gojko Adzic · Gherkin/Cucumber.
- **Producto / Agile** — Marty Cagan, *Inspired* · Mike Cohn, *User Stories Applied* (INVEST, Bill Wake) · Alan Cooper (personas).

Veredicto: lo que `referencia-regla-de-oro.md` define es **fiel** a la tradición (RF atómico ≈ *singular/shall* de IEEE; RNF con número ≈ *fit criterion* de Volere; AC Dado/Cuando/Entonces ≈ BDD; y en weasel words es incluso más estricto). Lo que sigue son prácticas canónicas que `referencia-regla-de-oro.md` **no** contempla.

## Huecos vs. la tradición (candidatos a futura evolución)

Ordenados por impacto observado al usar el skill en un PRD real.

| # | Práctica ausente | Autoridad | Impacto |
|---|---|---|---|
| 1 | **Priorización de requisitos** (MoSCoW / Must-Should-Could; corte MVP) | IEEE 830 *ranked* · Wiegers · Cagan | Alto — todos los RF quedan al mismo nivel, sin MVP ni orden. |
| 2 | **Sección "Supuestos" (Assumptions)** propia | IEEE 830 · Volere | Alto — sin lugar para supuestos abiertos en el template. |
| 3 | **Rationale / "por qué" por requisito** | Volere (campo *rationale*) | Medio — hay "por qué" global (Objetivos), no por RF. |
| 4 | **Matriz de actores × permisos** (quién puede qué) | Wiegers (*user classes & privileges*) | Alto — con múltiples roles, el control de acceso se resuelve ad hoc dentro de los AC. |
| 5 | **Métricas de éxito del producto** (KPI con baseline y target) | Cagan · PM | Medio — "Objetivos" cualitativo, no verificable como los RF. |
| 6 | **Taxonomía de RNF** (perf, seguridad, usabilidad, disponibilidad, accesibilidad, i18n…) | ISO 25010 · Wiegers | Medio — "RNF con número" sin catálogo → se olvidan dimensiones enteras. |
| 7 | **Chequeo de consistencia/completitud del conjunto** | IEEE *consistent/complete* | Medio — el checklist valida cada ítem, no contradicciones entre ellos. |
| 8 | **Trazado hacia atrás RF→Objetivo** | IEEE (trazabilidad bidireccional) | Medio — se traza RF→AC, no RF→objetivo. |
| 9 | **INVEST completo** (*Independent, Estimable, Valuable*) | Cohn · Wake | Bajo — se cubre *Atomic+Testable*; el acoplamiento oculto complica renumerar. |
| 10 | **Glosario / diccionario de datos** | IEEE 830 · Wiegers | Bajo — útil con dominios de vocabulario propio. |
| 11 | **Versionado / historial de cambios** | RE · gestión de configuración | Bajo — existe el espíritu "documento vivo", sin mecanismo. |

## Si algún día se evoluciona el skill

Los cuatro con mejor relación valor/costo (y que más se sintieron en la práctica):

1. **Priorización** — campo de prioridad por RF, o un corte MVP explícito. *(#1)*
2. **Sección "Supuestos"** en el template. *(#2)*
3. **Matriz de roles × permisos** cuando hay más de un actor. *(#4)*
4. **Paso de "consistencia del conjunto"** en el checklist. *(#7)*

El resto (glosario, versionado, INVEST completo) probablemente sea *scope creep* para un curso introductorio — el propio `referencia-regla-de-oro.md` predica no meter lo que no aporta.
