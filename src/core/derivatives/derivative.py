import sympy as sp
import re
from sympy import Symbol,Expr
from typing import List
from .types import Variables,Expression,PartialDerivative
from .interfaces.Iderivative import Iderivative
from typing import override



class Derivative(Iderivative):
    def __init__(
        self,
        expression:str = "",
        variables:List[str] = None,
        evaluated_point:List[float] = None,
        name:str = ""
        ):
        self.expression=expression
        self.variables = variables if variables is not None else []
        self.partial_derivatives = []
        self.evaluated_point = evaluated_point if evaluated_point is not None else []
        self.name = name

    @override
    def get_expression(self):
        return print(f'Expresión: {self.expression}')

    @override
    def get_variables(self):
        return print(f'Variables: {self.variables}')

    @override
    def get_partial_derivatives(self):
        return print(f'Derivadas parciales: \n {self.partial_derivatives}')

    @override
    def get_evaluated_point(self):
        return print(f'Punto de evaluación: {self.evaluated_point}')

    @override
    def get_derivative(self):
        print(f'Derivative: \n')
        self.get_expression()
        self.get_variables()
        self.get_partial_derivatives()

    @override
    def clear_partial_derivatives(self):
        self.partial_derivatives.clear()

    @override
    def clear_evaluated_point(self):
        self.evaluated_point.clear()

    @override
    def clear_variables(self):
        self.variables.clear()

    @override
    def clear_expression(self):
        self.expression = ""

    @override
    def clear_all(self):
        self.clear_partial_derivatives()
        self.clear_evaluated_point()
        self.clear_variables()
        self.clear_expression()

    @override
    def set_variables(self,variables:List[str]):

        self.clear_variables()
        pattern = r'^[a-zA-Z]\d?$'
        idx = 0

        while idx < len(variables):
            # Se validar si las variables insertadas son alfabeticas
            if not re.match(pattern,variables[idx]):
                raise ValueError(f"Variable inválida: {variables[idx]}")
            self.variables.append(variables[idx])
            idx += 1

    @override
    def set_expression(self,expression:str):
        self.clear_expression()
        self.expression = Expression(value=expression)

    @override
    def set_name(self,name:str):
        self.name = name

    @override
    def set_evaluated_point(self,values:List[float]):
        self.clear_evaluated_point()
        for value in values:
            # Se inserta cada valor como una coordenada del punto de evaluacion
            self.evaluated_point.append(value)

    @override
    def set_partial_derivatives(self):
        self.clear_partial_derivatives()
        for variable in self.variables:
            # Se convierte la variable en un operante valido
            current_variable = sp.Symbol(variable)
            # Se calcula la derivada parcial con respecto a la variable actual
            current_partial_derivative = sp.diff(self.expression.value,current_variable)
            # Se agrega la derivada parcial al listado
            self.partial_derivatives.append(PartialDerivative(variable=variable,expression=current_partial_derivative))
