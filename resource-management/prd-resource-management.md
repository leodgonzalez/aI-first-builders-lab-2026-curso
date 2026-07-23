# PRD-001: Reservas de espacios comunes de un edificio — reservar SUM/parrilla/cancha con disponibilidad al instante, aprobación de vecinos y reporte mensual de cobro

## Contexto y Problema

En nuestro edificio los espacios comunes (el SUM, la cancha de tenis, la parrilla) se reservan hoy mandándole un email a la administración. Cuando aprueba, pone en copia a todos; pero cuando rechaza porque el turno ya estaba ocupado, contesta en privado, solo al que pidió. Uno reserva a ciegas: no hay forma de ver la disponibilidad, y si el turno estaba tomado te enterás recién cuando te rechazan.

Encima, la administración lleva todo en un cuaderno bastante desordenado: se equivoca al cobrar y muchas veces no cobra cuando debía. Y como atiende hasta el viernes a las 17, si se te pasó ese horario ya no podés reservar para el fin de semana. Como tampoco siempre avisan al grupo, nadie sabe quién está usando qué, y termina pasando que alguien usa un espacio sin haberlo reservado (y sin pagarlo).

Queremos una app simple donde se vea la disponibilidad al instante, la administración cargue quién puede reservar, un grupo de vecinos apruebe según si el que reserva está al día, y quede un registro claro de qué cobrar y a quién.

Personas:
- **Martín (administrador):** carga los espacios y los vecinos, ajusta los turnos cuando la asamblea cambia el reglamento, y a fin de mes necesita la lista de reservas para cobrar sin reconstruirla de memoria.
- **Raúl (vecino aprobador):** además de reservar, integra el grupo que revisa que quien reserva esté al día antes de aprobar.
- **Bruno (vecino):** quiere reservar la parrilla un sábado desde el celular, sin depender de que el encargado esté en la portería.

## Objetivos

Que reservar un espacio común sea autogestión y ordenado: el vecino ve la disponibilidad y reserva, un aprobador controla que esté al día, y no se pisan dos reservas nunca. Que las reglas de cancelación y cobro sean automáticas y sin discusión, y que la administración saque a fin de mes una lista clara de **qué, cuándo y a quién** cobrar —propietario o inquilino—. Ganar = cero turnos pisados y cero ambigüedad sobre a quién se le cobra.

## Requerimientos Funcionales

*Autenticación y acceso*
- RF-01: El sistema debe autenticar a un vecino enviando un código de un solo uso a su correo y emitiendo una sesión cuando lo ingresa correctamente.
- RF-02: El sistema debe permitir el acceso únicamente a vecinos previamente dados de alta por la administración.
- RF-03: El sistema debe requerir sesión iniciada para toda operación de consulta o reserva.

*Alta de vecinos, roles y espacios*
- RF-04: El sistema debe permitir a la administración dar de alta un vecino con nombre, correo, unidad funcional y tipo (propietario o inquilino).
- RF-05: El sistema debe permitir a la administración asignar o revocar a un vecino el rol de aprobador.
- RF-06: El sistema debe permitir a la administración dar de alta un espacio con un nombre.
- RF-07: El sistema debe permitir definir para un espacio uno o más turnos, cada uno con un rango horario.
- RF-08: El sistema debe permitir a la administración modificar el rango horario de un turno, indicando la fecha a partir de la cual rige el nuevo horario (fecha de vigencia).
- RF-09: El sistema debe impedir una fecha de vigencia anterior a la fecha actual.
- RF-10: El sistema debe determinar el rango horario de cada reserva según la fecha de su turno: si esa fecha es igual o posterior a la fecha de vigencia, aplica el horario nuevo —incluso a reservas ya existentes—; si es anterior, conserva el horario que regía antes.

*Reservas*
- RF-11: El sistema debe mostrar los turnos disponibles de un espacio en la fecha elegida, dentro de la misma pantalla de reserva.
- RF-12: El sistema debe permitir a un vecino autenticado reservar un turno disponible de un espacio en una fecha; la reserva queda en estado Pendiente.
- RF-13: El sistema debe impedir reservar en una fecha anterior a la de hoy.
- RF-14: El sistema debe impedir que exista más de una reserva activa (Pendiente o Aprobada) para el mismo espacio, turno y fecha.

