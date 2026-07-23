---
titulo: "Product Requirements Document (PRD): qué es y cómo se arma"
capitulo: "03-Módulo 1 AI-First Development mindset y PRD del proyecto"
orden: 8
source: "apuntes/slides/00-raw/03-Módulo 1 AI-First Development mindset y PRD del proyecto/08-Product Requirements Document (PRD)_ qué es y cómo se arma – MUG.html"
source_sha256: 4e356eb8075d809f
extraido: 2026-07-16
---

# Product Requirements Document (PRD): qué es y cómo se arma

Antes de escribir el PRD de tu proyecto, parémonos un segundo en **qué es** uno y, sobre todo, en **cómo se arma uno bueno**. Esta lección es la teoría y el oficio; la próxima son tus manos sobre tu idea. Acá lo vamos a hacer **a mano, sin IA** —y a propósito—: si no sabés cómo se ve un PRD sólido, no vas a poder dirigir ni juzgar a un agente que lo escriba por vos. Primero el ojo, después la automatización. 📋

## 🧐 Qué es un PRD (y por qué uno *bueno* es verificable)

**PRD** son las siglas de *Product Requirements Document*, y responde dos preguntas a nivel producto: **qué** vas a construir y **por qué**. Hasta ahí, la definición de manual. Pero acá viene lo que separa un PRD profesional de un punteo de buenas intenciones: **un buen PRD es verificable**. No alcanza con «quiero una app de tickets que ande bien»; eso no lo podés construir ni comprobar. Un PRD serio se puede *validar*, igual que validás código.

¿Por qué obsesionarnos con esto desde el primer documento? Porque es **el contrato que le vas a dar a la IA**. Un agente construye exactamente lo que le pedís; si tu pedido es ambiguo, la ambigüedad la resuelve él —y casi nunca como vos querías—. Un requerimiento vago es una invitación a que invente. Un requerimiento verificable no deja lugar: o se cumple o no se cumple.

## 🧱 Las piezas de un PRD

Una aclaración antes de la lista, porque importa: **no hay una receta mágica ni un formato único de PRD**. Cada equipo, cada empresa y cada herramienta tienen su propia variante, y todas pueden estar bien. Lo que sigue no es *la* verdad revelada: es **la estructura que vamos a usar en este curso**, elegida porque te ayuda a ordenar la historia y te obliga a no dejar ambigüedades. Tomala como un molde que te guía el pensamiento, no como un dogma. Con esa cabeza, estas son las piezas:

- **Contexto y problema:** qué dolor real resolvés y para quién. Si no hay dolor, no hay app. Sumá las **personas** (quién lo usa y qué necesita).
- **Objetivos:** qué significa ganar, en términos de producto.
- **Requerimientos funcionales (RF):** lo que el sistema **debe** hacer, **atómico** (una acción por requerimiento) y con verbo imperativo. *«El sistema debe permitir crear un ticket con asunto y descripción.»* Nada de «debería».
- **Requerimientos no funcionales (RNF):** las cualidades, pero **con número**. No «rápido» → *«la clasificación debe responder en < 3 s p95"*. Sin métrica, no es un requisito, es un deseo.
- **Criterios de aceptación (AC):** la prueba de fuego, en formato **Dado / Cuando / Entonces**. *«Dado un ticket sobre reseteo de clave, cuando se genera el borrador, entonces incluye el link de la base de conocimiento y no inventa otro.»* Cada AC se evalúa como pasa o no pasa, sin opinión.
- **Fuera de alcance:** lo que explícitamente NO entra. Clave, porque *todo lo que no excluís, se asume incluido* — y ahí nace el scope creep.
- **Riesgos** y **dependencias:** qué puede salir mal y de qué depende.

> 🧭 **La regla mental para saber si tu PRD está bien:** ¿cada RF tiene un AC que lo verifique? ¿Cada RNF tiene un número? ¿Tus criterios son binarios (pasa/no pasa) o están llenos de «correctamente» y «adecuado»? ¿Pusiste IDs (RF-01, AC-01) para poder trazar? Si todo eso da que sí, tenés un PRD que se puede construir y comprobar. Esto no es burocracia: es lo que hace que la IA construya **exactamente** lo que querés.

## 🆚 PRD vs spec: dónde termina uno y empieza el otro

Vas a escuchar las dos palabras todo el curso, y conviene separarlas bien —pero con cuidado, porque la diferencia no es la que mucha gente cree—. El **PRD** (esto, M1) es el *qué* y el *por qué*, **con sus criterios de aceptación**: es el **contrato de producto**, verificable. El **spec** (que llega en M4) es el *cómo* técnico: toma cada requerimiento del PRD y lo **mapea a un diseño y a tests** (trazabilidad: cada RF → un bloque de diseño, cada AC → un test).

O sea: el spec **no inventa** criterios nuevos —los **cubre**—. El PRD dice «esto tiene que pasar y así se comprueba»; el spec dice «así lo construyo y este test demuestra que el AC se cumple». Primero el contrato de producto (PRD), después el diseño que lo honra (spec). En este módulo nos quedamos en el PRD, y está perfecto así.

