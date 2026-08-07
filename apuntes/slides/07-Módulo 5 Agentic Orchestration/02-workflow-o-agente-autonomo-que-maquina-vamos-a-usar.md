---
titulo: "Workflow o agente autónomo: qué máquina vamos a usar"
capitulo: "07-Módulo 5 Agentic Orchestration"
orden: 2
source: "apuntes/slides/00-raw/07-Módulo 5 Agentic Orchestration/02-Workflow o agente autónomo_ qué máquina vamos a usar – MUG.html"
source_sha256: 796357c57a09ed42
extraido: 2026-08-04
---

# Workflow o agente autónomo: qué máquina vamos a usar

Antes de mirar ninguna herramienta hay una decisión de arquitectura que tomar, y es de esas que definen todo lo que viene después. La buena noticia es que se resuelve en cinco minutos. La mala es que **si no la tomás explícitamente, la tomás igual** — por omisión, agarrando lo primero que encontrás — y ahí casi siempre sale mal. 🔀

Te pongo la escena, porque seguro te suena. Alguien del equipo instala una herramienta agéntica nueva, le tira un ticket, y la cosa se va sola veinte minutos, toca catorce archivos y vuelve con algo que **parece** andar. La sensación es de magia. Y funciona… tres veces. A la cuarta hace algo que nadie pidió, en un archivo que nadie esperaba, y cuando querés reconstruir qué pasó no hay forma: no quedó rastro, solo un diff enorme y una conversación de doscientos mensajes. Nadie eligió que fuera así. Simplemente **nadie eligió**.

## 📖 Las dos formas de poner un agente a trabajar

La distinción que ordena todo esto la formuló **Anthropic** en *Building effective agents*, y conviene hacerla tuya porque te sirve para leer cualquier producto del mercado — incluso los que no te la explican:

- **Workflow** — el sistema recorre **caminos predefinidos**. *Vos* decidís cuáles son los pasos y en qué orden; el modelo se encarga de completarlos. La inteligencia está adentro de cada paso, pero la secuencia la pusiste vos.
- **Agente autónomo** — el modelo **dirige su propio proceso**: decide qué pasos dar, en qué orden y con qué herramientas, y va corrigiendo el rumbo según lo que encuentra. Vos le das un objetivo; el camino lo arma él.

Parece una sutileza académica. No lo es: cambia **todo lo que podés esperar del sistema**, y sobre todo cambia qué podés prometerle a alguien más.

Ubiquemos lo que ya conocés, que es la forma más rápida de que la distinción se vuelva concreta. **Spec Kit**, el del Módulo 4, está a mitad de camino: hay pasos definidos con nombre y artefactos —specify, plan, implement— así que en el papel es un workflow. Pero el que dispara cada paso sos vos, y no hay ninguna condición que se verifique entre uno y otro. Es un workflow **en la intención**, no en la ejecución: si un día corrés `implement` sin haber corrido `plan`, la herramienta no se entera. En el otro extremo está eso de «le tiro un issue de GitHub y vuelve con un pull request»: ahí el modelo eligió absolutamente todo, incluido si valía la pena hacer el trabajo.

## ⚖️ El trade-off, sin el marketing encima

Acá quiero ser honesto, porque la industria empuja fuerte para el lado de la autonomía y conviene tener el criterio propio armado antes de que te lo armen.

**No hay una mejor.** Hay un eje entre **autonomía** y **previsibilidad**, y es un eje de suma cero: lo que ganás de un lado lo perdés del otro.

- **Más autonomía** te compra capacidad de resolver **lo imprevisto**. Un agente que decide su proceso puede encarar un problema que vos no anticipaste, buscar por caminos que no se te habían ocurrido y adaptarse cuando la realidad no coincide con el plan. Y te cobra, a cambio, **saber qué va a pasar**: dos corridas del mismo pedido pueden tomar caminos distintos y llegar a resultados distintos, los dos defendibles.
- **Más rieles** te compran **repetibilidad y auditoría**. Sabés qué va a pasar, en qué orden, y podés reconstruir después por qué pasó lo que pasó. Y te cobran **flexibilidad**: frente a algo que el diseño no contempló, el sistema se traba en vez de improvisar, y tenés que meter mano.

Fijate que ninguna de las dos columnas es «la buena». Por eso la pregunta correcta no es *«¿cuál es mejor?»* sino ***«¿qué necesito para esta tarea puntual: que resuelva lo inesperado, o que sea confiable y repetible?»***

Y esa pregunta tiene respuestas distintas el mismo día. Investigar por qué se cae un endpoint en producción pide autonomía: no sabés dónde está el problema, y el valor está justamente en que el agente explore lugares que vos no pensaste. Agregar el cuarto endpoint del mismo CRUD pide rieles: sabés perfectamente qué tiene que pasar y querés que pase igual que las tres veces anteriores.

