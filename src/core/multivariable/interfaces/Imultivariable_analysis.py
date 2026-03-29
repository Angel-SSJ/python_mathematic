from abc import ABC,abstractmethod
from ..types import Expression

class IMultivariableAnalysis(ABC):

    @abstractmethod
    def get_parent_derivatives(self):
        """Obtiene las derivadas padres"""
        pass

    @abstractmethod
    def get_child_derivatives(self):
        """Obtiene las derivadas hijas"""
        pass

    @abstractmethod
    def get_expressions(self):
        """Obtiene las expresiones"""
        pass

    @abstractmethod
    def clear_parent_derivatives(self):
        """Limpia las derivadas padres"""
        pass

    @abstractmethod
    def clear_child_derivatives(self):
        """Limpia las derivadas hijas"""
        pass

    @abstractmethod
    def clear_expressions(self):
        """Limpia las expresiones"""
        pass

    @abstractmethod
    def clear_all(self):
        """Limpia todos los datos"""
        pass

    @abstractmethod
    def set_expression(self,expression:Expression):
        """Establece la expresión"""
        pass

    @abstractmethod
    def add_expression(self,expression:Expression):
        """Agrega una expresión"""
        pass

    @abstractmethod
    def remove_expression(self,type:str):
        """Remueve una expresión"""
        pass

    @abstractmethod
    def set_parent_derivatives(self,derivative:IFunction):
        """Establece las derivadas padres"""
        pass
    @abstractmethod
    def add_parent_function(self,derivative:IFunction):
        """Agrega una funcion padre"""
        pass


    @abstractmethod
    def set_child_derivatives(self,derivative:IFunction):
        """Establece las derivadas hijas"""
        pass
    @abstractmethod
    def add_child_function(self,derivative:IFunction):
        """Agrega una derivada hija"""
        pass

    @abstractmethod
    def set_parent_first_partial_derivarive(self):
        """Establece las derivadas parciales de las derivadas padres"""
        pass

    @abstractmethod
    def set_parent_second_partial_derivarive(self):
        """Establece las derivadas parciales de las derivadas padres"""
        pass

    @abstractmethod
    def set_child_first_partial_derivarive(self):
        """Establece las derivadas parciales de las derivadas hijas"""
        pass

    @abstractmethod
    def set_child_second_partial_derivarive(self):
        """Establece las derivadas parciales de las derivadas hijas"""
        pass
