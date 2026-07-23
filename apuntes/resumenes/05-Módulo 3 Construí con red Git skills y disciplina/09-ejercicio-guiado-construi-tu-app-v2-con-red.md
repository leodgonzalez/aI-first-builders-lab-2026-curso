---
titulo: "Ejercicio guiado: Construí tu app v2 (con red)"
capitulo: "05-Módulo 3 Construí con red Git skills y disciplina"
orden: 9
leccion: "apuntes/slides/05-Módulo 3 Construí con red Git skills y disciplina/09-ejercicio-guiado-construi-tu-app-v2-con-red.md"
---

# Ejercicio guiado: Construí tu app v2 (con red)

## De qué trata

El **ejercicio grande del módulo** (~2 a 4 hs): reconstruir la app —la v1 la
hiciste a mano limpia, sin red— **desde el PRD final y con todo el equipamiento**.
No se retoca la v1: se **rehace mejor**, en el repo nuevo, con red desde el primer
commit. La diferencia entre las dos versiones es exactamente todo lo aprendido
desde entonces.

> ⚠️ **El código de la v1 no se copia.** Espiarlo como referencia, sí; mudarlo en
> bloque, no. La v2 se escribe entera acá, commit a commit, desde el PRD. Ver
> [[04-ejercicio-guiado-prepara-tu-proyecto]] (solo viajan `PRD.md` + guardrails).

## Con qué arrancás (vs. la v1)

| Tenés hoy | En la v1 no estaba |
|---|---|
| Repo con espejo en GitHub | «No hay vuelta atrás» |
| `PRD.md` final (skill `create-prd`, curado por vos) | Idea suelta |
| `AGENTS.md` + `CLAUDE.md` (reglas de la casa) | Nada de contexto |
| Skills `create-prd` y `conventional-commit` versionadas | — |
| La experiencia de ya haberla construido una vez | Primera pasada a ciegas |

## La meta

**Las 1 a 3 features core del PRD, funcionando y endurecidas** (la v1 tenía una
sola, cruda), en el repo, con historia commiteada **y pusheada a `main`**.
Requisitos: más completa que la v1, **que corra** (una app que «casi anda» no
cuenta) y con historia en la nube. Entregable: **la URL del repo de GitHub**.

## La receta con Claude Code

| # | Paso | Clave |
|---|---|---|
| 1 | `claude` parado en la carpeta nueva | El agente lee el guardrail solo |
| 2 | **Plan-first**: `Leé @PRD.md. NO escribas código todavía…` | Corregí en palabras antes de que escriba una línea — el checkpoint más barato |
| 3 | **Pasos chicos**, un pedido por feature | «mostrame qué cambiaste y no sigas hasta que lo revise» |
| 4 | Si se enrosca, **revertí** | «volvé al último commit que funcionaba» / `git restore .` — no parchees sobre parches |
| 5 | **Leé el `git diff`** antes de aceptar | Aceptar sin leer es el pecado capital |
| 6 | **Cerrá contra el PRD**: ¿arranca?, ¿corre?, ¿muestra el core? | Último push → la URL es la entrega |

## La regla de oro (el ritmo del resto del curso)

> **Funcionalidad andando → commit + push a `main`.** Se lo pedís con palabras;
> `conventional-commit` formatea el mensaje solo. El `git log` termina contando la
> app **funcionalidad por funcionalidad**. Mismo ritmo que
> [[04-ejercicio-guiado-prepara-tu-proyecto]].

Hábitos vivos mientras construís: `/context` cada tanto y `/clear` al cambiar de
feature; **test-first** en la pieza que si falla, falla el producto.

## La reflexión (no la saltees)

Dos respuestas honestas al terminar:

1. **¿Qué cambió respecto de la v1?** Revertir desastres en segundos, el agente
   respetando reglas, commits que dan tranquilidad para experimentar. Eso es
   trabajar **con red**.
2. **¿Dónde sigue doliendo?** La red no lo cura todo: código que ya te cuesta
   entender, decisiones que la IA tomó por vos, el miedito a tocar algo. Guardá esa
   sensación cruda — la próxima lección le pone nombre (**anti-patterns y el muro
   de los 3 meses**).
