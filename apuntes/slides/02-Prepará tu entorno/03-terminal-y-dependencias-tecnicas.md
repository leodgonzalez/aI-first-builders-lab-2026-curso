---
titulo: "Terminal y dependencias técnicas"
capitulo: "02-Prepará tu entorno"
orden: 3
source: "apuntes/slides/00-raw/02-Prepará tu entorno/03-Terminal y dependencias técnicas – MUG.html"
source_sha256: 227401d9ad7fcea2
extraido: 2026-07-16
---

# Terminal y dependencias técnicas

[Video de la lección](https://vimeo.com/1201573153)

Esta es **la lección más «técnica» de toda la preparación** — pero quedate tranquilo: la hacemos juntos, despacio, y **se resuelve todo copiando y pegando comandos**, sin bajar instaladores ni andar haciendo clic en mil ventanas. Si nunca tocaste una terminal, es la lección perfecta para perderle el miedo. 🧰

Al terminar vas a tener instaladas, **una sola vez**, todas las dependencias que los agentes necesitan para funcionar. Vamos una por una, sin apuro.

## 🖥️ ¿Qué terminal vas a usar? (esto importa)

En las demos del curso yo voy a trabajar en **Windows con WSL** — que es una **Ubuntu (Linux) corriendo adentro de Windows**. Te lo aclaro porque define qué comandos vas a copiar:

- 🪟 **Windows con WSL** o 🐧 **Linux** → es **exactamente lo mismo**. Los comandos que ves son idénticos a los que corro yo en pantalla.
- 🍎 **Mac** → es **prácticamente igual**: la terminal de Mac es muy parecida a la de Linux y los comandos del curso funcionan igual. La única diferencia está en *cómo se instala* cada herramienta (en Mac se usa **Homebrew**), así que, cuando haga falta, te dejo **la versión de Mac al lado**.

En resumen: seguí los comandos de **Linux/WSL** (los principales), o los de **Mac** si estás en una Mac. Cualquiera de los dos te deja en el mismo lugar.

## 1️⃣ Abrí la terminal

- 🪟 **Windows:** primero necesitás **WSL** (esa Ubuntu adentro de Windows):

1. Abrí **PowerShell como Administrador**: botón derecho en el menú inicio → *Terminal (Administrador)* (o *Windows PowerShell (Administrador)*).
2. Instalá **WSL** con:

```
wsl --install
```

Si te lo pide, **reiniciá Windows**.

1. Ahora instalá la distribución **Ubuntu 24.04**:

```
wsl --install Ubuntu-24.04
```

1. **Ubuntu se abre solo** y te pide crear un **usuario y contraseña** — poné los que quieras y **anotalos** (esa contraseña te la va a pedir cuando instales cosas).
2. Para abrir tu Ubuntu cuando quieras, buscá *Ubuntu* en el menú inicio (o escribí `wsl` en PowerShell). Esa ventana de Ubuntu **es tu terminal para todo el curso**.

- 🍎 **Mac:** apretá `Cmd + Espacio`, escribí **Terminal**, Enter.
- 🐧 **Linux:** `Ctrl + Alt + T`.

> 📌 **¿Cómo «corro un comando»?** Copiás la línea que te damos, la pegás (en WSL/Linux se pega con `Ctrl+Shift+V`; en Mac, `Cmd+V`), Enter, y mirás lo que aparece debajo. Y un detalle: cuando un comando empieza con `sudo`, te va a pedir **tu contraseña** (la que creaste). Escribila —ojo, **no se ve mientras tipeás, es normal**— y Enter.

## 🍎 Solo en Mac: instalá Homebrew primero

Si estás en **Mac**, antes que nada instalá **Homebrew**, que es el gestor con el que vas a instalar todo lo demás por terminal. Pegá esto y seguí lo que te indique (te puede pedir tu contraseña):

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Al terminar, ya tenés disponible el comando `brew`. *(En Linux/WSL no hace falta nada de esto: ya viene con `apt`, su propio gestor.)*

Ahora sí, las dependencias. Para cada una hacemos lo mismo: **primero verificamos si ya la tenés** (muchas veces ya está) y, si no, la instalamos con un comando. 👇

## 📦 Node.js — el motor de los agentes

**Qué es:** Node es lo que permite correr varias herramientas modernas (entre ellas, el Copilot CLI que vas a instalar más adelante). Necesitás la **versión 22 o mayor**. Fijate primero si ya lo tenés:

```
node --version
```

- ✅ Si ves `v22.x.x` (o mayor), ya está — pasá al siguiente.
- ❌ Si falta o es una versión vieja, instalalo:
- 🐧 **Linux / WSL Ubuntu** (un solo comando, copialo entero):

```
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash - && sudo apt install -y nodejs
```

- 🍎 **Mac:** `brew install node`

Volvé a correr `node --version`: tenés que ver `v22` o mayor. ✅

## 🔧 Git — para guardar tu código

**Qué es:** la herramienta estándar para **versionar** tu código — guardar el historial de cambios, volver atrás, no perder nada. La vas a usar todo el curso.

```
git --version
```

- ✅ `git version 2.x.x` → listo.
- ❌ Si falta:
- 🐧 **Linux / WSL:** `sudo apt install -y git`
- 🍎 **Mac:** `brew install git`

## 🐍 Python — lo necesita Spec Kit

**Qué es:** un lenguaje de programación. No vas a programar en él, pero una herramienta del curso (Spec Kit, Módulo 4) lo necesita por debajo. Pedimos **3.12 o mayor**.

```
python3 --version
```

- ✅ `Python 3.12.x` o mayor → perfecto.
- ❌ Si falta o es viejo:
- 🐧 **Linux / WSL:** `sudo apt install -y python3`
- 🍎 **Mac:** `brew install python`

## ⚡ uv — para instalar Spec Kit

**Qué es:** un gestor de paquetes de Python, moderno y rapidísimo. Lo usamos para instalar Spec Kit en un solo paso. Se instala igual en todos lados, por terminal:

```
curl -LsSf https://astral.sh/uv/install.sh | sh && source "$HOME/.local/bin/env"
```

Ese `&& source …` del final deja `uv` disponible en la terminal **al toque**, sin que tengas que cerrarla y reabrirla. Verificá:

```
uv --version
```

→ si te muestra un número de versión, salió bien. ✅

## 🧰 El CLI de Spec Kit

**Qué es:** la herramienta de *Spec-Driven Development* que vas a usar en el Módulo 4. Acá instalás su comando `specify`. Importante: **instalar no es usar** — recién lo vas a «enchufar» a un proyecto en el Módulo 4 (¿te acordás de instalar ≠ inicializar?). Con `uv` ya instalado:

```
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

Verificá:

```
specify --version
```

→ un número de versión = listo. ✅

## 🆘 Si algo no sale (es de lo más normal)

Trabarse en el setup **le pasa a todo el mundo**, no es señal de nada. La mayoría de las veces se arregla con algo tan tonto como **cerrar y reabrir la terminal** después de instalar algo. Si aun así no sale:

- **Copiá el error completo** (todo el texto raro que aparezca).
- **Pegalo en los comentarios de esta lección**, contando **en qué paso** estabas — te respondemos ahí.

No te claves una hora solo: preguntá y seguís. 🙌

Con la terminal abierta y todo instalado, ya tenés la base lista. Antes de instalar los agentes, una parada corta y clave: **cómo editar archivos y qué es Markdown**, eso que vas a usar en cada lección. 📝
