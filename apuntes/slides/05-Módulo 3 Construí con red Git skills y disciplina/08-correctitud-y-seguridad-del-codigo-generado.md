---
titulo: "Correctitud y seguridad del código generado"
capitulo: "05-Módulo 3 Construí con red Git skills y disciplina"
orden: 8
source: "apuntes/slides/00-raw/05-Módulo 3 Construí con red Git skills y disciplina/08-Correctitud y seguridad del código generado – MUG.html"
source_sha256: 8dc68594aefcfb13
extraido: 2026-07-21
---

# Correctitud y seguridad del código generado

Hay una trampa en la que es facilísimo caer cuando ves lo rápido que produce un agente: **confundir velocidad con que esté bien.** Son cosas distintas. La IA escribe rápido, prolijo y convincente —pero se equivoca, y lo hace *con seguridad*, sin avisarte que duda—. Un código puede arrancar, correr sin errores y verse impecable, y aun así estar haciendo lo que no querías. En esta lección, la última antes de construir tu app, te dejo **dos reflejos** que te separan del que vibecodea con los dedos cruzados: **probar antes** y **desconfiar de la seguridad**. 🔒

## 🧪 Escribí la prueba antes que el código

Primero, sin tecnicismos: **un «test» (o prueba) es un chequeo automático** que dice *«esto tiene que dar tal resultado»* y prende una luz roja si no se cumple. Nada más que eso.

La técnica, entonces, es simple de enunciar y muy poderosa: **decidí qué tiene que pasar ANTES de pedirle el código a la IA.** ¿Por qué en ese orden? Pensá qué pasa al revés. Si primero dejás que la IA escriba el código y *después* le pedís la prueba, la IA tiende a escribir una prueba que **le da la razón a lo que ya hizo** —aunque esté mal—. Es como dejar que el alumno escriba su propio examen después de haber resuelto el problema: se aprueba solo. 🎓

En cambio, si la prueba existe **primero** y fija cuál es el resultado correcto, la IA **no se puede auto-aprobar**: no le queda otra que escribir código que de verdad la pase. El orden es todo:

1. **Vos decidís qué tiene que pasar** y lo dejás escrito como prueba (podés pedírselo a la IA con un ejemplo bien claro).
2. **La IA escribe el código** que haga pasar esa prueba.
3. **Corrés la prueba:** si da verde, vas bien; si da rojo, la IA sigue trabajando —sobre el código, nunca tocando la prueba—.

Así, el *«parece que anda»* se transforma en un juez objetivo: pasó o no pasó. No hace falta que testees todo —eso sería una locura—; con aplicarlo a **la pieza que más importa** (la que si falla, se rompe el producto) ya ganaste muchísimo. Guardate esto, porque en el ejercicio que viene lo vas a usar exactamente así.

## ⚠️ Por qué esto importa tanto (el dato que lo justifica)

Y ahora el número que conviene tener clavado: alrededor del **45% del código generado por IA introduce alguna vulnerabilidad de seguridad** (Veracode, 2025). No es «de vez en cuando»: es casi la mitad. ¿Por qué? Porque el agente **no tiene conciencia de seguridad**: te da lo que le pediste, funcionando, pero no se da cuenta de que, de paso, dejó una puerta abierta —por ejemplo:

- una forma de que alguien lea datos de otro usuario,
- una contraseña guardada en texto plano,
- una parte del sistema accesible sin pedir login.

El agujero viene de regalo y sin aviso. Por eso el reflejo que quiero dejarte es tajante: **revisar no es opcional.** Todo lo que sale de la IA entra a tu sistema bajo *tu* responsabilidad, con tu nombre en el commit —nadie va a ver que lo escribió la IA, van a ver que lo aprobaste vos—.

## 🛡️ Un aliado: los escáneres de seguridad

