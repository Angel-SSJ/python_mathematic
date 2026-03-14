from src.utils.menu import Menu
from src.utils.input_handler import InputHandler
from src.core.derivatives.operations_derivatives import OperationsDerivatives
from src.core.derivatives.derivative import Derivative
import sympy as sp



class Operations:
    def __init__(self):
        self.operations = OperationsDerivatives()

    def define_children_derivatives(self):
        names = InputHandler.get_list_of_strings("Introduce los nombres de las variables intermedias (ej: x,y)")
        independent_variables = InputHandler.get_list_of_strings("Introduce las variables independientes (ej: v,u)")
        expressions = InputHandler.get_list_of_strings("Introduce las expresiones hijas (ej: 2*v-u)")
        evaluated_point = InputHandler.get_list_of_floats("Introduce los valores de coordenas del punto de evaluacion (ej: 1,1)")

        for name, expression in zip(names, expressions):
            child_derivative = Derivative()
            child_derivative.set_name(name)
            child_derivative.set_expression(expression)
            child_derivative.set_variables(independent_variables)
            child_derivative.set_evaluated_point(evaluated_point)
            child_derivative.set_partial_derivatives()
            self.operations.add_child_derivative(child_derivative)

    def define_parent_derivatives(self):
        name = InputHandler.get_string("Introduce el nombre de la variable (ej: w)")
        variables = InputHandler.get_list_of_strings("Introduce las variables de las expresiones padres (ej: x,y)")
        expressions = InputHandler.get_list_of_strings("Introduce las expresiones padres (ej: E**(x*y))")
        evaluated_point = InputHandler.get_list_of_floats("Introduce los valores de coordenas del punto de evaluacion (ej: 1,1)")
        for expression in expressions:
            parent_derivative = Derivative()
            parent_derivative.set_expression(expression)
            parent_derivative.set_variables(variables)
            parent_derivative.set_name(name)
            parent_derivative.set_evaluated_point(evaluated_point)

            parent_derivative.set_partial_derivatives()
            self.operations.add_parent_derivative(parent_derivative)

    def calculate_chain_rule(self):
        self.operations.get_chain_rule()

    def evaluate_chain_rule(self):
        self.operations.evaluate_chain_rule()

    def run(self):
        menu = Menu("Operaciones con Derivadas")
        menu.add_option("Definir derivadas padres", self.define_parent_derivatives)
        menu.add_option("Definir derivadas hijas", self.define_children_derivatives)
        menu.add_option("Calcular regla de la cadena", self.calculate_chain_rule)
        menu.add_option("Evaluar regla de la cadena", self.evaluate_chain_rule)
        menu.run()



if __name__ == "__main__":
    operations = Operations()
    operations.run()
