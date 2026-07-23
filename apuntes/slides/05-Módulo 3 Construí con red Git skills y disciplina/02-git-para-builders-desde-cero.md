---
titulo: "Git para builders (desde cero)"
capitulo: "05-Módulo 3 Construí con red Git skills y disciplina"
orden: 2
source: "apuntes/slides/00-raw/05-Módulo 3 Construí con red Git skills y disciplina/02-Git para builders (desde cero) – MUG.html"
source_sha256: 9ed4901815a18a18
extraido: 2026-07-18
---

# Git para builders (desde cero)

¿Te acordás del momento de la v1 en que la IA te rompió algo que andaba… y no había vuelta atrás? Esta lección existe para que **eso no te pase nunca más**. Hablemos de la herramienta que te va a salvar la vida más de una vez: **Git**. 🛟 Y arranco con una promesa: aunque nunca lo hayas usado —aunque no vengas del mundo técnico—, en esta lección te vas a quedar tranquilo. No vamos a ver los cien comandos de Git ni a memorizar nada raro. Vamos a ver **los cinco que importan** y, sobre todo, la **idea** detrás, que es simple y poderosa —una vez que la agarrás, no la soltás más—. Si ya usás Git a diario, tratá esta lección como un repaso exprés: la práctica sobre tu proyecto llega en el ejercicio de acá a dos lecciones.

## 🎮 La idea en una imagen: los save points de un videojuego

Pensá en cualquier videojuego. Antes de entrar a la pelea difícil, **grabás la partida**. Si te va mal, no empezás todo de nuevo desde el primer nivel: **cargás desde el último punto guardado** y volvés a intentar, cuantas veces haga falta. Esa idea —tan simple, tan salvadora— es **exactamente** lo que hace Git con tu código.

Git es un **control de versiones**: un sistema que va guardando fotos de tu proyecto a lo largo del tiempo, para que **siempre puedas volver** a una versión que funcionaba. Cada foto queda ahí, esperándote. Nada se pierde, nada es irreversible: si algo sale mal, hay red abajo.

Y esto, cuando dirigís a una IA, deja de ser un lujo para volverse **imprescindible**. ¿Por qué? Porque tarde o temprano la IA va a alucinar y romper algo —te va a reescribir un archivo que andaba bien, o borrar una parte que necesitabas—, y en ese momento vos vas a querer tu save point a mano. Con Git, ese desastre es un susto de treinta segundos. Sin Git, puede ser una tarde perdida.

## 🗂️ Los tres nombres que vas a escuchar siempre

Con solo tres palabras ya entendés el 90% de las conversaciones sobre Git. No hace falta más para empezar:

- **Repositorio (repo):** es tu **carpeta de proyecto, pero con memoria**. Una carpeta normal solo tiene los archivos de hoy; cuando la convertís en repo, Git empieza a recordar toda su historia —cada cambio, cada versión, desde el día uno—. Es donde vive tu app y, de acá en más, todo lo que le pase.
- **Commit:** es un **punto guardado**. Cada vez que hacés un commit, Git saca una foto del proyecto en ese momento exacto y le pega una etiqueta con tu mensaje («agregué el login», «arreglé el bug de fechas»). Ese mensaje es tu recordatorio de qué había en esa foto. Es, ni más ni menos, tu save point.
- **GitHub:** es la **nube donde guardás una copia** de tu repo. Cumple dos funciones: sirve de respaldo (si se te rompe la compu o la perdés, tu código sigue a salvo en internet) y es el lugar desde donde compartís y colaborás con otros. La diferencia clave: Git vive en tu máquina; GitHub vive en internet. Y en este módulo lo vas a usar de verdad: tu repo nuevo se **da de alta en GitHub** y todo lo que construyas va a terminar subido ahí —de hecho, la entrega del módulo es la **URL de tu repo**—.

> 💡 Regla mental: **Git** es el sistema de save points; el **repo** es la partida guardada; el **commit** es cada punto de guardado; **GitHub** es el respaldo en la nube.

## 🧰 Los cinco comandos que de verdad usás

No te asustes con la terminal: son cinco líneas, nada más. Las vas a repetir tantas veces que en unos días te van a salir de memoria, sin pensarlas.

