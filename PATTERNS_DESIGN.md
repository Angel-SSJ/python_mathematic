# Patrones de Diseño Implementados

Este repositorio utiliza patrones de diseño de software para garantizar escalabilidad y mantenibilidad.

## 1. Strategy Pattern (Estrategia)
**Uso**: En el sistema de menús y operaciones.
**Descripción**: Encapsulamos cada opción del menú como una "estrategia" (función callback). Esto permite agregar nuevas opciones sin modificar la clase `Menu`.

## 2. Interface/Protocol Pattern (Interfaz)
**Uso**: En `OperationsVector`.
**Descripción**: Definimos una interfaz abstracta con todas las operaciones vectoriales requeridas (magnitude, normalize, dot_product, etc.). La clase `Vector` implementa esta interfaz, garantizando que todas las operaciones estén presentes.

## 3. Multiple Inheritance (Herencia Múltiple)
**Uso**: En la clase `Vector`.
**Descripción**: `Vector` hereda de `MathematicalObject` (operaciones básicas) y `OperationsVector` (operaciones vectoriales específicas), separando responsabilidades y manteniendo el principio de segregación de interfaces.

## 4. Validation Pattern (Patrón de Validación)
**Uso**: En métodos `validate_vector()`, `validate_scalar()`, `validate_magnitude()`.
**Descripción**: Centralizamos la validación de tipos y valores en métodos dedicados, mejorando la mantenibilidad y proporcionando mensajes de error claros en español.

## 5. NumPy Integration (Integración NumPy)
**Uso**: En todas las operaciones vectoriales.
**Descripción**: Delegamos cálculos matemáticos a NumPy para máximo rendimiento, usando `np.linalg.norm()`, `np.dot()`, `np.cross()`, etc. Los componentes se almacenan como `np.ndarray` con dtype `float64`.
