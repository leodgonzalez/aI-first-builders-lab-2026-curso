---
titulo: "Guardrails II: Permisos y seguridad de agentes"
capitulo: "03-Módulo 1 AI-First Development mindset y PRD del proyecto"
orden: 5
source: "apuntes/slides/00-raw/03-Módulo 1 AI-First Development mindset y PRD del proyecto/05-Guardrails II_ Permisos y seguridad de agentes – MUG.html"
source_sha256: 99e99ac059c8faeb
extraido: 2026-07-16
---

# Guardrails II: Permisos y seguridad de agentes

Los archivos de contexto que vimos recién le dicen al agente **cómo comportarse**. Pero hay una pregunta más urgente, y bastante más peligrosa, que todavía no tocamos: **¿qué le permitís hacer?** Porque un agente moderno no se queda en sugerir texto —puede ejecutar comandos en tu máquina, borrar archivos, instalar cosas, mandar datos por la red—. En esta lección vemos el segundo guardrail, el que define el radio de acción: los **permisos**. 🔒

## 🚦 Allow, Ask, Deny: el semáforo

El control central son los permisos, y la forma más clara de pensarlos es como un semáforo de tres luces. En **Claude Code** están modelados exactamente así.

- En **Allow** quedan las cosas que el agente hace solo, sin molestarte —leer archivos, por ejemplo, que es inofensivo y constante—.
- En **Ask**, las que ejecuta solo después de pedirte confirmación: típicamente correr un comando, donde querés ver qué va a hacer antes de que lo haga.
- Y en **Deny**, lo que no toca jamás, ni siquiera preguntando —tocar tu `.env`, por caso—.

**Copilot** y **OpenCode** tienen sus propios equivalentes (modos de auto-approve y de confirmación), pero el concepto es universal y es lo que quiero que te lleves: **vos decidís, de antemano, hasta dónde llega el agente.** No es algo que negociás en el momento; lo configurás una vez y te protege siempre.

## 🚫 Por qué *nunca* full-auto en producción

Sé lo que vas a sentir la primera semana: confirmar cada comando cansa, y la tentación de poner todo en «allow» para que el agente vuele es enorme. **No lo hagas sobre un sistema real.** Y acá vuelve, intacta, la regla de oro del módulo: el agente es un *intern poderoso pero no confiable*.

Pensalo con esa imagen y la decisión se vuelve obvia. Darle permiso total para ejecutar lo que se le ocurra sobre producción es como entregarle las llaves del entorno productivo a alguien que entró ayer. Brillante, sí; rapidísimo, también; hasta que con la mejor de las intenciones corre un comando que borra algo que no debía, y ahí no hay velocidad que valga la pena. 💥 La autonomía total es para entornos descartables, no para donde duele.

## 📦 Sandbox y mínimo privilegio

La contracara sana de todo esto es acotar el ambiente donde el agente trabaja, y hay una idea que ordena la práctica: **dale el menor privilegio que la tarea necesite, y ni uno más.** En concreto, eso significa correrlo en un entorno aislado siempre que puedas —un sandbox, un contenedor, una carpeta delimitada— en lugar de soltarlo sobre todo tu sistema; y mantener lo verdaderamente sensible (los secretos, el acceso a producción) **fuera de su alcance por defecto**, no a un permiso de distancia. El agente no necesita las llaves de todo para escribirte una función: dale el cuartito donde tiene que trabajar, no el edificio entero.

## ✋ Lo que se confirma siempre, sin excepción

Hay un puñado de operaciones donde el «ask» no se discute, porque el costo de equivocarse es demasiado alto:

- Las **destructivas** —borrar, sobrescribir, resetear— siempre se confirman.
- Las de **red** —mandar datos afuera, llamar APIs externas— también, porque ahí se te pueden ir cosas que no querés que salgan.
- Y todo lo que toque **secretos** —claves, tokens, credenciales— ni hablar.

La aritmética es simple y conviene tenerla presente: el costo de un «ask» de más es un clic tuyo; el de un «allow» de menos puede ser un incidente. Ante la duda, que pregunte.

## 🎯 Dos guardrails, un mismo objetivo: el control

Si juntás esta lección con la anterior, ya tenés el cuadro completo de cómo se encuadra a un agente.

1. Por un lado, los **archivos de contexto**, que definen *cómo se comporta*.
2. Por el otro, los **permisos**, que definen *qué puede hacer*. Juntos son las dos manos con las que lo manejás.

Y fijate el cambio de actitud que esto implica: un Builder no le tiene miedo a los agentes ni los suelta a lo loco —los **encuadra**, y dentro de ese encuadre los deja correr tranquilo—.

## 💡 Para aplicar

Abrí la configuración de permisos de tu agente y mirala con ojo crítico: ¿qué tenés hoy en *allow* que en realidad debería pedirte confirmación? Identificá al menos **una operación** —destructiva, de red, o que toque secretos— que quieras mover a *ask*. Ese pequeño ajuste es la diferencia entre encuadrar al agente y rezar.

Con la cabeza, el stack y los dos guardrails listos, es hora de dar el primer paso práctico de verdad: **conectarle al agente una capacidad externa con MCP** y, de paso, aprender a no fundir tu cuota en el intento. ➡️
