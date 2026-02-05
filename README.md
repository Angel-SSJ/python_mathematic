# Python Mathematic Repository

Este repositorio contiene implementaciones de tareas matemáticas (Vectores, Matrices, etc.) utilizando Python, POO de nivel intermedio y NumPy para alto rendimiento.

## Características

- ✅ **Operaciones Vectoriales completas**: Magnitud, normalización, producto escalar, producto vectorial, ángulos, proyecciones, distancias y ecuaciones vectoriales
- ✅ **Arquitectura limpia**: Interfaces abstractas (`MathematicalObject`, `OperationsVector`) con herencia múltiple
- ✅ **Alto rendimiento**: Uso de NumPy para todas las operaciones matemáticas
- ✅ **Interfaz en español**: Todos los mensajes, menús y prompts están en español
- ✅ **Validación robusta**: Validación de tipos y valores con mensajes de error descriptivos
- ✅ **Sistema de menú interactivo**: CLI amigable con manejo de errores y confirmaciones

## Estructura del Proyecto

El proyecto está diseñado para ser modular y escalable.

- `src/core/`: Contiene las clases base abstractas, interfaces y implementaciones core
  - `mathematical_object.py`: Clase base para objetos matemáticos
  - `operations_vector.py`: Interfaz de operaciones vectoriales
  - `vector.py`: Implementación de la clase Vector con NumPy
- `src/utils/`: Utilidades compartidas (Input handlers, Menús)
- `src/tasks/`: Implementaciones específicas de cada tarea

## Requisitos

- Python 3.8+
- NumPy

## Instalación

```bash
pip install numpy
```

## Ejecución

Para ejecutar la tarea de operaciones vectoriales:

```bash
python -m src.tasks.task_01_vectors.main
```

## Documentación

- [`SYSTEM_FILES.md`](SYSTEM_FILES.md): Estructura detallada del proyecto
- [`PATTERNS_DESIGN.md`](PATTERNS_DESIGN.md): Patrones de diseño implementados
