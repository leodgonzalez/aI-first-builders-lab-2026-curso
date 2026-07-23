---
titulo: "Ejercicio guiado: Prepará tu proyecto"
capitulo: "05-Módulo 3 Construí con red Git skills y disciplina"
orden: 4
source: "apuntes/slides/00-raw/05-Módulo 3 Construí con red Git skills y disciplina/04-Ejercicio guiado_ Prepará tu proyecto – MUG.html"
source_sha256: 85043872a901a78b
extraido: 2026-07-18
---

# Ejercicio guiado: Prepará tu proyecto

Este es el **primer ejercicio del módulo**, y es el momento de juntar las últimas dos lecciones y pasarlas por las manos. 🧰 Ya entendés la idea de Git (los save points, los cinco comandos) y la disciplina para usarlo (commit-as-checkpoint, revertir en vez de parchar, diffs chicos). Hoy nace el **hogar definitivo de tu proyecto**: una carpeta **nueva**, que arranca como **repo Git desde el día cero** y queda publicada en **GitHub**.

Y antes del primer paso, el recordatorio que ya viste en la intro del módulo —lo repito acá porque es *el* error a no cometer—:

> ⚠️ **NO pongas la carpeta de la v1 bajo Git.** La carpeta del módulo pasado **no se toca**: queda como está, de testigo de cómo se trabaja sin red. En este ejercicio creás un **directorio NUEVO** y copiás ahí **solo tres archivos**: `PRD.md`, `AGENTS.md` y `CLAUDE.md`. **El código de la v1 NO se copia** — la app se va a reconstruir en el repo nuevo, con red, a partir del PRD. Si te llevás el código viejo, te perdés el ejercicio entero del módulo.

¿Por qué así? Porque tu proyecto de verdad merece nacer bien: cada línea de la v2 va a existir *ya versionada*, con su historia desde el primer commit. Los documentos (el contrato y las reglas) son lo que vale oro y por eso viajan; el código, con todo lo que aprendiste desde entonces, sale mejor si lo reconstruís.

## 🛠️ Tu turno: paso a paso

⏱️ **Tiempo estimado:** ~25 min · 📦 **Entregable:** tu repo nuevo con `PRD.md` + `AGENTS.md` + `CLAUDE.md`, al menos 2 commits, publicado en GitHub, una reversión probada y un commit dirigido al agente.

**1. Creá la carpeta nueva y copiá los tres archivos.** El nombre que quieras (idealmente, el de tu app). Desde la carpeta de la v1, copiá **solo** `PRD.md` (tu v2, la que endureciste dirigiendo), `AGENTS.md` y `CLAUDE.md`. Nada más: ni código, ni carpetas, ni archivos sueltos.

**2. Convertila en repo.** Parado en la carpeta nueva, en la terminal:

```
git init
git branch -M main
```

Listo: la carpeta ahora tiene memoria (Git guarda lo suyo en una carpeta oculta `.git`), y su rama principal se llama `main` —el nombre estándar, el mismo que va a usar GitHub—.

**3. Primer save point.** Guardá la primera foto:

```
git add .
git commit -m "estado inicial: PRD + guardrails"
```

Verificalo con `git log --oneline`: tiene que aparecer tu commit, con su mensaje. Fijate que la foto es **liviana** —dos documentos y una línea de importación, ni un archivo de código—, y está perfecto que así sea: es el punto cero de tu proyecto real. Todo lo que se construya de acá en más nace **ya versionado**, algo que tu v1 nunca tuvo.

