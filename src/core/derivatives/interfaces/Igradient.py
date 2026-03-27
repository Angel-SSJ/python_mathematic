from abc import ABC,abstractmethod
from ..types import Expression

class IGradient(ABC):
    @abstractmethod
    def get_gradient(self):
        """Obtiene el vector gradiente"""
        pass

    @abstractmethod
    def set_gradient(self):
        """Establece el vector gradiente de la expresión"""
        pass

    @abstractmethod
    def clear_gradient(self):
        """Limpia el vector gradiente"""
        pass

    @abstractmethod
    def get_symbolic_gradient(self):
        """Retorna el gradiente simbolico (sin evaluar en el punto) para adaptarse a problemas similares a lambda"""
        pass
