# PRD-001: Notas y Seguimiento — capturar notas en Markdown y convertirlas en casos con bitácora fechada

## Contexto y Problema

Las notas sueltas se pierden y no evolucionan hacia una acción con seguimiento. Un pendiente rara vez es una sola acción: es una historia que avanza a lo largo de días o semanas —una llamada, un presupuesto, una espera, una fecha para presentarse—. Las apps de tareas tradicionales guardan el pendiente pero no el *historial* de lo que se fue haciendo (a quién se llamó, qué respondieron, qué se está esperando), y ese historial es justo lo que hace falta para retomar un tema sin reconstruirlo de memoria.

Persona:
- **El usuario:** maneja varios pendientes personales en paralelo, cada uno con pasos y esperas que se estiran en el tiempo. Necesita capturar una nota en segundos, convertirla en algo con seguimiento, y poder retomar cualquier pendiente semanas después sin haber perdido el historial de lo hecho.

## Objetivos

Que una nota simple, escrita en Markdown, se transforme en un **caso** con **tareas**, cada una con una **bitácora de entradas fechadas** que registra todo lo que fue pasando, con estados claros y con la posibilidad de crear eventos de calendario y recurrencias para los seguimientos periódicos. Ganar = poder reconstruir el estado de cualquier pendiente en segundos, sin perder el hilo.

## Requerimientos Funcionales

- RF-01: El sistema debe requerir inicio de sesión para acceder; la v1 opera con una única cuenta de usuario (sin gestión de múltiples usuarios).
- RF-02: El sistema debe permitir crear una nota escrita en **Markdown** en un solo paso; la nota puede ser una línea, un texto o una lista.
- RF-03: El editor de nota debe mostrar una **previsualización en vivo** del Markdown junto al área de edición (panel lateral, o superior/inferior según el tamaño de pantalla), actualizada mientras el usuario escribe, sin necesidad de guardar.
- RF-04: El sistema debe **detectar listas** Markdown en el texto de la nota: desordenadas (`- ítem`) y numeradas (`1. ítem`).
- RF-05: El sistema debe permitir listar las notas y abrir cualquiera.
- RF-06: El sistema debe permitir convertir una nota en un caso; cada ítem de la lista se convierte en una tarea del caso, y el caso conserva la referencia a la nota de origen.
- RF-07: El sistema debe permitir crear un caso directamente, sin nota previa.
- RF-08: El sistema debe permitir agregar tareas a un caso existente.
- RF-09: El sistema debe permitir listar los casos y abrir cualquiera para ver sus tareas.
- RF-10: El sistema debe permitir abrir una tarea y ver su bitácora completa ordenada por fecha ascendente.
- RF-11: El sistema debe permitir agregar una entrada de texto simple a la bitácora de una tarea, asignándole automáticamente la fecha y hora de creación.
- RF-12: El sistema debe cambiar el estado de una tarea solo por transiciones válidas del diagrama de estados (ver *Anexo: diagrama de transición*).
- RF-13: El sistema debe ofrecer, para cambiar el estado de una tarea, un botón por cada estado destino válido desde su estado actual, y no mostrar los estados no alcanzables.
- RF-14: El sistema debe permitir, al agregar una entrada, cambiar el estado de la tarea en la misma acción (por edición o por los botones de RF-13).
- RF-15: El sistema debe permitir, al agregar una entrada, crear un evento en el calendario interno con fecha y hora, único o recurrente.
- RF-16: El sistema debe permitir a casos y tareas una fecha límite opcional; sin fecha, el seguimiento queda abierto de forma indefinida.
- RF-17: El sistema debe permitir marcar una tarea como recurrente definiendo una condición de fin: fecha tope, tras N ocurrencias, o nunca.
- RF-18: El sistema debe generar automáticamente la siguiente ocurrencia de una tarea recurrente al completar la ocurrencia actual, salvo que la condición de fin ya se haya cumplido.
- RF-19: El sistema debe **sugerir** cerrar (completar) un caso cuando ninguna de sus tareas queda abierta (todas Completadas o Canceladas); el cierre lo **confirma el usuario**, no es automático.
- RF-20: El sistema debe mostrar una vista de calendario interno con los eventos creados desde las entradas.

## Requerimientos No Funcionales

- RNF-01: La fecha y hora de cada entrada de bitácora debe ser inmutable: el 100% de las entradas conserva su timestamp original y no existe operación de usuario para editarlo.
- RNF-02: La aplicación debe ser web y **responsive**, funcionando en navegador de escritorio y móvil sin instalación.
- RNF-03: La generación de la siguiente ocurrencia recurrente (RF-18) debe ser perezosa: en todo momento existe como máximo 1 ocurrencia futura materializada por tarea recurrente.
- RNF-04: La captura de una nota (RF-02) debe completarse en ≤ 2 s desde que el usuario abre la app hasta que la nota queda guardada.
- RNF-05: La previsualización en vivo (RF-03) debe actualizarse en ≤ 150 ms (p95) desde la última tecla presionada.
- RNF-06: La lista de casos (RF-09) debe renderizar en ≤ 1 s (p95) con hasta 1.000 casos.
- RNF-07: Las credenciales de acceso (RF-01) deben almacenarse con hash seguro (bcrypt/argon2), nunca en texto plano.

