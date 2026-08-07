---
titulo: "Ejercicio guiado: Personalizá DAW para tu proyecto"
capitulo: "07-Módulo 5 Agentic Orchestration"
orden: 12
source: "apuntes/slides/00-raw/07-Módulo 5 Agentic Orchestration/12-Ejercicio guiado_ Personalizá DAW para tu proyecto – MUG.html"
source_sha256: f23bfb0b7c66a163
extraido: 2026-08-07
---

# Ejercicio guiado: Personalizá DAW para tu proyecto

Hasta acá usaste DAW **como viene**, y ya sabés de qué está hecho. Ahora le metés mano. 🔧

Y quiero ser claro con lo que estamos haciendo, porque es un cambio de rol importante: **hasta esta lección eras usuario de la herramienta; a partir de acá sos su autor.** Ése es, en el fondo, el objetivo del curso — que no termines sabiendo usar un pipeline, sino pudiendo diseñar el tuyo.

Trabajás sobre **tu repo de M5**, el mismo donde corriste la feature. No es una carpeta de juguete: es el repo con el que vas a seguir en el Módulo 6, así que lo que dejes acá te lo llevás. No te asustes por eso: **está todo en Git**. Si rompés algo, `git diff` te muestra qué tocaste y `git checkout` te lo devuelve. Ésa es exactamente la red que te pusiste en el Módulo 3, y hoy se cobra.

Los dos cambios de abajo están elegidos a propósito: cada uno te obliga a tocar **una capa distinta** del pipeline —el grafo y el orquestador por un lado, los hooks por el otro— y juntos te dan el mapa de dónde se toca qué.

## 🛠️ Tu turno

⏱️ **Tiempo estimado:** ~40 min · 📦 **Entregable:** tu DAW modificado corriendo, con los dos cambios aplicados.

### Cambio 1 — Sacá una fase

Elegí una fase que a tu proyecto no le aplique. **RELEASE** suele ser la candidata —si trabajás solo y todavía no tenés flujo de pull requests, la ceremonia de cierre te sobra— pero puede ser otra: vos sabés qué te pesó cuando corriste el pipeline.

1. En **`.daw/rules/transition-graph.json`**, redirigí la transición: la fase anterior a la que sacás tiene que poder ir directo a donde iba ella.
2. En **`.daw/orchestrator.md`**, sacá el router de esa fase — la sección que dice qué se carga, qué skills se habilitan y qué está bloqueado.
3. Corré un pedido chico y comprobá que el pipeline llega al final sin pasar por ahí.

👉 **Lo que aprendés:** que una fase **vive en dos lugares** —el grafo (las reglas de movimiento) y el orquestador (qué se hace mientras estás en ella)— y que hay que tocar los dos. Si tocás uno solo, la máquina queda incoherente. Y fijate qué interesante: **te lo va a decir**, porque el hook que valida transiciones va a encontrar una que no existe en el grafo. Ése es el sistema protegiéndose de vos, que es exactamente para lo que lo diseñaron.

### Cambio 2 — Metele un candado nuevo

Ahora tocás la otra capa: la del enforcement. Elegí **una** de las dos, según cuánto quieras ensuciarte las manos.

**Opción A — sin escribir código (10 min).** Agregale un gate a una transición, editando solo `.daw/rules/transition-graph.json`. Por ejemplo, exigí un gate `changelog` para salir de RELEASE:

```
"RELEASE->IDLE": { "gates": ["commit", "pr", "changelog"] }
```

Después corré un pedido chico y llegá hasta el cierre. **No te va a dejar cerrar**, y el mensaje te va a decir qué gate falta. Acabás de agregar una condición no negociable **sin tocar una línea de código**: eso es lo que significa que las reglas vivan en datos.

**Opción B — metiendo mano en el gate (25 min).** Abrí `.daw/scripts/hook-gate.py` y buscá `NO_SOURCE_PHASES`: es la lista de fases que tienen prohibido escribir código fuente. Agregale `"RELEASE"` y probá escribir un archivo de código estando en esa fase.

