import sympy as sp
from sympy import Expr
from typing import List
from .types import Variables,Expressions,Derivatives
from .derivative import Derivative
from .types import Expression
from .interfaces.Ioperations_derivatives import IOperationsDerivatives
from typing import override

class OperationsDerivatives(IOperationsDerivatives):

    def __init__(self):

        self.derivatives:Derivatives = Derivatives()
        self.expressions:Expressions = Expressions()

    @override
    def get_parent_derivatives(self):
        return self.derivatives.parents

    @override
    def get_child_derivatives(self):
        return self.derivatives.childs

    @override
    def get_expressions(self):
        return self.expressions

    @override
    def clear_parent_derivatives(self):
        self.derivatives.parents.clear()

    @override
    def clear_child_derivatives(self):
        self.derivatives.childs.clear()

    @override
    def clear_expressions(self):
        self.expressions.clear()

    @override
    def clear_all(self):
        self.clear_parent_derivatives()
        self.clear_child_derivatives()
        self.clear_expressions()

    @override
    def set_expression(self,expression:Expression):
        self.clear_expressions()
        self.expressions.values.append(expression)

    @override
    def add_expression(self,expression:Expression):
        self.expressions.values.append(expression)

    @override
    def remove_expression(self,type:str):
        # Se remueve una expression buscando por el tipo
        for idx in range(len(self.expressions.values)):
            if self.expressions.values[idx].type == type:
                self.expressions.values.pop(idx)

    @override
    def get_chain_rule(self):


        # Se capturan las variables de la derivada hija
        variables = self.derivatives.childs[0].variables


        # se recorren las derivadas padres
        for parent in self.derivatives.parents:
            # se inicializa un diccionario con las variables de la derivada hija
            results = {var: 0 for var in variables}

            # se calculan las derivadas parciales de cada derivada padre
            parent.set_partial_derivatives()

            for child in self.derivatives.childs:
                # se  calculan las derivadas parciales de cada derivada hija
                child.set_partial_derivatives()

                # se captura la derivada parcial de la derivada padre segun la variable de la derivada hija
                # ejemplo: wx => Xu
                parent_partial = next(
                    (p for p in parent.partial_derivatives if p.variable == child.name),None
                )

                if parent_partial:
                    # se recorren las derivadas parciales de la derivada hija actual
                    for child_partial in child.partial_derivatives:
                        # se guarda el valor de la operacion entre derivadas parciales el campo correspondiente
                        # {x:wx*Xu}
                        results[child_partial.variable] += sp.sympify(parent_partial.expression) * sp.sympify(child_partial.expression)

            # Se guurda la expression resultante dw/du=WxXu+WyYu
            self.add_expression(Expression(type="chain_rule", value=results, name=parent.name))
            final_result = {var: sp.simplify(expr) for var, expr in results.items()}


            # Se las respectivas expresiones dw/du y dw/dv
            for var, expr in final_result.items():
                print(f'\nd{parent.name}/d{var} = {expr}\n')


    def evaluate_chain_rule(self):

        # Sustitución de variables intermedias
        # por ejemplo: {x: 2*v-u**2,y: v-u}
        # se crea una key por cada child.name (relacionada a variable de la derivada padre) y se asigna el valor de le child expression
        intermediate_subs = {
            sp.symbols(child.name): sp.sympify(child.expression.value)
            for child in self.derivatives.childs
        }


        # Se capturan las variables de la derivada hija
        independent_vars = self.derivatives.childs[0].variables
        # Se captura el punto de evaluacion de la derivada hija
        point = self.derivatives.childs[0].evaluated_point
        # Se inicializa un diccionario con las variables y valores de la derivada hija
        points_subs = {sp.symbols(var): val for var, val in zip(independent_vars, point)}

        # Se imprimen los puntos de evaluacion
        print("\n--- Puntos de evaluación ---")
        for var, val in points_subs.items():
            print(f"{var} = {val}")

        # Se recorren las expresiones
        for expression in self.expressions.values:
            # Se verifica que la expression seta de tipo chain_rule
            if expression.type == "chain_rule":
                # Se recorren los items del campo expression.value

                for var, expr in expression.value.items():
                    # ejemplo: {v: 4*u*v*exp(x*u)}
                    print(f'\n --- d{expression.name}/d{var} ---')
                    # convertir la expresion normal en una expresion simbólica
                    result = sp.sympify(expr)
                    # sustituir las variables intermedias
                    result = result.subs(intermediate_subs)
                    # sustituir los puntos de evaluacion
                    result = result.subs(points_subs)

                    print(f'd{expression.name}/d{var} = {result}\n')




    @override
    def set_parent_derivatives(self,derivative:Derivative):
        self.clear_parent_derivatives()
        self.derivatives.parents.append(derivative)

    @override
    def add_parent_derivative(self,derivative:Derivative):
        self.derivatives.parents.append(derivative)

    @override
    def set_child_derivatives(self,derivative:Derivative):
        self.clear_child_derivatives()
        self.derivatives.childs.append(derivative)

    @override
    def add_child_derivative(self,derivative:Derivative):
        self.derivatives.childs.append(derivative)

    @override
    def set_parent_partial_derivarive(self):
        for derivative in self.derivatives.parents:
            derivative.set_partial_derivatives()

    @override
    def set_child_partial_derivarive(self):
        for derivative in self.derivatives.childs:
            derivative.set_partial_derivatives()