- **`git init`** — le dice a Git *«empezá a recordar esta carpeta»*. Lo corrés **una sola vez**, al principio de todo, y tu carpeta pasa a ser un repo. Después de eso, ya no lo tocás más.
- **`git add .` + `git commit -m "mensaje"`** — el **save point**. Van siempre juntos: `add` marca qué cambios querés guardar y `commit` los graba con un mensaje que explica qué hiciste. Este par es el que vas a usar todo el tiempo, cada vez que llegues a un punto que querés conservar.
- **`git diff`** (y `git status`) — te muestra **qué cambió** desde el último commit: qué líneas agregaste, cuáles borraste, qué tocaste. Es tu ventana para revisar antes de guardar. Regla de oro: nunca guardes a ciegas.
- **`git restore .`** — el **superpoder**: descarta los cambios de los archivos ya versionados y te devuelve al último punto guardado. Es «cargar la partida». Cuando la IA rompe algo, este comando es tu botón de pánico —el que te devuelve la calma—. (Ojo: sobre archivos que todavía no están en ningún commit no actúa; para el resto, es tu vuelta atrás.)
- **`git push`** — **sube tus commits a GitHub**. Los save points viven en tu máquina; el push manda la copia a la nube. En este curso el ritmo va a ser siempre el mismo: **funcionalidad lista → commit → push directo a `main`** (así se llama la rama principal del repo). Se configura una sola vez, en el próximo ejercicio; después es una palabra.

Con eso alcanza para todo este módulo. En serio, no exagero. Todo lo demás lo vas a ir aprendiendo cuando lo necesites, no antes: nadie aprende Git entero de golpe, ni falta.

## 🤝 Y lo mejor: el agente lo maneja por vos

Acá va la buena noticia para el que se puso nervioso con la terminal: en la práctica, **muchas veces ni siquiera vas a tipear estos comandos**. Le decís al agente *«commiteá esto con un mensaje claro»* o *«volvé al último commit que funcionaba»* y lo hace él por vos, sin que toques una tecla.

Pero —y esto es lo clave— **necesitás entender qué está pasando** para dirigirlo bien y para saber cuándo pedírselo. No es lo mismo apretar botones sin saber qué hacen que dar una orden entendiendo exactamente el efecto. Pensalo así: entender Git es lo que te deja **dirigir** el proceso en vez de rezar para que salga bien.

## 💻 Un atajo cómodo: mirá todo desde VS Code

Toda esta historia —los archivos, los cambios, el historial de commits— se ve **mucho más cómoda desde un editor visual** que desde la terminal pelada, sobre todo si recién arrancás. Para eso está **VS Code**, que ya instalaste en *Prepará tu entorno*.

El truco para abrirlo en tu proyecto es un comando cortito. Parado en la carpeta de tu proyecto, en la terminal, escribí:

```
code .
```

Es literalmente `code`, un **espacio**, y un **punto**. Ese punto significa «la carpeta actual», así que el comando le dice a VS Code *«abrí todo lo que hay acá»*. En segundos tenés el proyecto entero adentro del editor:

- En el panel de la **izquierda** ves todos tus archivos, para navegarlos con un clic.
- En la pestaña de **control de versiones** (el iconito de las ramitas) ves, en verde y rojo, exactamente qué cambió desde el último commit —el mismo `git diff` de recién, pero coloreado y clickeable— y podés commitear con un botón.

No reemplaza entender los comandos (eso sigue siendo tuyo), pero los vuelve mucho más fáciles de *ver*. Cuando llegue el ejercicio, si te sentís más cómodo mirando los cambios en VS Code, dale para adelante.

### 🔎 La muestra: TicketTriage bajo control

Para que veas a dónde va esto, así arranca la historia del repo de **TicketTriage**. Acordate del modelo del módulo: es una **carpeta NUEVA** —no la de la v1— a la que solo viajaron el `PRD.md`, el `AGENTS.md` y el `CLAUDE.md`:

```
git init                                              # la carpeta nueva ahora recuerda
git add . && git commit -m "estado inicial: PRD + guardrails"
git push                                              # ...y la copia queda en GitHub
# ... y de acá en más, una foto por cada paso que funciona ...
```

Fijate que el primer commit es **liviano**: dos documentos, ni una línea de código. Es a propósito: la app **se reconstruye acá adentro**, con red desde el primer minuto —cada paso de la v2 nace ya versionado, algo que tu v1 nunca tuvo—.

Cada commit es un punto seguro al que volver. Con esto abajo, ya podés dejar que la IA experimente sin miedo: total, siempre tenés a dónde regresar.

Y ojo que **todavía no te pido que toques nada**: esto mismo lo vas a hacer con **tu** proyecto en el próximo ejercicio, *Prepará tu proyecto*. Antes hay una lección corta pero decisiva: los comandos ya los tenés; falta el **método** con el que un builder los usa mientras dirige a la IA. Eso es **iterar con red**. ➡️