1. Leé primero cómo decide: es la función `source_write_denied`. Un `if` sobre la fase y la ruta, y un `return` con el motivo.
2. Hacé tu cambio.
3. Provocá el bloqueo. Si no te frena, tu condición está mal — y descubrirlo ahora es gratis.

👉 **Lo que aprendés:** que un gate se puede endurecer **por dos vías muy distintas** — declarándolo en el grafo o programándolo en el gate compartido— y que la primera te alcanza mucho más seguido de lo que creerías. La parte difícil nunca es el código: son veinte líneas. Es **decidir qué condición merece un candado**. Volvé a la pregunta de la lección 8: ¿rompe, es riesgo, o solo molesta? Si tu respuesta fue «molesta» y aun así le pusiste candado, sacalo: estás construyendo algo que en dos semanas vas a querer desactivar.

> 🌍 **Un detalle que no es menor:** si tocaste `hook-gate.py`, tu cambio ya funciona en **las seis herramientas** que DAW soporta, no solo en Claude. El gate es uno solo y los adapters no tienen lógica propia — por eso una mejora se escribe una vez. Y por eso un bug también se arregla una vez, que es la mitad más importante del argumento.

> 💡 **Sobre agregar skills propios:** podés hacerlo cuando quieras — es tu repo. La única condición es que **no choquen con los de DAW**: si le ponés a uno tuyo el nombre de uno que ya existe, hay ambigüedad y el agente te la va a marcar en vez de adivinar. Para este ejercicio no hace falta: DAW ya trae los dieciséis que el pipeline necesita.

## ✅ Lo lograste cuando

- Corriste un pedido de punta a punta con **tu** versión modificada.
- El pipeline **no pasa** por la fase que sacaste.
- El candado que agregaste **te frenó** cuando intentaste saltearlo, con su mensaje.

## 🩹 Si algo se rompe

Se va a romper, y está perfecto: es la parte del ejercicio donde más se aprende. Tres herramientas, en orden de menor a mayor:

- **`/daw-self-check`** — verifica la coherencia de la instalación y del state, y te dice qué quedó mal. Empezá siempre por acá.
- **`git diff`** — te muestra exactamente qué tocaste. La mayoría de las veces el problema está en un JSON al que le falta una coma.
- **Reinstalar.** `install.sh` es idempotente y **no te pisa lo tuyo** — respeta tus skills y agents propios. Si querés volver el método a fábrica, `git checkout .daw/` y listo.
- **Empezar de cero de verdad.** `uninstall.sh` saca el método, el runtime y el cableado, dejando intacto lo tuyo: tus skills propios, tu `AGENTS.md` y **todo `docs/`**. Después reinstalás y probás otra personalización sobre limpio. Vale para experimentar sin miedo.

Y hay una observación que vale más que el ejercicio en sí: fijate **cuánto tardaste en encontrar dónde tocar**. Con un plugin cerrado no habrías podido — habrías tenido que leer documentación, buscar un punto de extensión, y probablemente aceptar que lo que querías no se podía. Con archivos de texto en tu repo, abriste dos y listo. **Eso es lo que significa que sea un drop-in**, y es la razón por la que en este curso trabajamos así.

## 🤔 Anotá para el capstone

Mientras hacías esto seguro pensaste «esto lo cambiaría» varias veces más. Anotalas ahora, en crudo, que en la próxima lección las pasás en limpio:

- ¿Qué fase **te sobra** para tu proyecto? ¿Cuál **te falta**?
- ¿Qué gate te gustaría con candado que hoy no lo tiene? ¿Y cuál sacarías?
- ¿Qué te resultó **innecesariamente pesado** al correrlo?

Eso ya es tu diseño, en borrador. Solo falta escribirlo bien. ➡️
