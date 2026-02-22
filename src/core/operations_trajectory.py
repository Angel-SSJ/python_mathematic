from abc import ABC, abstractmethod
from typing import Tuple, List, Union
import numpy as np

class OperationsTrajectory(ABC):
    """
    Interface que define las operaciones para el manejo y análisis de trayectorias.
    """

    @abstractmethod
    def validate_dimensions(self):
        """Valida que las dimensiones de la trayectoria sean coherentes."""
        pass

    @abstractmethod
    def validate_coordinates(self):
        """Valida que las coordenadas de la trayectoria sean válidas."""
        pass

    @abstractmethod
    def validate_point(self):
        """Valida que el punto de referencia para cálculos sea válido."""
        pass

    @abstractmethod
    def validate_coefficients(self, coefficients: Tuple[float, float, float]):
        """Valida los coeficientes utilizados para generar la trayectoria."""
        pass

    @abstractmethod
    def validate_limits(self, limits: Tuple[float, float]):
        """Valida los límites del parámetro (t_start, t_end)."""
        pass

    @abstractmethod
    def validate_amount_points(self, amount_points: int):
        """Valida que la cantidad de puntos sea un entero positivo."""
        pass

    @abstractmethod
    def validate_intercepted_coordinates(self):
        """Valida las coordenadas del punto de intersección o punto más cercano."""
        pass

    @abstractmethod
    def validate_projection(self, projection: str = '3d'):
        """Valida que la proyección (2D/3D) sea compatible con la trayectoria."""
        pass

    @abstractmethod
    def calculate_euclidean_distance(self, point: 'Vector', coordinate: Union[List[float], np.ndarray] = np.array([])):
        """Calcula la distancia euclidiana entre un vector y una coordenada específica."""
        pass

    @abstractmethod
    def calculate_shortest_euclidean_distance(self, point: 'Vector'):
        """
        Encuentra el punto más cercano en la trayectoria a un vector dado
        y calcula la distancia mínima.
        """
        pass

    @abstractmethod
    def helicoidal_trajectory(self, coefficients: Tuple[float, float, float], limits: Tuple[float, float], amount_points: int):
        """Genera los puntos de una trayectoria helicoidal."""
        pass

    @abstractmethod
    def display_trajectory(self, projection: str = '3d', type_trajectory: str = 'Helicoidal'):
        """Visualiza la trayectoria y los puntos de referencia en un gráfico."""
        pass
