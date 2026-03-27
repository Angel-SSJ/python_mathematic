from abc import ABC, abstractmethod

class ILagrangianAnalysis(ABC):
    @abstractmethod
    def set_system_of_lagrangian_equations(self):
        """
        Define el sistema de ecuaciones de lagrange
        """
        pass

    @abstractmethod
    def get_system_of_lagrangian_equations(self):
        """
        Obtiene el sistema de ecuaciones de lagrange
        """
        pass

    @abstractmethod
    def set_lagrangian_function(self):
        """
        Define la ecuacion lagrangiana
        """
        pass
