---
titulo: "Ejercicio desafío: Tu segundo skill (conventional-commit)"
capitulo: "05-Módulo 3 Construí con red Git skills y disciplina"
orden: 7
source: "apuntes/slides/00-raw/05-Módulo 3 Construí con red Git skills y disciplina/07-Ejercicio desafío_ Tu segundo skill (conventional-commit) – MUG.html"
source_sha256: b3ac82999f692c7e
extraido: 2026-07-21
---

# Ejercicio desafío: Tu segundo skill (conventional-commit)

Tu primer skill te lo di masticado: el contenido completo, paso por paso. Este no. 😏 Y es a propósito: la mejor forma de comprobar que una habilidad es tuya es usarla **sin la receta adelante**. El desafío es simple de enunciar: **construí tu segundo skill, solo, en un cuarto de hora** —uno chiquito y utilísimo que va a mejorar cada commit que hagas de acá al final del curso—.

## 🎯 El problema a resolver: tus mensajes de commit

Vení, mirá tu `git log --oneline`. Si tus mensajes son tipo *«cambios»*, *«update»*, *«arreglos varios»*, tenés el problema clásico: un historial que no cuenta nada. Existe una convención profesional para esto, **Conventional Commits**, y es muy simple:

```
tipo(scope): descripción en imperativo

feat(auth): agregar validación de email en el registro
fix(tickets): rechazar tickets con asunto vacío
docs(prd): aclarar criterio de control de acceso
```

- **El tipo** dice qué clase de cambio es: `feat` (feature nueva), `fix` (arreglo), `docs` (documentación), `refactor`, `test`, `chore` (mantenimiento).
- **El scope** (opcional) dice qué parte del proyecto toca.
- **La descripción**: en imperativo, minúscula, sin punto final, corta (≤ 72 caracteres).

¿Por qué molestarse? Porque un historial así **se lee como un índice**: entendés qué pasó en cada commit sin abrir un solo diff. Hoy te ordena a vos; en el Módulo 9 (GitHub, PRs y code review) vas a ver que es el idioma en el que trabajan los equipos profesionales.

El problema: acordarte de aplicar el formato **en cada commit**, a mano, no va a pasar. ¿Te suena? Es exactamente el caso de uso de un skill —la regla mental: **si se lo explicaste dos veces, es candidato a skill**—. Vamos a cablearlo.

## 🛠️ El desafío

⏱️ **Tiempo estimado:** ~15 min · 📦 **Entregable:** el skill `conventional-commit` en tu repo, y un commit real donde **se disparó solo**.

Esta vez las consignas son metas, no pasos. Todo lo que necesitás ya lo viste en la lección de Skills y lo practicaste en el ejercicio anterior:

1. **Creá el skill** en `.claude/skills/conventional-commit/SKILL.md`. Vos decidís el contenido, pero tiene que lograr que el agente genere mensajes con el formato de arriba. Dos pistas, y no te doy más:

- La `description` es lo que decide si se dispara. Tercera persona + el **cuándo** («se usa al…»).
- En el cuerpo, decile que **mire qué cambió** antes de elegir tipo y descripción (¿con qué comando se ve lo que está por commitearse? Lo viste en la lección de Git 😉).

1. **Probalo de verdad.** Hacé un cambio chico en tu proyecto y pedile al agente, con naturalidad: *«commiteá esto»*. Sin nombrar el skill, sin pedir el formato.
2. **Verificá en el historial** (`git log --oneline` o VS Code) que el mensaje salió con formato Conventional Commits —y no un genérico—.
3. **¿No se disparó o salió flojo?** Ya sabés dónde mirar: la `description` primero, el cuerpo después. Afilá e intentá de nuevo. Ese ciclo de ajuste también es parte del desafío.

> ✅ **Lo lograste cuando** pediste *«commiteá esto»* sin mencionar formato ni skill, y el mensaje salió bien formado —tipo `feat(gastos): agregar categoría en el alta`— porque tu skill se disparó solo. De acá en adelante, **todos** tus commits del curso salen así, gratis.

### 🔎 La muestra: la solución de TicketTriage (no espíes antes de intentar)

¿Lo intentaste? Bueno. 👀 Así quedó el de TicketTriage —compará con el tuyo, no para copiarlo sino para juzgar el propio—:

```
---
name: conventional-commit
description: Genera mensajes de commit siguiendo Conventional Commits. Se usa al crear un commit o cuando el usuario pide un mensaje de commit.
---

# Conventional Commit

Cuando generes un mensaje de commit:

1. Mirá el `git diff --staged` para entender QUÉ cambió.
2. Elegí el tipo: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`.
3. Formato: `tipo(scope): descripción en imperativo`
   - en minúscula, sin punto final, máx. 72 caracteres.
4. Si rompe compatibilidad, agregá `BREAKING CHANGE:` en el cuerpo.

Ejemplo: feat(auth): agregar validación de email en el registro
```

Diez líneas. Fijate el contraste con `create-prd`: aquel empaquetaba un workflow entero con loop; este cablea una disciplina de una sola cosa. Los dos son skills legítimos —**uno grande y uno chico**— y juntos te muestran el rango completo de la herramienta.

Ahora sí, tu proyecto quedó equipado de punta a punta: contrato afilado (`PRD.md`), reglas (`AGENTS.md`), red (Git) y **dos capacidades empaquetadas**. Antes del gran final —construir la app— faltan dos cosas que un builder profesional jamás saltea, por más rápido que vaya: la **correctitud y la seguridad** del código que genera la IA. ➡️
