# Proyecto mínimo: Calculadora con Testing (UT 2.4)

**Autores:** _Tu nombre y el de tu compañero/a_  
**Profesor:** Pablo Vallejo  
**Asignatura:** UT 2.4 – Tipos de pruebas  

---

## Descripción

Este proyecto implementa una **calculadora básica** en Python con diferentes tipos de pruebas automatizadas usando `pytest`.

La aplicación incluye:
- Pruebas **unitarias** para funciones matemáticas básicas.
- Pruebas **de integración** que combinan lectura de archivo y cálculo.
- Pruebas **de sistema (E2E)** simulando el uso real del programa por consola.
- Una **prueba de humo** que verifica que la aplicación arranca sin errores.

---

## Estructura del proyecto

calculadora/
├── src/
│ └── calculadora.py
├── tests/
│ ├── test_unit.py
│ ├── test_integration.py
│ ├── test_system.py
│ └── test_smoke.py
├── data/
│ └── numeros.txt
├── main.py
├── Makefile
└── README.md

---

## Ejecución

Instala dependencias:
```bash
pip install pytest pytest-cov

--------------------

Ejecuta toda la suite de pruebas:

make test