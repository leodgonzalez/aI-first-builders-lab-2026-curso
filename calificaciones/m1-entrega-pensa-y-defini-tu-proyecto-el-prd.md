---
tipo: entrega
titulo: "Pensá y definí tu proyecto: el PRD"
modulo: 1
nota: 100
resultado: "Aprobado"
enunciado: "apuntes/slides/03-Módulo 1 AI-First Development mindset y PRD del proyecto/09-pensa-y-defini-tu-proyecto-el-prd.md"
repo: null
proyecto: "../src/modulo-1"
consigna: "Ingresá la URL de tu PRD para que el instructor/a pueda revisarlo y darte feedback."
source: "calificaciones/00-raw/M1-ENTRGABLE-Pensá y definí tu proyecto_ el PRD Assignment – MUG.html"
source_sha256: a8d71ec51a18b415
extraido: 2026-08-04
---

# Pensá y definí tu proyecto: el PRD

**Nota: 100%** — Aprobado

## Devolución del instructor

Hola Leonardo! Gracias por el envío de la tarea. La idea está muy buena y se entiende perfecto el problema: hoy la reserva depende de mails, cuadernos y confirmaciones manuales, entonces se generan demoras, turnos pisados, poca visibilidad y errores al momento de cobrar. Idea simple y poderosa desde mi punto de vista!

Te paso feedback que ojalá te sirva para próximas iteraciones:

- Me gusta que el MVP no intente hacer todo el sistema de expensas o pagos, sino enfocarse en reservas, aprobación, cancelaciones y reporte mensual. Eso lo hace bastante construible.  
- Los requerimientos funcionales están sólidos y bastante completos: alta de vecinos, alta de espacios, turnos, reserva pendiente, aprobación/rechazo, mails, cancelación, reglas de cobro y reporte mensual. Se nota que pensaste el flujo completo.  
- Hay un punto importante para aclarar: el PRD dice que “un grupo de vecinos apruebe según si el que reserva está al día”, pero después no aparece claramente cómo se define eso. ¿El sistema sabe si el vecino tiene deuda? ¿Lo carga la administración? ¿El aprobador lo revisa manualmente? Como el cobro real está fuera de alcance, conviene aclarar que la aprobación por deuda será manual o que el estado “al día / con deuda” se carga dentro del sistema.  
- También conviene definir mejor los roles. Aparecen vecino, administración y aprobador, pero faltaría precisar quién puede hacer qué. Por ejemplo: administración carga vecinos/espacios/turnos y ve reportes; aprobador solo aprueba/rechaza reservas; vecino solo ve y cancela sus reservas. Eso ayuda mucho para permisos y seguridad.  
- La regla de cancelación está buena, pero tiene una parte delicada: si alguien cancela tarde y otro vecino toma el turno, el PRD dice que se le cobra al que lo usó. Está bien, pero habría que dejar más claro qué pasa si nadie toma el turno liberado: ¿se cobra al que canceló tarde? Entiendo que sí por RF-15, pero conviene explicitarlo.  
- Los RNF están bien porque tienen números concretos: código de un solo uso por 10 minutos, sesión de 30 días, cancelación configurable y 0 turnos pisados. Sumaria algún RNF de tiempo de respuesta, por ejemplo que la disponibilidad cargue en menos de 2 segundos.  
- Los criterios de aceptación están muy bien: están en Dado/Cuando/Entonces, cubren bastantes casos y son binarios. Sumaria algunos casos más: intentar reservar sin estar dado de alta como vecino, mail que no llega, vecino con deuda si eso entra en el flujo, y cancelación de una reserva ya pasada.  
- El fuera de alcance está claro y ayuda bastante: no procesa pagos, no calcula importes, no es multi-edificio y no usa contraseñas. Me parece bien para mantener el MVP simple.  
- Como mejora de alcance, aclararía si el reporte mensual solo lista reservas cobrables o si también indica quién debería pagarlas según propietario/inquilino. Mencionás tipo de vecino, pero no queda del todo claro cómo se usa esa información.

Sobre la tecnología, no sé si pensaste o no en algo. Pero yo te recomendaría algo simple que le estoy recomendando a todos los que no explicitaron algo:

