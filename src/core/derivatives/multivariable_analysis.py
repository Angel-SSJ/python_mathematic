import sympy as sp
from sympy import Expr
from typing import List
from .types import Expressions,IHierarchyFunctions
from .types import Expression
from .interfaces.Imultivariable_analysis import IMultivariableAnalysis
from typing import override
from .multivariable_function import MultivariableFunction
from .interfaces.Ichain_rule import IChainRule
from .interfaces.Itaylor_second_order_polynomial import ITaylorSecondOrderPolynomial
from .interfaces.Ibordered_hessian_matrix import IBorderedHessianMatrix
from .interfaces.Ilagrange_analysis import ILagrangianAnalysis
import matplotlib.pyplot as plt
import numpy as np

class MultivariableAnalysis(IMultivariableAnalysis,ITaylorSecondOrderPolynomial,IChainRule,ILagrangianAnalysis,IBorderedHessianMatrix):

    def __init__(self):

        self.functions:IHierarchyFunctions = IHierarchyFunctions()
        self.expressions:Expressions = Expressions()

    # GETTERS
    @override
    def get_parent_derivatives(self):
        return self.functions.parents

    @override
    def get_child_derivatives(self):
        return self.functions.childs

    @override
    def get_expressions(self):
        return self.expressions

    @override
    def clear_parent_derivatives(self):
        self.functions.parents.clear()

    @override
    def clear_child_derivatives(self):
        self.functions.childs.clear()

    @override
    def clear_expressions(self):
        self.expressions.values.clear()

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
        variables = self.functions.childs[0].variables


        # se recorren las derivadas padres
        for parent in self.functions.parents:
            # se inicializa un diccionario con las variables de la derivada hija
            results = {var: 0 for var in variables}

            # se calculan las derivadas parciales de cada derivada padre
            parent.set_partial_derivatives()

            for child in self.functions.childs:
                # se  calculan las derivadas parciales de cada derivada hija
                child.set_partial_derivatives()

                # se captura la derivada parcial de la derivada padre segun la variable de la derivada hija
                # ejemplo: wx => Xu
                parent_partial = next(
                    (p for p in parent.first_partials.values if p.variable == child.name),None
                )

                if parent_partial:
                    # se recorren las derivadas parciales de la derivada hija actual
                    for child_partial in child.first_partials.values:
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
            sp.symbols(child.name): sp.sympify(next(e for e in child.expressions.values if e.type == 'por defecto').value
)
            for child in self.functions.childs
        }


        # Se capturan las variables de la derivada hija
        independent_vars = self.functions.childs[0].variables
        # Se captura el punto de evaluacion de la derivada hija
        point = self.functions.childs[0].evaluated_point
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
    def set_taylor_second_order_polynomial(self,idx:int):
        self.functions.parents[idx].set_taylor_second_order_polynomial()

    @override
    def get_taylor_second_order_polynomial(self,idx:int):
        # Se obtiene la funcion
        current_function = self.functions.parents[idx]
        # Se calcula el polinomio de taylor
        current_function.set_taylor_second_order_polynomial()
        # Se obtiene el string de las variables
        variables_str = ','.join(map(str, current_function.variables))
        # Se obtiene el resultado
        result = current_function.get_taylor_second_order_polynomial()
        # Se imprime el resultado
        print(f"P({variables_str}) = {result}\n")
        return result


    @override
    def evaluate_taylor_second_order_polynomial(self,idx:int):
        self.functions.parents[idx].evaluate_taylor_second_order_polynomial()

    @override
    def set_parent_derivatives(self,derivative:MultivariableFunction):
        self.clear_parent_derivatives()
        self.functions.parents.append(derivative)


    @override
    def add_parent_function(self,derivative:MultivariableFunction):
        self.functions.parents.append(derivative)

    @override
    def set_child_derivatives(self,derivative:MultivariableFunction):
        self.clear_child_derivatives()
        self.functions.childs.append(derivative)

    @override
    def add_child_function(self,derivative:MultivariableFunction):
        self.functions.childs.append(derivative)

    @override
    def set_parent_first_partial_derivarive(self):
        for function in self.functions.parents:
            function.set_first_partial_derivatives()

    @override
    def set_parent_second_partial_derivarive(self):
        for function in self.functions.parents:
            function.set_second_partial_derivatives()


    @override
    def set_child_first_partial_derivarive(self):
        for function in self.functions.childs:
            function.set_first_partial_derivatives()

    @override
    def set_child_second_partial_derivarive(self):
        for function in self.functions.childs:
            function.set_second_partial_derivatives()

    @override
    def get_hessian_matrix(self,idx:int):
        return self.functions.parents[idx].get_hessian_matrix()

    @override
    def get_gradient(self,idx:int):
        return self.functions.parents[idx].get_gradient()

    @override
    def set_hessian_matrix(self,idx:int):
        self.functions.parents[idx].set_hessian_matrix()

    @override
    def set_system_of_lagrangian_equations(self):

        system_equations = []
        gradient_default_function = []
        bounding_gradient = []
        lambda_symbol = sp.symbols('lambda')

        # Se recorre la lista de functions
        for idx, func in enumerate(self.functions.parents):

            if not func.vector_gradient.values:
                # Si no se han calculado las derivadas parciales, se calculan
                func.set_first_partial_derivatives()
                func.set_second_partial_derivatives()
                func.set_gradient()

            # Se recorre la lista de expresiones
            for expression in func.expressions.values:

                # Se verifica si la expresion es de tipo delimitadora
                if expression.type == "delimitadora":
                    left, right = '',''
                    val = expression.value
                    # Se verifica si la expresion tiene un signo de igual
                    if "=" in val:
                        # Se divide la expresion en dos partes
                        left, right = val.split("=", 1)
                        # Se agrega la ecuacion al sistema
                        system_equations.append(sp.Eq(sp.sympify(left), sp.sympify(right)))
                    else:
                        # Si no tiene un signo de igual, se agrega la ecuacion al sistema
                        system_equations.append(sp.Eq(sp.sympify(val), 0))

                    # Se agrega el gradiente de la funcion delimitadora al listado (simbolica => sin evaluar)
                    bounding_gradient = func.get_symbolic_gradient()
                if expression.type == "por defecto":
                    # Se agrega el gradiente de la funcion por defecto al listado (simbolica => sin evaluar)
                    gradient_default_function = func.get_symbolic_gradient()

        # Se recorre el gradiente de la funcion por defecto y el gradiente de la funcion delimitadora
        for default_factor, bounding_factor in zip(gradient_default_function, bounding_gradient):
            # Se crea la ecuacion
            equation = sp.Eq(default_factor - bounding_factor * lambda_symbol, 0)
            # Se agrega la ecuacion al sistema
            system_equations.append(equation)

        print(f'\n--- Sistema de ecuaciones de Lagrange ---\n')
        for equation in system_equations:
            print(f'\n{equation.lhs} = {equation.rhs}\n')
            self.add_expression(Expression(value=equation,type="lagrangian_system_equations"))


    @override
    def get_system_of_lagrangian_equations(self):
        equations =[]
        variables =[]
        # se recorre el listado de expresiones
        for expression in self.expressions.values:
            # se verifica si la expresion es de tipo lagrangian_system_equations
            if expression.type == "lagrangian_system_equations":
                # se agrega la ecuacion al listado
                equations.append(expression.value)

        # se recorre el listado de variables
        for variable in self.functions.parents[0].variables:
            # se convierte la variable en un operante valido
            variables.append(sp.symbols(variable))

        # se agrega la variable lambda al listado
        variables.append(sp.symbols('lambda'))

        # se resuelve el sistema de ecuaciones
        solutions = sp.solve(equations,variables,dict=True)
        # se agrega la solucion al listado
        self.add_expression(Expression(value=solutions,type="lagrangian_solution"))

        # se recorre la solucion
        for soluction in solutions:
            # se recorre la solucion
            for key,value in soluction.items():
                print(f'{key}: {value}\n')


    @override
    def set_lagrangian_function(self):
        boundaring_sympy = None
        default_sympy = None
        variables = self.functions.parents[0].variables
        evaluated_point = self.functions.parents[0].evaluated_point
        lam = sp.symbols('lambda')


        # se obtiene la funcion delimitadora
        func_boundaring = self.get_function("delimitadora")
        if func_boundaring:
            # se recorre el listado de expresiones
            for expr in func_boundaring.expressions.values:
                # se verifica si la expresion es de tipo delimitadora
                if expr.type == "delimitadora":
                    # se divide la expresion en dos partes
                    val = expr.value
                    if "=" in val:
                        # se divide la expresion en dos partes
                        left, right = val.split("=", 1)
                        # se convierte la expresion en un operante valido
                        boundaring_sympy = sp.sympify(left) - sp.sympify(right)
                    else:
                        # se convierte la expresion en un operante valido
                        boundaring_sympy = sp.sympify(val)

        # se obtiene la funcion por defecto
        func_default = self.get_function("por defecto")
        if func_default:
            # se recorre el listado de expresiones
            for expr in func_default.expressions.values:
                # se verifica si la expresion es de tipo por defecto
                if expr.type == "por defecto":
                    # se convierte la expresion en un operante valido
                    default_sympy = sp.sympify(expr.value)

        # se crea la funcion de lagrange
        lagrangian_expr = default_sympy - lam * boundaring_sympy

        print(f'\n--- Funcion de Lagrange ---\n')
        print(f'\n{lagrangian_expr}\n')

        # se agrega la funcion de lagrange al listado
        self.add_parent_function(
            MultivariableFunction(
                expressions=Expressions(values=[Expression(type="lagrangiana", value=lagrangian_expr)]),
                variables=variables,
                evaluated_point=evaluated_point,
                name="lagrangiana"
            ))


    @override
    def get_function(self,type:str):
        # se recorre el listado de funciones
        for func in self.functions.parents:
            # se recorre el listado de expresiones
            for expression in func.expressions.values:
                # se verifica si la expresion es del tipo solicitado
                if expression.type == type:
                    # se retorna la funcion
                    return func

    @override
    def set_bordered_hessian_matrix(self):
        # se obtiene la funcion delimitadora
        boundaring_function = self.get_function("delimitadora")
        # se establecen las derivadas parciales de primer orden
        boundaring_function.set_first_partial_derivatives()
        # se establecen las derivadas parciales de segundo orden
        boundaring_function.set_second_partial_derivatives()

        # se obtiene la funcion lagrangiana
        lagrangian_function = self.get_function("lagrangiana")
        # se establecen las derivadas parciales de primer orden
        lagrangian_function.set_first_partial_derivatives()
        # se establecen las derivadas parciales de segundo orden
        lagrangian_function.set_second_partial_derivatives()

        # se obtiene la matriz hessiana
        matrix_lagrangian = lagrangian_function.get_symbolic_hessian_matrix()

        # se obtiene la matriz de derivadas parciales de primer orden de la funcion delimitadora
        first_partial_derivatives_boundaring_function = [
            pd.expression for pd in boundaring_function.derivatives.first_partials.values
        ]

        # se obtiene el tamaño de la matriz
        n = len(first_partial_derivatives_boundaring_function)
        bordered_matrix = []

        # se agrega la primera fila de la matriz
        bordered_matrix.append([sp.Integer(0)] + first_partial_derivatives_boundaring_function)

        # se recorre la matriz
        for i in range(n):
            # se obtiene la fila de la matriz
            row = list(matrix_lagrangian[i])
            # se agrega la fila de la matriz
            bordered_matrix.append([first_partial_derivatives_boundaring_function[i]] + row)

        # se convierte la matriz en una matriz de sympy
        bordered_matrix = sp.Matrix(bordered_matrix)

        print(f'\n--- Matriz Hessiana Orleada ---\n')
        print(f'\n{bordered_matrix}\n')

        # se agrega la matriz al listado
        self.add_expression(Expression(value=bordered_matrix, type="bordered_hessian_matrix"))


    @override
    def get_bordered_hessian_matrix(self):
        bordered_matrix = ''
        soluctions = ''

        # se recorre el listado de expresiones
        for expression in self.expressions.values:
            # se verifica si la expresion es de tipo bordered_hessian_matrix
            if expression.type == "bordered_hessian_matrix":
                # se obtiene la matriz orlada
                bordered_matrix = expression.value

        # se recorre el listado de expresiones
        for expression in self.expressions.values:
            if expression.type == "lagrangian_solution":
                solutions = expression.value

        # se verifica si hay matriz orlada o soluciones
        if not bordered_matrix or not solutions:
            print("No hay matriz orlada o soluciones disponibles.")
            return

        # se evalua la matriz orlada
        eval_matrix = bordered_matrix.subs(solutions[0])

        # se calcula el determinante
        det = eval_matrix.det()

        # se crea el punto de evaluacion
        point = {}
        # se recorre la solucion
        for soluction in solutions:
            # se recorre la solucion
            for key,value in soluction.items():
                # se verifica si la clave no es lambda
                if str(key) != 'lambda':
                    # se agrega la clave y el valor al punto
                    point[key] = value

        print(f'\n--- Evaluando Punto Crítico ---\n')
        for key,value in point.items():
            print(f'{key}: {value}')
        print(f'Determinante |H|: {det}\n')

        if det > 0:
            print('Veredicto: Es un máximo relativo')
        elif det < 0:
            print('Veredicto: Es un mínimo relativo')
        else:
            print('Veredicto: El criterio no es concluyente (|H| = 0)')
