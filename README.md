# Python Mathematic Repository

Este repositorio contiene implementaciones de tareas matemáticas (Vectores, Matrices, etc.) utilizando Python, POO de nivel intermedio y NumPy para alto rendimiento.

## Características

- ✅ **Operaciones Vectoriales completas**: Magnitud, normalización, producto escalar, producto vectorial, ángulos, proyecciones, distancias y ecuaciones vectoriales
- ✅ **Cálculo de Trayectorias**: Generación de trayectorias helicoidales y cálculo de distancias euclidianas mínimas
- ✅ **Arquitectura limpia**: Interfaces abstractas (`MathematicalObject`, `OperationsVector`, `OperationsTrajectory`) con herencia múltiple
- ✅ **Alto rendimiento**: Uso de NumPy para todas las operaciones matemáticas y generación de puntos
- ✅ **Visualización Avanzada**: Gráficos 3D y 2D con Matplotlib para vectores y trayectorias
- ✅ **Interfaz en español**: Todos los mensajes, menús y prompts están en español
- ✅ **Validación robusta**: Validación de tipos y valores con mensajes de error descriptivos
- ✅ **Sistema de menú interactivo**: CLI amigable con manejo de errores y confirmaciones

## Estructura del Proyecto

El proyecto está diseñado para ser modular y escalable.

- `src/core/`: Contiene las clases base abstractas, interfaces y implementaciones core
  - `mathematical_object.py`: Clase base para objetos matemáticos
  - `operations_vector.py`: Interfaz de operaciones vectoriales
  - `operations_trajectory.py`: Interfaz de operaciones de trayectoria
  - `vector.py`: Implementación de la clase Vector con NumPy
  - `trajectory.py`: Implementación de la clase Trajectory para análisis de rutas
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

Para ejecutar la tarea de operaciones vectoriales (Tarea 01):
```bash
python -m src.tasks.task_01_vectors.main
```

Para ejecutar la tarea de trayectorias (Tarea 02):
```bash
python -m src.tasks.02_trajectories.main
```

## Documentación

- [`SYSTEM_FILES.md`](SYSTEM_FILES.md): Estructura detallada del proyecto
- [`PATTERNS_DESIGN.md`](PATTERNS_DESIGN.md): Patrones de diseño implementados
