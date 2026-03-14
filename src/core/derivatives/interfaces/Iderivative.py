
from abc import ABC,abstractmethod
from ..types import Variables,Expression
from typing import List


class Iderivative(ABC):


    @abstractmethod
    def get_expression(self):
        """Obtiene la expresión de la derivada"""
        pass

    @abstractmethod
    def get_variables(self):
        """Obtiene las variables de la derivada"""
        pass

    @abstractmethod
    def get_derivative(self):
        """Obtiene datos globales de la derivada"""
        pass

    @abstractmethod
    def get_partial_derivatives(self):
        """Obtiene las derivadas parciales de la expresión"""
        pass

    @abstractmethod
    def get_evaluated_point(self):
        """Obtiene el punto de evaluación de la derivada"""
        pass

    @abstractmethod
    def get_derivative(self):
        """Obtiene la derivada de la expresión"""
        pass

    @abstractmethod
    def clear_partial_derivatives(self):
        """Limpia las derivadas parciales de la expresión"""
        pass

    @abstractmethod
    def clear_evaluated_point(self):
        """Limpia el punto de evaluación de la expresión"""
        pass

    @abstractmethod
    def clear_variables(self):
        """Limpia las variables de la expresión"""
        pass

    @abstractmethod
    def clear_expression(self):
        """Limpia la expresión de la derivada"""
        pass

    @abstractmethod
    def clear_all(self):
        """Limpia todas las variables de la expresión"""
        pass

    @abstractmethod
    def set_variables(self,variables:List[str]):
        """Establece las variables de la expresión"""
        pass

    @abstractmethod
    def set_expression(self,expression:str):
        """Establece la expresión de la derivada"""
        pass
    @abstractmethod
    def set_name(self,name:str):
        """Establece el nombre de la derivada"""
        pass

    @abstractmethod
    def set_evaluated_point(self,evaluated_point:List[float]):
        """Establece el punto de evaluación de la derivada"""
        pass

    @abstractmethod
    def set_partial_derivatives(self):
        """Establece las derivadas parciales de la expresión"""
        pass
