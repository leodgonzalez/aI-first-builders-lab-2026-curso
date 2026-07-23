---
titulo: "Alta y setup de Claude Code"
capitulo: "02-Prepará tu entorno"
orden: 5
source: "apuntes/slides/00-raw/02-Prepará tu entorno/05-Alta y setup de Claude Code – MUG.html"
source_sha256: cee66daa2cccc044
extraido: 2026-07-16
---

# Alta y setup de Claude Code

[Video de la lección](https://vimeo.com/1201623422)

**Claude Code** es el agente de terminal de Anthropic y el **tool principal del curso** (corre con tu cuenta Claude Pro). En esta lección lo dejamos instalado, logueado y respondiendo. 🤖

> 📍 **Una aclaración para todo el curso:** las demos las hacemos en **Linux** — y en Windows usamos **WSL**, que *es* Linux (lo dejaste listo en la lección de la terminal). Por eso los comandos que ves son los de Linux/Mac. Si usás otro sistema (Windows nativo, por ejemplo), **algún comando puede cambiar un poco**, pero la idea es siempre la misma. Ante la duda, mirá la doc oficial de cada herramienta.

## 📥 Paso 1: instalarlo

Vamos a usar el **instalador nativo** de Claude Code — es el método recomendado hoy: no necesita Node ni npm, y se **actualiza solo**. Abrí la terminal y pegá:

```
curl -fsSL https://claude.ai/install.sh | bash
```

Apretá Enter y esperá a que termine. Después **cerrá y reabrí la terminal** y verificá:

```
claude --version
```

Si te devuelve un número de versión, ✅ vas bien.

> 💡 Quizás veas tutoriales viejos que instalan Claude Code con `npm install -g @anthropic-ai/claude-code`. Eso **todavía funciona, pero quedó como método secundario** — el instalador nativo de arriba es el que Anthropic recomienda y mantiene al día. Más métodos en la [doc oficial](https://docs.claude.com/claude-code).

## 🔑 Paso 2: loguearte con tu cuenta Pro

Iniciá Claude Code escribiendo:

```
claude
```

La **primera vez** te va a abrir el navegador para hacer **login** (esto se llama *OAuth*: te autenticás en la web y la terminal queda conectada, sin pegar contraseñas).

- Iniciá sesión con la cuenta que tiene tu **Claude Pro**.
- Cuando termine, volvé a la terminal: ya vas a estar dentro de Claude Code (te aparece un prompt esperando que le escribas).

## ✅ Paso 3: probarlo en una carpeta de prueba

Vamos a confirmar que funciona. Creá una carpeta **de prueba** (¡no es tu proyecto todavía!) y abrí Claude Code ahí:

```
mkdir ~/claude-test
cd ~/claude-test
claude
```

Ahora, dentro de Claude Code, escribí en lenguaje normal:

```
Creá un archivo hola.txt con un saludo adentro.
```

**Qué deberías ver:** Claude te muestra que va a crear el archivo y te pide confirmación (o lo crea). Si después corrés `ls` (lista los archivos de la carpeta) y aparece `hola.txt`, **está andando** 🎉. Esa carpeta de prueba la podés borrar cuando quieras.

> 🧩 **¿Y el `CLAUDE.md`?** Quizás escuchaste de ese archivo que le dice a Claude cómo trabajar en un proyecto. **Eso lo creás dentro del repo de cada módulo, más adelante** — todavía no tenés un proyecto. Por ahora solo confirmamos que el agente corre.

## 🆘 Si algo no sale

- *«command not found: claude»* → reabrí la terminal (recién instalado, a veces hace falta para que lo «vea»). Si sigue, reintentá el Paso 1.
- *No abre el navegador para el login* → fijate si la terminal te muestra un **link**: copialo y pegalo en el navegador a mano.
- *Login rechazado* → asegurate de usar la cuenta con **Claude Pro activo**.

¿Trabado? Dejá tu consulta en los **comentarios al pie de esta lección** (con el error concreto) y te ayudamos. Con Claude Code andando, seguimos con **GitHub Copilot**. ➡️
