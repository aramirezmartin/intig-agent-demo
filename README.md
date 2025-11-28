# 🤖 Demo init.g: Creación de Agentes con Google ADK

¡Bienvenido! Este repositorio contiene el código fuente y los ejemplos prácticos presentados en la sesión de **init.g**.

Aquí exploramos cómo diseñar, configurar y desplegar agentes de Inteligencia Artificial utilizando el framework **Google Gen AI Agent Development Kit (ADK)**.

## 📋 Descripción

Este proyecto es una demostración práctica que abarca:
- Configuración inicial de un proyecto ADK.
- Definición de flujos de conversación.
- Integración con modelos de Gemini.
- Despliegue del servidor de desarrollo local.

## 🚀 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado en tu sistema:
* **Python 3.10** o superior.
* **Git**.
* Una API Key de Google Cloud (Vertex AI) o Google AI Studio.

## 🛠️ Instalación y Configuración

Sigue estos pasos para preparar tu entorno de desarrollo local.

### 1. Clonar el repositorio

```bash
git clone git@github.com:aramirezmartin/intig-agent-demo.git
cd initg-agent-demo
```

### 2. Crear un entorno virtual

Es fundamental aislar las dependencias del proyecto. Ejecuta el siguiente comando en la raíz:

```bash
python -m venv venv
```

### 3. Activar el entorno virtual

El comando varía según tu sistema operativo:

* **macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```

* **Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```

* **Windows (CMD):**
  ```cmd
  venv\Scripts\activate
  ```

> **Nota:** Deberías ver `(venv)` al inicio de tu línea de comandos indicando que está activo.

### 4. Instalar dependencias

Instala todas las librerías necesarias, incluido el núcleo de Google ADK:

```bash
pip install -r requirements.txt
```

### 5. Configurar Variables de Entorno

Crea un un [API Key de Google AI](https://aistudio.google.com/api-keys) y guardararlo en `.env` de tu agent.

```bash
GOOGLE_API_KEY = <YOUR_API_KEY_HERE>
```

## 💻 Ejecución de la Demo

Una vez instalado todo, levanta el servidor de desarrollo local para interactuar con el agente:

1. **Iniciar el servidor ADK:**
   ```bash
   adk web
   ```

2. **Acceder a la interfaz:**
   Abre tu navegador web y ve a la siguiente dirección:

   👉 **[http://localhost:8000](http://localhost:8000)**

## 🤝 Contribución

Este es un proyecto educativo para el evento **init.g**. Si encuentras un error o quieres mejorar la demo, ¡los Pull Requests son bienvenidos!

---
Hecho con ❤️ para **init.g**
