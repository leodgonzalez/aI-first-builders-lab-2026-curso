# Reserva de Recursos Comunes de un Edificio

La aplicación sirve para que los vecinos de un edificio **reserven los recursos comunes** (un salón de usos múltiples, un gimnasio, una parrilla, una cancha, etc.) y para que la **administración** controle esas reservas y su cobro.

## Los recursos y sus turnos

El edificio tiene uno o varios **recursos**, cada uno con su **nombre** (por ejemplo, "SUM Planta Baja", "Gimnasio" o "Terraza"). Cada recurso se reserva por **turnos con nombre y rango horario**: por ejemplo, **turno tarde de 10 a 17** y **turno noche de 19 a 2**. Una **reserva** es un recurso + un turno + una fecha. Un mismo turno de un recurso, en una fecha, lo puede tener **una sola reserva**: el sistema no deja que dos personas pisen el mismo turno.

## Quién puede usarlo

No cualquiera entra: una persona existe en el sistema solo si la **administración la dio de alta**. Hay dos tipos:

- **Propietarios**: dados de alta con **nombre**, **correo** y la **lista de unidades funcionales** (departamentos, cocheras) de las que son propietarios. Una misma unidad funcional puede tener **varios propietarios** (por ejemplo, un matrimonio), y cada uno entra con su propio correo.
- **Inquilinos**: cuando una unidad se alquila, la administración da de alta un **inquilino** para esa unidad, con **un único correo responsable** (uno solo, para evitar problemas de gestión). El inquilino tiene un **vencimiento**: por defecto **2 años**, o el plazo que se indique según el **contrato de alquiler**. El **propietario sigue dado de alta** igual: el inquilino se suma, no lo reemplaza.

Para entrar, la persona no usa contraseña. Escribe su **correo**, el sistema le **envía un código** a ese mail, y cuando lo ingresa y queda verificado recibe una **sesión que dura bastante** (para no tener que repetir el código cada vez que entra).

## Cómo se reserva y cómo se aprueba

El vecino elige un recurso, un turno y una fecha libre, y **solicita la reserva**. La reserva no queda confirmada de una: entra como **pendiente**.

Ahí aparecen los **aprobadores**. Son un **grupo de propietarios con un rol especial** que **controla las expensas y las deudas**; además, la **administración** también puede aprobar o rechazar. Cualquiera de ellos revisa la solicitud y:

- Si está todo en orden (sin deudas ni otras irregularidades), la **aprueba**.
- Si hay algún problema, la **rechaza con una explicación**.

En los dos casos, la decisión **dispara un correo** al vecino avisándole si su reserva quedó aprobada o rechazada, y por qué.

## Qué se puede hacer con una reserva

Una vez creada, una reserva **pendiente o aprobada no se puede modificar**: no se cambia el recurso, el turno ni la fecha. Lo único que se puede hacer es **cancelarla**, o **aprobarla / rechazarla** cuando el rol lo permite.

## Cancelaciones

Una reserva se puede **cancelar en cualquier momento**, y al cancelarla el turno **queda libre** para que otro vecino lo tome.

Ahora bien, hay una regla de cobro. Si la cancelación se hace con **al menos 48 horas de anticipación** (ese plazo es **configurable**), no se cobra nada. Pero si se cancela **con menos de 48 horas**, aunque el turno se libere, **se le cobra igual** al que canceló… **salvo que otro vecino tome ese turno liberado**: en ese caso al que canceló **no se le cobra**, y el turno se le cobra **al que efectivamente lo usa**.

## El cobro de expensas del mes

La administración entra a ver **a quiénes tiene que cobrarles** las reservas del mes. Genera un **resumen del mes** con la **lista de reservas a cobrar**, mostrando para cada una la **fecha**, el **nombre del recurso**, la **unidad funcional**, y el **nombre y correo de quien efectivamente la usó**, indicando además si es **propietario o inquilino**. Ese dato importa porque de una misma unidad pueden reservar tanto el propietario como el inquilino, y hay que saber **quién la usó** para cobrarla.

El sistema **solo muestra esa información**: el **cobro efectivo** de la expensa y el **arreglo del pago entre inquilino y propietario** los hace la administración **por fuera** (fuera del alcance del sistema).

Al abrir el resumen, el sistema propone un **mes por defecto** (formato **MM-yyyy**): el **mes anterior** si todavía no pasó el **día 20**, o el **mes en curso** si ya pasó. La administración puede **cambiarlo a cualquier mes**, con un límite: **no se puede elegir un mes futuro**.

El resumen respeta la regla de cancelación: incluye las reservas que efectivamente se usan y las **canceladas tarde que nadie retomó**, y deja fuera las que **retomó otro** (esas se le cobran al nuevo).

## Mano libre de la administración

Tanto el **administrador** como el **aprobador** pueden **dar vuelta cualquier cosa** sin restricciones: aprobar o rechazar, cancelar una reserva, liberar un turno o corregir lo que haga falta.

## Un ejemplo de punta a punta

1. La administración da de alta a **Bruno**, **inquilino** de la unidad **4°B** (contrato a 2 años), con su correo como único responsable.
2. Bruno entra: escribe su correo, le llega un **código**, lo ingresa y queda adentro.
3. Bruno pide el **SUM Planta Baja**, **turno noche**, para el **sábado**. Queda **pendiente**.
4. Un **aprobador** (propietario con el rol especial) ve que la unidad no tiene deudas y la **aprueba**; a Bruno le llega un **correo** confirmando.
5. El jueves Bruno **cancela** (menos de 48 h): el turno se libera. Como **nadie más lo toma**, esa reserva **se le cobra igual**.
6. El **5 de agosto**, la administración abre el **resumen**: como es antes del día 20, viene cargado el **mes anterior** (`07-2026`), y ahí aparece la reserva de Bruno con su **fecha** y el **recurso**, lista para cobrar.
