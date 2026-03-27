from abc import ABC,abstractmethod
from ..types import Expression

class IHessianMatrix(ABC):
    @abstractmethod
    def get_hessian_matrix(self):
        """Obtener la matriz hessiana"""
        pass

    @abstractmethod
    def set_hessian_matrix(self):
        """Establecer la matriz hessiana"""
        pass

    @abstractmethod
    def clear_hessian_matrix(self):
        """Limpiar la matriz hessiana"""
        pass

    @abstractmethod
    def get_symbolic_hessian_matrix(self):
        """Retorna la matriz hessiana simbolica (sin evaluar en el punto) para adaptarse a problemas similares a lambda"""
        pass