**4. Dale de alta en GitHub.** Ahora el espejo en la nube. Entrá a [github.com](https://github.com/) → **New repository** → poné el mismo nombre que tu carpeta → elegí **Private** (o Public, si querés mostrarlo) → y **NO marques** «Add a README» ni «.gitignore» (tu repo ya existe en tu máquina; lo queremos vacío del lado de GitHub). Al crearlo, GitHub te muestra los comandos para *«push an existing repository»*; son estos dos, con tu usuario y tu repo:

```
git remote add origin https://github.com/<tu-usuario>/<tu-repo>.git
git push -u origin main
```

Refrescá la página del repo: tus tres archivos están en la nube. 🎉 Y guardá esa URL —`https://github.com/<tu-usuario>/<tu-repo>`— porque **es la que vas a entregar al final del módulo**, con la app v2 adentro. A partir de acá, subir tus commits nuevos es una sola palabra: `git push`.

**5. Cambiá algo y mirá el diff.** Editá una línea de tu `PRD.md` (la que quieras). Antes de guardar, mirá qué cambió:

```
git diff
```

Fijate cómo Git te muestra exactamente la línea que tocaste (lo viejo en rojo, lo nuevo en verde). Este es el hábito de **diffs chicos** de la lección anterior: revisar *antes* de guardar. Si el cambio te cierra, segundo commit: `git add .` y `git commit -m "ajuste en el PRD"`.

**6. Rompé a propósito (la parte divertida).** Ensuciá tu `AGENTS.md`: borrale la mitad, escribí cualquier cosa arriba. Ahora, el botón de pánico:

```
git restore .
```

Abrilo de nuevo: **volvió, intacto**, al último commit. Eso que acabás de sentir —el alivio— es la lección entera de Git. Cuando la IA te rompa algo de verdad, ya sabés qué se siente y qué se hace.

**7. Ahora dirigí, no tipees.** Cerrá el círculo como builder: abrí **Claude Code** (`claude`) en la carpeta, hacé cualquier cambio chico (una línea más en el PRD) y pedíselo con palabras:

```
Commiteá este cambio con un mensaje claro y pushealo a main.
```

El agente corre el `add`, el `commit` y el `push` por vos. Esto es lo que viste en la lección de Git: **el agente maneja los comandos, vos entendés lo que está pasando** —por eso los aprendiste primero—. Verificá con `git log --oneline` que el commit está, y refrescá GitHub: el cambio ya tiene que estar arriba. Grabate este ritmo, porque es el del resto del curso: **funcionalidad lista → commit → push a `main`** — vos dirigís, la IA ejecuta.

> 💻 **¿Preferís verlo con el mouse?** Abrí la carpeta en **VS Code** (`code .`): en la pestaña de control de versiones ves los diffs coloreados y el historial de commits, clickeable. Mismo dato, sin terminal.

> ✅ **Lo lograste cuando** tu carpeta nueva es un repo con al menos 2 commits y **solo los tres archivos** (nada de código viejo), está **publicado en GitHub** (la URL abre y muestra tus archivos), **sentiste el alivio** de deshacer un desastre con `git restore`, y el agente hizo un commit + push **dirigido por vos** que verificaste en el historial y en la nube.

### 🔎 La muestra: TicketTriage, versionado y en la nube

Así quedó el historial de **TicketTriage** al salir de este ejercicio:

```
$ git log --oneline
8c2f4a1 docs: aclarar criterio de aceptación de control de acceso
7b40d12 estado inicial: PRD + guardrails
```

Dos fotos, cada una con su mensaje honesto, y el repo vivo en `github.com/<usuario>/tickettriage` con los mismos tres archivos: `PRD.md`, `AGENTS.md`, `CLAUDE.md`. La carpeta de la v1 sigue intacta donde estaba —nadie la tocó—; todo el futuro del proyecto pasa por acá. Ese es el punto de partida de un builder: no una carpeta suelta, un **proyecto versionado y respaldado**.

Tu proyecto quedó preparado: contrato (`PRD.md`), reglas (`AGENTS.md`), red (Git) y espejo (GitHub). Falta equiparlo con la pieza que más te separa de un prompter: **capacidades que el agente invoca solo cuando hacen falta** —los skills—. Y no con un ejemplo cualquiera: tu primer skill va a empaquetar un workflow que ya hiciste a mano y conocés bien. ➡️
