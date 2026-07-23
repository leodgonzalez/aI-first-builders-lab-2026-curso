---
name: create-prd
description: Crea un PRD (Product Requirements Document) verificable siguiendo la metodología del curso AI-First Builders Lab. Úsalo cuando el usuario quiera escribir, armar o generar un PRD para un proyecto/idea, partiendo de un pitch crudo. Produce el qué y el por qué con RF atómicos, RNF con números y AC binarios (Dado/Cuando/Entonces), todos trazables por ID.
---

# create-prd

Genera un PRD **verificable**: un contrato de producto que la IA (o un humano) puede construir y comprobar sin resolver ambigüedades por su cuenta. Un requerimiento vago es una invitación a que el agente invente; uno verificable no deja lugar: o se cumple o no.

## Alcance: PRD, no spec

El PRD es el **qué** y el **por qué**, con sus criterios de aceptación. No es el **cómo** técnico (eso es el spec: diseño + tests, viene después). No inventes diseño, stack ni arquitectura salvo que el usuario lo pida. El spec cubrirá cada RF con diseño y cada AC con un test.

## Flujo de trabajo

1. **Pitch crudo.** Si el usuario no lo dio, pídele una o dos frases en lenguaje natural: qué quiere construir y para qué. No avances sin esto.
2. **Bajar al template.** Llena cada sección del template de abajo, aunque sea en borrador. No frenes en redactar lindo primero; primero completar.
3. **Apretar cada pieza con las preguntas de calidad** (checklist de abajo). Recorre requerimiento por requerimiento y corrige todo lo flojo. Aquí un punteo de buenas intenciones se vuelve un contrato.
4. **Cerrar el alcance.** Escribe explícitamente qué NO entra. Todo lo que no excluyas, se asume incluido (ahí nace el scope creep).

Si algo del pitch es ambiguo (persona, métrica, límite de alcance), **pregunta** en lugar de inventar. Un dato inventado en el PRD se propaga a todo lo que se construya encima.

## Template

Cópialo y complétalo. Numera el PRD (PRD-001, PRD-002…) y usa IDs para trazar (RF-01, RNF-01, AC-01).

```markdown
# PRD-00N: <nombre del proyecto> — <una línea de qué es>

## Contexto y Problema
<Qué dolor real resuelves y para quién. Cuenta una historia humana con personas
nombradas (no "el usuario"): quién lo usa y qué necesita. Si no hay dolor, no hay app.>

## Objetivos
<Qué significa ganar, a nivel producto.>

## Requerimientos Funcionales
- RF-01: El sistema debe <una acción, verbo imperativo>.
- RF-02: ...

## Requerimientos No Funcionales
- RNF-01: <cualidad con número: "< 3 s p95", "≥ 85%", "hash bcrypt/argon2">.

## Criterios de Aceptación
- AC-01 (RF-01): Dado <contexto>, cuando <acción>, entonces <resultado medible>.

## Fuera de Alcance
- <Lo que explícitamente NO entra.>

## Riesgos y Dependencias
- Riesgo: <qué puede salir mal> → mitigación: <cómo lo cubres>.
- Dependencia: <de qué depende para funcionar>.
```

## Reglas por sección

- **Contexto y Problema:** historia humana con personas nombradas y su necesidad concreta. Evita "el usuario".
- **Requerimientos Funcionales (RF):** **atómicos** (una sola acción por RF) y con **verbo imperativo "debe"**. Nunca "debería". Ej: *"El sistema debe permitir crear un ticket con asunto y descripción."*
- **Requerimientos No Funcionales (RNF):** cualidades **con número**. "Rápido" no es un requisito; "< 3 s p95" sí. Sin métrica es un deseo, no un requerimiento.
- **Criterios de Aceptación (AC):** formato **Dado / Cuando / Entonces**, cada uno **binario** (pasa/no pasa) y **atado a un RF concreto** por ID. Nada de "correctamente", "adecuado" o "bien". Incluye casos de borde y de seguridad (p. ej. que un usuario no vea datos de otro → control de acceso).
- **Fuera de Alcance:** lista explícita de lo que NO entra. Aclara excepciones si algo cercano SÍ entra.
- **Riesgos y Dependencias:** cada riesgo con su mitigación; cada dependencia externa nombrada.

## Checklist de calidad (aplícalo antes de entregar)

- [ ] ¿Cada RF es atómico (una sola acción)?
- [ ] ¿Cada RF dice "debe" (imperativo), no "debería"?
- [ ] ¿Cada RNF tiene un número/métrica?
- [ ] ¿Cada AC es binario (pasa/no pasa), sin "correctamente"/"adecuado" escondidos?
- [ ] ¿Cada AC está atado a un RF por ID?
- [ ] ¿Cada RF tiene al menos un AC que lo verifique?
- [ ] ¿Todos los elementos tienen IDs (RF-01, RNF-01, AC-01) para trazar?
- [ ] ¿El "Fuera de Alcance" corta el scope de forma explícita?
- [ ] ¿El contexto cuenta una historia humana con personas nombradas?

Regla mental: si cada RF tiene un AC que lo verifica, cada RNF tiene un número y cada AC es binario y trazable, tienes un PRD que se puede construir y comprobar.

## Salida

- Guarda el PRD en la raíz del proyecto como `prd-<tema-en-kebab>.md` (o el nombre que pida el usuario).
- Un PRD es un documento vivo: entrégalo como primera versión sólida y verificable; se afinará al construir.
- Si el usuario también quiere una versión en prosa/redacción corrida para leer, ofrécela como archivo aparte (`prd-<tema>-redaccion.md`), sin reemplazar el PRD estructurado.