*Aprobación*
- RF-15: El sistema debe permitir a un aprobador o a la administración aprobar una reserva Pendiente.
- RF-16: El sistema debe permitir a un aprobador o a la administración rechazar una reserva Pendiente.
- RF-17: El sistema debe exigir un motivo no vacío al rechazar una reserva.
- RF-18: El sistema debe enviar un correo al vecino cuando su reserva se aprueba.
- RF-19: El sistema debe enviar un correo al vecino cuando su reserva se rechaza, incluyendo el motivo.
- RF-20: El sistema debe aprobar automáticamente una reserva que siga Pendiente al llegar el inicio de su turno.

*Cancelación*
- RF-21: El sistema debe permitir cancelar una reserva en cualquier momento, registrando la fecha y hora de la cancelación y dejando el turno libre.
- RF-22: El sistema debe conservar las reservas canceladas como registro histórico; una reserva cancelada no cuenta para la unicidad de RF-14.

*Determinación del cobro*
- RF-23: El sistema debe determinar el responsable de pago de cada turno al generar el reporte mensual, no al momento de cancelar.
- RF-24: El sistema debe asignar el pago de un turno usado a la persona que lo usó.
- RF-25: El sistema debe asignar el pago de un turno no usado a quien realizó la última cancelación tardía (con menor anticipación que el plazo configurable respecto del inicio del turno), si existió alguna.
- RF-26: El sistema debe no cobrar un turno que no fue usado ni cancelado tardíamente.
- RF-27: El sistema debe considerar un turno usado cuando su reserva quedó Aprobada y no fue cancelada antes del inicio del turno.

*Reporte mensual*
- RF-28: El sistema debe permitir a la administración generar un reporte mensual de reservas a cobrar.
- RF-29: El reporte debe listar, por cada turno cobrable del mes, la fecha, el nombre del espacio, la unidad funcional, y el nombre y el tipo (propietario o inquilino) de quien debe pagarlo.
- RF-30: El reporte debe listar exactamente un responsable de pago por turno; los turnos sin responsable no aparecen.
- RF-31: El sistema debe proponer como mes por defecto del reporte el mes anterior si la fecha actual es anterior al día 20, o el mes en curso si es el día 20 o posterior.
- RF-32: El sistema debe permitir cambiar el mes del reporte a cualquier mes que no sea futuro.

*Visibilidad y estados*
- RF-33: El sistema debe mostrar a cada vecino únicamente sus propias reservas.
- RF-34: El sistema debe permitir a la administración y a los aprobadores ver las reservas de todas las unidades.
- RF-35: El sistema debe impedir cualquier transición de estado desde una reserva en estado terminal (Rechazada o Cancelada).

## Requerimientos No Funcionales

- RNF-01: El código de acceso (RF-01) debe ser de un solo uso, expirar a los 10 minutos de emitido e invalidar cualquier código anterior del mismo correo.
- RNF-02: La sesión emitida (RF-01) debe durar 30 días, renovarse con cada uso y poder ser revocada por la administración.
- RNF-03: El plazo de cancelación sin cargo (RF-25) debe ser un parámetro configurable, con valor por defecto de 48 horas.
- RNF-04: El sistema debe garantizar unicidad de reserva activa por (espacio, turno, fecha) (RF-14): 0 turnos pisados, incluso ante dos solicitudes simultáneas.
- RNF-05: Ningún vecino debe poder acceder por ningún medio a datos ni reservas de otra unidad funcional: 0 fugas en el set de pruebas de control de acceso.
- RNF-06: El correo de aprobación o rechazo (RF-18, RF-19) debe enviarse dentro de 1 minuto (p95) del cambio de estado.

## Criterios de Aceptación

