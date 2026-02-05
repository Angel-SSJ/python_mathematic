# Sistema de Archivos

```
python_mathematic/
├── .gitignore             # Configuración de Git
├── README.md              # Documentación general
├── SYSTEM_FILES.md        # Este archivo
├── PATTERNS_DESIGN.md     # Documentación de patrones
├── requirements.txt       # Dependencias
└── src/
    ├── core/              # NÚCLEO
    │   ├── __init__.py
    │   ├── mathematical_object.py  # Clase Base Abstracta (ABC) para objetos matemáticos
    │   ├── operations_vector.py    # Interfaz de operaciones vectoriales
    │   └── vector.py      # Clase Vector con NumPy
    ├── utils/             # UTILIDADES
    │   ├── __init__.py
    │   ├── input_handler.py # Validaciones de entrada (español)
    │   └── menu.py        # Sistema de menú CLI interactivo (español)
    └── tasks/             # TAREAS
        ├── __init__.py
        └── task_01_vectors/
            ├── __init__.py
            └── main.py    # Ejecutable de operaciones vectoriales (español)
```
