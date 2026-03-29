from abc import ABC,abstractmethod
from ..types import Expression

class IChainRule(ABC):
    @abstractmethod
    def get_chain_rule(self):
        """Obtiene la regla de la cadena"""
        pass

    @abstractmethod
    def evaluate_chain_rule(self):
        """Evalua la regla de la cadena"""
        pass
