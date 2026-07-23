---
titulo: "Prompting profesional: tu arsenal para cualquier IA"
capitulo: "04-Módulo 2 Vibecoding profesional"
orden: 9
source: "apuntes/slides/00-raw/04-Módulo 2 Vibecoding profesional/09.Prompting profesional_ tu arsenal para cualquier IA – MUG.html"
source_sha256: bd325e5201476349
extraido: 2026-07-16
---

# Prompting profesional: tu arsenal para cualquier IA

Antes de cerrar el módulo, quiero regalarte la lección más *reutilizable* de todas —una que vas a seguir usando mucho después de que termine el curso—. En la L3 viste los fundamentos del prompting para código; acá te doy el **arsenal completo**: las estrategias que usan los profesionales para sacarle a una IA respuestas que parecen de otro nivel. 🎯

Y ojo con esto, porque es la 
clave: **estas técnicas no son para código ni para Claude Code solamente.** Funcionan igual contra ChatGPT, Claude, Gemini, Copilot o la IA que salga el mes que viene, y sirven para *cualquier* cosa —redactar un mail difícil, resumir un contrato, planear un viaje, estudiar—. La diferencia entre una respuesta mediocre y una brillante casi nunca está en el modelo: está en **cómo preguntás**. Guardate esta lección; es de las que cambian tu día a día.

Una aclaración para bajar la ansiedad: **no hay palabras mágicas.** Un buen prompt es pensamiento claro, ordenado. Nadie usa las diez técnicas de golpe: agarrás las que la tarea pide. Vamos con ellas.

## 🎭 1. Dale un rol (y para quién)

La más famosa —la que repiten todos— pero casi siempre a medias. No alcanza con *«actuá como experto en finanzas»*. Un rol rinde cuando le sumás **para quién** y **con qué objetivo**:

- ❌ *«Explicame los fondos comunes de inversión.»*
- ✅ *«Actuá como un asesor financiero explicándole a alguien que nunca invirtió y le tiene miedo al tema. Usá analogías de la vida diaria, cero jerga, y terminá con un ejemplo concreto con números chicos.»*

El rol enfoca el *tono* y el *nivel*; el «para quién» evita que te hable como a un colega cuando necesitabas algo simple (o al revés).

## 🎯 2. Sé específico y pedí el formato de salida

La IA rellena todo hueco que dejes con lo que se le ocurre. Cerralos vos: decí exactamente qué querés y **en qué forma** lo querés (tabla, lista, JSON, un párrafo, 100 palabras, tal tono).

- ❌ *«Dame ideas de nombres para mi app.»*
- ✅ *«Dame 10 nombres para una app de gestión de tickets de soporte. Que sean cortos (una o dos sílabas), fáciles de pronunciar en español, y sin guiones. Devolvémelos en una tabla con dos columnas: nombre y por qué funciona.»*

Pedir el formato no es un detalle estético: una respuesta con la forma que necesitás te ahorra el trabajo de reordenarla después.

## 📎 3. Dale el contexto que vos tenés en la cabeza (y la IA no)

Vos sabés el trasfondo; la IA no adivina. Contale el para qué, lo que ya probaste, las restricciones, quién lo va a leer.

- ❌ *«¿Cómo respondo este mail?»*
- ✅ *«Un cliente importante me escribió enojado porque su pedido llegó tarde por segunda vez. Necesito una respuesta que se haga cargo del error, no suene a plantilla, ofrezca una solución concreta y lo retenga como cliente. Tono cercano pero profesional, máximo 6 líneas.»*

Regla de oro: si tuvieras que explicarle la situación a un colega nuevo para que te ayude, esa explicación es el contexto que le falta a la IA.

## 🧩 4. Con ejemplos (few-shot) o sin ejemplos (zero-shot)

Dos modos, y saber cuándo usar cada uno te distingue:

- **Zero-shot** — pedir directo, sin ejemplos. Sirve para tareas comunes y claras: *«traducime esto al inglés»*, *«resumí este texto en 3 bullets»*.
- **Few-shot** — mostrarle **uno a tres ejemplos** de entrada → salida antes de tu pedido real. Es la técnica más subestimada, y la que más sube la calidad cuando querés un **formato o estilo consistente**. La IA imita tus ejemplos mejor de lo que sigue cualquier descripción.

Un few-shot se ve así:

```
Convertí títulos en slugs de URL. Ejemplos:
"Cómo armar un PRD" → como-armar-un-prd
"IA para todos, 2026" → ia-para-todos-2026
Ahora convertí: "Vibecoding: la guía definitiva"
```

Un ejemplo bien elegido vale más que un párrafo de instrucciones. Si te cuesta *describir* lo que querés, **mostralo**.

## 🪜 5. Pedile que piense paso a paso

Para tareas que requieren razonar —un problema con lógica, una decisión con varios factores, algo de matemática—, agregá una frase mágica de verdad: **«pensá paso a paso antes de darme la respuesta final.»**

¿Por qué funciona? Porque la obligás a *mostrar el razonamiento* en vez de tirar la primera conclusión que le sale, y en ese proceso se corrige sola. Es la diferencia entre una respuesta impulsiva y una pensada.

- ❌ *«¿Me conviene el plan A o el B?»*
- ✅ *«Compará el plan A y el plan B para mi caso. Pensá paso a paso: listá los pros y contras de cada uno según mis necesidades, y recién al final dame tu recomendación con el porqué.»*

