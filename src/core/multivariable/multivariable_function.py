import sympy as sp
import re
from sympy import Symbol,Expr
from typing import List
from .types import Expression,IPartialDerivative,IVectorGradient,Expressions,IDerivatives
from .interfaces.Imultivariable_function import IMultivariableFunction
from .interfaces.Ihessian_matrix import IHessianMatrix
from .interfaces.Igradient import IGradient
from .interfaces.Itaylor_second_order_polynomial import ITaylorSecondOrderPolynomial
from typing import override



class MultivariableFunction(IMultivariableFunction,IHessianMatrix,IGradient,ITaylorSecondOrderPolynomial):
    def __init__(
        self,
        expressions:Expressions = None,
        variables:List[str] = None,
        evaluated_point:List[float] = None,
        name:str = ""
        ):
        self.expressions = expressions if expressions is not None else Expressions()
        self.variables = variables if variables is not None else []
        self.evaluated_point = evaluated_point if evaluated_point is not None else []
        self.name = name
        self.derivatives = IDerivatives()
        self.vector_gradient = IVectorGradient()
        self.hessian_matrix = []
        self.symbolic_hessian_matrix = []




    # GETTERS
    @override
    def get_expressions(self):
        return print(f'Expresión: \n {self.expressions.values}')

    @override
    def get_variables(self):
        return print(f'Variables: {self.variables}')

    @override
    def get_partial_derivatives(self):
        return print(f'Derivadas parciales: \n {self.derivatives.first_partials.values}')

    @override
    def get_evaluated_point(self):
        return print(f'Punto de evaluación: {self.evaluated_point}')

    @override
    def get_gradient(self):
        variables_str = ",".join(self.variables)
        print(f'∇{self.name}({variables_str}): {self.vector_gradient.values}')
        return self.vector_gradient.values


    @override
    def set_gradient(self):
        self.clear_gradient()
        subs = {sp.Symbol(v):val for v,val in zip(self.variables,self.evaluated_point)}
        for partial_derivative in self.derivatives.first_partials.values:
            evaluated = partial_derivative.expression.subs(subs)
            self.vector_gradient.values.append(evaluated)

    @override
    def set_symbolic_gradient(self):
        self.clear_gradient()
        for partial_derivative in self.derivatives.first_partials.values:
            self.vector_gradient.values.append(partial_derivative.expression)

    @override
    def get_symbolic_gradient(self):
        variables_str = ",".join(self.variables)
        print(f'∇{self.name}({variables_str}): {self.vector_gradient.values}')
        return self.vector_gradient.values

    @override
    def get_second_partial_derivatives(self):
        return print(f'Derivadas parciales de segundo orden: \n {self.derivatives.second_partials.values}')

    @override
    def get_hessian_matrix(self):
        return print(f'H({self.name}): \n {self.hessian_matrix}')


    @override
    def set_hessian_matrix(self):
        # Se limpia la matriz hessiana
        self.clear_hessian_matrix()
        # Se obtiene el numero de variables
        n = len(self.variables)
        # Se crea un diccionario con las variables y sus valores
        subs =  {sp.Symbol(v):val for v, val in zip(self.variables,self.evaluated_point)}
        # Se crea la matriz hessiana
        matrix = []
        for i in range(n):
            # Se crea una fila
            row = []
            for j in range(n):
                # Se calcula el indice
                idx = i*n+j
                # Se evalua la derivada parcial
                evaluated = self.derivatives.second_partials.values[idx].expression.subs(subs)
                # Se agrega la derivada parcial evaluada a la fila
                row.append(evaluated)
            matrix.append(row)
        self.hessian_matrix = matrix

    @override
    def set_symbolic_hessian_matrix(self):
        # Se obtiene el numero de variables
        self.clear_hessian_matrix()
        n = len(self.variables)
        # Se crea la matriz hessiana
        matrix = []
        for i in range(n):
            # Se crea una fila
            row = []
            for j in range(n):
                # Se calcula el indice
                idx = i*n+j
                # Se agrega la derivada parcial a la fila
                row.append(self.derivatives.second_partials.values[idx].expression)
            matrix.append(row)
        self.symbolic_hessian_matrix = matrix

    @override
    def get_symbolic_hessian_matrix(self):
        return self.symbolic_hessian_matrix


    @override
    def get_derivative(self):
        print(f'Derivative: \n')
        self.get_expressions()
        self.get_variables()
        self.get_partial_derivatives()



    # CLEARS
    @override
    def clear_hessian_matrix(self):
        self.hessian_matrix.clear()

    @override
    def clear_second_partial_derivatives(self):
        self.derivatives.second_partials.values.clear()
    @override
    def clear_partial_derivatives(self):
        self.derivatives.first_partials.values.clear()

    @override
    def clear_gradient(self):
        self.vector_gradient.values.clear()

    @override
    def clear_evaluated_point(self):
        self.evaluated_point.clear()

    @override
    def clear_variables(self):
        self.variables.clear()

    @override
    def clear_expression(self):
        self.expressions.values.clear()


    @override
    def clear_all(self):
        self.clear_partial_derivatives()
        self.clear_evaluated_point()
        self.clear_variables()
        self.clear_expression()


    # SETTERS
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
    def set_expression(self,expression:str,type:str='default'):
        self.clear_expression()
        self.expressions.values.append(Expression(type=type, value=expression))

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
    def set_first_partial_derivatives(self):
        self.clear_partial_derivatives()
        for variable in self.variables:
            # Se convierte la variable en un operante valido
            current_variable = sp.Symbol(variable)
            # Se calcula la derivada parcial con respecto a la variable actual
            for expression in self.expressions.values:
                if expression.type in ["lagrangiana", "por defecto", "delimitadora"]:
                    val = expression.value
                    if isinstance(val, str) and "=" in val:
                        left, right = val.split("=", 1)
                        val = f"({left}) - ({right})"
                    current_partial_derivative = sp.diff(val,current_variable)
                    # Se agrega la derivada parcial al listado
                    self.derivatives.first_partials.values.append(IPartialDerivative(variable=variable,expression=current_partial_derivative))

    @override
    def set_second_partial_derivatives(self):
        self.clear_second_partial_derivatives()
        for variable in self.variables:
            for partial_derivative in self.derivatives.first_partials.values:
                current_variable = sp.Symbol(variable)

                current_second_partial_derivative = sp.diff(partial_derivative.expression,current_variable)

                self.derivatives.second_partials.values.append(
                    IPartialDerivative(
                        variable=f'{partial_derivative.variable}{variable}',
                        expression=current_second_partial_derivative
                    )
                )




    @override
    def set_taylor_second_order_polynomial(self):
        vector_delta = []
        hessian_term = 0
        # Se obtiene el numero de variables
        n = len(self.variables)
        # Se crea un diccionario con las variables y sus valores
        subs = {sp.Symbol(v): val for v, val in zip(self.variables, self.evaluated_point)}
        # Se obtiene la funcion inicial
        initial_function = None
        # Se recorren las expresiones
        for expression in self.expressions.values:
            # Se obtiene la funcion inicial
            if (expression.type == 'default'):
                initial_function = sp.sympify(expression.value).subs(subs)
        # Se recorren las variables
        for variable, value in zip(self.variables, self.evaluated_point):
            # Se agrega el delta de la variable
            vector_delta.append(sp.Symbol(variable) - value)

        # Se calcula el termino del gradiente
        gradient_term = sum(g * d for g, d in zip(self.vector_gradient.values, vector_delta))

        # Se calcula el termino de la matriz hessiana
        for i in range(n):
            # Se crea una fila
            for j in range(n):
                # Se calcula el indice
                hessian_term += self.hessian_matrix[i][j] * vector_delta[i] * vector_delta[j]

        # Se divide el termino de la matriz hessiana entre 2
        hessian_term = sp.Rational(1, 2) * hessian_term

        # Se expande el polinomio de taylor
        current_value = sp.expand(initial_function + gradient_term + hessian_term)

        # Se agrega el polinomio de taylor a las expresiones
        self.expressions.values.append(Expression(type='taylor_second_order_polynomial', value=current_value))

    @override
    def get_taylor_second_order_polynomial(self):
        for expression in self.expressions.values:
            if (expression.type == 'taylor_second_order_polynomial'):
                return expression.value

    @override
    def evaluate_expression(self):
        for expression in self.expressions.values:
            if (expression.type == 'default'):
                # Se crea un diccionario con las variables y sus valores
                syms = [sp.Symbol(v) for v in self.variables]

                # Se crea una funcion lambda
                expression_lambda = sp.lambdify(syms, expression.value, 'numpy')

                # Se evalua la funcion
                result = expression_lambda(*self.evaluated_point)

                # Se imprime el resultado
                variables_str = ','.join(map(str, self.variables))
                print(f'f({variables_str}) = {result}\n')
                return result

    @override
    def evaluate_taylor_second_order_polynomial(self):
        syms = [sp.Symbol(v) for v in self.variables]
        default_result = None
        taylor_result = None

        # Se crea un string con las variables
        variables_str = ','.join(map(str, self.variables))

        # Se recorren las expresiones
        for expression in self.expressions.values:
            # Se obtiene la funcion inicial
            if (expression.type == 'default'):
                # Se crea una funcion lambda
                default_lambda = sp.lambdify(syms, expression.value, 'numpy')
                # Se evalua la funcion
                default_result = default_lambda(*self.evaluated_point)

            if (expression.type == 'taylor_second_order_polynomial'):
                # Se crea una funcion lambda
                taylor_lambda = sp.lambdify(syms, expression.value, 'numpy')
                # Se evalua la funcion
                taylor_result = taylor_lambda(*self.evaluated_point)

        # Se imprime el resultado
        print(f'{self.name}({variables_str}) = {default_result}\n')
        print(f'P({variables_str}) = {taylor_result}\n')
