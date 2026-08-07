---
tipo: quiz
titulo: "Quiz Módulo 4"
modulo: 4
intento: 1
nota: 93.33
resultado: "Aprobado"
correctas: 14
preguntas: 15
erradas: [10]
fecha: "2026-08-03 12:49"
tiempo: "13 minutos, 13 segundos"
tiempo_segundos: 793
enunciado: "apuntes/slides/06-Módulo 4 Spec Driven Development (SDD)/15-quiz-modulo-4.md"
source: "calificaciones/00-raw/Quiz — Quiz Módulo 4 – MUG.html"
source_sha256: da65cec283319a7c
extraido: 2026-08-04
---

# Quiz Módulo 4 — intento 1

**Nota: 93.33%** — Aprobado · 14/15 correctas · 13 minutos, 13 segundos

## Preguntas

### 1. ✓ ¿De dónde sale el spec en `/speckit.specify`?

*1/1 punto*

Respondí:

- De tu PRD2: le pasás el archivo por ruta o URL y el agente lo redacta a partir de él

### 2. ✓ ¿Cuál es la diferencia entre la constitución y el guardrail (`AGENTS.md`)?

*1/1 punto*

Respondí:

- El guardrail es cómo se comporta el agente en general, incluido el stack; la constitución son los principios de diseño que el flujo SDD respeta en cada feature

### 3. ✓ ¿Con qué agentes funciona Spec Kit?

*1/1 punto*

Respondí:

- Es agnóstico: anda con más de 30 agentes (Claude Code, Copilot, OpenCode, Cursor, Gemini, Codex…) y elegís cuál al inicializar

### 4. ✓ ¿Qué es un marcador `[NEEDS CLARIFICATION]` y qué hay que hacer con él?

*1/1 punto*

Respondí:

- Es algo que el agente detectó como ambiguo; hay que resolverlo con `/speckit.clarify` antes de avanzar

### 5. ✓ ¿Qué caracteriza a cada fase del flujo de Spec Kit respecto de tu rol?

*1/1 punto*

Respondí:

- Cada fase es un checkpoint tuyo: el agente propone, vos revisás y aprobás antes de avanzar

### 6. ✓ ¿Qué hace Spec Kit «atrás de escena» al correr `/speckit.specify`?

*1/1 punto*

Respondí:

- Crea una rama de Git para la feature y su propia carpeta numerada dentro de `specs/`

### 7. ✓ ¿En qué orden van las primeras tres fases del flujo de Spec Kit?

*1/1 punto*

Respondí:

- constitution → specify → clarify

### 8. ✓ ¿Cuál es el entregable del ejercicio integrador del módulo?

*1/1 punto*

Respondí:

- Constitución + spec + plan + tareas de tu proyecto, con la primera parte construida, commiteada y validada contra los criterios de aceptación

### 9. ✓ ¿Qué es la constitución del proyecto en Spec Kit?

*1/1 punto*

Respondí:

- Los principios persistentes del proyecto, que valen en toda feature; vive en `.specify/memory/constitution.md`

### 10. ✗ ¿Por qué SDD es especialmente útil sobre código legacy?

*0/1 punto*

Respondí:

- Porque Spec Kit puede generar el spec del sistema existente automáticamente

### 11. ✓ ¿Qué NO debe contener el spec?

*1/1 punto*

Respondí:

- Decisiones técnicas: stack, frameworks y arquitectura, que llegan recién en la fase de plan

### 12. ✓ ¿Cuál es la diferencia entre un guardrail (`AGENTS.md`) y un spec?

*1/1 punto*

Respondí:

- El guardrail dice cómo se comporta el agente siempre en tu proyecto; el spec dice qué construir esta vez, para una feature puntual

### 13. ✓ ¿Cuándo NO conviene usar SDD?

*1/1 punto*

Respondí:

- Cuando estás prototipando o explorando una idea: ahí la velocidad importa más que el contrato y el costo de equivocarse es bajo

### 14. ✓ ¿Qué caracteriza a una buena tarea generada por `/speckit.tasks`?

*1/1 punto*

Respondí:

- Que sea chica y verificable: «creá la función clasificar() en app/ai.py», no «construí la clasificación»

### 15. ✓ Sobre los commits durante `/speckit.implement`, ¿qué es correcto?

*1/1 punto*

Respondí:

- Spec Kit marca las tareas como completadas pero NO hace commits: la práctica del curso es cerrar cada tarea con el skill `conventional-commit` de M3
