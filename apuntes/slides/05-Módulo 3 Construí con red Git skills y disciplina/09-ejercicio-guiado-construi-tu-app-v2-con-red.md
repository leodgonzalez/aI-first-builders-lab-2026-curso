---
titulo: "Ejercicio guiado: Construí tu app v2 (con red)"
capitulo: "05-Módulo 3 Construí con red Git skills y disciplina"
orden: 9
source: "apuntes/slides/00-raw/05-Módulo 3 Construí con red Git skills y disciplina/09-Ejercicio guiado_ Construí tu app v2 (con red) – MUG.html"
source_sha256: e941f6d090a9f0e0
extraido: 2026-07-21
---

# Ejercicio guiado: Construí tu app v2 (con red)

Este es el **ejercicio grande del módulo**: volvés a construir tu app —la que en el módulo pasado hiciste a mano limpia, sin red— pero esta vez **desde tu PRD final y con todo el equipamiento puesto**. 🏗️ Ojo con el matiz, que es la clave del ejercicio: no vas a *retocar* la v1. Vas a **reconstruirla, mejor**, en tu repo nuevo, con red desde el primer commit. La diferencia entre aquella experiencia y esta es, exactamente, todo lo que aprendiste desde entonces.

Mirá con qué arrancás hoy, comparado con la v1:

- **Un repo con espejo en GitHub**: cada paso bueno se guarda y se sube; cada desastre se revierte. El «no hay vuelta atrás» quedó en el módulo pasado.
- Tu **`PRD.md` final** —generado con tu skill `create-prd` y curado por vos—, que le dice al agente qué construir.
- Tu `AGENTS.md` con su `CLAUDE.md`, el guardrail que fija las reglas de la casa.
- Tus **dos skills** (`create-prd` y `conventional-commit`), versionados y ya probados.
- Y la **experiencia de la v1**: ya construiste esto una vez; sabés dónde está el corazón de tu app y dónde se enrosca.

> ⚠️ **¿Y el código de la v1?** Sigue en su carpeta, y **ahí se queda**. Si querés espiarlo como referencia, dale —es tuyo—, pero **no lo copies en bloque al repo nuevo**: el punto del ejercicio es reconstruir desde el PRD con mejor método, no mudar código viejo. La v2 se escribe entera acá adentro, commit a commit.

Pensalo así: la v1 fue armar el mueble a pulso, sin banco de trabajo. Hoy tenés el taller completo: el plano afilado sobre la mesa, las herramientas a mano y un banco al que volver si un corte sale mal.

## 🎯 Qué vas a lograr

La meta es concreta: construir tu **app v2** —**las 1 a 3 features principales de tu PRD, funcionando y endurecidas** (la v1 tenía una sola, cruda)— viviendo en tu repo, con toda su historia commiteada **y pusheada a `main`**. Y tiene que ser así:

- **Más completa que la v1.** Lo que el PRD pide y la v1 no tenía, más sólido lo que quedaba atado con alambre.
- **Que corra.** Que la puedas abrir y ejecutar. Una app que «casi anda» no cuenta.
- **Con historia, y en la nube.** Al final, tu `git log` cuenta el viaje —un commit por cada funcionalidad que quedó andando— y tu repo de GitHub muestra exactamente lo mismo, porque cada commit cerró con su push.

Si al final podés mostrar esa versión andando —y la URL del repo que la respalda—, ganaste el ejercicio. Ese es el listón, ni más alto ni más bajo.

## 🛠️ Tu turno: paso a paso con Claude Code

⏱️ **Tiempo estimado:** ~2 a 4 hs (es el ejercicio grande del módulo) · 📦 **Entregable:** tu app v2 corriendo en tu repo, con su historia en Git — **se entrega la URL de tu repositorio de GitHub**.

Te dejo la secuencia con Claude Code. Cada paso es, en realidad, una técnica del módulo aplicada en su momento justo:

**1. Abrí tu repo con Claude Code.** Desde la terminal, parado en la carpeta nueva (la que tiene el PRD final, los guardrails y tus skills, con Git y GitHub ya configurados), escribí:

```
claude
```

El contexto ya está: no tenés que explicarle nada, el agente lee el guardrail solo.

**2. Plan-first: que proponga antes de tocar.** Igual que en la v1, no lo largues a codear de una. Pedile el plan primero y aprobalo. Copiá y pegá:

```
Leé @PRD.md. NO escribas código todavía. Quiero construir la app desde cero en este
repo: las features core del PRD (1 a 3 en total). Proponeme un plan corto, en pasos
chicos y en orden, agrupado por funcionalidad. Espero tu plan para aprobarlo antes
de que toques nada.
```