Buena noticia: no estás solo cuidando esto a ojo. Existen herramientas que **revisan tu código buscando esos agujeros de forma automática** —pensalas como un corrector, pero de seguridad: leen el código y te marcan lo peligroso—. No hace falta que te vuelvas experto; alcanza con saber que **existen y las vas a querer**. Cómo dejarlas corriendo solas en tu proyecto lo vemos más adelante, en el Módulo 9.

## 🔭 Y lo grande, para más adelante

Un último deslinde para que no te satures: lo de hoy es la versión **«de a una pieza»** —chequeás que cada parte importante haga lo que tiene que hacer mientras construís—. Medir la calidad de **todo el sistema en conjunto** (que la IA responda bien de forma consistente, con datos de verdad, a lo largo del tiempo) es un tema más grande y con nombre propio: lo vas a ver en el **Módulo 10, QA AI-First**. Hoy sembramos el hábito; allá lo profesionalizamos.

### 🔎 La muestra: una prueba en TicketTriage

Aunque no seas técnico, mirá la *idea* (no hace falta que leas el código). Antes de pedir la parte que crea tickets, dejamos escrito qué tiene que pasar con un caso clarísimo: **si el asunto viene vacío, tiene que rechazarlo**.

```
# la prueba: "un ticket sin asunto tiene que ser rechazado (error 400)"
def test_asunto_vacio_devuelve_400(client):
    r = client.post("/tickets", json={"asunto": "", "descripcion": "x"})
    assert r.status_code == 400
```

Con esa prueba escrita primero, la IA no puede hacer trampa: tiene que programar la validación de verdad para que dé verde. Funciona bárbaro con **reglas claras** como esta (asunto vacío → error). Para juzgar cosas más «de criterio» —por ejemplo, si la IA clasificó *bien* un ticket, donde a veces hay más de una respuesta defendible— se usan técnicas distintas, y esas son las del Módulo 10.

### 🗣️ Y así se ve vibecodeando (sin escribir una línea de código)

Ahora, la parte que te va a bajar la ansiedad si el bloque de código de arriba te resultó chino: **ese test no lo escribís vos**. Lo escribe la IA — vos lo *dirigís*, en palabras, igual que todo lo demás en este módulo. La conversación completa, en TicketTriage, fue así:

```
Antes de programar la creación de tickets, escribí un test que verifique esta regla:
"un ticket sin asunto tiene que ser rechazado". Mostrámelo y esperá mi OK
antes de escribir nada más.
```

El agente te muestra el test. ¿Y qué revisás vos, si no leés código? **La regla, no la sintaxis**: el nombre del test y el comentario cuentan qué verifica («un ticket sin asunto tiene que ser rechazado») — y esa regla es de negocio, no de programación. ¿Es la regla que vos querías? ¿El caso es el que importa? Eso lo podés juzgar perfectamente, vengas de donde vengas. Si te cierra, seguís:

```
Perfecto. Ahora implementá la creación de tickets de modo que ese test pase.
Corré el test y mostrame el resultado. NO modifiques el test.
```

Ese *«NO modifiques el test»* es la cláusula anti-trampa —el examen quedó fijado antes, la IA solo puede aprobar escribiendo código que de verdad lo pase—. Cuando te muestra el resultado en **verde**, tenés algo que ninguna lectura de código te da: una comprobación objetiva de que la regla se cumple. Y fijate dónde estuvo tu aporte en todo esto: en **decidir qué tiene que pasar** —la regla de negocio— que es exactamente lo que vos sabés mejor que nadie. El test-first, vibecodeado, es eso: vos ponés el «qué», la IA pone la sintaxis, y el verde no negocia.

Con esto cerramos el bloque de teoría: ya sabés **dirigir** a la IA, **equipar** tu proyecto y **construir con red**. Llegó el momento de la verdad, y acá se conecta todo: en el **próximo ejercicio construís tu app** desde el PRD que endureciste —y vas a aplicar el «probar antes» justo en su pieza más importante, para no construir sobre arena—. ➡️
