import numpy as np
from src.core.vector import Vector
from typing import List, Union, Any, Tuple, override
import matplotlib.pyplot as plt
from src.core.operations_trajectory import OperationsTrajectory

class Trajectory(OperationsTrajectory):

    def __init__(self, coordinates: Union[List[float], np.ndarray] = np.array([])):
        self.coordinates = np.array(coordinates, dtype=np.float64)
        self.t_values = np.array([])
        self.point = np.array([])
        self.intercepted_coordinates = np.array([])
        if self.coordinates.ndim == 1 and self.coordinates.size > 0:
            self.coordinates = self.coordinates.reshape(1, -1)

    @override
    def validate_dimensions(self):
       if not isinstance(self.coordinates, (list, np.ndarray)) or self.coordinates.size == 0:
           raise ValueError("Las dimensiones deben ser un array o lista")

    @override
    def validate_coordinates(self):
       if not isinstance(self.coordinates, (list, np.ndarray)) or self.coordinates.size == 0:
           raise ValueError("Las coordenadas deben ser un array o lista")

    @override
    def validate_point(self):
       if not isinstance(self.point, (list, np.ndarray)) or self.point.size == 0:
           raise ValueError("El punto debe ser un array o lista")
    @override
    def validate_coefficients(self, coefficients: Tuple[float, float, float]):
       if not isinstance(coefficients, tuple) or len(coefficients) != 3:
           raise ValueError("Los coeficientes deben ser un tuple de 3 float/int")

    @override
    def validate_limits(self, limits: Tuple[float, float]):
       if not isinstance(limits, tuple) or len(limits) != 2:
           raise ValueError("Los limites deben ser un tuple de 2 float/int")

    @override
    def validate_amount_points(self, amount_points: int):
       if not isinstance(amount_points, int) or amount_points <= 0:
           raise ValueError("El número de puntos debe ser un entero positivo")

    @override
    def validate_intercepted_coordinates(self):
       if not isinstance(self.intercepted_coordinates, (list, np.ndarray)) or self.intercepted_coordinates.size == 0:
           raise ValueError("Las coordenadas interceptadas deben ser un array o lista")

    @override
    def validate_projection(self, projection: str = '3d'):
        if projection == '3d' and self.validate_dimensions() != 3:
            raise ValueError("La trayectoria debe ser en 3D para proyección 3D")
        if projection == '2d' and self.validate_dimensions() != 2:
            raise ValueError("La trayectoria debe ser en 2D para proyección 2D")

    @override
    def calculate_euclidean_distance(self, point: 'Vector', coordinate: Union[List[float], np.ndarray] = np.array([])):
        self.validate_coordinates()

        axis = 1 if coordinate.ndim > 1 else None
        return np.sqrt(np.sum((coordinate - point.components) ** 2, axis=axis))

    @override
    def calculate_shortest_euclidean_distance(self, point: 'Vector'):
        self.validate_coordinates()

        distances = []
        for coordinate in self.coordinates:

            #Calcular distancia euclidiana entre el vector/punto y cada coordenada de la trayectoria
            distance = self.calculate_euclidean_distance(point,coordinate)
            distances.append(distance)

        #Encontrar el idx del valor minimo en el array de distancias
        min_idx = np.argmin(distances)
        #Obtener el valor minimo mediante idx
        min_dist = distances[min_idx]
        #Obtener las coordenadas interceptadas/ mas cercanas al vector mediante idx
        intercepted_coordinates = self.coordinates[min_idx]
        #Obtener el valor de t mas cercano
        closest_t = self.t_values[min_idx]

        #Asignar los valores de point y intercepted_coordinates a los atributos de la clase
        self.point = point.components
        self.intercepted_coordinates = intercepted_coordinates

        print(f'\n \n =====Valores obtenidos===== \n')
        print(f"Distancia Euclidiana más corta: {min_dist:.4f}")
        print(f"Valor de t: {closest_t:.4f}")
        print(f"Coordenadas más cercanas:\n x: {intercepted_coordinates[0]:.4f}\n y: {intercepted_coordinates[1]:.4f}\n z: {intercepted_coordinates[2]:.4f}")

    @override
    def helicoidal_trajectory(self, coefficients: Tuple[float, float, float], limits: Tuple[float, float], amount_points: int):

        #Validar los coeficientes, limites y cantidad de puntos
        self.validate_coefficients(coefficients)
        self.validate_limits(limits)
        self.validate_amount_points(amount_points)

        #Generar los valores de t
        t = np.linspace(limits[0], limits[1], amount_points)

        #Asignar los valores de t a los atributos de la clase
        self.t_values = t

        #Calcular las coordenadas de la trayectoria
        x = coefficients[0] * np.cos(t)
        y = coefficients[1] * np.sin(t)
        z = coefficients[2] * t

        #Validar las coordenadas
        self.validate_coordinates()
        #Sumar las coordenadas de la trayectoria
        # self.coordinates[0, 0] es la coordenada x del punto de referencia
        # self.coordinates[0, 1] es la coordenada y del punto de referencia
        # self.coordinates[0, 2] es la coordenada z del punto de referencia
        x += self.coordinates[0, 0]
        y += self.coordinates[0, 1]
        z += self.coordinates[0, 2]

        #Asignar las coordenadas a los atributos de la clase
        # [[x1,y1,z1],[x2,y2,z2],...,[xn,yn,zn]]
        self.coordinates = np.column_stack((x, y, z))

    @override
    def display_trajectory(self, projection: str = '3d', type_trajectory: str = 'Helicoidal'):

        #Validar las coordenadas
        self.validate_coordinates()

        #Obtener las coordenadas actualizadas de la trayectoria
        # [[x1,y1,z1],[x2,y2,z2],...,[xn,yn,zn]]
        x = self.coordinates[:, 0]
        y = self.coordinates[:, 1]
        # Si la trayectoria es en 3D, obtener la coordenada z sino se crea un array de ceros con la misma forma que x
        z = self.coordinates[:, 2] if self.coordinates.shape[1] > 2 else np.zeros_like(x)

        #Crear la figura y los ejes
        fig, ax = plt.subplots(subplot_kw={"projection": projection})

        #Graficar la trayectoria
        ax.plot(x, y, z,color='c', label=f'Trayectoria {type_trajectory}')


        #Validar el punto de referencia
        self.validate_point()

        #Graficar el punto de referencia (P)
        ax.scatter(*self.point, color='k', s=100, label='Punto P')

        #Validar las coordenadas interceptadas
        self.validate_intercepted_coordinates()
        #Graficar las coordenadas interceptadas
        ax.scatter(*self.intercepted_coordinates, color='r', s=100, label='Coordenadas interceptadas')

        #Graficar la linea que une el punto de referencia (P) con las coordenadas interceptadas en la trayectoria
        ax.plot([self.intercepted_coordinates[0],self.point[0]],[self.intercepted_coordinates[1],self.point[1]],[self.intercepted_coordinates[2],self.point[2]],color='k',)

        #Agregar titulo y etiquetas a los ejes
        ax.set_title(f'Visualización de Trayectoria {type_trajectory}')
        ax.set_xlabel('Eje X')
        ax.set_ylabel('Eje Y')
        if projection == '3d':
            ax.set_zlabel('Eje Z')

        #Agregar leyenda
        ax.legend()
        #Mostrar la grafica
        plt.show()