## 📏 En la práctica es un espectro

Binario es una simplificación útil para entender la idea, pero cuando mirás herramientas reales vas a encontrar cinco niveles. Te dejo la escala completa para que puedas ubicar cualquier cosa que te crucen:

1. **Prompt suelto** — un pedido, una respuesta. Sin proceso ni memoria.
2. **Chain (encadenamiento)** — pasos fijos en orden fijo; la salida de uno es la entrada del siguiente. Muy previsible y muy rígido.
3. **Router** — un paso de clasificación decide a qué rama va el pedido. Sigue siendo predefinido, pero con caminos alternativos según el caso.
4. **Workflow orquestado con gates** — fases predefinidas, con **condiciones verificables** para pasar de una a otra y memoria de dónde está parado. ⬅️ *acá vamos nosotros*
5. **Agente autónomo con herramientas** — objetivo + caja de herramientas, y decide todo lo demás.

La diferencia entre el 3 y el 4 es la que más se subestima, y es toda la diferencia. En el 3 hay pasos ordenados. En el 4 hay **condiciones que se chequean** — o sea, el sistema puede decir «todavía no».

## 🎯 Por qué en este curso vamos con workflow

Porque estamos **construyendo software que otra gente va a usar**, y ahí necesitás tres cosas que un agente suelto no te puede dar:

- **Que el mismo pedido produzca el mismo proceso** el martes y el jueves. Si cada corrida improvisa, no tenés un proceso: tenés una lotería con buen promedio. Y una lotería con buen promedio es imposible de mejorar, porque no sabés qué cambiar.
- **Poder auditar qué pasó.** Cuando algo sale mal —y va a salir mal— necesitás reconstruir la cadena de decisiones: qué se pidió, qué se decidió, qué se verificó. Un workflow deja ese rastro por diseño; con un agente autónomo tenés un log de acciones que hay que interpretar como si fuera arqueología.
- **Poder poner condiciones no negociables.** «No se escribe código sin spec aprobado» solo tiene sentido si existe un lugar donde ponerla que el modelo no pueda ignorar. En un agente autónomo ese lugar es el prompt — y ya vas a ver, en un par de lecciones, cuánto vale una regla que vive en el prompt.

Dicho al revés, para que no suene a que el agente autónomo es el malo de la película: para **explorar** —investigar un bug raro, prototipar una idea, entender un codebase ajeno— el agente suelto sigue siendo la mejor herramienta que hay, y sería una tontería atarlo. La distinción no es «bueno y malo», es **explorar versus producir**.

## 🚫 El malentendido que hay que sacarse de encima ya

Mucha gente escucha «workflow con gates» y entiende «le até las manos al agente para que no haga desastres». **Es exactamente al revés, y vale la pena entender por qué.**

Dentro de cada paso el agente sigue siendo tan autónomo y creativo como siempre. Si le tocó implementar un bloque, decide la estructura, elige los nombres, resuelve los casos borde, te propone alternativas que no habías pensado y discute con vos si algo del spec no cierra. Nada de eso cambia. Lo que fijás **no es el *cómo* se resuelve cada paso, sino el *orden* de los pasos y las *condiciones* para avanzar de uno al siguiente**.

> 🚄 Son **rieles, no correa corta.** El tren va a toda velocidad y con toda su potencia; lo único que no puede es irse por el campo.

Y hay un corolario que conviene decir de una vez, porque es lo que separa un diseño maduro de uno rígido: **un buen workflow tiene lugares donde deja suelto al agente a propósito**.

Pensalo así. La etapa en la que todavía no sabés qué querés construir —explorar una idea de producto, ver qué features tendría sentido tener— es justamente aquella en la que la improvisación **aporta**. Meterle gates ahí sería contraproducente: estarías pidiéndole condiciones verificables a una etapa cuyo valor es no tener el resultado predefinido. Cuando veamos el pipeline por dentro vas a encontrar un modo específico para eso, sin fases estrictas. No es una inconsistencia del diseño: **es el diseño reconociendo dónde no conviene poner rieles**.

Diseñar bien un pipeline es, en buena medida, saber **dónde poner riel y dónde no**.

## 💡 Para aplicar

Agarrá las tareas que hacés con IA en una semana típica y separalas en dos listas: **«acá quiero exploración»** y **«acá quiero repetibilidad»**.

La segunda lista es la que merece un pipeline. Y el tamaño relativo de las dos te dice algo útil: si tenés diez tareas en la primera y dos en la segunda, montar una máquina pesada sería un error. Si es al revés, ya estás pagando en desprolijidad lo que no invertiste en proceso.

Decisión tomada: **workflow con gates**. Ahora sí, la máquina concreta con la que vas a trabajar los próximos tres módulos. ➡️
