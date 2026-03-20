from abc import ABC,abstractmethod
from ..types import Expression

class ITaylorSecondOrderPolynomial(ABC):
    @abstractmethod
    def set_taylor_second_order_polynomial(self):
        """Establecer el polinomio de segundo orden de Taylor"""
        pass

    @abstractmethod
    def get_taylor_second_order_polynomial(self):
        """Obtiene el polinomio de segundo orden de Taylor"""
        pass

    @abstractmethod
    def evaluate_taylor_second_order_polynomial(self):
        """Evaluar el polinomio de segundo orden de Taylor"""
        pass
