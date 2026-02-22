from src.utils.menu import Menu
from src.utils.input_handler import InputHandler
from src.core.trajectory import Trajectory
from src.core.vector import Vector

class OperationsTrajectory:
    def __init__(self):
        pass

    def create_trajectory(self, prompt: str = "Introduce las coordenadas iniciales de la trayectoria") -> Trajectory:
        coordenates = InputHandler.get_list_of_floats(prompt)
        return Trajectory(coordenates)

    def helicoidal_trajectory(self):
        print("\n--- Trayectoria Helicoidal ---")
        trajectory = self.create_trajectory()
        coefficients = InputHandler.get_list_of_floats("Introduce los coeficientes (a, b, c) de la trayectoria helicoidal ( r(t) = <acos(t),bsin(t),ct> )")
        limits = InputHandler.get_list_of_floats("Introduce los límites ( eje. 0,2pi)")
        amount_points = InputHandler.get_int("Introduce la cantidad de puntos de la trayectoria helicoidal (eje. 1000)")


        vector = InputHandler.get_list_of_floats("Introduce el vector/punto P(x, y, z)")

        trajectory.helicoidal_trajectory(tuple(coefficients[:3]), tuple(limits[:2]), amount_points)
        trajectory.calculate_shortest_euclidean_distance(Vector(vector))
        trajectory.display_trajectory(projection='3d', type_trajectory='Helicoidal')

    def run(self):
        menu = Menu('Operaciones con Trayectorias')
        menu.add_option("Trayectoria helicoidal", self.helicoidal_trajectory)
        menu.run()

if __name__ == "__main__":
    operations = OperationsTrajectory()
    operations.run()