- Front: Next.js o React para una web responsive usable desde el celular.  
- Back: Next.js API routes, Express o NestJS.  
- Base de datos: PostgreSQL para vecinos, unidades, espacios, turnos, reservas, estados y reportes.  
- Email: algún servicio tipo SendGrid, Resend o SMTP para códigos de acceso y avisos. Ojo con esto! 🙂

En general está muy bien encaminado. Es una idea concreta, útil y muy viable para el curso. Saludos!

## Lo entregado

# PRD-001: Reservas de espacios comunes del edificio

## Contexto y Problema

En nuestro edificio los espacios comunes (el SUM, la cancha de tenis, la parrilla) se reservan mandándole un email a la administración. Cuando aprueba, pone en copia a todos; pero cuando rechaza porque el turno ya está ocupado, contesta en privado, solo al que pidió. El problema es que uno reserva a ciegas: no hay forma de ver la disponibilidad, y si el turno estaba tomado te enterás recién cuando te rechazan a vos.

Además, la administración lleva todo en un cuaderno bastante desordenado, así que se equivoca al cobrar y muchas veces no cobra cuando debería. Y como atiende hasta el viernes a las 17, si se te pasó ese horario ya no podés reservar para el fin de semana.

Adicionalmente, muchas veces no mandan el email avisando al grupo, así que nadie sabe quién está usando qué: termina pasando que alguien usa un espacio sin haberlo reservado (y sin pagarlo).

Queremos una app simple donde se vea la disponibilidad al instante, la administración cargue quién puede reservar, un grupo de vecinos apruebe según si el que reserva está al día, y quede un registro claro de qué cobrar.

Personas:

- **Martín (administrador):** carga los espacios y los vecinos, y a fin de mes necesita la lista de reservas para cobrar sin reconstruirla de memoria.

- **Bruno (vecino):** quiere reservar la parrilla un sábado desde el celular, sin depender de que el encargado esté en la portería.

## Objetivos

Que reservar un espacio común sea autogestión y ordenado: el vecino reserva, un aprobador controla que no haya deudas, y no se pisan dos reservas nunca. Que la administración saque a fin de mes una lista clara de qué cobrar y a quién.

## Requerimientos Funcionales

- RF-01: El sistema debe autenticar al vecino enviando un código a su correo y dándole una sesión al ingresarlo.

- RF-02: El sistema debe permitir a la administración dar de alta un vecino con nombre, correo, unidad funcional y tipo (propietario o inquilino).

- RF-03: El sistema debe permitir a la administración dar de alta un espacio con un nombre.

- RF-04: El sistema debe permitir definir los turnos de un espacio, cada uno con un rango horario.

- RF-05: El sistema debe mostrar los turnos disponibles de un espacio en la fecha elegida, dentro de la misma pantalla de reserva.

- RF-06: El sistema debe permitir a un vecino autenticado reservar un turno disponible de un espacio en una fecha; la reserva queda pendiente.

- RF-07: El sistema debe impedir reservar en una fecha anterior a la de hoy.

- RF-08: El sistema debe impedir que exista más de una reserva activa para el mismo espacio, turno y fecha.

- RF-09: El sistema debe permitir a un aprobador o a la administración aprobar una reserva pendiente.

- RF-10: El sistema debe permitir a un aprobador o a la administración rechazar una reserva pendiente.

- RF-11: El sistema debe exigir un motivo al rechazar una reserva.

- RF-12: El sistema debe enviar un correo al vecino cuando su reserva se aprueba.

- RF-13: El sistema debe enviar un correo al vecino cuando su reserva se rechaza, incluyendo el motivo.

- RF-14: El sistema debe permitir cancelar una reserva en cualquier momento, dejando el turno libre.

- RF-15: El sistema debe cobrar una reserva cancelada con menos de 48 horas de anticipación al inicio del turno.

- RF-16: El sistema debe cobrar el turno a quien lo use, si otro vecino toma un turno liberado por una cancelación tardía.

- RF-17: El sistema debe permitir a la administración generar un reporte mensual con las reservas a cobrar, indicando fecha, espacio, y nombre y tipo (propietario o inquilino) de quien usó cada una.

- RF-18: El sistema debe mostrar a cada vecino únicamente sus propias reservas.

- RF-19: El sistema debe permitir a la administración y a los aprobadores ver las reservas de todos.

## Requerimientos No Funcionales

