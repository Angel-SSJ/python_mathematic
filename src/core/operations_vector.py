from abc import ABC, abstractmethod
import numpy as np

class OperationsVector(ABC):
    """
    Interface defining vector operations using NumPy arrays.
    """

    @abstractmethod
    def magnitude(self) -> float:
        """Calcula la magnitud (norma) del vector."""
        pass

    @abstractmethod
    def normalize(self) -> np.ndarray:
        """Retorna el vector unitario."""
        pass

    @abstractmethod
    def scalar_product(self, scalar: float) -> np.ndarray:
        """Multiplica el vector por un escalar."""
        pass

    @abstractmethod
    def dot_product(self, other: np.ndarray) -> float:
        """Calcula el producto escalar con otro vector."""
        pass

    @abstractmethod
    def angle(self, other: np.ndarray) -> float:
        """Calcula el ángulo entre este vector y otro en grados/radianes."""
        pass

    @abstractmethod
    def cross_product(self, other: np.ndarray) -> np.ndarray:
        """Calcula el producto vectorial con otro vector."""
        pass

    @abstractmethod
    def distance(self, point: np.ndarray, p0: np.ndarray) -> float:
        """
        Calcula la distancia de un punto a la recta definida por este vector.
        Formula: ||v x (P - Po)|| / ||v||
        """
        pass

    @abstractmethod
    def vector_projection(self, other: np.ndarray) -> np.ndarray:
        """
        Calcula la proyección del vector 'other' sobre este vector (self).
        Formula: ((other . self) / ||self||^2) * self
        """
        pass

    @abstractmethod
    def vector_equation(self) -> str:
        """Retorna la ecuación vectorial de la recta: P = Po + tV"""
        pass
