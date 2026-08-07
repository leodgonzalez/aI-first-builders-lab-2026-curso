---
titulo: "Los gates de seguridad: threat modeling y SAST"
capitulo: "07-Módulo 5 Agentic Orchestration"
orden: 10
source: "apuntes/slides/00-raw/07-Módulo 5 Agentic Orchestration/10-Los gates de seguridad_ threat modeling y SAST – MUG.html"
source_sha256: 118138cd22a7f450
extraido: 2026-08-07
---

# Los gates de seguridad: threat modeling y SAST

En el gráfico de DAW hay dos gates que todavía no miramos de cerca: `gates.threat` al salir de PLAN y `gates.sast` al salir de CODE. No están ahí de adorno, y esta lección es para que entiendas por qué la seguridad **tiene que ser un gate del pipeline** y no una revisión de después. 🛡️

Y quiero encuadrarlo bien, porque el tema arrastra fama de aburrido: esto no es compliance ni un checkbox para quedar bien. Es que en un flujo AI-First la seguridad es exactamente **el tipo de cosa que se posterga hasta que es tarde** — y ahora se posterga más rápido que nunca.

## 📉 El problema, con datos

El estudio de **Veracode de 2025** encontró que alrededor del **45%** de las tareas de generación de código evaluadas produjeron código con vulnerabilidades conocidas. Casi una de cada dos.

Ahora, ojo con la lectura fácil, porque la conclusión importa: **no es que el modelo sea descuidado**. Es que el modelo **optimiza por que funcione**, y «que funcione» y «que sea seguro» **no son lo mismo**.

Pensalo con un caso concreto. Le pedís un endpoint que devuelva los datos del usuario. Te lo escribe y anda perfecto: le pasás un ID, devuelve los datos. Que devuelva los datos de *cualquier* usuario si le cambiás el ID **también «funciona»** — cumple exactamente lo que le pediste. El modelo no tiene forma de saber cuál de las dos cosas querías, salvo que alguien lo haya pensado antes y lo haya dicho.

Y a eso sumale la variable nueva: **ahora generás mucho más rápido**. La velocidad no crea el problema, lo **amplifica** — en las dos direcciones. Sin controles, generás vulnerabilidades a la misma velocidad a la que generás features.

## 🚪 Por qué gate, y no «lo reviso después»

Acá se junta todo lo que venís viendo en el módulo.

Si la revisión de seguridad es *«algo que hago cuando me acuerdo»* o *«algo que le pido al agente en el prompt»*, ya sabés en qué se convierte: **una promesa**. Y las promesas se rompen justo el día en que estás apurado — que es, casualmente, el día en que más código estás generando.

Como **gate del pipeline**, en cambio, **no se puede avanzar sin ella**. Deja de depender de tu memoria y pasa a ser parte de la definición de «esta fase terminó». No es que seas más disciplinado: es que el sistema no te da la opción.

El otro argumento es de costo, y es el que convence a los equipos que no se convencen con el primero. Una vulnerabilidad detectada:

- **en el diseño** cuesta cambiar un párrafo del spec;
- **en el pull request** cuesta una conversación y unas horas de alguien;
- **en producción** cuesta un incidente, una ventana de exposición y —según qué datos toque— una notificación a los usuarios y una conversación mucho menos agradable.

Mover el control lo más temprano posible es lo que se llama *shift-left*. No es un eslogan de consultora: es aritmética.

## 🎯 Threat modeling — en la fase de planificación

**Qué es:** pensar, **antes de construir**, qué puede salir mal. No auditar lo que ya está hecho: anticipar sobre el diseño.

**Cómo se hace sin que sea burocracia.** Nadie quiere —ni lee— un documento de cuarenta páginas. La versión útil y liviana es sentarse sobre el diseño de la feature y contestar tres preguntas honestas:

- **¿Quién querría romper esto, y para qué?** Un usuario curioso, alguien que quiere ver datos ajenos, alguien que quiere no pagar, un competidor. Poné nombres y motivos: «cualquiera» no sirve como respuesta.
- **¿Qué datos toca esta feature?** Si toca datos personales, credenciales o plata, el listón sube y conviene ser más paranoico.
- **¿Qué está confiando sin verificar?** Input del usuario, respuestas de terceros, IDs que vienen del cliente, tokens que asume válidos. Casi todos los agujeros viven acá.

