---
titulo: "MCP: el Model Context Protocol"
capitulo: "03-Módulo 1 AI-First Development mindset y PRD del proyecto"
orden: 6
source: "apuntes/slides/00-raw/03-Módulo 1 AI-First Development mindset y PRD del proyecto/06-MCP_ el Model Context Protocol – MUG.html"
source_sha256: 4d774437dec4f4fe
extraido: 2026-07-16
---

# MCP: el Model Context Protocol

Hasta acá viste qué es un agente, cómo dirigirlo y cómo ponerle guardrails. Pero hay un techo del que todavía no hablamos: por más capaz que sea el modelo, **solo puede razonar sobre lo que tiene adentro de su contexto**. No ve tu base de datos, no entra a tu repo, no toca tus archivos. Es un cerebro brillante encerrado en una habitación sin puertas. **MCP es la puerta.** Esta lección es conceptual —entender *qué* es y *por qué* importa—; el *cómo* técnico de conectarlos lo vas a ver cuando toque construir. 🔌

## 🧩 Qué es MCP

**MCP** son las siglas de *Model Context Protocol*, y la forma más simple de entenderlo es esta: es un **estándar abierto para conectarle herramientas y datos externos a un agente**. Una base de datos, tu repositorio de GitHub, el sistema de archivos, una API, un servicio cualquiera. Fue propuesto por Anthropic a fines de 2024 y, por ser abierto, lo adoptaron rápidamente el resto de las herramientas del ecosistema —no es algo de una sola marca—.

¿Por qué hizo falta un estándar? Porque antes, cada vez que querías que un agente hablara con un sistema externo, había que programar esa integración a medida, una por una, y atada a cada herramienta. Un lío que no escalaba. MCP resuelve eso igual que lo resolvieron en su momento los **puertos USB**: en vez de un cable distinto para cada dispositivo, **un solo estándar** que todos respetan. Conectás y funciona.

## 🔌 La analogía del USB

Quedátela, porque es la que mejor explica todo. Tu agente es la **computadora**; cada **server MCP** es un dispositivo que enchufás a un puerto. Conectás el server de GitHub y de golpe el agente sabe leer tus issues y tus PRs; conectás el de tu base de datos y puede consultarla; conectás el del sistema de archivos y opera sobre tus documentos con todas las de la ley.

Lo importante de la analogía es que **no reprogramás nada**: no reescribís el agente para que «aprenda» GitHub. Enchufás una capacidad y queda disponible al instante, lista para usar. Y cuando no la necesitás más, la desenchufás. Esa es la gracia del estándar: la misma «computadora» sirve para mil «dispositivos» distintos sin tocarle nada por dentro.

## 🦾 Qué cambia: de razonar a actuar

Acá está el salto de fondo, y vale la pena que lo veas claro. **Sin MCP, un agente solo razona** sobre el texto que le diste: puede pensar, redactar, explicar, sugerir —pero no *hacer* nada en el mundo real—. **Con MCP, le das manos.** Pasa de «te explico cómo cerrarías ese issue» a «cerré el issue». De «este sería el query» a «consulté la base y estos son los datos».

Es la diferencia entre un asesor que te dicta instrucciones y un colaborador que ejecuta. Y es exactamente lo que convierte a un chatbot en un **agente** de verdad: la capacidad de tomar acciones sobre sistemas reales, no solo de producir texto.

## 🏗️ Cómo funciona, a grandes rasgos

No necesitás los detalles técnicos hoy, pero sí el modelo mental, porque lo vas a reusar todo el curso. MCP tiene dos lados:

- **El cliente:** es tu agente (Claude Code, por ejemplo). Es quien *quiere* usar capacidades externas.
- **El server:** es el componente que *expone* una capacidad concreta —el «dispositivo USB»—. Hay servers de filesystem, de GitHub, de bases de datos, de Slack, de navegadores web, y muchísimos más.

Cuando un server se conecta, le **anuncia** al agente qué sabe hacer (qué herramientas ofrece, qué datos puede leer). El agente, a partir de ahí, decide **cuándo** usar cada una para cumplir lo que le pediste. Vos no tenés que decirle paso a paso «ahora llamá a esta función»: le das el objetivo y, si tiene la herramienta enchufada, la usa solo.

> 💡 **Dos sabores de server.** Algunos corren **localmente** en tu máquina (por ejemplo, el que opera sobre tus archivos); otros son **remotos**, viven detrás de una URL (un servicio en la nube). A efectos de hoy es el mismo concepto —una capacidad que enchufás—; la diferencia es dónde vive.

## 🛑 La frontera, marcada con fibrón

Para no marearte, fijemos bien hasta dónde llegamos en este módulo:

1. **Hoy (M1):** entendés *qué es* MCP y *por qué* convierte a un modelo en un agente con manos. Puro concepto.
2. **Más adelante:** vas a **usar** servers que ya existen, hechos por otros —enchufar y aprovechar—.
3. **Módulo 5:** vas a **construir tus propios servers MCP**, para exponer capacidades a medida de tu proyecto.

Es una tentación común querer saltar directo a conectar cosas. Aguantá las ganas: primero que el concepto te quede sólido, que el resto cae solo cuando llegue su momento.

> 🧠 **Para fijar la idea:** pensá en tu propio proyecto. ¿Qué sistema externo necesitaría tocar tu agente para ser realmente útil —tu repo, una base de datos, un servicio de mails, tus documentos—? Esa respuesta es, casi siempre, tu primer candidato a server MCP. Anotala; la vas a usar.

Ya tenés el concepto que le da superpoderes a un agente. Pero los superpoderes se pagan —en cuota y en plata—, y un agente mal manejado puede fundirte el presupuesto en una sola sesión. En la próxima lección vemos cómo manejar el **contexto y los costos** para que eso no te pase. ➡️
