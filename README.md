# QA Automation Python Roadmap

Este repositorio documenta mi proceso de aprendizaje y práctica con Python orientado a QA Automation, con el objetivo de fortalecer las bases necesarias para posteriormente integrar herramientas como Playwright, pytest y frameworks de automatización más avanzados.

El proyecto está organizado por semanas y módulos prácticos, comenzando desde fundamentos de Python hasta la creación de un mini framework para pruebas de API utilizando Python puro.

---

## Objetivo del repositorio

El objetivo principal de este repositorio es evidenciar mi progreso en el aprendizaje de Python aplicado a QA Automation.

A través de este roadmap practico conceptos como:

- Fundamentos de Python.
- Variables, condicionales y bucles.
- Listas, tuplas, sets y diccionarios.
- Funciones.
- Programación orientada a objetos.
- Manejo de excepciones.
- Lectura de archivos CSV y JSON.
- Consumo de APIs REST.
- Validaciones con `assert`.
- Separación de responsabilidades en un mini framework.
- Organización de código por paquetes y módulos.
- Preparación para automatización con Playwright.

---

## Tecnologías utilizadas

- Python
- Requests
- JSON
- CSV
- Git
- GitHub
- Visual Studio Code

---

## Estructura general del proyecto

```text
QA-AUTOMATION-PYTHON/
│
├── ejercicios/
│   ├── ejercicios_api_test.py
│   ├── ejercicios_assert.py
│   ├── ejercicios_bucles_for.py
│   ├── ejercicios_bucles_while.py
│   ├── ejercicios_enumerate.py
│   ├── ejercicios_len.py
│   ├── ejercicios_sets.py
│   ├── ejercicios_tuplas.py
│   └── ejercicios_variables.py
│
├── semana1/
│   ├── bucles.py
│   ├── condicionales.py
│   └── variables.py
│
├── semana2/
│   ├── diccionarios.py
│   ├── funciones.py
│   └── listas.py
│
├── semana3/
│   ├── modulos_y_paquetes/
│   ├── poo/
│   └── excepciones.py
│
├── semana4/
│   └── automatizacion_simple/
│       ├── api/
│       ├── data/
│       ├── models/
│       ├── services/
│       ├── tests/
│       └── utils/
│
├── csv/
│   ├── csv_reader.py
│   ├── empleados_activos.csv
│   ├── empleados.csv
│   └── usuario.csv
│
├── json/
│   ├── json_reader.py
│   └── usuario.json
│
├── mini_framework_api/
│   ├── api/
│   └── data/
│
├── .gitignore
└── README.md

---

## Para las prácticas de automatización API se utilizó:
https://jsonplaceholder.typicode.com

---

## Cómo ejecutar el proyecto

1. Clonar el repositorio:

git clone https://github.com/Masuelm04/QA-Automation-Python.git

2. Entrar al proyecto:

cd QA-AUTOMATION-PYTHON

3. Crear un entorno virtual:

python -m venv .venv

4. Activar el entorno virtual:

En Windows
.venv\Scripts\activate

En macOS/Linux:
source .venv/bin/activate

5. Instalar dependencias:

pip install requests

6. Ejecutar las pruebas del mini framework de automatizacion_simple:

python -m semana4/automatizacion_simple/tests/test_users.py
python -m semana4/automatizacion_simple/tests/test_posts.p