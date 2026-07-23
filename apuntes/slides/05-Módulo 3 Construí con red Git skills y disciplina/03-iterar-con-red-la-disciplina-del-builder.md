---
titulo: "Iterar con red: la disciplina del builder"
capitulo: "05-Módulo 3 Construí con red Git skills y disciplina"
orden: 3
source: "apuntes/slides/00-raw/05-Módulo 3 Construí con red Git skills y disciplina/03-Iterar con red_ la disciplina del builder – MUG.html"
source_sha256: f0f62b28892e27e3
extraido: 2026-07-18
---

# Iterar con red: la disciplina del builder

En la lección anterior conociste Git —los save points, los cuatro comandos, el alivio de deshacer—. Tenés la herramienta. Lo que falta ahora es algo menos vistoso pero igual de decisivo: el **ritmo y la disciplina** con que un builder la usa. Porque vibecodear rápido sin red es la receta perfecta para acelerar derecho contra un paredón. En esta lección instalamos la disciplina que te deja ir rápido **sin** acumular un desastre. 🛟

## 🪢 Git como red de seguridad: de los comandos a los hábitos

Ya sabés *qué* hace cada comando; acá va *cómo* los usa un builder. Cuando dirigís a una IA, tarde o temprano va a **alucinar** y romper algo —no es un «si», es un «cuándo»—. La diferencia entre que eso sea un sustito de dos minutos o una tarde perdida la hacen tres hábitos:

- **Commit-as-checkpoint.** Cada vez que algo funciona, commiteás —son los *save points* que viste en la lección anterior, ahora convertidos en hábito—. No esperás a «terminar la feature»: cada estado bueno es un punto seguro al que podés volver. Cuanto más seguido commiteás, más finita es la distancia entre «se rompió» y «estoy sano de nuevo». Y cuando tu repo viva en GitHub (próximo ejercicio), el hábito se completa: **cada funcionalidad terminada cierra con su push a `main`** — checkpoint local + respaldo en la nube, siempre.
- **Revertir en vez de parchar.** Si el agente se mandó una macana, no te pongas a arreglar el desastre encima: eso suele empeorarlo, porque terminás apilando fixes sobre un código que ya salió torcido. Volvé atrás con `git restore` a tu último commit bueno y reintentá desde ahí, limpio. Casi siempre es más rápido reconstruir sobre una base sana que desenredar una podrida.
- **Diffs chicos.** Revisá `git diff` *antes* de aceptar. Un cambio chico se revisa de un vistazo; uno gigante esconde problemas que se te van a colar entre líneas y líneas que «parecen bien». Además, si algo falla después, el culpable está en un diff acotado y no en una avalancha de cambios donde no sabés ni por dónde empezar a mirar.

> 🧠 La frase para tatuarte: **poder deshacer una alucinación es la red de seguridad definitiva.** Con Git debajo tuyo, dejás que la IA pruebe, se equivoque y experimente sin que te dé miedo, porque sabés que el camino de vuelta está a un comando de distancia.

## 🥾 El ritmo del builder

Con la red puesta, el ritmo se vuelve casi natural, y se sostiene en tres movimientos:

- **Pasos chicos.** Una cosa a la vez, en vez de pedir «construime toda la app» y rezar. Cada paso chico es acotado, verificable y fácil de revertir si sale mal.
- **Verificá seguido.** Corré, probá, mirá después de cada paso, en lugar de apilar diez cambios sin chequear ninguno. Verificar temprano significa que cuando algo se rompe, se rompió *recién*, y sabés exactamente dónde.
- **Revisá siempre.** Mirá el output antes de aceptarlo —sí, otra vez el intern poderoso pero no confiable; te lo voy a repetir hasta que sea reflejo—. Aceptar sin leer es firmar un documento sin haberlo leído: funciona hasta que un día no.

Este ritmo no te hace más lento: te hace más rápido en serio, porque evitás las vueltas largas de «¿en qué momento se rompió todo esto?». El tiempo que parece que «perdés» verificando lo recuperás con creces cuando *no* tenés que arqueologiar un bug enterrado bajo diez cambios.

## 🛑 Saber cuándo frenar

Cierro con una señal de madurez que cuesta aprender: saber **cuándo dejar de insistir**. Si vas tres vueltas y el agente se enrosca cada vez peor, parcheando sobre parches, no sigas tirando prompts encima del lío. Frená. `git restore` al último estado bueno, replanteá el pedido desde cero —mejor contexto, mejor prompt, quizás partir el problema en dos— y arrancá limpio.

El instinto natural es el contrario: «una más y sale». Pero cuando el agente ya perdió el rumbo, cada prompt extra suma ruido en vez de acercarte. Insistir sobre un rumbo torcido no es perseverancia, es acumular deuda mientras te convencés de que estás «acelerando». Es como cavar más hondo para salir de un pozo. El builder experimentado reconoce ese momento —esa sensación de estar remando en dulce de leche— y resetea sin culpa: volver a empezar con mejor contexto casi siempre es más corto que rescatar el intento fallido.

### 🔎 La muestra: TicketTriage

Mientras construíamos el clasificador, el ritmo se ve así en el historial de Git:

```
git commit -m "feat: endpoint POST /tickets con validación de asunto"   # anda → checkpoint
git commit -m "feat: clasificación con IA (categoría + prioridad)"      # anda → checkpoint
# el agente alucina al tocar el borrador y rompe el endpoint:
git restore .                                                            # vuelvo al último checkpoint, sin drama
```

Cada commit es un punto seguro; revertir una alucinación es un comando, no una tarde perdida.

Ya tenés el ritmo y la red — por ahora, en la cabeza. Toca pasarlas a las manos: en el **próximo ejercicio** nace la **carpeta nueva de tu proyecto** —la que se convierte en repo Git, con su espejo en GitHub—, hacés tus primeros commits y push de verdad y probás el botón de pánico sobre tus archivos reales. ➡️
