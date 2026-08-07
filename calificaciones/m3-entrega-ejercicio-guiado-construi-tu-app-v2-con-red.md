---
tipo: entrega
titulo: "Ejercicio guiado: Construí tu app v2 (con red)"
modulo: 3
nota: 90
resultado: "Aprobado"
enunciado: "apuntes/slides/05-Módulo 3 Construí con red Git skills y disciplina/09-ejercicio-guiado-construi-tu-app-v2-con-red.md"
repo: "https://github.com/leodgonzalez/aI-first-builders-lab-2026-modulo-3"
proyecto: "../src/modulo-3"
consigna: "Pegá el link de tu repo (público) de GitHub donde estuviste trabajando en este módulo 3. Lo que vamos a hacer es revisarlo y dejarte feedback sobre tu PRD y sobre tu app. No te preocupes: no es evaluatoria: es 100% feedback. Gracias!"
source: "calificaciones/00-raw/M3-ENTREGABLE-Ejercicio guiado_ Construí tu app v2 (con red) Assignment – MUG.html"
source_sha256: 2352fd7d22c16ad7
extraido: 2026-08-04
---

# Ejercicio guiado: Construí tu app v2 (con red)

**Nota: 90%** — Aprobado

## Devolución del instructor

Leo! Arranco distinto: en vez de contarte lo que está bien, te cuento por dónde te fui a buscar los agujeros.

(Como siempre digo, esto es una mirada de alto nivel. Levantar y analizar un repo con IA es caro, así que voy a lo estratégico y no línea por línea.)

Primero fui contra tu informe, porque un informe también es un artefacto y también se verifica. Los 136 tests son 136: 94 de backend contra Postgres real y 42 de front, los corrí acá. Las cuatro ramas existen, los cuatro PRs están mergeados, el CI corre. Todo lo que dijiste, es. Eso no es poco y quiero que lo registres.

Después me metí en la base a ver si la unicidad estaba de verdad en el motor, como decís. Y es mejor de lo que contaste: no es un índice único a secas, es un índice único parcial sobre espacio, turno y fecha filtrado por los estados activos. O sea que una reserva rechazada libera el turno sola, sin ningún job de limpieza. Esa es una decisión de diseño que resuelve un problema antes de que exista.

Lo mismo con la decisión única. Tu Decide es un solo UPDATE condicionado a que la reserva siga pendiente, y el comentario que dejaste ahí es la mejor línea del repo: "El chequeo previo del estado es cortesía para el caso común; el que garantiza es este." Sabés cuál es la defensa real y cuál es la comodidad.

Y después me puse a jugar. Pedí un código con un correo que no existe: me contestó exactamente lo mismo que con uno registrado. Bien, la pantalla de ingreso no es un buscador de vecinos. Entré como Ana, reservé la parrilla, y al volver el turno mostraba "Ana Vecina — 3B": la ocupación con nombre y unidad, ni un dato más, tal cual dice tu AGENTS.md. Entré como administración, aprobé y desapareció de pendientes. Anda todo.

Ah, y el cartel del modo demo. Que digas ahí mismo, en pantalla, que mostrar el código deja entrar a cualquiera que sepa un correo registrado, es honestidad de ingeniería. La mayoría pone la muleta y no la nombra. Bien ahí!

Lo que te marco, poco y menor:

- Hiciste cuatro features y la consigna pedía de una a tres. Está bien porque lo decidiste vos con el enunciado a la vista y lo escribiste en ESTADO.md. Pero mirá el patrón, porque en M4 también te pasaste de largo con el spec. Tenés más facilidad para agregar alcance que para recortarlo, y en el proyecto final eso se paga.  
- En el informe nombrás una skill levantar-demo que no existe. Detalle, pero si el artefacto tiene que decir la verdad, el informe también.  
- Marcar a un vecino como aprobador todavía no tiene pantalla.

Muy buen trabajo! A seguir avanzando! Nos vemos.

## Lo entregado

Informe de entrega — App v2 "Reservas de espacios comunes" (Módulo 3): La entrega es la URL del repo — https://github.com/leodgonzalez/aI-first-builders-lab-2026-modulo-3 — donde vive la app v2 reconstruida desde cero a partir del PRD.md final, sin copiar código de la v1, con red desde el primer commit. Cubre el core del PRD en cuatro features incrementales —identificarse por código de un solo uso al correo, crear una reserva con disponibilidad en vivo, y aprobar/rechazar con decisión única y firme, sobre el ABM mínimo de maestros— una más de las 1–3 que pide la consigna, decisión tomada con el enunciado a la vista y documentada en ESTADO.md: se priorizó que la identidad fuera real antes que el conteo. La app corre entera con docker compose up (Postgres → migraciones → seed → api .NET 10 → web React) y está endurecida donde importa: la unicidad de turnos y la decisión única las garantiza la base bajo concurrencia (tests de 50 solicitudes simultáneas), la autorización va por rol con revalidación contra la base, y todo se construyó con plan aprobado antes de codear, TDD con fase roja revisada por el usuario en cada feature, y 136 tests en verde (94 backend contra Postgres real, 42 front). La historia lo cuenta todo: una rama y un PR por feature mergeado a main protegida por CI, un commit por paso con conventional-commit, y en el repo conviven el PRD, los guardrails (AGENTS.md), las skills propias (create-prd, conventional-commit, cerrar-feature, migracion-ef, levantar-demo, entre otras) y la bitácora ESTADO.md con cada decisión, su porqué y la deuda que queda declarada.

*Minimum: 1*275 words