- RNF-01: El código de acceso debe ser de un solo uso y expirar a los 10 minutos.

- RNF-02: La sesión debe durar 30 días antes de pedir un nuevo código.

- RNF-03: El plazo de cancelación sin cargo debe ser configurable, con 48 horas por defecto.

- RNF-04: No debe existir más de una reserva para el mismo espacio, turno y fecha (0 turnos pisados).

- RNF-05: Un vecino no debe poder ver reservas ni datos de otra unidad funcional (0 accesos indebidos en las pruebas de control de acceso).

## Criterios de Aceptación

- AC-01 (RF-01, RNF-01): Dado un código recién enviado, cuando el vecino lo ingresa dentro de los 10 minutos, entonces entra.

- AC-02 (RF-01, RNF-01): Dado un código vencido o ya usado, cuando el vecino lo ingresa, entonces el sistema lo rechaza.

- AC-03 (RF-02, RF-03, RF-04): Dado que la administración da de alta un vecino y el espacio "Parrilla" con un turno noche, cuando el vecino inicia sesión, entonces puede reservar la Parrilla en ese turno.

- AC-04 (RF-05): Dado un espacio con el turno noche del sábado ya reservado, cuando un vecino inicia una reserva para ese sábado, entonces el sistema le muestra los turnos libres y no le ofrece el turno noche.

- AC-05 (RF-06): Dado un turno disponible, cuando un vecino lo reserva, entonces la reserva queda pendiente.

- AC-06 (RF-07): Dada una fecha anterior a hoy, cuando se intenta reservar, entonces el sistema no lo permite.

- AC-07 (RF-08, RNF-04): Dada una reserva activa para "Cancha de tenis / turno noche / sábado", cuando otro vecino intenta reservar ese mismo turno, entonces el sistema lo rechaza.

- AC-08 (RF-09): Dada una reserva pendiente, cuando un aprobador la aprueba, entonces queda aprobada.

- AC-09 (RF-11): Dada una reserva pendiente, cuando se intenta rechazarla sin motivo, entonces el sistema no la rechaza.

- AC-10 (RF-10): Dada una reserva pendiente, cuando se la rechaza con un motivo, entonces queda rechazada.

- AC-11 (RF-12): Dada una reserva pendiente, cuando se la aprueba, entonces el vecino recibe un correo de aprobación.

- AC-12 (RF-13): Dada una reserva que se rechaza con un motivo, cuando se confirma, entonces el vecino recibe un correo que incluye ese motivo.

- AC-13 (RF-14): Dada una reserva, cuando el vecino la cancela, entonces el turno queda libre para otra reserva.

- AC-14 (RF-15, RNF-03): Dada una reserva cancelada con 72 horas de anticipación, cuando se genera el reporte, entonces no se cobra.

- AC-15 (RF-15): Dada una reserva cancelada con 24 horas de anticipación, cuando se genera el reporte, entonces se cobra.

- AC-16 (RF-16): Dada una reserva cancelada tarde y luego un vecino que toma ese turno, cuando se genera el reporte, entonces se le cobra al que lo usó y no al que canceló.

- AC-17 (RF-17): Dado un mes con reservas para cobrar, cuando se genera el reporte, entonces cada línea muestra fecha, espacio, y nombre y tipo de quien la usó.

- AC-18 (RF-18, RNF-05): Dado el vecino A dueño de una reserva y el vecino B de otra unidad, cuando B intenta ver la reserva de A, entonces el sistema no se la muestra.

- AC-19 (RF-19): Dada la administración, cuando abre las reservas, entonces ve las de todas las unidades.

## Fuera de Alcance

- El cobro real de las expensas y el pago: el sistema solo arma la lista; el cobro lo hace la administración por su cuenta.

- Los importes: el reporte no calcula montos, solo el detalle de las reservas.

- Otros edificios u otros usos (peluquerías, oficinas): esto es para un solo edificio.

- Contraseñas o login con Google/redes: la única forma de entrar es el código al correo.

## Riesgos y Dependencias

- Riesgo: dos vecinos reservan el mismo turno al mismo tiempo → mitigación: controlar la unicidad en la base de datos, no solo en la pantalla.

- Dependencia: un servicio de envío de correos para los códigos de acceso y los avisos de aprobación/rechazo.

*Minimum: 1*1.342 words
