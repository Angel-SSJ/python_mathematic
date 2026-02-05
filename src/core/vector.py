import numpy as np
from typing import List, Union, Any, override
from src.core.mathematical_object import MathematicalObject
from src.core.operations_vector import OperationsVector

class Vector(MathematicalObject, OperationsVector):

    def __init__(self, components: Union[List[float], np.ndarray]):
        self.components = np.array(components, dtype=np.float64)
        self.dimension = self.components.size

    def validate_vector(self, other: Any):
        if not isinstance(other, Vector):
            if isinstance(other, np.ndarray):
                if other.size != self.dimension:
                    raise ValueError(f"Dimensión incompatible: {self.dimension} vs {other.size}")
                return
            raise TypeError("Se requiere un objeto Vector o numpy array")
        if self.dimension != other.dimension:
            raise ValueError(f"Los vectores deben tener la misma dimensión ({self.dimension} != {other.dimension})")

    def validate_scalar(self, scalar: Any):
        if not isinstance(scalar, (int, float, np.number)):
            raise TypeError("El escalar debe ser un número (int o float)")

    def validate_magnitude(self, magnitude: float):
        if np.isclose(magnitude, 0):
            raise ValueError("La magnitud no puede ser cero para esta operación")

    def __str__(self) -> str:
        return f"Vector({', '.join(map(lambda x: format(x, '.4f').rstrip('0').rstrip('.'), self.components))})"

    @override
    def add(self, other: 'Vector') -> 'Vector':
        self.validate_vector(other)
        other_comp = other.components if isinstance(other, Vector) else other
        return Vector(self.components + other_comp)

    @override
    def sub(self, other: 'Vector') -> 'Vector':
        self.validate_vector(other)
        other_comp = other.components if isinstance(other, Vector) else other
        return Vector(self.components - other_comp)

    @override
    def mul(self, other: Any) -> 'Vector':
        if isinstance(other, (int, float, np.number)):
            return self.scalar_product(other)
        elif isinstance(other, Vector):
            return Vector(self.components * other.components)
        raise TypeError("Multiplicación no soportada para este tipo")

    @override
    def div(self, other: Union[float, int]) -> 'Vector':
        self.validate_scalar(other)
        if np.isclose(other, 0):
            raise ZeroDivisionError("División por cero")
        return Vector(self.components / other)

    @override
    def magnitude(self) -> float:
        return float(np.linalg.norm(self.components))

    @override
    def normalize(self) -> 'Vector':
        mag = self.magnitude()
        self.validate_magnitude(mag)
        return Vector(self.components / mag)

    @override
    def scalar_product(self, scalar: float) -> 'Vector':
        self.validate_scalar(scalar)
        return Vector(self.components * scalar)

    @override
    def dot_product(self, other: Union['Vector', np.ndarray]) -> float:
        self.validate_vector(other)
        other_comp = other.components if isinstance(other, Vector) else other
        return float(np.dot(self.components, other_comp))

    @override
    def angle(self, other: 'Vector') -> float:
        self.validate_vector(other)
        dot = self.dot_product(other)
        m1 = self.magnitude()
        m2 = other.magnitude()
        self.validate_magnitude(m1)
        self.validate_magnitude(m2)

        cos_theta = np.clip(dot / (m1 * m2), -1.0, 1.0)
        return float(np.degrees(np.arccos(cos_theta)))

    @override
    def cross_product(self, other: 'Vector') -> 'Vector':
        self.validate_vector(other)
        if self.dimension not in (2, 3):
            raise ValueError("El producto cruz solo está definido para 2D o 3D")
        return Vector(np.cross(self.components, other.components))

    @override
    def distance(self, point: 'Vector', p0: 'Vector') -> float:
        self.validate_vector(point)
        self.validate_vector(p0)

        p_minus_p0 =  point.components - p0.components
        cross = np.cross(self.components, p_minus_p0)
        numerator = np.linalg.norm(cross)
        denominator = self.magnitude()
        self.validate_magnitude(denominator)


        return float(numerator / denominator)

    @override
    def orthogonality(self, other: 'Vector') -> bool:
        self.validate_vector(other)
        return bool(np.isClose(self.add(other).magnitude(), self.sub(other).magnitude(), atol=1e-9))

    @override
    def vector_projection(self, u: 'Vector') -> 'Vector':
        self.validate_vector(u)
        v_mag_sq = self.magnitude()**2
        self.validate_magnitude(v_mag_sq)

        dot_uv =  self.dot_product(u)
        return Vector((dot_uv / v_mag_sq) * self.components)

    @override
    def vector_equation(self, point: 'Vector') -> str:
        self.validate_vector(point)
        return f"P = {point} + t{self}"
