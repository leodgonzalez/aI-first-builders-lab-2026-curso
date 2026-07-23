---
titulo: "Certificaciones de requisitos y estado del spec-driven development"
tipo: investigacion
fecha: 2026-07-18
metodo: "deep research — 6 ángulos, 26 fuentes, 124 claims extraídos, 25 verificados adversarialmente (22 ✓ / 3 ✗)"
---

# Certificaciones de requisitos y spec-driven development (julio 2026)

**La pregunta:** el PRD que enseña el curso (RF atómicos con ID, RNF cuantificados, AC
binarios Dado/Cuando/Entonces, trazabilidad RF→AC) es en los hechos un SRS de ingeniería de
requisitos clásica vestido de PRD. ¿Vale capitalizarlo con una credencial? ¿Tiene futuro?

**La respuesta en una línea:** sí, con **CPRE Foundation de IREB** — en español, proctored,
no vence, material gratis. No existe certificación de PRD ni de spec-driven development.

---

## 1. Certificaciones

### IREB CPRE — la que más se acerca

Tres cosas que cambiaron o que conviene saber:

**a) La nomenclatura ya no es Foundation/Advanced/Expert.**

| Nivel | Nombre actual |
|---|---|
| 1 | Foundation |
| 2 | Practitioner |
| 3 | Specialist |
| 4 | Expert |

Cuatro módulos en niveles 2 y 3: Requirements Elicitation, Requirements Management,
Requirements Modeling, **RE@Agile**. Poner "CPRE Advanced" en el CV es nomenclatura vieja.

**b) CPRE Foundation (Level 1) — el punto de entrada.**

| | |
|---|---|
| **Idioma** | ✅ **Se rinde en español** (Certible, GASQ, tecnovy) |
| **Examen** | 45 preguntas MC ponderadas → 70 puntos · 75 min (+15 si no es tu idioma nativo) · 70% para aprobar (49/70) |
| **Modalidad** | Proctored en serio: invigilator humano en vivo, webcam + micrófono, ID con reconocimiento facial, sala privada |
| **Vigencia** | **No vence nunca.** Sin recertificación |
| **Curso** | **Opcional.** IREB publica syllabus, handbook, glosario y examen de práctica **gratis** |
| **Estructura** | ISO/IEC 17024: IREB no certifica — lo hacen certification bodies licenciados, filtrables por país |

> El contraste que importa: **PMI-PBA** pide 60 PDU cada 3 años, **IIBA CBAP** 60 CDU cada 3
> años **más fee de recertificación**. CPRE no pide nada.

**c) IREB sí se movió hacia IA: micro-credencial `AI4RE`.**

Operativa y vendida por Certible, isqi y GASQ — no es un anuncio. Temario: fundamentos de
IA, LLMs, prompt engineering, riesgos, y aplicación de IA en elicitación, documentación,
validación y gestión de requisitos.

**Pero es señal débil:** 22 preguntas · 30 min · 80% para aprobar · **unproctored** (sin
webcam, de hecho open-book) · sin prerrequisitos · **vence a los 3 años** · solo alemán e
inglés.

> ⚠️ **Ojo con la dirección.** AI4RE es *IA-para-escribir-requisitos* — el **inverso** de lo
> que enseña el curso, que es *requisitos-para-dirigir-agentes*.

> 📌 Matiz sobre "no vence": el **certificado** CPRE no caduca, pero las **micro-credenciales
> sí** (3 años). Decir "nada de IREB vence" es incorrecto. Y vitalicio significa que el papel
> no expira, no que el temario siga vigente si IREB publica syllabus nuevo.

### IIBA — precios verificados (página oficial de fees, 2026-07-18)

| | Application | Examen (no-miembro) | Recertificación |
|---|---|---|---|
| **ECBA** | No requiere | USD 395 (tarifa única) | **No requiere** |
| **CCBA** | USD 145 | USD 405 (miembro 250) | USD 85-120 c/3 años |
| **CBAP** | USD 145 | USD 505 (miembro 350) | USD 85-120 c/3 años |

El primer año de membresía viene incluido con la compra del examen, así que la brecha
miembro/no-miembro es menor de lo que parece. Todas las tarifas son no reembolsables y
"subject to change without notice". **No se verificó temario, examen ni idioma** — solo precios.

### 1(b) ¿Hay certificación de PRD / spec-driven / dirección de agentes?

**No. Ninguna.** Lo que se chequeó:

| Emisor | Qué hay en 2026 | ¿Sirve? |
|---|---|---|
| **IREB** | AI4RE (micro-credencial) | Va en la dirección inversa; badge liviano |
| **ISTQB** | CT-AI v2.0 (liberado 17/04/2026) + CT-GenAI v1.1 (27/04/2026) | **No.** Es testing de sistemas de IA |
| **GitHub/MS** | **GH-300** (Copilot) — vigente, proctored | Señal de vendor, pero **cero requisitos** |
| **IIBA / PMI** | Nada nuevo en esta línea | — |

**El censo de keywords sobre el syllabus completo de CT-AI v2.0** es la evidencia más dura
de que ISTQB no es el camino:

```
EARS = 0        Gherkin = 0        PRD = 0
spec-driven = 0     "requirements engineering" = 0
Machine Learning = 107      prompt = 15
```

(Los 17 hits de "acceptance criteria" son umbrales de aceptación **de modelo**, no AC estilo
Gherkin/Volere.)

**GH-300 en detalle** — porque es el único con algo de agentes:

- Proctored por Pearson VUE · 100 min · nivel Intermediate · **se rinde en español**.
- Pesos: uso responsable 15-20% · features 25-30% · datos y arquitectura 10-15% ·
  **prompt engineering and context crafting** 10-15% · productividad 10-15% · privacidad 10-15%.
