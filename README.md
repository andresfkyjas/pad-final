# pad-final
# 🧠 Programación para Análisis de Datos – Clase 1

## 📌 Descripción
Este repositorio contiene los recursos y configuraciones necesarios para la **Clase 1** del curso **Programación para Análisis de Datos**. En esta sesión, los estudiantes aprenderán a:

- Instalar **Python 3.9.2** en Windows  
- Configurar **Visual Studio Code (VSCode)** como entorno de desarrollo  
- Instalar y configurar **Git** y **GitHub**  
- Crear y activar un entorno virtual con `venv`  
- Configurar el archivo **`.gitignore`**  
- Crear el archivo **`setup.py`** para la gestión del proyecto  
- Configurar un flujo de trabajo automatizado con GitHub Actions (`entregables.yml`)  

---

## 📁 Estructura del Proyecto
```plaintext
mi_proyecto/
├── src/
│   └── pad20251/
│       ├── __init__.py
│       ├── actividad_1.py
│       ├── actividad_2.py
│       ├── actividad_3.py
│       └── actividad_final.ipynb
├── venv/                   # Entorno virtual (excluido por .gitignore)
├── .gitignore
├── setup.py
├── README.md
└── .github/
    └── workflows/
        └── entregables.yml
🛠️ Requisitos Previos

    Windows 10 o superior

    Conexión a Internet

    Cuenta en GitHub
🧰 Instalación de Herramientas
1. Python 3.9.2

    Descarga el instalador desde:
    https://www.python.org/downloads/release/python-392/

    Ejecuta el instalador y marca “Add Python 3.9 to PATH”.

    Verifica la instalación en CMD:
      python --version
      pip --version
2. Visual Studio Code (VSCode)

    Descarga desde:
    https://code.visualstudio.com/

    Instala la extensión de Python desde el Marketplace de VSCode.

3. Git

    Descarga desde:
    https://git-scm.com/download/win

    Verifica la instalación:
      git --version
  
  🐍 Creación y Activación del Entorno Virtual
  
  En la carpeta raíz del proyecto, abre CMD o PowerShell y ejecuta:
      # Crear entorno
      python -m venv venv
      
      # Activar entorno
      .\venv\Scripts\activate