Leé el plan de verdad. Si encaró mal algo, corregilo **ahí**, en palabras, antes de que escriba una línea —es el checkpoint más barato que existe: un plan son palabras y se revisa en segundos; el código ya generado cuesta mucho más, y encima lo tenés que revisar igual—. Aprobar los planos antes de que se levante la pared, no después de verla parada en el lugar equivocado.

**3. Construí en pasos chicos, con el ritmo del módulo.** Recién con el plan aprobado, avanzá una cosa a la vez. Un pedido por paso, por ejemplo:

```
Dale, arranquemos por el paso 1 del plan: <la feature>. Implementalo siguiendo el
CLAUDE.md. Cuando termines, mostrame qué cambiaste y no sigas hasta que lo revise.
```

Y acá va la regla de oro de esta v2 —grabátela, porque es el ritmo del resto del curso—: **cada vez que una funcionalidad queda andando, commit y push a `main`.** Se lo pedís con palabras:

```
Esta funcionalidad quedó andando: commiteá y pusheá a main.
```

Tu skill `conventional-commit` le pone formato profesional al mensaje solo, y el push deja el avance visible en GitHub al instante. Cuando termines, tu repo en la nube va a contar la historia de la app **funcionalidad por funcionalidad**. Mientras avanzás, los otros hábitos vivos:

- **Cuidá el contexto:** mirá `/context` cada tanto y hacé `/clear` al cambiar de funcionalidad.
- **Test-first en la lógica clave:** pedile el test *antes* que la implementación para la pieza que importa (la que si falla, falla el producto).

**4. Si algo se enrosca, revertí.** No parchees sobre parches. Volvé al último commit bueno (*«volvé al último commit que funcionaba»* o `git restore .`) y replanteá con mejor contexto.

**5. Revisá antes de aceptar.** Cada vez que el agente te propone un cambio, leé el `git diff` antes de decir que sí —en la v1 no tenías esta lupa; usala—. Si no entendés qué hace un pedazo, no lo aceptes: pedile que te lo explique o que lo simplifique. Aceptar sin leer es el pecado capital.

**6. Cerrá contra el PRD y entregá.** Antes de dar por terminado, corré la app y chequeá: ¿arranca?, ¿se ejecuta sin explotar?, ¿muestra funcionando las 1 a 3 features del core que definiste en el PRD? Pedile el último push si quedó algo sin subir, abrí tu repo en GitHub y verificá que esté todo: la app, el PRD, los skills, la historia. **Esa URL es tu entrega** — pegala en la entrega de esta lección.

No es una lista de pasos sueltos: son los dos módulos de vibecoding funcionando juntos, en el orden en que se usan de verdad. Cada paso es una técnica que ya viste —acá la ponés a trabajar.

> ✅ **Lo lograste cuando** tu app v2 **arranca, corre y muestra el core del PRD** (1 a 3 features), en el historial hay **un commit por cada funcionalidad** que fue quedando andando, y **tu repo de GitHub está al día** — la URL que entregás abre y muestra la app completa, con su historia.

## 🪞 La reflexión (esta parte no la saltees)

Cuando termines, antes de cerrar la compu, parate un segundo y escribí dos respuestas honestas.

La primera: **¿qué cambió respecto de la v1?** Compará con aquellas notas de dolor: ¿revertiste algún desastre en segundos que antes te hubiera costado la tarde?, ¿el agente respetó tus reglas sin que se las repitas?, ¿los commits te dieron la tranquilidad de experimentar?, ¿reconstruir desde el PRD te salió más rápido y mejor que la primera vez? Eso que sentís es trabajar **con red** —no vuelvas atrás nunca—.

La segunda, y es la importante: **¿dónde sigue doliendo?** Porque ojo: la red no lo resuelve todo. Aun con Git y skills, la incomodidad de fondo del vibecoding sigue asomando, con señales como estas:

- Código que ya te cuesta entender cuando lo volvés a mirar.
- Decisiones que la IA tomó por vos sin que te dieras cuenta.
- Ese miedito a tocar algo porque no sabés qué se rompe.

Guardá esa sensación tal cual la sentiste, sin maquillarla. En la próxima lección le vamos a poner **nombre** —a ese muro y a los errores que lo construyen— porque entender lo que viviste es lo que te va a hacer un mejor builder. La incomodidad de hoy es la materia prima del aprendizaje que viene.

## 📦 Entrega del módulo

> El entregable de este módulo es **doble** —tu **PRD final** (regenerado con tu skill `create-prd` y curado por vos) y tu **app v2** corriendo— y se entrega con **una sola cosa: la URL de tu repositorio de GitHub**. Ahí adentro está todo: el PRD, los guardrails, tus dos skills, la app y la historia commit a commit. Pegá la URL en la entrega de esta lección.

Construiste tu app dos veces —cada vez con mejor método—. Ahora, la reflexión que le da sentido a todo lo que viene: los **anti-patterns y el muro de los 3 meses**. 👉
