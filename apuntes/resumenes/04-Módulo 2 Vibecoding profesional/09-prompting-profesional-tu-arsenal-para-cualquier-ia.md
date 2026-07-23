---
titulo: "Prompting profesional: tu arsenal para cualquier IA"
capitulo: "04-Módulo 2 Vibecoding profesional"
orden: 9
leccion: "apuntes/slides/04-Módulo 2 Vibecoding profesional/09-prompting-profesional-tu-arsenal-para-cualquier-ia.md"
---

# Prompting profesional: tu arsenal para cualquier IA

## De qué trata

Cierre del Módulo 2 y la lección más **transversal** del curso: no es sobre código ni sobre
Claude Code. Son 10 técnicas de prompting que funcionan contra cualquier IA (ChatGPT,
Gemini, Copilot, la que salga) y para cualquier cosa — un mail difícil, un contrato, un viaje.

La tesis: **la diferencia entre una respuesta mediocre y una brillante casi nunca está en el
modelo, está en cómo preguntás.**

Y la aclaración que baja la ansiedad: **no hay palabras mágicas.** Un buen prompt es
pensamiento claro y ordenado. Nadie usa las diez juntas; agarrás las que la tarea pide.

## Las 10 técnicas

| # | Técnica | La clave |
|---|---|---|
| 1 | **Rol** | No alcanza "actuá como experto": sumá **para quién** y **con qué objetivo**. El rol fija tono y nivel. |
| 2 | **Especificidad + formato** | La IA rellena todo hueco que dejes. Pedí la forma exacta (tabla, JSON, 100 palabras). |
| 3 | **Contexto** | Si se lo explicarías a un colega nuevo, eso es lo que le falta a la IA. |
| 4 | **Zero-shot vs few-shot** | 1 a 3 ejemplos entrada→salida. La más subestimada: imita ejemplos mejor que descripciones. |
| 5 | **Paso a paso** | "Pensá paso a paso antes de la respuesta final" — la obliga a razonar y se corrige sola. |
| 6 | **Encadenar** | Una tarea por prompt, la salida de una alimenta la siguiente. Te deja dirigir entre paso y paso. |
| 7 | **Límites (qué NO)** | Lo que no prohibís, se asume permitido. Un buen "no" ahorra tres vueltas. |
| 8 | **Instrucciones ≠ datos** | Separá con `"""`, si no "obedece" frases que estaban dentro del texto a procesar. |
| 9 | **Iterar / auto-crítica** | El primer output es borrador. "Marcá 3 cosas mejorables y reescribila." |
| 10 | **Que pregunte primero** | "Antes de responder, hacéme todas las preguntas que necesites." Saca a la luz los supuestos que iba a inventar. |

## La receta base

> **[Rol] + [Contexto] + [Tarea específica] + [Formato] + [Restricciones] + [Ejemplo, si tenés]**

Pobre vs pro, mismo pedido:

- ❌ *«Escribime un posteo para LinkedIn sobre mi curso.»*
- ✅ *«Actuá como community manager. Escribí un posteo de LinkedIn para anunciar mi curso de
  IA para desarrolladores (arranca en junio, 100% práctico). Público: devs con experiencia
  curiosos por la IA. Tono cercano y con energía, nada corporativo. Máximo 120 palabras, con
  un gancho fuerte en la primera línea y 3 hashtags al final. No uses emojis en exceso
  (máximo 2).»*

## El bonus que conecta todo: Plan Mode

Las técnicas 5, 6 y 10 van de lo mismo: **que piense y proponga antes de ejecutar**. Claude
Code lo tiene como feature — **Plan Mode**, con `Shift+Tab`.

La diferencia con pedirlo por prompt: ahí confiás en que el agente se aguante las ganas; en
Plan Mode **no puede** tocar un archivo aunque quiera. Es solo lectura hasta que aprobás.

Cuándo: cambios grandes, tareas que tocan varios archivos, o cuando no confiás en cómo
formulaste el pedido.

## El cierre

Cuando una respuesta venga floja, **no le eches la culpa al modelo**: volvé a la lista y
fijate cuál de las diez te faltó. Casi siempre es una.

## Nota propia

La técnica 10 tiene un reverso: preguntar es la joya **para tareas ambiguas**. Si el pedido
ya venía claro, preguntar no agrega — estorba. Calibrar cuándo *no* preguntar es parte de la
técnica.
