from abc import ABC, abstractmethod
from typing import Any

class MathematicalObject(ABC):

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def add(self, other: 'MathematicalObject') -> 'MathematicalObject':
        pass

    @abstractmethod
    def mul(self, other: Any) -> 'MathematicalObject':
        pass
    @abstractmethod
    def sub(self, other: 'MathematicalObject') -> 'MathematicalObject':
        pass
    @abstractmethod
    def div(self, other: 'MathematicalObject') -> 'MathematicalObject':
        pass
