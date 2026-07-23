---
titulo: "Iterar con red: la disciplina del builder"
capitulo: "05-Módulo 3 Construí con red Git skills y disciplina"
orden: 3
leccion: "apuntes/slides/05-Módulo 3 Construí con red Git skills y disciplina/03-iterar-con-red-la-disciplina-del-builder.md"
---

# Iterar con red: la disciplina del builder

## De qué trata

La lección anterior dio la **herramienta** (Git); esta da el **método**. La tesis:
la IA va a alucinar y romper algo — no es «si», es «cuándo» —, así que la velocidad
sin red no es velocidad, es acelerar contra un paredón. La disciplina es lo que
te deja ir rápido de verdad.

## Los tres hábitos (Git como red)

| Hábito | Qué es | Por qué |
|---|---|---|
| **Commit-as-checkpoint** | Cada vez que algo funciona, commit. No esperás a «terminar la feature». | Cuanto más seguido commiteás, más corta es la distancia entre «se rompió» y «estoy sano». Con GitHub, cierra con `push` a `main`. |
| **Revertir en vez de parchar** | El agente se mandó una macana → `git restore` al último commit bueno y reintentar limpio. | Parchar apila fixes sobre código ya torcido. Reconstruir sobre base sana casi siempre es más rápido que desenredar la podrida. |
| **Diffs chicos** | `git diff` *antes* de aceptar. | Un cambio chico se revisa de un vistazo; uno gigante esconde problemas. Y si falla después, el culpable está acotado. |

> 🧠 **Poder deshacer una alucinación es la red de seguridad definitiva.** Con Git
> abajo, dejás que la IA experimente sin miedo: la vuelta está a un comando.

## El ritmo del builder

- **Pasos chicos** — una cosa a la vez, no «construime toda la app» y rezar.
  Acotado, verificable, reversible.
- **Verificá seguido** — correr y probar después de *cada* paso. Si se rompe, se
  rompió recién y sabés dónde.
- **Revisá siempre** — mirar el output antes de aceptarlo. El intern poderoso pero
  no confiable, otra vez. Aceptar sin leer es firmar sin leer.

No te hace más lento: te ahorra las vueltas largas de «¿en qué momento se rompió
todo esto?». Lo que «perdés» verificando lo recuperás no haciendo arqueología.

## Saber cuándo frenar

La señal de madurez que más cuesta: **tres vueltas enroscado → parar**. Si el
agente parchea sobre parches, cada prompt extra suma ruido, no te acerca.

> **Receta:** `git restore` al último estado bueno → replantear el pedido desde
> cero (mejor contexto, mejor prompt, quizás partir el problema en dos) → arrancar
> limpio.

El instinto dice «una más y sale». Pero insistir sobre un rumbo torcido no es
perseverancia, es cavar más hondo para salir del pozo. La sensación a reconocer:
**remar en dulce de leche**. Resetear sin culpa.

## El cierre

Ritmo y red, por ahora en la cabeza. La lección siguiente
([[04-ejercicio-guiado-prepara-tu-proyecto]]) las pasa a las manos: nace la carpeta
nueva del proyecto como repo, con sus primeros commits y push reales.
