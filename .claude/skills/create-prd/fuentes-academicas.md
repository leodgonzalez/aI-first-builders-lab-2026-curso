# create-prd — Fuentes académicas de cada concepto

> 📚 **Documento de enriquecimiento, no de reglas.**
> No agrega nada a lo que hay que hacer: la regla vigente sigue siendo `referencia-regla-de-oro.md` + `SKILL.md`.
> Esto solo mapea **cada concepto que YA está en la regla de oro** a su origen (estándar, libro, autor),
> para poder **ampliar, desambiguar y buscar ejemplos** cuando un término (p. ej. "atómico" o "verificable")
> quede corto. Es material de consulta, no criterios nuevos de evaluación.

## Cómo usarlo

Cuando la regla de oro use un término y quieras entenderlo más hondo o ver ejemplos canónicos, buscá el
concepto acá abajo y andá a la fuente indicada. Los términos entre comillas son los que aparecen literalmente
en `referencia-regla-de-oro.md` / `SKILL.md`.

---

## Concepto transversal: "PRD verificable"

- **Origen:** IEEE 830 → ISO/IEC/IEEE 29148 (atributo *verifiable* de un buen requisito) · Karl Wiegers, *Software Requirements*.
- **Qué amplía:** la idea de que un requisito "se valida igual que el código" es el atributo formal *verifiable*. Wiegers lista las características de un buen requisito (correcto, no ambiguo, completo, verificable, trazable): ahí está el marco entero del que la regla de oro toma su columna vertebral.

## Contexto y Problema — "personas nombradas (no 'el usuario')"

- **Origen:** Alan Cooper, *The Inmates Are Running the Asylum* (1998) — inventor de las **personas** · Marty Cagan, *Inspired* (descubrimiento de producto, "si no hay dolor no hay app").
- **Dónde buscar ejemplos:** los arquetipos de persona (con metas y frustraciones) están en Cooper; el encuadre "qué dolor y para quién" en Cagan.
- **Personas vs. roles (importante):** las **personas nombradas** (Cooper) viven en *Contexto y Problema* — dan empatía y el *por qué / para quién*. Los **roles/actores** (IEEE 830 *user classes*, actores de casos de uso — Jacobson/UML; Wiegers) son lo que referencian los **RF y AC** ("el aprobador debe…"). No se reemplazan: personas para el *por qué / para quién*, roles para el *quién puede qué*. En un enunciado de requisito nunca va un nombre propio ("Martín debe…"), va el rol ("el aprobador debe…").

## Requerimientos Funcionales — "atómico (una sola acción)" y verbo "debe"

- **Atómico:** IEEE 830 / ISO 29148 (*singular* / un requisito = una capacidad) · Wiegers ("un requisito por enunciado") · INVEST — la **A**tomic/**S**mall — de Bill Wake, difundido por Mike Cohn, *User Stories Applied*.
- **Verbo imperativo "debe" / "shall":** convención "**shall**" de IEEE/ISO 29148 · **RFC 2119** (Bradner, 1997), *Key words to Indicate Requirement Levels* — define con precisión MUST / SHALL / SHOULD; es la fuente exacta de por qué "debe" ≠ "debería".
- **Sin weasel words ("correctamente/adecuado"):** atributo *unambiguous* de IEEE · Wiegers, capítulo sobre lenguaje ambiguo.

## Requerimientos No Funcionales — "cualidad con número"

- **Fit criterion (métrica pegada a la cualidad):** Suzanne & James Robertson, *Mastering the Requirements Process* (metodología **Volere**) — el "fit criterion" ES tu "RNF con número".
- **Cuantificar lo cualitativo:** **Tom Gilb**, *Competitive Engineering* (lenguaje **Planguage**) — la autoridad en convertir "rápido/usable" en números; fuente ideal para el mantra "sin métrica es un deseo".
- **Qué tipos de RNF existen (para ejemplos):** ISO/IEC 25010 — modelo de calidad de producto (rendimiento, seguridad, usabilidad, fiabilidad, mantenibilidad, portabilidad…). Útil solo como catálogo de ejemplos, no como checklist obligatorio.

## Criterios de Aceptación — "Dado / Cuando / Entonces", binario

- **BDD y Given/When/Then:** Dan North, *Introducing BDD* (2006) — origen del enfoque · Aslak Hellesøy — **Gherkin/Cucumber**, sintaxis Given-When-Then.
- **Ejemplos concretos como especificación:** Gojko Adzic, *Specification by Example* (2011) y *Bridging the Communication Gap* (2009) — "key examples", *living documentation*; la mejor fuente de ejemplos de AC bien escritos.
- **AC como "confirmación" de la historia:** Mike Cohn ("conditions of satisfaction") · Ron Jeffries — las **3 C's** (Card, Conversation, **Confirmation**).

## Trazabilidad — "IDs (RF-01, AC-01) para trazar"

- **Origen:** IEEE 830 / ISO 29148 (atributo *traceable*) · Wiegers — matriz de trazabilidad de requisitos.
- **Qué amplía:** el trazado RF→AC de la regla de oro es una forma mínima de la trazabilidad; la fuente explica la versión completa (necesidad→requisito→diseño→test).

## Fuera de Alcance — "todo lo que no excluís se asume incluido"

- **Origen:** gestión de alcance / *scope creep* — Wiegers ("project scope and limitations") · Marty Cagan (recorte de alcance / MVP) · PMBOK (control de alcance).

## Riesgos y Dependencias

- **Origen:** IEEE 830 ("Assumptions and Dependencies") · gestión de riesgos (PMBOK) — cada riesgo con su mitigación, cada dependencia externa nombrada.

## PRD vs spec y "documento vivo"

- **Qué (PRD) vs cómo (spec):** distinción requisitos-vs-diseño de IEEE/Wiegers; el spec cubre cada RF con diseño y cada AC con un test (trazabilidad a test).
- **Living documentation / se refina al construir:** Gojko Adzic (*living documentation*) · requisitos ágiles como conversación (Cohn, Jeffries 3 C's).

## Anexo — "diagrama de transición de estados"

- **Origen:** modelos de análisis de requisitos — Wiegers (capítulo de *analysis models*: state-transition diagrams/tables) · máquinas de estados de UML.
- **Qué amplía:** justifica por qué un anexo con estados y transiciones es un artefacto de requisitos legítimo (y el ejemplo de la regla de oro lo usa).

---

## Bibliografía (para ir a la fuente)

- **IEEE 830-1998** → **ISO/IEC/IEEE 29148:2018** — *Requirements engineering / SRS*.
- **RFC 2119** — Bradner (1997), *Key words for use in RFCs to Indicate Requirement Levels*.
- **ISO/IEC 25010** — *Systems and software quality models*.
- Karl Wiegers & Joy Beatty — *Software Requirements*, 3.ª ed., Microsoft Press.
- Suzanne & James Robertson — *Mastering the Requirements Process* (Volere).
- Tom Gilb — *Competitive Engineering* (Planguage).
- Dan North — *Introducing BDD* (2006).
- Gojko Adzic — *Specification by Example* (2011); *Bridging the Communication Gap* (2009).
- Mike Cohn — *User Stories Applied* (2004); INVEST (Bill Wake).
- Ron Jeffries — *Essential XP: Card, Conversation, Confirmation* (3 C's).
- Marty Cagan — *Inspired* (SVPG).
- Alan Cooper — *The Inmates Are Running the Asylum* (1998).
- Ivar Jacobson — casos de uso y **actores** (*Object-Oriented Software Engineering*, 1992); base de los actores de UML.