## Criterios de Aceptación

- AC-01 (RF-01, RNF-07): Dado un usuario no autenticado, cuando intenta ver notas o casos, entonces el sistema no muestra ningún dato y exige iniciar sesión.
- AC-02 (RF-02): Dado un texto vacío, cuando el usuario intenta guardar la nota, entonces el sistema no la crea.
- AC-03 (RF-03): Dado que el usuario escribe `# Auto` en el editor, cuando termina de tipear, entonces la previsualización muestra "Auto" como encabezado sin que el usuario guarde ni recargue.
- AC-04 (RF-04): Dada una nota con las líneas `- comprar aceite` y `1. llamar al taller`, cuando se muestra la previsualización, entonces ambas se reconocen y renderizan como ítems de lista (desordenada y numerada, respectivamente).
- AC-05 (RF-06): Dada una nota con una lista de 3 ítems, cuando se convierte en caso, entonces el caso tiene exactamente 3 tareas y guarda la referencia a la nota de origen.
- AC-06 (RF-11, RNF-01): Dada una entrada recién agregada, cuando se guarda, entonces queda con la fecha y hora actuales y no existe ninguna acción para modificar ese timestamp.
- AC-07 (RF-13): Dada una tarea en estado "En progreso", cuando el usuario abre las opciones de estado, entonces se muestran solo "En espera", "Completada" y "Cancelada", y no "Pendiente".
- AC-08 (RF-12): Dada una tarea en estado "Completada", cuando se solicita pasarla a "En progreso" (transición no definida), entonces el sistema rechaza el cambio y la tarea permanece "Completada".
- AC-09 (RF-14): Dada una tarea "En progreso", cuando el usuario agrega una entrada y elige "En espera" en la misma acción, entonces la entrada queda registrada y la tarea pasa a "En espera".
- AC-10 (RF-15, RF-20): Dado que el usuario agrega una entrada y crea un evento recurrente semanal, entonces el calendario interno muestra ese evento repetido cada 7 días.
- AC-11 (RF-18): Dada una tarea recurrente semanal sin condición de fin cumplida, cuando se marca "Completada", entonces se genera automáticamente la siguiente ocurrencia con fecha límite +7 días respecto de la anterior.
- AC-12 (RF-17): Dada una tarea recurrente con condición "tras 3 ocurrencias", cuando se completa la 3.ª ocurrencia, entonces no se genera una 4.ª.
- AC-13 (RF-16): Dada una tarea creada sin fecha límite, cuando pasa cualquier cantidad de tiempo, entonces nunca se marca como vencida.
- AC-14 (RF-19): Dado un caso cuyas tareas quedan todas Completadas o Canceladas, cuando ocurre esa última transición, entonces el sistema sugiere cerrar el caso y este permanece Abierto hasta que el usuario confirma; al confirmar, el caso pasa a Completado.

## Fuera de Alcance

- Integración con calendarios externos (Google Calendar, Outlook) en la v1: el calendario es interno; la integración externa queda para una fase posterior (confirmado).
- Multiusuario, cuentas compartidas o colaboración: la v1 es de una sola cuenta con login (confirmado).
- App móvil nativa y funcionamiento offline: la v1 es web responsive (confirmado).
- Markdown avanzado: tablas, imágenes, HTML embebido y bloques de código quedan fuera; la v1 soporta solo básico (encabezados, listas ordenadas/desordenadas, énfasis, enlaces, saltos de línea) (confirmado).
- Listas de pendientes anidadas dentro de una entrada de bitácora: la entrada es texto simple (confirmado, para no crear casos dentro de casos).
- Estados propios para notas sueltas: los estados aplican a tareas, no a notas (confirmado).

## Anexo: diagrama de transición de estados (tarea)

Estados: `Pendiente`, `En progreso`, `En espera`, `Completada` (terminal), `Cancelada` (terminal).

- `Pendiente` → `En progreso`, `Cancelada`
- `En progreso` → `En espera`, `Completada`, `Cancelada`
- `En espera` → `En progreso`, `Completada`, `Cancelada`
- `Completada` → (sin transiciones: terminal)
- `Cancelada` → (sin transiciones: terminal)

Estado de caso: `Abierto` mientras exista al menos una tarea no terminal. Cuando todas las tareas quedan `Completada`/`Cancelada`, el sistema sugiere cerrar y el caso pasa a `Completado` solo tras la confirmación del usuario (RF-19).
