---
titulo: "Ejercicio guiado: Tu primer skill (create-prd)"
capitulo: "05-Módulo 3 Construí con red Git skills y disciplina"
orden: 6
source: "apuntes/slides/00-raw/05-Módulo 3 Construí con red Git skills y disciplina/06-Ejercicio guiado_ Tu primer skill (create-prd) – MUG.html"
source_sha256: 690f1503e504554d
extraido: 2026-07-18
---

# Ejercicio guiado: Tu primer skill (create-prd)

Llegó uno de los momentos más lindos del módulo: vas a **escribir tu primer skill** y a verlo dispararse solo. 🧩 Y no un skill de juguete: `create-prd`, el que empaqueta el workflow de PRD que ya hiciste a mano —así que sabés exactamente qué tiene que hacer y vas a poder juzgar si lo hace bien—. El plan completo: creás el skill, lo usás para **regenerar tu PRD** (un `PRD2.md` nuevo), lo comparás con el original, te quedás con lo mejor… y todo el recambio queda **prolijamente commiteado, vibecodeando también los commits** —vos no tipeás un solo comando git—. Skills y Git, trabajando juntos por primera vez.

## 🪜 Por qué un archivo nuevo (y no pisar el original)

Una aclaración de método antes de arrancar: el skill va a **leer tu `PRD.md`** —la versión que endureciste a mano, que ya está **commiteada y a salvo** en tu repo— pero el resultado lo va a escribir en un archivo aparte, **`PRD2.md`**. ¿Para qué? Para poder **comparar**. Tu PRD actual salió de varias vueltas de dirigir y juzgar a mano; el nuevo va a salir del skill corriendo tu método completo de una. Ponerlos lado a lado te muestra, con tus propios requerimientos, qué garantiza el empaquetado (la estructura, el checklist, nada olvidado) y qué sigue dependiendo de tu juicio. Y de paso, el recambio de un archivo por otro es práctica de Git en el mundo real. Esa comparación vale más que cualquier teoría sobre skills.

## 🛠️ Tu turno: paso a paso con Claude Code

⏱️ **Tiempo estimado:** ~35 min · 📦 **Entregable:** el skill `create-prd` en tu repo + tu **PRD final** (el `PRD2` generado con el skill y curado por vos) como PRD oficial del proyecto, con toda la historia en Git.

**1. Abrí Claude Code en tu proyecto** (el repo del ejercicio anterior) con `claude`.

**2. Creá el skill.** Este es el corazón del ejercicio, así que no lo vamos a improvisar: el `SKILL.md` empaqueta **todo tu método de PRD del curso** —el template de M1 (de *PRD: qué es y cómo se arma*), el checklist y los prompts que usaste en *Vibecodeá tu PRD*, y la mentalidad de **loop** de aquel ejercicio—. Es la versión con todo el músculo del esqueleto que viste en la anatomía de la lección anterior. Pedile a Claude Code:

```
Creá el archivo .claude/skills/create-prd/SKILL.md con exactamente este contenido:
```

…y pegale a continuación este bloque, completo:

