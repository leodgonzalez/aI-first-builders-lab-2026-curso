# Sistema de Notas, Casos y Seguimiento

La aplicación sirve para capturar notas rápidas y convertirlas en casos a los que se les da seguimiento con el tiempo.

Todo empieza con una **nota**, que escribes en **Markdown**. Mientras tipeas el texto de un lado, en el otro panel (a la derecha, o arriba/abajo según convenga) ves de inmediato la **previsualización** de cómo queda.

El editor **detecta listas** escritas en Markdown: las desordenadas (`- comprar aceite`) y las numeradas (`1. llamar al taller`). Una nota puede ser una sola línea, un texto o una lista.

Esa nota puede quedarse como está o convertirse en un **caso**. Un **caso** agrupa **tareas**: al crear el caso desde una nota, cada ítem de la lista se vuelve una tarea dentro del caso.

Cada **tarea** tiene su propia **bitácora**: entradas ordenadas por fecha, con las que registras todo lo que va pasando (llamadas, respuestas, esperas, avances). Cada vez que hay novedad, agregas una **entrada** de texto simple y el sistema le pone la fecha automáticamente. Además, al agregar una entrada puedes:

- **Cambiar el estado de la tarea** (por ejemplo, pasarla a "En espera"), para que al registrar el avance actualices de una vez cómo va.
- **Crear un evento en el calendario**, único o recurrente según convenga (por ejemplo, uno recurrente para dar seguimiento periódico).

Los casos y las tareas pueden tener **fecha límite opcional**: si no le pones fecha, el seguimiento queda abierto de forma indefinida. También pueden ser **recurrentes**, y al completar una repetición se genera la siguiente automáticamente.

## Cómo se navega

Ves una **lista de casos**. Al entrar a un caso, ves sus **tareas** y eliges una. Dentro de la tarea puedes **agregar una entrada**. Al agregar la entrada tienes dos formas de cambiar el estado de la tarea:

- En **edición**, eligiendo el estado directamente.
- Con **botones por cada estado posible**, que muestran solo las transiciones válidas según el diagrama de transición de estados (por ejemplo, desde "En progreso" solo aparecen "En espera", "Completada" o "Cancelada").

**Ejemplo:**
1. Escribes la nota "Problema con la pintura del auto".
2. La conviertes en un caso.
3. Agregas una entrada: "Llamé al taller X, 555-1234" (con fecha automática).
4. Agregas otra entrada y pasas la tarea a "En espera": "Esperando la pieza".
5. Desde una entrada creas un evento en el calendario: "Llevar el auto el martes 10 AM".
6. Cuando terminas, cierras la tarea como "Completada" (y el caso, cuando ya no queden tareas abiertas).