- AC-01 (RF-01, RNF-01): Dado un código recién enviado, cuando el vecino lo ingresa dentro de los 10 minutos, entonces obtiene sesión; y dado ese mismo código ya usado o vencido, cuando lo reingresa, entonces el sistema lo rechaza.
- AC-02 (RF-02): Dado un correo no dado de alta por la administración, cuando se solicita un código para ese correo, entonces el sistema no permite el acceso.
- AC-03 (RF-03): Dada una persona sin sesión iniciada, cuando intenta ver o crear reservas, entonces el sistema no muestra ningún dato y exige iniciar sesión.
- AC-04 (RF-04, RF-06, RF-07): Dado que la administración da de alta un vecino y el espacio "Parrilla" con un turno noche, cuando el vecino inicia sesión, entonces puede reservar la Parrilla en ese turno.
- AC-05 (RF-05): Dado un vecino sin rol de aprobador, cuando la administración le asigna el rol, entonces puede aprobar reservas; y cuando se lo revoca, deja de poder aprobarlas.
- AC-06 (RF-08, RF-09, RF-10): Dado el turno "noche 19–2" con una reserva ya hecha para el día 15, cuando la administración cambia su fin a las 24 con fecha de vigencia el día 10, entonces la reserva del 15 pasa a regirse por el horario 19–24 y una reserva para el día 5 conserva el horario 19–2; y cuando se intenta fijar una fecha de vigencia anterior a hoy, entonces el sistema no lo permite.
- AC-07 (RF-11): Dado un espacio con el turno noche del sábado ya reservado, cuando un vecino inicia una reserva para ese sábado, entonces el sistema le muestra los turnos libres y no le ofrece el turno noche.
- AC-08 (RF-12): Dado un turno disponible, cuando un vecino lo reserva, entonces la reserva queda Pendiente.
- AC-09 (RF-13): Dada una fecha anterior a hoy, cuando se intenta reservar en esa fecha, entonces el sistema no crea la reserva.
- AC-10 (RF-14, RNF-04): Dada una reserva activa para "Cancha de tenis / turno noche / sábado", cuando otro vecino intenta reservar ese mismo espacio, turno y fecha, entonces el sistema rechaza la segunda y no la crea.
- AC-11 (RF-15, RF-18): Dada una reserva Pendiente, cuando un aprobador la aprueba, entonces queda Aprobada y el vecino recibe un correo de aprobación.
- AC-12 (RF-16, RF-17): Dada una reserva Pendiente, cuando se intenta rechazarla sin motivo, entonces el sistema no la rechaza; y cuando se la rechaza con un motivo, entonces queda Rechazada.
- AC-13 (RF-19, RNF-06): Dada una reserva que se rechaza con el motivo "la unidad tiene deuda", cuando se confirma el rechazo, entonces el vecino recibe un correo que incluye ese motivo, dentro de 1 minuto.
- AC-14 (RF-20, RF-27, RF-24): Dada una reserva que sigue Pendiente al llegar el inicio de su turno, cuando ocurre el turno, entonces el sistema la deja Aprobada automáticamente, el turno cuenta como usado y su pago se asigna a esa persona.
- AC-15 (RF-21, RF-22): Dada una reserva Aprobada, cuando el vecino la cancela, entonces queda registrada la cancelación con su fecha y hora, el turno vuelve a quedar libre y otro vecino puede reservarlo sin conflicto de unicidad; y la reserva cancelada se conserva como historial.
- AC-16 (RF-23, RF-25, RF-26, RNF-03): Dado un turno cuyo único registro es una reserva cancelada con 72 horas de anticipación, cuando se genera el reporte del mes, entonces ese turno no se cobra; y dado un turno cuyo único registro es una reserva cancelada con 24 horas de anticipación, cuando se genera el reporte, entonces paga quien la canceló.
- AC-17 (RF-24, RF-30): Dado un turno con una reserva cancelada tarde (24 h) y luego otra reserva que lo usó, cuando se genera el reporte, entonces figura un único responsable —quien lo usó— y no quien lo canceló.
- AC-18 (RF-28, RF-29): Dado un mes con reservas cobrables, cuando se genera el reporte, entonces cada línea muestra fecha, nombre del espacio, unidad funcional, y nombre y tipo (propietario o inquilino) de quien debe pagarla.
- AC-19 (RF-31, RF-32): Dado que hoy es día 5, cuando se abre el reporte, entonces el mes por defecto es el anterior; dado que hoy es día 25, entonces el mes por defecto es el mes en curso; y cuando se intenta elegir un mes futuro, entonces el sistema no lo permite.
- AC-20 (RF-33, RF-34, RNF-05): Dado el vecino A dueño de una reserva y el vecino B autenticado de otra unidad, cuando B intenta ver la reserva de A, entonces el sistema no se la muestra; mientras que la administración y los aprobadores sí pueden verla.
- AC-21 (RF-35): Dada una reserva Cancelada (terminal), cuando se intenta aprobarla o reactivarla, entonces el sistema rechaza la acción y la reserva permanece Cancelada.

