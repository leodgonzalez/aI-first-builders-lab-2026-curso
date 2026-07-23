---
titulo: "Resumen y conclusiones del Módulo 1"
capitulo: "03-Módulo 1 AI-First Development mindset y PRD del proyecto"
orden: 10
source: "apuntes/slides/00-raw/03-Módulo 1 AI-First Development mindset y PRD del proyecto/10-Resumen y conclusiones del Módulo 1 – MUG.html"
source_sha256: 4cdd81194ddad395
extraido: 2026-07-16
---

# Resumen y conclusiones del Módulo 1

Arrancaste sin escribir una línea de código y te llevás un montón. Antes del quiz, repasemos las ideas que importan —cortas y directas, para que te queden fijas—. Si algo de esto no te suena, volvé a la lección antes de seguir. 🧠

## 🧠 El mindset AI-First

- Pasaste de **escribir cada línea** a **dirigir y juzgar**. Tu valor ya no es teclear: es decidir *qué* construir y evaluar si lo que produce la IA está bien.
- **Desconfiá por defecto.** La IA acelera, pero también mete errores y vulnerabilidades. Revisar **no es opcional**.
- AI-First no es solo para programar: es para **pensar mejor y más rápido** —empezando por la definición del producto—.

## 🧰 El stack del AI Builder

- Tres familias de agentes que vas a usar: **Claude Code** (terminal, el tool principal del curso), **GitHub Copilot** (dentro de VS Code) y **OpenCode** (terminal, agnóstico de modelo).
- Cada uno se dirige con su **archivo de contexto**: `CLAUDE.md`, `copilot-instructions.md`, `AGENTS.md`.
- No existe «el mejor»: existe **el que mejor te sirve** para cada tarea.

## 🛡️ Guardrails: cómo se dirige y se contiene un agente

- **Archivos de contexto** = la memoria y las reglas del agente. Documentá **solo lo que no puede inferir** y mantenelo corto.
- **Permisos** (allow / ask / deny) = qué puede hacer sin pedirte permiso. Un agente **sin guardrails es un riesgo**, no una ayuda.

## 🔌 MCP (Model Context Protocol)

- Es el **estándar para enchufarle herramientas y datos externos** a un agente (la analogía del USB).
- Lo que cambia: de **solo razonar** a **actuar** sobre sistemas reales. Eso es lo que convierte a un modelo en un **agente**.
- Frontera de M1: hoy es **concepto**; *construir* tus propios servers MCP es **Módulo 5**.

## 💸 Gestión de contexto y costos

- La **ventana de contexto** es finita y se re-procesa entera en cada turno: más contexto = **más costo y más confusión**.
- **Contexto viejo es peor que poco contexto** (context rot). Limpiá al cambiar de tarea.
- Tu kit: `/context` (tablero), `/compact` (comprimir), `/clear` (empezar fresco), `/usage` (cuota). Sesiones enfocadas, limpiá seguido.

## 📋 El PRD

- Un buen PRD es **verificable**: RF atómicos con «debe», RNF **con número**, AC binarios en Dado/Cuando/Entonces, fuera de alcance explícito, IDs para trazar.
- **No hay receta mágica**: usamos esta estructura para ordenar la historia y **matar la ambigüedad**.
- Un PRD cuenta una **historia humana** (personas reales, no «el usuario») y es un **documento vivo**: lo vas a seguir mejorando.
- En M1 lo hiciste **a mano** para entrenar el ojo; la IA lo potencia después (mejorarlo en M2, empaquetarlo en un skill en M3, orquestarlo en M5).
- Es **la columna vertebral del curso**: lo único que viaja por todos los módulos.

## 🎯 La gran conclusión

Sin una sola línea de código, ya tenés lo que hace posible todo lo que viene: **el chip cambiado** (dirigir y juzgar), **el mapa del stack**, un agente **con guardrails y bajo control de costos**, y tu proyecto **definido en un PRD verificable**. Esa base es sólida y es tuya.

En el **Módulo 2** tomás ese PRD y **construís tu app por primera vez, vibecodeando**. Pero antes, un último paso para fijar lo aprendido: el **quiz del Módulo 1**. Ahí te espero. 💪