## 🖊️ Cómo se arma, a mano, desde una idea

Acá está el oficio. Un PRD no nace redondo: arranca de una idea cruda y se va **endureciendo pieza por pieza**. El error típico es querer escribirlo perfecto de una; el camino real es empezar flojo y apretar las tuercas. Te muestro el flujo, en cuatro pasos, **sin IA** —papel, editor de texto, lo que tengas—:

**1. Tirá el pitch crudo.** Una o dos frases en lenguaje natural, como se lo contarías a un amigo. Sin estructura todavía:

> *«Quiero un software que reciba consultas de soporte, las clasifique solo por tema y urgencia, y me redacte un borrador de respuesta usando las FAQ del equipo, para no escribir todo de cero.»*

**2. Bajalo al template.** Copiá el esqueleto de abajo y empezá a llenar las casillas. No te frenes en redactar lindo: poné lo que tengas en cada sección, aunque sea en borrador.

**3. Apretá cada pieza con las preguntas de calidad.** Recorré requerimiento por requerimiento: ¿este RF es atómico (una sola acción)?, ¿dice «debe»?, ¿este RNF tiene un número o es un deseo?, ¿este AC es binario (pasa/no pasa) o tiene un «correctamente» escondido? Cada cosa floja, corregila. Acá es donde un punteo de buenas intenciones se convierte en un contrato.

**4. Cerrá el alcance.** Escribí explícitamente qué **no** entra. Es contraintuitivo pero es lo que más te protege: todo lo que no excluís, el agente lo asume incluido.

### 📄 El template (copialo y completalo)