## Fuera de Alcance

- **Cobro y pago real:** el sistema solo arma la lista de qué cobrar y a quién; el cobro efectivo en las expensas lo hace la administración por su cuenta.
- **Montos y tarifas:** el reporte no calcula ni muestra importes; solo el detalle de las reservas a cobrar.
- **Cálculo de deudas:** el sistema no computa deudas; el aprobador evalúa si el vecino está al día con información externa al decidir una aprobación.
- **Eliminación o desactivación de turnos:** un turno se puede crear (RF-07) y modificar su rango horario (RF-08), pero no eliminar ni desactivar.
- **Otros contextos y múltiples edificios:** el sistema es para un solo edificio; no contempla otros usos (peluquerías, oficinas) ni la administración de varios edificios.
- **Contraseñas y login con Google/redes:** la única forma de entrar es el código enviado al correo.
- **Reserva de invitados o personas no habilitadas:** solo reservan vecinos dados de alta por la administración.
- **Modificación de una reserva ya creada:** no se edita espacio/turno/fecha de una reserva; se cancela y se crea otra.

## Riesgos y Dependencias

- Riesgo: dos vecinos reservan el mismo turno al mismo tiempo (RNF-04) → mitigación: controlar la unicidad a nivel de datos, no solo en la pantalla.
- Riesgo: al cambiar el horario de un turno, no queda claro qué horario rige para reservas ya hechas → mitigación: la fecha de vigencia determina, por la fecha de cada reserva, qué rango horario aplica (RF-08, RF-10).
- Riesgo: con varias cancelaciones tardías sobre el mismo turno sin que nadie lo use, podría dudarse quién paga → mitigación: las reglas de pago (RF-24, RF-25) lo resuelven determinísticamente al generar el reporte (paga quien lo usó; si nadie lo usó, la última cancelación tardía).
- Riesgo: un token de 30 días filtrado da acceso prolongado (RNF-02) → mitigación: sesión revocable por la administración y un único código activo por correo (RNF-01).
- Dependencia: un servicio de envío de correos para los códigos de acceso y los avisos de aprobación/rechazo.

## Anexo: estados de una reserva

Estados: `Pendiente`, `Aprobada`, `Rechazada` (terminal), `Cancelada` (terminal).

- `Pendiente` → `Aprobada`, `Rechazada`, `Cancelada`
- `Aprobada` → `Cancelada`
- `Rechazada` → (terminal)
- `Cancelada` → (terminal)

Una reserva que sigue `Pendiente` al iniciar su turno pasa automáticamente a `Aprobada` (RF-20), y un turno se considera **usado** si su reserva quedó Aprobada y no se canceló antes del inicio del turno (RF-27). El horario que define ese inicio no es fijo: cada reserva usa el que corresponde a la fecha de su turno (RF-10). Por eso, si se modifica el horario de un turno con una fecha de vigencia, las reservas ya existentes de fechas iguales o posteriores pasan a usar el horario nuevo.

Quién paga un turno **no** es un estado de la reserva ni se marca al cancelar: se **calcula al generar el reporte** (RF-23) sobre todos los registros de ese turno —usos y cancelaciones—. Las reservas canceladas se conservan como historial y no bloquean nuevas reservas del mismo turno (RF-21, RF-22). No se puede reabrir un estado terminal (RF-35).
