---
titulo: "El proyecto final como Builder"
capitulo: "01-Introducción al curso"
orden: 3
source: "apuntes/slides/00-raw/01-Introducción al curso/03-El proyecto final como Builder – MUG.html"
source_sha256: 8ed76cd1ddb8c1e7
extraido: 2026-07-16
---

# El proyecto final como Builder

Te lo adelanté en la lección anterior y ahora lo abrimos entero, porque es **el corazón del curso**: el proyecto final. Todo lo que vas a aprender converge acá. Y te lo cuento el día uno a propósito — si sabés a dónde vas, cada clase tiene sentido. 🎯

## 🧱 Qué vas a construir

Tu propio **app AI-First**: una aplicación real, construida dirigiendo agentes de IA, que vas a **presentar en el Demo Day**. Tema libre, stack libre — la idea es tuya.

Pero acá está lo distinto: **no la vas a construir una sola vez.** La vas a construir **varias, cada vez con más método**, y *esa* es la enseñanza.

## 🧬 El PRD: la columna vertebral que viaja

En el **Módulo 1** vas a escribir el **PRD** (*Product Requirements Document*, o sea «documento de requisitos del producto») de tu app: un documento corto que define **qué** construís y **por qué** (el problema, los usuarios, las features núcleo). En criollo: es el papel donde dejás claro qué app querés antes de empezar a construirla.

Ese PRD es **lo único que viaja** por todo el curso. Cada módulo lo toma como punto de partida y construye la misma app **con un método distinto, en su propio repositorio**:

- **Módulo 2:** la construís **vibecodeando** (rápido, sin red) → sentís la velocidad… y dónde duele.
- **Módulo 3:** le ponés **red y superpoderes** —Git, skills, disciplina— y la llevás a su **v2**, esta vez sin miedo.
- **Módulo 4:** la construís con **Spec-Driven Development** usando Spec Kit → del PRD sale un spec, y el agente construye con disciplina.
- **Módulo 5 (Agentic Orchestration):** **diseñás** tu propio pipeline agéntico —tu **Dilux Agentic Flow**—, el método, sin atarte a una herramienta.
- **Módulo 6:** lo **construís con Claude** → automatizás el método y llegás al punto de madurez.
- **Módulos 7 y 8:** portás ese pipeline a otras herramientas (OpenCode, Copilot — opcional).

Misma app, métodos distintos. Cuando la construís por tercera vez y ves la diferencia de calidad, **entendés en el cuerpo** por qué el método importa. 💡

Y para que no estés solo frente a la hoja en blanco, en cada práctica vas a ver el mismo paso hecho sobre una **app de ejemplo que construimos nosotros: TicketTriage** 🎫 (una mesa de ayuda donde la IA clasifica tickets y redacta borradores de respuesta). No es tu proyecto —el tuyo lo elegís vos—, pero te sirve de **molde y de red**: cuando te trabes, mirás cómo quedó en TicketTriage y seguís.

## 🏁 De varias versiones a una que se publica

Podés repetir el ciclo **las veces que quieras**. Para producción, **elegís una versión** (te vamos a recomendar la del pipeline, por madurez) y la **endurecés**: tests automáticos de IA (evals), integración continua, deploy. Esa es la que llega al Demo Day.

## 📏 Con qué te evaluamos (la rúbrica, desde hoy)

Para que sepas exactamente hacia dónde remás, esta es la rúbrica del Demo Day:

1. **Spec-Driven:** partió de un spec, no de improvisación.
2. **Evals:** tiene evaluaciones automáticas del output de IA.
3. **Code review:** pasó por revisión (humana + IA).
4. **Métricas del proceso:** observabilidad del loop agéntico (costo, iteraciones, calidad).
5. **Documentación:** un README claro.
6. **Deploy:** corre desplegada.
7. **Presentación:** una demo que se entienda.

## 📐 Las reglas de tu app (para que sea demostrable)

Como la vas a construir varias veces, conviene que sea **chica y demostrable**:

- **Una idea, no un producto** (un «core loop» que muestres en ~2 minutos).
- **1 a 3 features núcleo**, no veinte.
- **Que corra y se vea** (una UI o una API).
- **Apta para IA** (un CRUD, una API, una app web típica).
- **Poca fricción externa** (evitá depender de mil integraciones o claves).
- **Que te importe** — la vas a construir varias veces, elegí algo que te entusiasme. 🙂

Ya sabés qué vas a construir y cómo se evalúa. En la próxima lección te cuento **cómo se cursa el día a día**; y en la siguiente, cómo nos hacemos **comunidad** y dónde pedir soporte — porque a esto no lo hacés solo.
