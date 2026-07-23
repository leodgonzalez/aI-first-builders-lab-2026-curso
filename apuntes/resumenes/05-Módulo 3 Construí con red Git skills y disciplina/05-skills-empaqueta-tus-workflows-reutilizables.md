---
titulo: "Skills: empaquetá tus workflows reutilizables"
capitulo: "05-Módulo 3 Construí con red Git skills y disciplina"
orden: 5
leccion: "apuntes/slides/05-Módulo 3 Construí con red Git skills y disciplina/05-skills-empaqueta-tus-workflows-reutilizables.md"
---

# Skills: empaquetá tus workflows reutilizables

## De qué trata

Un **skill** es una carpeta con un `SKILL.md` que el agente carga **solo cuando la tarea
lo amerita**. Es el salto de *prompter* a *builder*: en vez de pedir mejor, **equipás** al
agente con capacidades que antes no tenía.

> La analogía: el chef ya sabe cocinar (el modelo ya sabe programar). El skill es la
> **recetita** que le decís cómo querés vos ese plato, sin pararte al lado cada vez.

## Por qué vale más que un prompt largo

Porque **vive en el proyecto**, y eso arrastra cuatro cosas:

| | |
|---|---|
| **Reutilizable** | Se escribe una vez, se usa siempre |
| **Versionable** | Entra en Git: evoluciona, queda en el historial |
| **Automático** | No hay que acordarse de invocarlo |
| **Compartible** | El equipo arranca con las mismas capacidades |

## Las tres cosas que se confunden

| | Qué es | Cuándo actúa |
|---|---|---|
| **Guardrail** (`CLAUDE.md`) | Contexto siempre-on: cómo comportarse en TODO el proyecto | Siempre, cada turno |
| **Custom command** | Un prompt guardado (`/loquesea`) | Cuando vos lo disparás |
| **Skill** | Una capacidad empaquetada | Cuando la tarea lo amerita (solo) |

Regla mental: el guardrail es *cómo te comportás siempre*, el command es *un atajo que
vos apretás*, el skill es *una habilidad que el agente saca de la galera*.

## Anatomía

```
.claude/skills/<nombre>/SKILL.md      ← del proyecto (se versiona, se comparte)
~/.claude/skills/<nombre>/SKILL.md    ← personal, en todos tus proyectos
```

Dos partes, nada más:

- **Frontmatter** (`name`, `description`) → **configura**: es la ficha que el agente lee
  para decidir si lo usa.
- **Cuerpo** → **instruye**: el workflow paso a paso, una vez que ya decidió activarlo.

Es un archivo de texto sin magia. El valor no está en la sintaxis: está en **lo claro y
específico** que seas describiendo *cómo lo hacés vos*.

## 🎯 La regla que casi nadie cuenta

> **Si tu skill no se dispara, el problema es la `description` — casi nunca el cuerpo.**

El agente escanea las `description` de todos los skills antes de ejecutar nada, como quien
mira los títulos en un estante sin abrir los libros. Si esa línea está vaga, el skill nunca
se enciende.

- Escribila en **tercera persona** y aclarando **cuándo** usarlo.
- ❌ «ayuda con PRDs» → ✅ «Se usa cuando el usuario pide crear, revisar o endurecer un PRD».
- Nombrá los **disparadores concretos**, las situaciones donde aplica.

## Buenas prácticas (con el porqué)

| Práctica | Por qué |
|---|---|
| **Una responsabilidad por skill** | Si hace tres cosas, son tres skills: más fácil de disparar y mantener |
| **`SKILL.md` corto (< ~500 líneas)** | El detalle pesado va en archivos aparte que se cargan a demanda → **progressive disclosure**, ahorra contexto y tokens |
| **Código determinista para trabajo determinista** | No le pidas al LLM que «calcule» lo que un `for` resuelve gratis y sin equivocarse |
| **Ejemplos concretos > reglas abstractas** | Un ejemplo bien elegido enseña más que diez bullets de teoría |

## El cierre

El ejemplo de la lección es `create-prd`: exactamente lo que en el módulo 2 le dictaste al
agente prompt a prompt ([[07-ejercicio-guiado-vibecodea-tu-prd]]), ahora cableado en un
archivo. Pedís *«armame el PRD de una app para los turnos del club»* y el skill se dispara
solo: preguntas, template, checklist.

Acá aprendiste a **escribir** skills. En el **Módulo 5** se van a **orquestar** —
combinados con hooks, subagents y estado persistente para armar un pipeline propio. Pero
todo arranca en esta pieza: la recetita.