```
---
name: create-prd
description: Crea o audita un PRD siguiendo el template y el checklist de calidad del curso, iterando en loop hasta que quede firme. Se usa cuando el usuario pide crear, escribir, revisar, auditar o endurecer un PRD.
---

# Create PRD

Trabajás en LOOP, nunca en one-shot: normalizar → auditar → esperar el juicio del
usuario → reescribir → volver a auditar. El PRD está listo solo cuando una
auditoría sale limpia.

## El template del curso (estructura obligatoria)

# PRD-001: <nombre del proyecto> — <una línea de qué es>
## Contexto y Problema           (el dolor real y para quién; personas: quién lo usa y qué necesita)
## Objetivos                     (qué significa ganar, a nivel producto)
## Requerimientos Funcionales    (RF-01, RF-02, … — "El sistema debe <una sola acción>")
## Requerimientos No Funcionales (RNF-01, … — cualidad CON número: "< 3 s p95", "≥ 85%")
## Criterios de Aceptación       (AC-01 (RF-01): Dado <contexto>, cuando <acción>, entonces <resultado medible>)
## Fuera de Alcance              (lo que explícitamente NO entra)
## Riesgos y Dependencias        (riesgo → mitigación; de qué depende)

## Paso 1 — Crear o normalizar

- Si el usuario pide un PRD nuevo: hacele TODAS las preguntas que necesites ANTES
  de escribir (el dolor, las personas, las features core, las restricciones).
  NO inventes requerimientos.
- Si el usuario trae un PRD existente: si no está en Markdown limpio, pasalo a
  Markdown. Validá que respete la estructura del template y decile qué secciones
  faltan o están fuera de lugar. Si falta alguna, agregá el encabezado vacío para
  dejar el molde completo, pero NO inventes requerimientos ni criterios.

## Paso 2 — Auditar (sin reescribir todavía)

Auditá el contenido contra este checklist y marcá los problemas UNO POR UNO,
diciendo dónde está cada uno y por qué:
- ¿Cada RF es atómico (una sola acción) y dice "debe"?
- ¿Cada RNF tiene un número concreto? (no "rápido" → "< 3 s p95")
- ¿Cada RF tiene al menos un AC que lo verifique?
- ¿Cada AC es binario (pasa/no pasa) y está en formato Dado/Cuando/Entonces?
- ¿El "Fuera de Alcance" está explícito?
- ¿Hay un AC de control de acceso (que un usuario no vea datos de otro)?
NO agregues features nuevas.

## Paso 3 — Esperar el juicio del usuario

Presentá los hallazgos y esperá: el usuario aprueba o rechaza cada uno.
No corrijas nada sin aprobación.

## Paso 4 — Reescribir y volver a auditar

Reescribí SOLO los RF, RNF y AC que el usuario aprobó como débiles, aplicando las
correcciones aprobadas. Mantené el resto igual. Devolvé el PRD completo
actualizado. Después VOLVÉ al Paso 2 sobre la versión nueva: lo normal es que la
segunda pasada encuentre cosas que la primera no vio. Repetí el loop hasta que la
auditoría salga limpia.

## Reglas duras (siempre)

- Todo lo que el usuario no pidió explícitamente va a "Fuera de Alcance": nada de
  features "que quedan bien".
- Criterios con "correctamente" o "adecuado" no sirven: binarios o nada.
- Ante la duda, preguntá; nunca inventes.
```

Releelo antes de seguir: ¿lo reconocés? El template es el de M1, el checklist y las instrucciones son **los mismos prompts que tipeaste a mano** en *Vibecodeá tu PRD*, y los pasos 2→4 son el **loop** que aprendiste ahí (auditar → juzgar vos → reescribir → re-auditar). Tu método entero, escrito una vez, para siempre. Y es TUYO: si aquel ejercicio te enseñó algo que acá falta, agregalo.

**3. Commiteá el skill.** Ya sabés cómo se dirige esto:

```
Commiteá el skill nuevo con un mensaje claro y pushealo a main.
```

Algo como `chore: agregar skill create-prd` en tu historial —y en GitHub, al instante—. El skill ahora **vive en tu repo**: versionado, respaldado, mejorable, compartible.

**4. Disparalo — sin nombrarlo.** Este es el momento de la verdad. Limpiá el contexto (`/clear`, ya sabés por qué: tarea nueva, mesa limpia) y pedile algo natural, **sin mencionar el skill**:

```
Leé @PRD.md: es el PRD de mi proyecto, la versión que endurecí a mano en el módulo pasado (ya está commiteada en Git, así que trabajá tranquilo).
Quiero que generes una versión nueva y más rigurosa en un archivo aparte, PRD2.md:
pasala por el template y el checklist de calidad completos del curso, auditá punto
por punto, y preguntame todo lo que necesites antes de inventar o cambiar nada.
NO modifiques el PRD.md original.
```

Mirá lo que pasa: aunque nunca nombraste al skill, el agente **matchea tu pedido con la `description`** y dispara `create-prd` solo. Y ahí lo ves girar: normaliza, audita tu PRD contra el checklist punto por punto, te presenta los hallazgos y **espera tu juicio** —el loop que escribiste en el archivo, corriendo solo—. Juzgá como en *Vibecodeá tu PRD*: aprobá lo real, rechazá el humo, contestá lo que te pregunte. El resultado queda en `PRD2.md`. Si el skill no se disparó (te das cuenta porque no sigue el template ni el loop), afilá la `description` y probá de nuevo: esa es *la* lección de skills.

