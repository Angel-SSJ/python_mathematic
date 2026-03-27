from abc import ABC, abstractmethod
from typing import List

class IBorderedHessianMatrix(ABC):
    @abstractmethod
    def set_bordered_hessian_matrix(self):
        """Define la matriz Hessiana orlada"""
        pass

    @abstractmethod
    def get_bordered_hessian_matrix(self):
        """Obtiene la matriz Hessiana orlada"""
        pass
