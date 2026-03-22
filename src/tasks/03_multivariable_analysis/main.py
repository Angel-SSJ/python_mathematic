from src.utils.menu import Menu
from src.utils.input_handler import InputHandler
from src.core.derivatives.multivariable_analysis import MultivariableAnalysis
from src.core.derivatives.multivariable_function import MultivariableFunction
import sympy as sp



class Operations:
    def __init__(self):
        self.operations = MultivariableAnalysis()

    def define_parent_functions(self):
        name = InputHandler.get_string("Introduce el nombre de la variable (ej: w)")
        variables = InputHandler.get_list_of_strings("Introduce las variables de las expresiones padres (ej: x,y)")
        expressions = InputHandler.get_list_of_strings("Introduce las expresiones padres (ej: E**(x*y))")
        evaluated_point = InputHandler.get_list_of_floats("Introduce los valores de coordenas del punto de evaluacion (ej: 1,1)")
        for expression in expressions:
            parent_function = MultivariableFunction()
            parent_function.set_expression(expression)
            parent_function.set_variables(variables)
            parent_function.set_name(name)
            parent_function.set_evaluated_point(evaluated_point)
            parent_function.set_first_partial_derivatives()
            parent_function.set_gradient()
            parent_function.set_second_partial_derivatives()
            self.operations.add_parent_function(parent_function)

    def define_children_functions(self):
        names = InputHandler.get_list_of_strings("Introduce los nombres de las variables intermedias (ej: x,y)")
        independent_variables = InputHandler.get_list_of_strings("Introduce las variables independientes (ej: v,u)")
        expressions = InputHandler.get_list_of_strings("Introduce las expresiones hijas (ej: 2*v-u)")
        evaluated_point = InputHandler.get_list_of_floats("Introduce los valores de coordenas del punto de evaluacion (ej: 1,1)")

        for name, expression in zip(names, expressions):
            child_function = MultivariableFunction()
            child_function.set_name(name)
            child_function.set_expression(expression)
            child_function.set_variables(independent_variables)
            child_function.set_evaluated_point(evaluated_point)
            child_function.set_first_partial_derivatives()
            child_function.set_second_partial_derivatives()
            self.operations.add_child_function(child_function)

    def calculate_chain_rule(self):
        self.operations.get_chain_rule()
        self.operations.evaluate_chain_rule()

    def calculate_gradient(self):
        """Calcula derivadas parciales y evalúa el vector gradiente en x₀"""

        for operation in self.operations.functions.parents:
            operation.get_gradient()

    def calculate_hessian_matrix(self):
        """Construye la matriz Hessiana evaluada en x₀"""
        idx = InputHandler.get_int("Introduce el indice de la funcion padre (ej: 0)")
        self.operations.set_hessian_matrix(idx)
        self.operations.get_hessian_matrix(idx)

    def define_taylor_function(self):
        """Define la función y punto base para el polinomio de Taylor"""
        idx = InputHandler.get_int("Introduce el indice de la funcion padre (ej: 0)")
        self.operations.set_taylor_second_order_polynomial(idx)

        self.operations.get_taylor_second_order_polynomial(idx)

    def calculate_taylor_polynomial(self):
        """Construye el polinomio de segundo orden de Taylor"""
        idx = InputHandler.get_int("Introduce el indice de la funcion padre (ej: 0)")
        print(f'\n')

        self.operations.evaluate_taylor_second_order_polynomial(idx)

    def run(self):
        menu = Menu("Operaciones con Derivadas")
        menu.add_option("Definir funciones padres", self.define_parent_functions)
        menu.add_option("Definir funciones hijas", self.define_children_functions)
        menu.add_option("Calcular regla de la cadena", self.calculate_chain_rule)
        menu.add_option("Calcular vector gradiente", self.calculate_gradient)
        menu.add_option("Calcular matriz Hessiana", self.calculate_hessian_matrix)
        menu.add_option("Definir polinomio de 2° orden de Taylor", self.define_taylor_function)
        menu.add_option("Evaluar polinomio de 2° orden de Taylor", self.calculate_taylor_polynomial)
        menu.run()



if __name__ == "__main__":
    operations = Operations()
    operations.run()