**5. Compará y juzgá.** Ahora sí, los dos lado a lado:

```
Compará @PRD.md y @PRD2.md sección por sección: ¿qué tiene cada uno que
al otro le falta? No cambies nada todavía.
```

Leé la comparación con ojo de juez. Lo típico: el `PRD2` sale con **estructura impecable y huecos tapados** (el skill no se olvida de ningún punto del checklist), pero tu versión a mano tiene **decisiones ganadas a pulso** —ese criterio de aceptación que afilaste tras rechazar humo, ese fuera-de-alcance que frenó el scope creep— y puede que el skill haya reescrito alguna peor. Portá al `PRD2` lo que tu versión tenga de mejor: *«pasá el AC-08 del PRD original al PRD2, tal cual está»*.

Y cerrá con una **última vuelta del loop**: pedile *«auditá @PRD2.md»*. El skill corre el checklist de nuevo sobre la versión final, te presenta lo que encuentre y espera tu juicio. Cuando la auditoría sale limpia, tenés **tu mejor PRD hasta ahora**.

**6. El recambio, en dos commits — vibecodeados, claro.** Acá no tipeás un solo comando git: **dirigís**, y el agente ejecuta. Primero guardá el PRD nuevo:

```
Commiteá PRD2.md con un mensaje que diga que fue generado con el skill create-prd.
```

Y ahora, el paso que hace un mes te hubiera dado pánico: **borrá el PRD viejo**.

```
Eliminá el PRD.md viejo, renombrá PRD2.md a PRD.md, commiteá el cambio
con un mensaje que cuente qué pasó, y pusheá todo a main.
```

¿Por qué podés borrarlo tan tranquilo? **Porque Git lo recuerda.** Tu versión a mano no se perdió: vive en el historial, recuperable cuando quieras. Eso es trabajar con red: borrar deja de ser irreversible. Verificalo vos mismo:

```
git log --oneline
```

> ✅ **Lo lograste cuando** el skill **se disparó solo** (sin que lo nombres), **corrió su loop** (auditó, esperó tu juicio y re-auditó hasta salir limpio), tu `PRD.md` final es el `PRD2` **curado por vos** (con lo mejor de tu versión a mano adentro), y el historial cuenta la historia completa: skill agregado → PRD2 generado → recambio. Ese `PRD.md` es la mitad de tu **entregable doble** —y el plano del que va a nacer tu app—.

### 🔎 La muestra: el historial de TicketTriage cuenta la historia

Así quedó el `git log` de **TicketTriage** al salir de este ejercicio —leelo de abajo hacia arriba: es la progresión del módulo entera—:

```
$ git log --oneline
f31c2d7 docs: PRD2 pasa a ser el PRD oficial (generado con create-prd)
9d84e01 docs: PRD2 generado con el skill create-prd
5a1b3c8 chore: agregar skill create-prd
8c2f4a1 docs: aclarar criterio de aceptación de control de acceso
7b40d12 estado inicial: PRD + guardrails
```

¿Y la comparación? El `PRD2` salió **estructuralmente perfecto** —las siete secciones, todos los RNF con número, cero olvidos—. Pero el AC-08 de control de acceso de la versión a mano (el que habíamos agregado juzgando una auditoría, ¿te acordás?) era más específico que como lo dejó el skill, así que lo portamos tal cual. La moraleja del ejercicio en una frase: **el skill garantiza el piso; tu juicio pone el techo.**

## 🪜 El peldaño, completado

Mirá el camino que hiciste con el mismo documento: lo escribiste **a mano** (M1), lo endureciste **dirigiendo a la IA** (módulo pasado), y hoy lo regeneraste **con un skill tuyo, con un solo pedido**. En el **Módulo 5**, skills como este se orquestan en un pipeline con gates que corre solo. Cada peldaño te preparó para juzgar el siguiente —por eso hoy pudiste mirar el output del skill y saber, al toque, qué le faltaba—.

Tu primer skill te llevó una lección entera —y valió cada minuto—. Pero acá viene lo lindo de esta habilidad: el segundo cuesta una fracción. Tanto, que **el próximo no te lo voy a dar masticado**: es un desafío, y lo vas a construir vos. ➡️
