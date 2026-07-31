---
titulo: "Qué es Spec-Driven Development"
capitulo: "06-Módulo 4 Spec Driven Development (SDD)"
orden: 2
source: "apuntes/slides/00-raw/06-Módulo 4 Spec Driven Development (SDD)/02-Qué es Spec-Driven Development – MUG.html"
source_sha256: 0c8abd9cd64f0a91
extraido: 2026-07-31
---

# Qué es Spec-Driven Development

Veníamos de sentir el dolor del vibecoding sin método. El Spec-Driven Development (SDD) es la respuesta disciplinada a ese dolor, y la idea es tan simple como potente: **antes de escribir una línea de código, escribís un spec ejecutable** —un documento preciso de qué tiene que hacer el sistema— y desde ahí dirigís al agente. El spec no es documentación que escribís después para cumplir; es el **punto de partida y la fuente de verdad** de la que sale todo lo demás. 📐

Hay una frase de Sean Grove (de OpenAI) que captura el cambio mejor que nada: **«specs are the new code»** —las especificaciones son el nuevo código—. Suena provocador, pero pensalo: si el agente puede generar el código a partir de un spec claro, entonces *lo que de verdad importa, lo que tenés que cuidar como artesano, es el spec*. El código se vuelve la traducción; el spec, la intención. No es una ocurrencia aislada: consultoras y empresas como Thoughtworks e IBM ya reconocen al SDD como una de las prácticas serias del desarrollo asistido por IA, y herramientas como GitHub Spec Kit o Amazon Kiro nacieron específicamente para sostenerlo.

## 🎬 Un ejemplo chico, para que se sienta la diferencia

Imaginate que tenés que agregar «clasificar tickets por prioridad» a tu app. En **vibecoding puro**, la conversación sería algo así: *«che, clasificá los tickets por prioridad»* → el agente elige tres niveles, o cuatro, decide qué hacer si no está seguro, quizás inventa un campo nuevo en la base de datos que a vos no se te había ocurrido. Todo eso queda enterrado en el código, sin que nadie lo haya decidido a propósito.

En **SDD**, esa misma necesidad primero se convierte en un spec: *«el sistema asigna una prioridad de {baja, media, alta} a cada ticket; si el ticket menciona una caída total del servicio, la prioridad es siempre alta; si el modelo no está seguro, prioridad baja y se marca para revisión humana»*. Recién con eso escrito y acordado, el agente construye. La diferencia no es de velocidad en el momento —de hecho escribir el spec lleva un rato—; la diferencia es que, tres semanas después, cuando alguien pregunte «¿por qué este ticket quedó en prioridad media?», la respuesta está en un documento, no en la memoria de nadie.

## 🧭 Para que no lo confundas con lo que ya viste

SDD se parece de lejos a otras cosas del curso, así que marquemos los límites con claridad —entender qué *no* es te lo fija mejor—.

- **No es vibecoding (M2-M3).** El vibecoding **improvisa hacia el resultado**: pedís, ves, corregís, sobre la marcha. El SDD hace lo contrario: **primero fija el contrato y después construye** contra él. Uno es jazz; el otro es partitura. Ninguno es «mejor» en abstracto —ya vamos a ver cuándo conviene cada uno, en la Lección 13—, pero son mentalidades distintas.
- **No es un guardrail (M1-M2).** El guardrail (`AGENTS.md`/`CLAUDE.md`) dice *cómo se comporta el agente siempre*, en cualquier tarea de tu proyecto —tu stack, tus convenciones, lo que tiene prohibido—. El spec dice *qué construir esta vez*, para una feature puntual. El guardrail es permanente y transversal; el spec es específico y por feature. Son capas distintas que conviven: el agente respeta tu guardrail *mientras* construye lo que pide el spec.

## 🎯 Por qué cambia el juego

Lo poderoso del SDD es que **mueve la conversación difícil al principio**, cuando es barata. En vibecoding, las ambigüedades («¿qué pasa si el ticket viene vacío?», «¿cuál es la prioridad por defecto?») aparecen cuando ya escribiste medio sistema, y resolverlas cuesta caro: hay que entender qué código ya depende de esa decisión implícita, y a veces hay que deshacer trabajo. En SDD, esas preguntas se contestan *en el spec*, antes de que exista una sola línea. Construís sobre acuerdos, no sobre suposiciones. Por eso, contra la intuición, **escribir el spec primero te hace ir más rápido**, no más lento: te ahorra las vueltas de «esto no era lo que quería», que es exactamente el tipo de retrabajo que sentiste en el muro de los 3 meses de M2-M3.

## 💡 Para aplicar

Mirá tu app de M2-M3 y elegí una decisión que la IA tomó por vos sin preguntarte (un default, un caso borde, un formato). Anotala. Esa es, exactamente, la clase de cosa que un spec te habría hecho decidir *antes* —y la que vas a ver desaparecer cuando trabajemos dirigidos por el spec—.

Ya tenés el concepto. Antes de entrarle a la herramienta, vale la pena que sepas de dónde sale esta idea —y por qué no es una moda que se te va a pasar en seis meses—. ➡️