> 📝 **¿Y esos `#` y** ? **Son** Markdown**: el `#` marca la jerarquía de títulos y los**  ponen negrita. Si no es lo tuyo, no te enganches —podés escribir tu PRD en **Google Docs o Word**, lo que importa es el contenido—. Si querés repasarlo, lo vemos paso a paso en [Markdown y editar archivos](https://mug.org.ar/leccion/aifbl26-markdown-y-editar-archivos/).

```
# PRD-001: <nombre del proyecto> — <una línea de qué es>

## Contexto y Problema
<Qué dolor resolvés y para quién. Personas: quién lo usa y qué necesita.>

## Objetivos
<Qué significa ganar, a nivel producto.>

## Requerimientos Funcionales
- RF-01: El sistema debe <una acción, verbo imperativo>.
- RF-02: ...

## Requerimientos No Funcionales
- RNF-01: <cualidad con número: "< 3 s p95", "≥ 85%">.

## Criterios de Aceptación
- AC-01 (RF-01): Dado <contexto>, cuando <acción>, entonces <resultado medible>.

## Fuera de Alcance
- <Lo que explícitamente NO entra.>

## Riesgos y Dependencias
- Riesgo: <qué puede salir mal> → mitigación: <cómo lo cubrís>.
- Dependencia: <de qué depende para funcionar>.
```

> 💡 **¿Y la IA?** Hoy lo armás a mano para entrenar el ojo: entender qué mira cada chequeo. Pero la IA entra enseguida. En el **Módulo 2**, vibecodeando, vas a **volver sobre este PRD y mejorarlo** —al construir descubrís huecos y lo refinás— y, en el **Módulo 3**, vas a **empaquetar este método en tu primer skill** (`create-prd`), que genera y audita PRDs automáticamente contra este mismo checklist. En el **Módulo 5**, skills como ese se orquestan en un pipeline completo. Para entonces vas a saber leer si la IA hizo un buen trabajo o te metió humo.

## 🔎 La muestra: el PRD completo de TicketTriage

Para que veas el nivel, este es el PRD entero de **TicketTriage**, la app de ejemplo que construimos a lo largo del curso: una mesa de ayuda donde la IA clasifica tickets (categoría + prioridad) y redacta un borrador de respuesta apoyado en una base de conocimiento, para que el humano arranque desde el 80% hecho. Salió de un pitch crudo —el mismo del paso 1— y se endureció con las preguntas de calidad. Leelo entero y fijate **cómo cada pieza es verificable**; si te trabás con el tuyo, volvé acá. 👇

```
# PRD-001: TicketTriage — triage de tickets asistido por IA

## Contexto y Problema
En el equipo de soporte del MUG —y en el de cualquier PyME— entran consultas todo
el día: "no puedo entrar a mi cuenta", "¿cuándo vence mi cuota?", "el video de la
clase no carga". Hoy una persona las lee una por una, decide de qué se trata cada
una, le pone urgencia y redacta la respuesta desde cero. Es lento, repetitivo y,
cuando se acumulan, los tickets se enfrían y el socio se calienta. No tenemos un
Zendesk ni recursos para configurarlo; necesitamos algo simple que se haga cargo
del trabajo mecánico y le deje a la persona lo que de verdad aporta criterio.

Personas:
- Sofía (agente de soporte): recibe 30-50 consultas por día y odia reescribir la
  misma respuesta de siempre. Quiere resolver rápido sin bajar la calidad.
- Martín (socio): mandó su consulta y quiere una respuesta correcta y pronta, no
  un número de ticket y silencio.

## Objetivos
Que un ticket entre y salga clasificado y con un borrador de respuesta listo en
segundos, dejando al humano solo para revisar, ajustar y firmar. Reducir el tiempo
de triage de minutos a segundos sin perder calidad ni inventar información.

## Requerimientos Funcionales
- RF-01: Un socio autenticado debe poder crear un ticket (asunto + descripción);
  el ticket queda asociado a su cuenta.
- RF-02: El agente debe poder listar todos los tickets (paginados, con su estado
  abierto/cerrado); el socio solo debe ver los suyos.
- RF-03: El agente debe poder cerrar un ticket.
- RF-04: Al crear un ticket, el sistema debe asignarle una categoría entre
  facturación, técnico, cuenta, otro.
- RF-05: Al crear un ticket, el sistema debe asignarle una prioridad entre
  baja, media, alta.
- RF-06: El sistema debe generar un borrador de respuesta anclado a la base de
  conocimiento (kb.md); no debe afirmar datos que no estén en la KB.
- RF-07: El sistema debe permitir editar el borrador antes de marcarlo como enviado.
- RF-08: El sistema debe requerir autenticación (email + contraseña, con sesión).
  Hay dos tipos de usuario por un flag is_agent: el socio (crea y ve solo sus
  tickets) y el agente (ve todos, clasifica, responde y cierra). Sin RBAC configurable.
- RF-09: El sistema debe permitir que un socio se registre con email + contraseña.

## Requerimientos No Funcionales
- RNF-01: La clasificación debe responder en < 3 s (p95).
- RNF-02: La accuracy de clasificación debe ser ≥ 85% sobre el dataset etiquetado.
- RNF-03: En el set de evaluación, el borrador no debe afirmar ninguna política que
  no esté en la KB (0 alucinaciones de política).
- RNF-04: La API key del modelo no debe estar en el código; se lee de la variable
  de entorno ANTHROPIC_API_KEY.
- RNF-05: Las contraseñas deben almacenarse con hash seguro (bcrypt/argon2), nunca
  en texto plano; la sesión expira tras 24 h de inactividad.

## Criterios de Aceptación
- AC-01 (RF-04, RF-05): Dado el ticket "me cobraron dos veces la cuota", cuando se
  crea, entonces categoría = facturación y prioridad = alta.
- AC-02 (RF-06): Dado un ticket sobre reseteo de contraseña, cuando se genera el
  borrador, entonces incluye el link de reset que está en la KB y no propone otro.
- AC-03 (RF-06): Dado un ticket cuya respuesta NO está en la KB, cuando se genera
  el borrador, entonces el borrador deriva a un humano y no inventa.
- AC-04 (RF-01): Dado un asunto vacío, cuando se intenta crear el ticket, entonces
  el sistema responde HTTP 400 y no lo crea.
- AC-05 (RF-02): Dados más de 20 tickets, cuando se listan, entonces se devuelven
  paginados de a 20 (parámetros page/size).
- AC-06 (RF-08): Dado un usuario no autenticado, cuando intenta ver la lista de
  tickets, entonces el sistema responde HTTP 401 y no muestra ningún dato.
- AC-08 (RF-02, RF-08): Dado el socio A dueño de un ticket y el socio B autenticado,
  cuando B intenta ver ese ticket, entonces responde HTTP 403 y no lo muestra.
  (control de acceso — OWASP #1)

## Fuera de Alcance
CRM completo · multi-canal real (mail/WhatsApp en vivo) · RBAC configurable / más de
dos roles · multi-tenant · envío real de mails (el borrador queda para copiar/pegar).
(La autenticación con dos roles —socio y agente vía is_agent— SÍ entra: RF-08.)

## Riesgos y Dependencias
- Riesgo: la IA alucina respuestas → mitigación: borrador anclado a la KB (RF-06,
  RNF-03) y eval de grounding más adelante.
- Riesgo: clasificación inconsistente en casos ambiguos → mitigación: dataset
  etiquetado y error analysis.
- Dependencia: API de Claude · base de conocimiento kb.md · SQLite.
```

Fijate la disciplina: el contexto cuenta una **historia humana** (Sofía y Martín, no «el usuario»), cada RNF tiene número (≥ 85%, < 3 s), cada AC es binario y atado a un RF concreto, y el fuera de alcance corta el scope **sin** olvidar la auth y el control de acceso —justo donde la IA mete vulnerabilidades (que un socio vea los tickets de otro)—. Eso es un PRD que se puede construir *y comprobar*.

Y ojo: esto es una **primera versión sólida, no la última**. Un PRD es un **documento vivo** —en el Módulo 2, mientras construís vibecodeando, vas a encontrarle huecos y volver a afinarlo—. Lo que importa hoy es que arranque verificable y con alma; mejorarlo después es parte del juego.

Ya tenés el ojo entrenado y el template en la mano. En la próxima lección le toca a tu idea: **escribís el PRD de tu proyecto**, la pieza que vas a arrastrar por todo el curso. ➡️
