---
titulo: "Ejercicio guiado: Tu primer skill (create-prd)"
capitulo: "05-Módulo 3 Construí con red Git skills y disciplina"
orden: 6
leccion: "apuntes/slides/05-Módulo 3 Construí con red Git skills y disciplina/06-ejercicio-guiado-tu-primer-skill-create-prd.md"
---

# Ejercicio guiado: Tu primer skill (create-prd)

## De qué trata

Empaquetar en un skill (`create-prd`) un workflow que **ya hiciste a mano** —el del
PRD—, y usarlo para regenerar tu propio PRD. Como conocés el resultado esperado,
podés juzgar si el skill lo hace bien. Skills + Git trabajando juntos por primera vez.
~35 min.

## Las tres decisiones de método

| Decisión | Por qué |
|---|---|
| El skill escribe en **`PRD2.md`**, no pisa el original | Para **comparar**: qué garantiza el empaquetado vs. qué sigue dependiendo de tu juicio |
| Se dispara **sin nombrarlo** | Es *la* prueba del skill: el agente matchea tu pedido contra la `description`. Si no se dispara, el bug está en la description |
| Los commits también se **vibecodean** | En todo el ejercicio no tipeás un solo comando git: dirigís, el agente ejecuta |

## Qué lleva adentro el SKILL.md

No es un skill de juguete: es **todo tu método de PRD del curso**, escrito una vez.

- **Template de M1** — las 7 secciones obligatorias (Contexto, Objetivos, RF, RNF, AC,
  Fuera de Alcance, Riesgos).
- **Checklist de calidad** — RF atómicos con "debe", RNF con número, cada RF con su AC,
  AC binarios en Dado/Cuando/Entonces, fuera-de-alcance explícito, AC de control de acceso.
- **El loop en 4 pasos**: normalizar → auditar (sin tocar) → **esperar tu juicio** →
  reescribir solo lo aprobado → volver a auditar. Listo solo cuando la auditoría sale limpia.
- **Reglas duras**: lo no pedido va a Fuera de Alcance; nada de "correctamente" ni
  "adecuado"; ante la duda, preguntá — nunca inventes.

El punto clave: **el loop vive en el archivo**, no en tu cabeza ni en el prompt del día.
Ver [[05-skills-empaqueta-tus-workflows-reutilizables]].

## La receta

1. Crear `.claude/skills/create-prd/SKILL.md`.
2. Commitear el skill (`chore: agregar skill create-prd`) → ya vive versionado en el repo.
3. `/clear` y pedir la regeneración **sin nombrar el skill**, aclarando "NO modifiques
   el PRD.md original".
4. Juzgar el loop: aprobar lo real, rechazar el humo.
5. Comparar `PRD.md` vs `PRD2.md` sección por sección y **portar a mano lo mejor del viejo**.
6. Última vuelta: «auditá @PRD2.md» hasta que salga limpia.
7. Recambio en dos commits: guardar `PRD2.md`, después borrar el viejo y renombrar.

## Lo que se aprende comparando

El `PRD2` sale **estructuralmente perfecto** (el skill no se olvida de ningún punto del
checklist), pero la versión a mano tiene **decisiones ganadas a pulso** —el AC afilado
tras rechazar humo, el fuera-de-alcance que frenó el scope creep— y el skill puede haber
reescrito alguna peor.

> **El skill garantiza el piso; tu juicio pone el techo.**

## Por qué se puede borrar el PRD viejo sin miedo

**Porque Git lo recuerda.** Vive en el historial, recuperable cuando quieras. Eso es
trabajar con red: **borrar deja de ser irreversible**
([[03-iterar-con-red-la-disciplina-del-builder]]).

El `git log --oneline` final cuenta la historia del módulo entero, de abajo hacia arriba:
estado inicial → endurecer PRD a mano → agregar skill → generar PRD2 → recambio.

## El cierre

El mismo documento recorrió tres peldaños: escrito **a mano** (M1), endurecido
**dirigiendo a la IA** (M2), regenerado **con un skill tuyo** de un solo pedido. En el
**Módulo 5** estos skills se orquestan en un pipeline con gates que corre solo. El primer
skill cuesta una lección entera; el segundo, una fracción — por eso el próximo no viene
masticado.
