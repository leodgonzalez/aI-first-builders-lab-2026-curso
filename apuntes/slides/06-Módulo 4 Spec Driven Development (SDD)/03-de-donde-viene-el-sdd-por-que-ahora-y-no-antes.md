---
titulo: "De dónde viene el SDD: por qué ahora y no antes"
capitulo: "06-Módulo 4 Spec Driven Development (SDD)"
orden: 3
source: "apuntes/slides/00-raw/06-Módulo 4 Spec Driven Development (SDD)/03-De dónde viene el SDD_ por qué ahora y no antes – MUG.html"
source_sha256: cd8cfe6d42f69dec
extraido: 2026-07-31
---

# De dónde viene el SDD: por qué ahora y no antes

Ya sabés qué es el Spec-Driven Development. Pero antes de conocer la herramienta con la que lo vamos a practicar, quiero que tengas un argumento que te va a servir toda la vida profesional: **de dónde sale esta idea, y por qué no es una moda que se te va a pasar en seis meses.** Porque si alguna vez le contás a un colega con años en esto que «ahora escribimos specs antes de codear», la primera respuesta que te va a dar —y con razón— es: *«¿eso no era lo que ya hacíamos hace veinte años, y no funcionaba?»* 🕰️ Tenés que poder responderle. Vamos.

## 🔄 El péndulo: de los specs eternos al código como única verdad

A principios de los 2000, la forma dominante de construir software era el **Waterfall**: se escribía un documento de requerimientos enorme y detallado *antes* de tocar una línea de código, y recién ahí el equipo se ponía a programar. La idea sonaba prolija en el papel —pensar todo antes de construir—, pero en la práctica fue un desastre conocido: el spec era un documento **para humanos**, nadie lo actualizaba a la par del código real, y a los pocos meses el spec describía un sistema que ya no existía. Se le llamó **Big Design Up Front (BDUF)**, y terminó siendo sinónimo de burocracia que no protegía nada.

La reacción llegó en 2001 con el **Manifiesto Ágil**, y su frase más citada lo dice todo: *«software funcionando, por encima de documentación exhaustiva»*. Tenía sentido —el spec de Waterfall era un lastre, no una ayuda—, pero como pasa con los péndulos, se fue al otro extremo: el código pasó a ser la **única fuente de verdad**. Documentar de más quedó mal visto. Dos décadas de «el código es la documentación» después, llegamos a otro problema: nadie tenía un contrato claro de qué se suponía que el sistema hacía, más allá de leer el código mismo.

## ⚡ 2023-2024: el vibecoding empuja el péndulo todavía más lejos

Con la explosión de los modelos de lenguaje generando código a velocidad brutal, el péndulo se fue todavía más al extremo del «solo código»: ¿para qué escribir nada si le podés pedir a la IA que programe directamente? Ese es, ni más ni menos, el **vibecoding** que viviste en M2 y M3: velocidad altísima, cero contrato. Y ya sentiste en el cuerpo adónde lleva ese extremo —el **muro de los 3 meses**: código que ya no entendés del todo, decisiones que tomó la IA sin que te dieras cuenta, ese miedo a tocar algo por las dudas.

## 🌱 2024-2025: el spec vuelve, pero no es el mismo de antes

Acá es donde la historia deja de ser un péndulo que va y viene, y empieza a ser algo nuevo. Desde 2024 y con fuerza en 2025, voces serias de la industria empezaron a decir que había que volver a escribir specs —**Sean Grove**, de OpenAI, lo resumió con una frase que ya viste: *«specs are the new code»*—. GitHub lanzó **Spec Kit** (la herramienta que vas a usar desde la próxima lección), Amazon lanzó su propia alternativa (**Kiro**), y consultoras como Thoughtworks empezaron a listar el SDD entre las prácticas serias del desarrollo asistido por IA.

Y acá está la pregunta que te tenías que hacer, la del colega escéptico: **¿esto no es volver al Waterfall que ya fracasó?** La respuesta es no, y el motivo es preciso: el problema de los specs de Waterfall nunca fue la idea de escribirlos antes —fue que **se desincronizaban del código**, porque mantenerlos al día dependía de que un humano se acordara de actualizar dos documentos a la vez. Hoy el spec no es un documento que «también» hay que mantener: es lo que un **agente lee directamente para generar (y regenerar) el código**. La sincronización deja de ser un acto de disciplina humana y pasa a ser una consecuencia automática de cómo se construye. Eso es lo que la IA cambió, y es la única razón por la que esta vuelta al spec no es nostalgia de los 2000: es una síntesis nueva, que solo es posible ahora.

## 💡 Para aplicar

Imaginate a ese colega senior escéptico preguntándote *«¿esto no es Waterfall de nuevo?»* — escribí, en dos o tres líneas, cómo se lo explicarías. Si mencionaste que el spec ahora es **ejecutable** y que un agente lo mantiene sincronizado con el código (en vez de un humano que se olvida), tenés el argumento. Guardátelo: te va a servir la primera vez que alguien te haga esa pregunta en un trabajo real —y te la van a hacer.

Con la historia clara y el argumento en el bolsillo, ahora sí: conozcamos **Spec Kit**, la herramienta que convierte todo esto en un flujo concreto de comandos. ➡️