## 🔗 6. Partí lo grande en pasos (no pidas todo junto)

Un pedido gigante («hacé toda la campaña de marketing») devuelve algo genérico y flojo. Los profesionales **encadenan**: una tarea por prompt, usando la salida de una como entrada de la siguiente.

- Primero: *«Ayudame a definir el público objetivo de este producto.»*
- Después: *«Con ese público, proponé 3 ángulos de mensaje.»*
- Después: *«Tomá el ángulo 2 y escribí 5 títulos.»*

Cada paso es chico, revisable y corregible. Además te deja **dirigir** —ajustás el rumbo entre paso y paso— en vez de recibir un mamotreto y tener que rehacerlo entero.

## 🚧 7. Poné límites: decí qué NO querés

Tan importante como pedir es prohibir. Lo que no aclarás, la IA lo asume permitido.

- *«…sin usar tecnicismos.»*
- *«…no inventes datos: si no sabés algo, decímelo.»*
- *«…no cambies el resto del texto, tocá solo el título.»*

Un buen «no» te ahorra tres vueltas de corrección.

## 📐 8. Separá tus instrucciones de los datos

Cuando le pasás un texto para que **procese** (resumir, corregir, traducir), separalo claramente de la instrucción, para que no confunda una cosa con la otra. Usá comillas triples, o un rótulo:

```
Resumí en 3 bullets el texto que está entre comillas. NO agregues opiniones.

"""
(acá pegás el texto largo)
"""
```

Sin esa separación, la IA a veces «obedece» frases que estaban *dentro* del texto que querías resumir. Con ella, sabe qué es orden y qué es material.

## 🔁 9. Iterá y hacela auto-corregirse

El primer resultado es un borrador, no la palabra final. Dos jugadas potentes:

- **Refinar:** *«Está muy largo, dejalo en la mitad y más directo.»* Cada vuelta lo acerca a lo que querías.
- **Auto-crítica:** *«Revisá tu propia respuesta, marcá 3 cosas que podrían estar mejor y reescribila corrigiéndolas.»* La IA es sorprendentemente buena encontrándose los errores… si se lo pedís.

## ❓ 10. Hacé que te pregunte antes de responder

La joya para tareas ambiguas o importantes —la misma que usaste al armar tu `AGENTS.md`—: en vez de dejar que adivine, invertí el orden.

> *«Antes de responder, hacéme todas las preguntas que necesites para darme la mejor respuesta posible.»*

De golpe la IA saca a la luz los diez supuestos que iba a inventar, vos los aclarás, y la respuesta sale a tu medida. Contraintuitivo y buenísimo.

## 🧪 La receta base (para tener a mano)

No necesitás las diez siempre, pero cuando algo importa, este molde mental cubre casi todo:

> **[Rol] + [Contexto] + [Tarea específica] + [Formato de salida] + [Restricciones] + [Ejemplo, si tenés]**

Mirá el salto en un caso real, el mismo pedido pobre y pro:

- ❌ *«Escribime un posteo para LinkedIn sobre mi curso.»*
- ✅ *«Actuá como community manager. Escribí un posteo de LinkedIn para anunciar mi curso de IA para desarrolladores (arranca en junio, 100% práctico). Público: devs con experiencia curiosos por la IA. Tono cercano y con energía, nada corporativo. Máximo 120 palabras, con un gancho fuerte en la primera línea y 3 hashtags al final. No uses emojis en exceso (máximo 2).»*

El segundo no le deja nada al azar —y por eso vuelve casi listo para publicar—.

## 🧭 Bonus para Claude Code: el «pensá antes» hecho botón — Plan Mode

Cierro con un bonus que conecta este arsenal con tu herramienta de todos los días. ¿Notaste que varias técnicas de la lista van de lo mismo —hacer que la IA **piense y proponga antes de ejecutar** (la 5, la 6, la 10)—? ¿Y te acordás de que en el ejercicio de la app le pediste el plan en palabras antes de dejarla tocar código? Bueno: **Claude Code tiene esa jugada incorporada como feature**, y se llama **Plan Mode**.

Lo activás apretando **Shift+Tab** (hasta que diga *plan mode*): el agente entra en un modo de **solo lectura** —investiga tu código, razona, te propone un plan paso a paso— pero **no puede modificar un solo archivo** hasta que vos apruebes el plan. Es exactamente el hábito que ya practicaste, con una diferencia importante: cuando lo pedís por prompt, confiás en que el agente se aguante las ganas; en Plan Mode **no puede** tocar nada aunque quiera. El checkpoint más barato del mundo, ahora con cinturón de seguridad.

¿Cuándo usarlo? Ante cambios grandes, tareas que tocan varios archivos, o cuando todavía no confiás en cómo formulaste el pedido. Aprobás el plan → el agente ejecuta → vos revisás. De acá en adelante en el curso lo vas a usar seguido; ya sabés qué es y por qué existe.

## 🌐 Lo mejor de todo

Cerramos donde empezamos: **este arsenal es tuyo para siempre y sirve en cualquier lado.** No depende de Claude Code ni de este curso. La próxima vez que le pidas algo a *cualquier* IA y la respuesta venga floja, no le eches la culpa al modelo: volvé a esta lista y fijate cuál de las diez te faltó. Casi siempre es una.

Con esto en el bolsillo, vamos al **repaso del módulo** para fijar todo lo que construiste. ➡️