**STRIDE** es el checklist clásico para no dejarte categorías afuera, y se usa **como disparador de preguntas, no como formulario**: suplantación de identidad, manipulación de datos, repudio (¿puede negar después que lo hizo?), filtración de información, denegación de servicio y elevación de privilegios. Recorrés las seis sobre tu diseño y anotás lo que aparece. Diez minutos bien invertidos.

**Por qué va en PLAN y no después:** porque **cambia el diseño**. Si descubrís que la feature necesita verificar que el usuario sea dueño del recurso, eso no es un detalle de implementación: es una decisión de arquitectura que afecta a la estructura del código. Descubrirlo en CODE significa **rehacer** — y rehacer es exactamente lo que un pipeline existe para evitar.

## 🔍 SAST — en la fase de implementación

**Qué es:** *Static Application Security Testing* — análisis **estático**. Se lee el código **sin ejecutarlo**, buscando patrones de vulnerabilidad conocidos.

**Qué encuentra bien:**

- **Inyección** (SQL, comandos, plantillas) donde se concatena input sin sanitizar.
- **Secretos hardcodeados**: API keys, tokens y contraseñas que se colaron en el código. Este solo ya justifica el gate — es de lo más común y de lo más caro.
- Criptografía obsoleta o mal configurada, deserialización insegura, rutas de archivo armadas con input del usuario.
- **Dependencias con vulnerabilidades publicadas** (CVEs conocidos).

**Qué NO puede encontrar** —y esto importa tanto como lo anterior—:

- **Lógica de negocio rota.** Que el descuento se pueda aplicar dos veces no es un patrón reconocible: es tu dominio, y ninguna herramienta lo sabe.
- **Autorización mal pensada.** El caso del endpoint de recién: verificar que estás logueado pero no que el recurso sea tuyo se ve **perfectamente correcto** para un analizador estático. El código está bien escrito; la decisión está mal tomada.

Ser honesto sobre el límite vale más que la promesa de completitud: **el SAST es un gate, no un certificado de seguridad.** Y su límite es exactamente lo que cubre el threat modeling una fase antes — por eso van los dos.

## 🧪 DAST — el tercero, y por qué DAW no lo tiene

Existe un tercer control clásico y conviene que lo conozcas, aunque en DAW no vas a encontrarlo.

**DAST** es *Dynamic Application Security Testing*: análisis **dinámico**. Se prueba la aplicación **corriendo**, mandándole entradas maliciosas y observando cómo responde. Complementa al SAST porque encuentra lo que **solo se ve en ejecución**: configuraciones inseguras del servidor, headers que faltan, comportamientos que aparecen recién cuando los componentes interactúan de verdad.

Sobre el papel es el complemento perfecto y el pipeline «debería» tenerlo. **DAW lo sacó a propósito**, y el razonamiento detrás es una de las cosas más importantes de todo el módulo, así que quedate un minuto acá.

Correr un DAST de verdad necesita un **ambiente levantado**: la app andando, con su base de datos, sus credenciales y datos con los que ejercitar los caminos que importan. Nada de eso lo puede montar honestamente una herramienta que vive adentro de tu repositorio y no sabe cómo se despliega tu proyecto. O sea: **`gates.dast` sería un gate que no se puede cumplir**.

¿Y qué le pasa a un gate que no se puede cumplir? La respuesta la sabés porque ya la viviste con cualquier proceso que te hayan impuesto: **se marca como cumplido igual**. Alguien pone el `true` a mano el primer martes que urge salir, y para el segundo martes ya nadie recuerda que ese campo significaba algo.

> ☠️ **Y acá está el daño real, que es mucho más grande que perder un control.** Un gate que se puede mentir **no queda solo en un gate inútil: convierte a todos los demás en sugerencias.** Si el equipo aprende que hay un campo del state que se pone en `true` «porque sí», ya no hay ninguna razón para que `tests` o `sast` sean distintos. La credibilidad del pipeline es una sola para todos los gates, y el más débil la fija.

Por eso el criterio de diseño que te llevás es éste, y vale para tu pipeline tanto como para éste:

