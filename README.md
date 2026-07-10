# 🐧Penguins Analytics Dashboard

Aplicación de análisis de datos construida con **Python**, **Streamlit**, **pandas** y **pytest**, desarrollada bajo un flujo de trabajo **Gitflow**. El proyecto permite validar, explorar y visualizar el dataset `penguins.csv` mediante una interfaz web simple, clara y orientada a la toma de decisiones.

---

## 📃Resumen Ejecutivo

| Elemento | Descripción |
| --- | --- |
| Proyecto | Dashboard Streamlit para análisis del dataset Penguins |
| Objetivo | Cargar, validar y visualizar información relevante del archivo `penguins.csv` |
| Enfoque técnico | Desarrollo por ramas con Gitflow, pruebas automatizadas y documentación formal |
| Versión entregable | `v1.0.0` |
| Autores | Oscar Maldonado, Daniel Alquinga |

---

## ✳️Propósito

El propósito del proyecto es entregar una aplicación reproducible para analizar datos de pingüinos, incorporando controles básicos de calidad sobre el archivo de entrada y una visualización tabular que permita inspeccionar la información por especie e isla.

La solución demuestra buenas prácticas de control de versiones, separación funcional del código, validación de datos y pruebas unitarias.

---

## 📚Funcionalidades

- Carga automática del archivo `penguins.csv`.
- Validación de existencia del archivo.
- Validación de columnas obligatorias del dataset.
- Validación de que el dataset no esté vacío.
- Métricas generales: registros, columnas, especies e islas disponibles.
- Gráfico de distribución por especie.
- Visualización tabular con filtros por especie e isla.
- Vista previa y tabla completa de datos.
- Resumen estadístico de columnas numéricas.
- Pruebas unitarias con `pytest`.

---

## 📇Tecnologías Utilizadas

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=fff)](#)
[![Matplotlib](https://custom-icon-badges.demolab.com/badge/Matplotlib-71D291?logo=matplotlib&logoColor=fff)](#)
[![Pytest](https://img.shields.io/badge/Pytest-fff?logo=pytest&logoColor=000)](#)
![GitFlow](https://img.shields.io/badge/GitFlow-Workflow-blue)


| Tecnología | Uso |
| --- | --- |
| Python | Lenguaje principal del proyecto |
| Streamlit | Construcción del dashboard web |
| pandas | Carga, validación y análisis de datos |
| matplotlib | Generación del gráfico principal |
| pytest | Pruebas unitarias |
| Git / Gitflow | Control de versiones y organización del desarrollo |

---

## 📂 Estructura Del Proyecto

```text
Tarea1Gitflow/
├── app.py
├── penguins.csv
├── requirements.txt
├── README.md
├── INFORME.md
├── .gitignore
├── docs/
│   └── .gitkeep
├── src/
│   ├── __init__.py
│   ├── validators.py
│   └── data_view.py
└── tests/
    ├── __init__.py
    └── test_validators.py
```

---

## 💾 Instalación

[![Informe Instalación](https://img.shields.io/badge/INSTALACIÓN-verde?style=for-the-badge)](./INFORME.md)

## 👬Autores

| Integrante | Rol | Url Git |
| --- | --- | --- |
| Oscar Maldonado | Desarrollo, documentación y control de versiones | https://github.com/Oscar112248/Tarea1Gitflow |
| Daniel Alquinga | Validación funcional, revisión y evidencias | https://github.com/superdavi/Gitflow_Tarea_1 |
