---
tipo: entrega
titulo: "Ejercicio guiado: Integrador — el spec de tu proyecto final"
modulo: 4
nota: 80
resultado: "Aprobado"
enunciado: "apuntes/slides/06-Módulo 4 Spec Driven Development (SDD)/14-ejercicio-guiado-integrador-el-spec-de-tu-proyecto-final.md"
repo: "https://github.com/leodgonzalez/ai-first-builders-lab-2026-modulo-4"
proyecto: "../src/modulo-4"
consigna: "Pasanos la URL de tu repositorio de GitHub (debe ser público) para que podamos darte feedback del trabajo realizado."
source: "calificaciones/00-raw/M4-ENTREGABLE-Ejercicio guiado_ Integrador — el spec de tu proyecto final Assignment – MUG.html"
source_sha256: 4588cee4d3f76617
extraido: 2026-08-04
---

# Ejercicio guiado: Integrador — el spec de tu proyecto final

**Nota: 80%** — Aprobado

## Devolución del instructor

Hola Leonardo! Gracias por compartir el repo. Antes de arrancar, dos aclaraciones:

1. Esta es una revisión de alto nivel. Este tipo de revisiones son costosas: implican analizar tu repo con IA, levantarlo en mi equipo muy rápido, así que el feedback apunta a lo estratégico y no al detalle línea por línea.  
2. Lo segundo: la conclusión con la que cerrás tu mensaje, que un principio que no baja a la plantilla que genera el trabajo no obliga a nada, es lo mejor que salió de esta camada. Y no es solo una frase: fui a leer tu Sync Impact Report de la 2.0.1 y ahí está el análisis completo, incluida la parte que casi nadie hace. Marcaste que la propagación de la 2.0.0 no lo detectó porque auditó solo el alcance de esa enmienda, y sacaste la regla: "una propagación que mira solo lo que cambió nunca encuentra lo que jamás llegó a propagarse". Encontraste un defecto en tu propio proceso de gobernanza y cambiaste el proceso, no el síntoma. Eso ya es Módulo 5! 🙂

Y lo de la skill también lo verifiqué: está el commit de revert y está la regla escrita en AGENTS.md sobre que la superficie de customización es .specify/. El gate quedó en la plantilla y bajó al tasks.md generado. Todo eso se sostiene.

Ahora dos cosas:

- Tenés 7 tests en rojo, y son todos el mismo caso: SysadminSinVisibilidadTests. Esperan 404 y reciben 403. No es un agujero de seguridad, el acceso está bloqueado igual; lo que no se cumple es tu decisión fina de no revelar que el recurso existe, o sea tu Principio V. Los corrí dos veces y se reproducen idénticos. Y ojo con esto: tu Principio I dice que nada entra sin un test en verde.

- Y los números de tu mensaje no cierran con la rama. Dijiste 137 commits y hay 111; 107 tareas implementadas y hay 84 marcadas de 186; 291 tests y hay 245. Te lo digo sin drama porque el repo es excelente, pero fijate el patrón: el reporte va un escalón adelante de lo que el repo muestra, igual que los 7 rojos que no mencionaste. Y justamente la tesis de todo esto es que el artefacto diga la verdad sobre el sistema. Esa distancia es la que hay que cerrar.

Muy buen trabajo! Seguí avanzando! Nos vemos 🙂

## Lo entregado

**URL del repo:** https://github.com/leodgonzalez/ai-first-builders-lab-2026-modulo-4

**rama:** 001-reservas-espacios-comunes

**Descripción:**

Corrí el flujo entero de Spec Kit sobre mi proyecto final —una app para que el vecino de un edificio reserve un turno de un espacio común, con .NET 10 + PostgreSQL y React + Zustand—: constitución de 5 principios, spec desde el PRD con 9 historias y 149 requisitos trazados 1:1, dos rondas de clarify hasta cero [NEEDS CLARIFICATION], checklist, plan con Constitution Check limpio, 186 tareas y 107 implementadas —cuatro historias completas de la pantalla a la base, 137 commits (uno por tarea, con la skill conventional-commit) y 291 tests, con los invariantes garantizados por restricciones de Postgres y no por la app—. Tres cosas se torcieron en el camino y las tres enseñaron algo: el agente editó una skill speckit-* para bajar un principio, cuando esas son definiciones vendorizadas del upstream que la próxima actualización pisa (lo revertí y dejé escrito en AGENTS.md que la superficie de customización es .specify/); me proponía parchear a mano el spec y las tareas, cuando esos artefactos se regeneran y el arreglo va aguas arriba; y aunque pedí que cada feature fuera punta a punta, el /speckit.analyze descubrió que tres historias cerraban en el endpoint y solo 28 de 166 tareas tocaban el frontend, porque la regla estaba en la constitución pero el orden canónico de tasks-template.md terminaba en «Endpoints». Enmendé la constitución a 2.0.1, le agregué el paso → UI y un «Slice Completeness Gate» a la plantilla, regeneré las tareas (166 → 186) y me llevé la lección de fondo: un principio que no baja a la plantilla que genera el trabajo no obliga a nada.

*Minimum: 1*285 words
