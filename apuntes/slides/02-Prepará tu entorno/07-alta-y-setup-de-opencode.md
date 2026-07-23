---
titulo: "Alta y setup de OpenCode"
capitulo: "02-Prepará tu entorno"
orden: 7
source: "apuntes/slides/00-raw/02-Prepará tu entorno/07-Alta y setup de OpenCode – MUG.html"
source_sha256: 4e6c65634b2c050b
extraido: 2026-07-16
---

# Alta y setup de OpenCode

[Video de la lección](https://vimeo.com/1203089320)

**OpenCode** es el tercer agente: de **terminal**, **open-source** y **agnóstico de modelo** (le podés enchufar distintos proveedores de IA). Es muy parecido a Claude Code en su forma de trabajar — volvemos a la terminal, paso a paso. 🧩

## 📥 Paso 1: instalarlo

Abrí la terminal y pegá:

```
curl -fsSL https://opencode.ai/install | bash
```

Apretá Enter y esperá a que termine. **Cerrá y reabrí la terminal** (para que tome el nuevo comando) y verificá:

```
opencode --version
```

Si te devuelve una versión, ✅.

> 💡 Si `opencode` no se reconoce tras instalar, casi siempre se arregla **reabriendo la terminal**. Si preferís otro método de instalación, mirá la doc oficial.

## 🔑 Paso 2: conectar un proveedor de modelo

Como OpenCode es **agnóstico de modelo**, tenés que decirle **qué IA usar**. Tenés dos caminos cómodos y baratos:

- **OpenCode Zen:** del propio equipo de OpenCode. Vende los modelos **a precio de costo, sin margen de ganancia** (solo te traslada lo que cuesta el modelo + el procesamiento de pago). Modelos curados y testeados; pagás por uso.
- **OpenRouter:** la cuenta que ya creaste en *Requisitos*. Una pasarela con cientos de modelos y un **plan gratis** para arrancar (sin tarjeta); pagás solo si querés modelos más potentes.

Elegí **uno de los dos** — con cualquiera OpenCode anda perfecto.

Iniciá OpenCode:

```
opencode
```

Adentro, configurás el proveedor y su API key con el comando `/connect` (o `auth login`): elegí tu proveedor (**OpenCode Zen** u **OpenRouter**) y seguí lo que te indica en pantalla. Te va a pedir la **API key**, que sacás del panel del proveedor (en OpenRouter: *Keys → Create key*).

## ✅ Paso 3: probarlo

En una carpeta de prueba:

```
mkdir ~/opencode-test
cd ~/opencode-test
opencode
```

Pedile algo simple, por ejemplo: *«creá un archivo hola.txt con un saludo»*. Si responde y crea el archivo, **está andando** 🎉.

## 🎛️ La ventaja agnóstica (un adelanto)

A diferencia de Claude Code (atado a Claude) o Copilot, con OpenCode podés **cambiar de modelo sin reescribir tu flujo**. Eso tiene un valor estratégico (evitar el *lock-in*, es decir, no quedar atado a un solo proveedor) que vas a explotar en el Módulo 6. Por ahora, con que corra, alcanza.

> 🧩 **¿Y el `AGENTS.md`?** Sí, OpenCode también lee un archivo de contexto — y, como ya sabés, **eso se crea dentro del repo de cada módulo**, no acá.

## 🆘 Si algo no sale

- *«command not found: opencode»* → **reabrí la terminal**; si sigue, reintentá la instalación del Paso 1.
- *No responde / error de modelo* → revisá que hayas configurado bien el proveedor y sus claves en el Paso 2.

¡Tres agentes instalados! Solo queda **verificar que todo esté en orden** antes de la clase 1. ➡️