- Sub-bullets incluyen Agent Mode, Agent Sessions/Sub-Agents, MCP, Copilot CLI, Edits, Spark.
- **En ningún sub-bullet** aparecen requisitos, PRD, specs, AC, EARS ni Gherkin. Lo más
  cercano son "instructions files" y reuso de prompt files, encuadrados como *context crafting*.
- ⚠️ La versión en inglés **se actualiza el 07/08/2026** y las localizaciones van con retraso:
  rendirlo en español después de esa fecha puede significar examinarse sobre temario anterior.
- ⚠️ Microsoft **no publica el precio** ("price based on the country or region"). Los ~USD 99
  que circulan son de terceros, sin verificar.

### 1(c) Recomendación

> **CPRE Foundation en español, por autoestudio, sin pagar curso.**

Es la única del inventario que combina: español + proctored + no vence + material gratis +
acredita exactamente el trabajo que ya hacés.

- **Saltear AI4RE**: unproctored, vence a 3 años, sin español, y apunta al revés de la tesis.
- **GH-300 solo si** querés señal de vendor sobre agentes de código. No sustituye lo anterior:
  son cosas distintas.
- **IIBA**: más caro, con costo recurrente, y el dato contrarian que apareció es feo —
  ~252 puestos abiertos en EE.UU. piden CBAP explícitamente. Número minúsculo.

---

## 2. Spec-driven development

> ⚠️ **Este bloque NO pasó el filtro adversarial** — el presupuesto de verificación se
> consumió en certificaciones. Viene de extractores sobre repos y docs primarios, sin voto
> de refutación. Tratalo como indicativo, no como confirmado.

| Proyecto | Estado a julio 2026 |
|---|---|
| **GitHub Spec Kit** | **Muy vivo.** ~90k ★, 8k forks, **v0.13.0 del 17/07/2026**, MIT, Python. Soporta 30+ agentes de código. El flujo se amplió respecto de `/specify → /plan → /tasks` |
| **AWS Kiro** | **Vivo.** Docs actualizadas 25/06/2026. Confirmado el trío `requirements.md` + `design.md` + `tasks.md`, y **sigue usando EARS** |
| **AGENTS.md** | **Convención de facto**, con spec oficial en agents.md. `CLAUDE.md` queda como nombre específico de Claude Code; práctica recomendada: **symlink**, no duplicar |
| **OpenSpec** (Fission-AI) | Nuevo. MIT, v1.6.0 del 10/07/2026, 41 releases, 651 commits. **No usa notación formal** tipo EARS |

**Notación:** no hay estándar de facto consolidado. Kiro empuja **EARS** (Mavin/Rolls-Royce,
2009); OpenSpec no usa notación formal; Spec Kit tampoco impone una.

**Estandarización:** ningún indicio de ISO, IEEE ni IREB trabajando en esto. La comunidad
académica sigue activa (RE'26, 34ª edición IEEE, Montréal, 17-21 agosto 2026) pero sin
normativa en camino.

---

## 3. Refutado — no repetir

| Afirmación | Voto |
|---|---|
| ❌ "IREB reporta **95.000 certificados** en 105 países, 80% de aprobación" | 0-3 — no está en la fuente |
| ❌ "CT-AI v2.0 **eliminó** el contenido de usar IA para testear" | 0-3 — sigue ahí |
| ❌ "IREB no fija idioma del examen y su página no menciona español" | 0-3 — sí lo hace |

También: **"recognized by companies worldwide"** de IREB es marketing, no dato.

---

## 4. Huecos — lo que quedó sin verificar

- **Todo el bloque producto**: PMI-PBA, Pragmatic Institute, Product School, SVPG, Reforge.
  La distinción pedida entre *certificación con examen independiente* vs *curso comercial que
  vende un badge* quedó sin resolver ahí. (Dato suelto sin verificar: Product School PMC
  USD 4.999, Pragmatic USD 2.495/curso, Reforge USD 1.995/año — ninguno con examen independiente.)
- **Costo real en USD de cualquier examen de IREB** — Certible usa calculador dinámico.
  Tampoco el precio del GH-300 en fuente primaria.
- **Reconocimiento de mercado en LATAM/Argentina**: cero ofertas de empleo, encuestas
  salariales o conteo de certificados. El único dato de escala que apareció fue refutado.
- **Toda la Pregunta 2**, como se aclaró arriba.

> 🔍 **Sesgo metodológico detectado:** dos claims de precios de IIBA casi se refutan por mal
> parseo de columnas en tablas HTML. Reconfirmá cualquier cifra antes de decidir con ella.

**Las ausencias son estado a julio de 2026, no imposibilidades permanentes.** IREB dice tener
más micro-credenciales "in planning".

---

## Fuentes principales

- `cpre.ireb.org` — /concept, /concept/foundationlevel, /concept/ai4re-micro-credential,
  /process/micro-credentials, /process/process-cpre-level-1-2, /training-certification, /benefits
- `certible.com/IREB/CPRE/` — FL-foundation-level, MC-micro-credential/AI4RE · `isqi.org`
- `iiba.org/business-analysis-certifications/certification-fees/`
- `istqb.org` — release de CT-AI v2.0 + syllabus PDF
- `learn.microsoft.com/credentials/certifications/github-copilot/` + study guide GH-300
- `github.com/github/spec-kit` · `kiro.dev/docs/specs/feature-specs/` ·
  `github.com/Fission-AI/openspec` · `conf.researchr.org/home/RE-2026`
