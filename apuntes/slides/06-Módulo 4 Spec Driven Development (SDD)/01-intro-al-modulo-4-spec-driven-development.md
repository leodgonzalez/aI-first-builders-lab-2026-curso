---
titulo: "Intro al módulo 4: Spec Driven Development"
capitulo: "06-Módulo 4 Spec Driven Development (SDD)"
orden: 1
source: "apuntes/slides/00-raw/06-Módulo 4 Spec Driven Development (SDD)/01-Intro al módulo 4_ Spec Driven Development – MUG.html"
source_sha256: 62a60acd5c64c98d
extraido: 2026-07-30
---

# Intro al módulo 4: Spec Driven Development

Bienvenido al Módulo 4, Builder. Cerremos primero el módulo anterior, porque este arranca justo donde aquel terminó. En M2 y M3 construiste tu app **vibecodeando** —dos veces: primero sin red, después con Git y skills—, y fue rápido y lindo… hasta que, aun con la red puesta, empezaste a sentir el famoso **«muro de los 3 meses»**: código que ya cuesta entender, decisiones que la IA tomó por vos, ese miedito a tocar algo porque no sabés qué se rompe. 🧱 Te dije que esa incomodidad no era un fracaso, sino la puerta de entrada a este módulo. Bueno, acá estamos.

Vale la pena que te detengas un segundo a pensar en la raíz del problema, porque de ahí sale todo lo que viene. El vibecoding, tal como lo practicaste, tiene una falla estructural: **el contrato de lo que hay que construir vive en tu cabeza**, no en ningún documento que el agente pueda consultar de nuevo. Cada sesión nueva, cada feature nueva, le explicás de vuelta (o peor, no se lo explicás y él improvisa) qué tiene que pasar en los casos borde, qué formato usar, qué prioridad va por defecto. Con una app chiquita eso se banca. Con una app que ya tiene meses, se vuelve insostenible: nadie —ni vos, ni el agente— tiene un lugar único donde mirar «qué se supone que hace este sistema, exactamente».

## 🧭 La idea que ordena todo lo que viene

Hay una sola idea detrás de todo el módulo, y quiero que te la lleves grabada: **el spec es la fuente de verdad.** En vez de improvisar hacia el resultado y rezar para que el código quede bien, vas a escribir primero un **spec ejecutable** —un contrato claro de qué construir— y vas a **dirigir al agente desde ese spec**. El código deja de ser la verdad del proyecto; pasa a ser una *consecuencia* del spec. Si mañana alguien te pregunta «¿esto tiene que pasar así?», la respuesta no está en tu memoria ni en un chat viejo: está escrita, en un archivo, versionada junto con el código.

## 🗺️ Qué vamos a hacer en este módulo

Vamos a tomar **la misma app que ya conocés** —tu proyecto, el del PRD— y la vamos a **reconstruir, ahora con método SDD**, en un repo nuevo. Sí, de nuevo desde cero: es a propósito, para que sientas en el cuerpo la diferencia entre improvisar y dirigir desde un contrato. No vas a perder lo que ya construiste en M2-M3 —tu PRD evolucionado, tu guardrail, tus skills viajan con vos, copiados tal cual—; lo único que se reconstruye es el código, porque el código es justo la variable que este módulo quiere que compares.

La herramienta que nos va a acompañar es **GitHub Spec Kit**, que convierte todo el flujo SDD en una secuencia de comandos que corren dentro de tu agente. Antes de tocarla vamos a hacer una parada breve por la historia: de dónde viene esta idea de «escribir specs antes de codear» y por qué no es simplemente volver a un pasado que ya sabemos que no funcionó. Con eso claro, el recorrido del módulo sigue el flujo real de la herramienta, una fase por lección: constitución → spec → clarificación → plan → tareas → implementación, aplicándolo a tu proyecto de punta a punta.

Las lecciones de acá en más son **cortas y enfocadas: una cosa cada una.** No te apures; el valor de SDD está en hacer cada paso con intención, no en correr al final. Un builder que se salta la clarificación «para llegar más rápido» termina exactamente en el mismo lugar del vibecoding sin método: código que hace algo distinto de lo que él creía haber pedido.

Arranquemos por el principio: **qué es, exactamente, el Spec-Driven Development** —y por qué cada vez más gente seria dice que es hacia donde va el oficio—. ➡️
