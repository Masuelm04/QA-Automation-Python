# QA Automation Python Roadmap

> Repositorio de aprendizaje práctico de **Python** orientado a **QA Automation**.
>
> Aquí documento mi progreso mediante ejercicios y proyectos prácticos que fortalecen las bases necesarias para posteriormente integrar herramientas como **Playwright**, **Pytest** y frameworks de automatización más avanzados.

---

# 📚 Objetivos

El objetivo principal de este repositorio es evidenciar mi progreso en el aprendizaje de **Python** aplicado a QA Automation.

A través de este roadmap practico conceptos como:

- Fundamentos de Python
- Variables, condicionales y bucles
- Listas, tuplas, sets y diccionarios
- Funciones
- Programación Orientada a Objetos (POO)
- Manejo de excepciones
- Lectura de archivos CSV y JSON
- Consumo de APIs REST
- Validaciones con `assert`
- Separación de responsabilidades en un mini framework
- Organización de código por paquetes y módulos
- Preparación para automatización con Playwright

---

# 🛠️ Tecnologías

- Python
- Requests
- JSON
- CSV
- Git
- GitHub
- Visual Studio Code

---

# 📁 Estructura del proyecto

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
```

---

# 📖 Contenido del repositorio

## 🟢 Semana 1 - Fundamentos de Python

Introducción a los conceptos básicos del lenguaje.

**Temas trabajados:**

- Variables
- Tipos de datos
- Condicionales
- Bucles

---

## 🔵 Semana 2 - Estructuras de datos y funciones

Práctica de las estructuras de datos más utilizadas en Python.

**Conceptos:**

- Listas
- Diccionarios
- Funciones
- Manipulación de datos

---

## 🟣 Semana 3 - Programación Orientada a Objetos

En esta etapa se profundiza en la organización del código y conceptos fundamentales para el desarrollo de aplicaciones más mantenibles.

**Conceptos:**

- Programación Orientada a Objetos (POO)
- Clases
- Objetos
- Métodos
- Módulos
- Paquetes
- Manejo de excepciones

---

## 🔴 Semana 4 - Automatización básica de APIs

Construcción de un pequeño proyecto simulando un framework de automatización.

**Incluye:**

- Consumo de APIs REST
- Organización por capas
- Modelos
- Servicios
- Utilidades
- Casos de prueba

---

## 📝 Carpeta ejercicios

Contiene ejercicios prácticos independientes para reforzar los conceptos aprendidos.

**Incluye prácticas de:**

- Variables
- Bucles
- Enumerate
- Sets
- Tuplas
- Assertions
- Consumo de APIs
- Funciones integradas

---

## 📄 Carpeta csv

Ejercicios relacionados con lectura y procesamiento de archivos CSV.

**Conceptos:**

- Lectura de archivos
- Iteración de registros
- Procesamiento de datos

---

## 📄 Carpeta json

Ejercicios para trabajar con archivos JSON.

**Conceptos:**

- Lectura
- Escritura
- Conversión de datos

---

## 🏗️ mini_framework_api

Proyecto donde se aplican los conceptos aprendidos para construir un pequeño framework orientado a pruebas de API utilizando Python puro.

**Objetivos:**

- Separación de responsabilidades
- Organización del proyecto
- Reutilización de código
- Buenas prácticas

---

# 🌐 API utilizada

Para las prácticas de automatización de APIs se utilizó:

> https://jsonplaceholder.typicode.com

---

# ▶️ Cómo ejecutar el proyecto

## 1. Clonar el repositorio

```bash
git clone https://github.com/Masuelm04/QA-Automation-Python.git
```

## 2. Entrar al proyecto

```bash
cd QA-AUTOMATION-PYTHON
```

## 3. Crear un entorno virtual

```bash
python -m venv .venv
```

## 4. Activar el entorno virtual

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

## 5. Instalar dependencias

```bash
pip install requests
```

## 6. Ejecutar las pruebas

```bash
python -m semana4.automatizacion_simple.tests.test_users
```

```bash
python -m semana4.automatizacion_simple.tests.test_posts
```

---

# 🎯 Conceptos practicados

- ✅ Variables
- ✅ Condicionales
- ✅ Bucles
- ✅ Funciones
- ✅ Listas
- ✅ Tuplas
- ✅ Sets
- ✅ Diccionarios
- ✅ Enumerate
- ✅ Programación Orientada a Objetos
- ✅ Módulos y Paquetes
- ✅ Manejo de excepciones
- ✅ Lectura de archivos CSV
- ✅ Lectura de archivos JSON
- ✅ Consumo de APIs REST
- ✅ Assertions
- ✅ Organización de proyectos
- ✅ Mini Framework API

---

# 💼 Objetivo profesional

Este repositorio forma parte de mi preparación como **QA Automation Engineer**, donde fortalezco mis conocimientos de **Python** mediante ejercicios progresivos y proyectos prácticos, construyendo una base sólida para el desarrollo de frameworks de automatización, pruebas de APIs y automatización de interfaces web.

---

# ⭐ Si este repositorio te resulta útil

Si este contenido te ha servido como guía para aprender Python aplicado a QA Automation, considera dejar una ⭐ al repositorio.
