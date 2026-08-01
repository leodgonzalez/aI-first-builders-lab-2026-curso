# Notas

## Normalización y validación de estructura

```md
Leé @PRD.md. Es el PRD de mi proyecto; si no está en Markdown limpio, pasalo a Markdown.
Validá que respete esta estructura (el template del curso) y decime qué secciones faltan
o están fuera de lugar. Si falta alguna, agregá el encabezado vacío para dejar el molde
completo, pero NO inventes requerimientos ni criterios:

# PRD-001: <nombre del proyecto> — <una línea de qué es>
## Contexto y Problema
## Objetivos
## Requerimientos Funcionales       (RF-01, RF-02, …)
## Requerimientos No Funcionales    (RNF-01, …)
## Criterios de Aceptación          (AC-01 (RF-01): Dado / Cuando / Entonces)
## Fuera de Alcance
## Riesgos y Dependencias
```

## Auditoría de calidad

```md
Leé @PRD.md de nuevo. Auditá su contenido, sin reescribir todavía,
contra este checklist y marcame los problemas UNO POR UNO:
- ¿Cada RF es atómico (una sola acción) y dice "debe"?
- ¿Cada RNF tiene un número concreto? (no "rápido" → "< 3 s p95")
- ¿Cada RF tiene al menos un AC que lo verifique?
- ¿Cada AC es binario (pasa/no pasa) y está en formato Dado/Cuando/Entonces?
- ¿El "Fuera de Alcance" está explícito?
- ¿Hay un AC de control de acceso (que un usuario no vea datos de otro)?
Para cada problema, decime dónde está y por qué. NO agregues features nuevas.
```

## Resolucion con alternativas

```md
Para cada hallazgo identificado:
- Proponé soluciones alternativas.
- Incluí siempre una opción de texto libre para ingresar una solución personalizada si ninguna alternativa aplica.
```

## 

```md
Leé @PRD.md. NO escribas código todavía. Quiero construir SOLO la feature central
del PRD: <tu feature core>. Proponeme un plan corto, en pasos chicos y en orden,
y esperá mi aprobación antes de tocar nada.
```

##

```md
Dale, la feature core está bien, arranquemos por el paso 1. Cuando termines, mostrame qué hiciste
y cómo lo pruebo. No sigas al paso 2 hasta que te lo confirme.
```

> **[Rol] + [Contexto] + [Tarea específica] + [Formato de salida] + [Restricciones] + [Ejemplo, si tenés]**


```md
Rol: para este pedido específicamente sos un especialista en agent instructions (guardrails, skills, subagents, etc)
Contexto: es un cusrso llamado "IA First builders lab" y el material de estudio está en "apuntes\slides"
La tarea: tenés que recolectar el conocimiento que te pida y ponerlas en instrucciones de agente como skills. en este caso tenes que crear un skill(si lo crees lo mas conveniente) para poder hacer un buen prompt. yo te voy a pedir: "haceme un prompt para pedir <tal cosa> que cumpla con las reglas del curso" y vos me vas a responder algo que a su vez yo usaré para pedir a otro chat d claude también. quiero que sean breves pero filosos, sin informacion que no sea util y que se pueda inferir fácil pero con la informacion justa para hacerlo. en ese sentido (no en el sentido de la estructura te doy  un ejemplo:
"""
Leé @PRD.md de nuevo. Auditá su contenido, sin reescribir todavía,
contra este checklist y marcame los problemas UNO POR UNO:
- ¿Cada RF es atómico (una sola acción) y dice "debe"?
- ¿Cada RNF tiene un número concreto? (no "rápido" → "< 3 s p95")
- ¿Cada RF tiene al menos un AC que lo verifique?
- ¿Cada AC es binario (pasa/no pasa) y está en formato Dado/Cuando/Entonces?
- ¿El "Fuera de Alcance" está explícito?
- ¿Hay un AC de control de acceso (que un usuario no vea datos de otro)?
Para cada problema, decime dónde está y por qué. NO agregues features nuevas.
"""
)
recordá que el ejemplo es bueno en el sentido de la cosición pero no de la estructura.
luego si lo crees convenienite agrega en donde sea necesario la forma de invocarlo o en la que se activa.
```

```md
Leé @PRD.md: es el PRD de mi proyecto, la versión que endurecí a mano en el módulo pasado (ya está commiteada en Git, así que trabajá tranquilo).
Quiero que generes una versión nueva y más rigurosa en un archivo aparte, PRD2.md:
pasala por el template y el checklist de calidad completos del curso, auditá punto
por punto, y preguntame todo lo que necesites antes de inventar o cambiar nada.
NO modifiques el PRD.md original.
```

```md
/speckit-constitution Reservas de espacios comunes de un edificio. Principios: (1) TDD estricto: test antes que implementación, ciclo rojo-verde-refactor. (2) Slices verticales por feature, de UI a datos; no está terminada hasta que se usa desde la UI. (3) Invariantes garantizadas por restricciones en la base de datos, no por la app: una reserva activa por espacio/turno/fecha, correo único por vecino, turnos activos de un espacio sin solaparse. (4) Sin borrado físico: solo baja lógica, y el histórico de ocupación y cobro se conserva siempre. (5) Cada respuesta expone solo lo que el rol necesita (un vecino ve ocupación ajena, nunca correo ni detalle) y la autorización se verifica en el backend, no escondiendo botones. Transversal: credenciales (conexión, SMTP, clave de firma) nunca versionadas en el código. Tratar de que la constitución sea lo mas agnostica a la tecnología posible.
```

```md
/speckit-constitution Reservas de espacios comunes de un edificio. Escribí solo estos 5 principios, en prosa breve (3-5 líneas + racional cada uno), sin citar identificadores de requisitos del PRD (RF/RNF/AC) y sin agregar principios ni secciones que no estén acá. (1) TDD estricto: el test se escribe antes que la implementación, se lo ve fallar, y el ciclo es rojo-verde-refactor. (2) Slices verticales por feature, de la UI a los datos; una feature no está terminada hasta que se puede usar desde la UI. (3) Las invariantes del dominio las garantizan restricciones declarativas de la base de datos, no la aplicación ni la pantalla: una sola reserva activa por espacio/turno/fecha, correo único por vecino, turnos activos de un mismo espacio sin solaparse. (4) Sin borrado físico: todo es baja lógica, y el histórico de ocupación y de cobro se conserva siempre. (5) Mínima exposición: cada respuesta expone solo lo que el rol necesita (un vecino ve de los demás solo la ocupación, nunca el correo ni el detalle ajeno) y la autorización se verifica siempre en el backend, no escondiendo botones. Las credenciales (cadena de conexión, contraseña SMTP, clave de firma) nunca se versionan en el código.
```