> ✅ **Si una condición no la podés verificar de verdad, no la pongas como gate.** Ponela como recomendación, como paso manual, como ítem de checklist — pero no como candado. Un candado que no cierra le enseña a la gente que los candados no cierran.

Que no haya gate **no significa que el control no exista**: el análisis dinámico se hace, en el lugar donde sí se puede hacer bien, que es la pipeline de CI con un ambiente desplegado. Eso es exactamente lo que vas a montar en el **Módulo 8**. Lo que cambia es la honestidad: DAW no promete algo que no puede garantizar.

## 📊 El cuadro que ordena todo

| Control | Qué mira | En qué fase | Qué marca | Qué NO cubre |
| --- | --- | --- | --- | --- |
| **Threat modeling** | El **diseño**, antes de que exista | PLAN | `gates.threat` | Errores de implementación |
| **SAST** | El **código**, sin ejecutarlo | CODE | `gates.sast` | Lógica de negocio, autorización |
| **DAST** | La **app corriendo** | *fuera del pipeline* — CI, M8 | — | Lo que no se ejercita en la prueba |

Mirá la última columna: **ninguno cubre todo**. Es la misma **defensa en capas** de la lección de enforcement, ahora aplicada a seguridad — cada control ve precisamente lo que los otros no pueden ver. Y mirá la anteúltima: la defensa en capas **no exige que todas las capas vivan en el mismo lugar**. Dos son gates del pipeline porque ahí se pueden imponer; la tercera vive en CI porque ahí es donde se puede correr de verdad. Poner cada control donde se puede cumplir es parte del diseño, no una concesión.

## ⚠️ El error clásico: tratar el resultado como verdad absoluta

Los analizadores de seguridad tienen **falsos positivos**. Bastantes. Y el reflejo natural cuando el gate te frena por algo que sabés que no aplica a tu caso es descartarlo y seguir de largo.

Está bien descartarlo. **El criterio es tuyo** — vos conocés el contexto que el analizador no tiene. Pero con una condición:

> ✍️ **Descartar un hallazgo tiene que quedar escrito.**

Por eso un gate de seguridad bien diseñado **produce un reporte, no solo un flag**. El reporte dice qué se encontró, qué se corrigió y —sobre todo— **qué se descartó y por qué**.

Ese «por qué» te salva de dos situaciones feas y bastante probables: la del hallazgo que era real y descartaste sin pensarlo un martes a las siete de la tarde, y la de la auditoría en la que alguien pregunta por qué esto sigue abierto y la única respuesta disponible es «no me acuerdo».

Y notá que es, otra vez, la regla de la lección anterior: **toda fase produce un artefacto**. Un gate que solo deja un `true` en el state es un gate a medias.

## 🛠️ Micro-ejercicio (15 min)

Sobre tu corrida de DAW, con la feature que ya pasaste por el pipeline:

1. **Buscá el threat model** que produjo la fase PLAN —está en `docs/daw/security/threat-<ticket>.md`— y leelo. La pregunta honesta: ¿encontró algo que vos no habías pensado? Si sí, ahí tenés el valor del gate en un caso concreto tuyo.
2. **Corré el skill de SAST** sobre el código que se implementó y mirá el reporte, que queda al lado en `docs/daw/security/sast-<ticket>.md`. Fijate si hay falsos positivos y practicá lo de arriba: descartalos **por escrito**, con el motivo.
3. **Sobre tu propia app**, escribí **tres amenazas concretas**, una línea cada una. Concretas de verdad: no *«podrían hackearnos»*, sino *«un usuario podría cambiar el ID en la URL y ver el ticket de otro»*.

Listo: eso es un threat model, y no te llevó cuarenta páginas. Guardalo, porque en el capstone vas a decidir en qué fase de **tu** pipeline vive este ejercicio.

> 🔭 Todo esto se profundiza después: en el **Módulo 8** los mismos controles corriendo en CI sobre cada pull request, más secret scanning y seguridad de la cadena de dependencias; en el **Módulo 9**, QA AI-First. Lo que importa acá es que **viva dentro del pipeline** y no al costado.

Nos queda una pieza técnica antes de que empieces a hacer tuya la máquina. ➡️
