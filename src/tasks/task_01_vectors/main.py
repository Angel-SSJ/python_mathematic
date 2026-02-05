from src.utils.menu import Menu
from src.utils.input_handler import InputHandler
from src.core.vector import Vector

class Operations:
    def __init__(self):
        pass

    def create_vector(self, prompt: str = "Introduce los componentes del vector") -> Vector:
        components = InputHandler.get_list_of_floats(prompt)
        return Vector(components)

    def magnitude(self):
        print("Magnitud: |V|")
        v = self.create_vector("Introduce un vector")
        print(f"Magnitud: {v.magnitude()}")

    def normalize(self):
        print("Vector unitario: V / |V|")
        v = self.create_vector("Introduce un vector")
        print(f"Vector unitario: {v.normalize()}")

    def scalar_product(self):
        print("Producto escalar: c * V")
        v = self.create_vector("Introduce un vector")
        scalar = InputHandler.get_float("Introduce un escalar")
        print(f"Producto escalar: {v.scalar_product(scalar)}")

    def dot_product(self):
        print("Producto escalar: V1 . V2")
        v1 = self.create_vector("Introduce el primer vector")
        v2 = self.create_vector("Introduce el segundo vector")
        print(f"Producto escalar: {v1.dot_product(v2)}")

    def angle(self):
        print("Angulo: V1 . V2 / (|V1| * |V2|)")
        v1 = self.create_vector("Introduce el primer vector")
        v2 = self.create_vector("Introduce el segundo vector")
        print(f"Angulo: {v1.angle(v2)}")

    def cross_product(self):
        print("Producto vectorial: V1 x V2")
        v1 = self.create_vector("Introduce el primer vector")
        v2 = self.create_vector("Introduce el segundo vector")
        print(f"Producto vectorial: {v1.cross_product(v2)}")

    def distance(self):
        print("Distancia: ||V x (P - Po)|| / ||V||")
        v = self.create_vector("Introduce un vector")
        p = self.create_vector("Introduce un punto")
        p0 = self.create_vector("Introduce un punto")
        print(f"Distancia: {v.distance(p, p0)}")

    def vector_projection(self):
        print("Proyección vectorial: ((V . U) / ||V||^2) * V")
        v = self.create_vector("Introduce el vector")
        u = self.create_vector("Introduce el vector")
        print(f"Proyección vectorial: {v.vector_projection(u)}")

    def vector_equation(self):
        print("Ecuación vectorial: P = Po + tV")
        v = self.create_vector("Introduce el vector")
        p0 = self.create_vector("Introduce el punto")
        print(f"Ecuación vectorial: {v.vector_equation(p0)}")

    def run(self):
        menu = Menu("Operaciones con Vectores")
        menu.add_option("Magnitud", self.magnitude)
        menu.add_option("Vector unitario", self.normalize)
        menu.add_option("Producto escalar", self.scalar_product)
        menu.add_option("Producto escalar", self.dot_product)
        menu.add_option("Angulo", self.angle)
        menu.add_option("Producto vectorial", self.cross_product)
        menu.add_option("Distancia", self.distance)
        menu.add_option("Proyección vectorial", self.vector_projection)
        menu.add_option("Ecuación vectorial", self.vector_equation)
        menu.run()


if __name__ == "__main__":
    operations = Operations()
    operations.run()
