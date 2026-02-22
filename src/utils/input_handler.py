import re
import numpy as np
from typing import Any, List, Optional, Callable

class InputHandler:
    @staticmethod
    def _parse_math_expression(value: str) -> float:
        """
        Parsea una expresión que puede contener constantes como 'pi' o 'euler'/'e'.
        """
        # Quitar espacios en blanco al inicio y al final y hacer minusculas todo
        value = value.strip().lower()

        # DESGLOSE DE LA EXPRESIÓN REGULAR
        # ^ Empezar desde el primer caracter
        # (... )? Crea grupo de captura
        # [-+]? Signo opcional
        # \d+ Obliga a que exista minimo un numero antes del punto
        # \.? Hace opcional el punto
        # \d* Si existe un punto, obliga a que exista minimo un numero despues de este
        # | es operador OR
        # \.\d+ Coincide con numeros que inician con un punto
        # \s* Represetna cero  o mas espacios en blanco
        # (pi|euler|e) Es otro grupo de captura, donde se busca en orden de escritura las constantes
        # $ Terminar en el último caracter
        #
        #
        pattern = r'^([-+]?(?:\d+\.?\d*|\.\d+))?\s*(pi|euler|e)$'
        match = re.match(pattern, value)

        if match:
            coeff_str, constant = match.groups()


            const_val = np.pi if constant == 'pi' else np.e


            if not coeff_str or coeff_str == '+':
                coeff = 1.0
            elif coeff_str == '-':
                coeff = -1.0
            else:
                coeff = float(coeff_str)

            return coeff * const_val


        return float(value)

    @staticmethod
    def get_string(prompt: str) -> str:
        """Obtiene un string no vacío del usuario."""
        while True:
            try:
                value = input(f"{prompt}: ").strip()
                if value:
                    return value
                print("Error: El valor no puede estar vacío.")
            except KeyboardInterrupt:
                print("\nOperación cancelada.")
                raise

    @staticmethod
    def get_float(prompt: str) -> float:
        """Obtiene un número flotante del usuario, soportando constantes."""
        while True:
            try:
                raw = input(f"{prompt}: ")
                return InputHandler._parse_math_expression(raw)
            except ValueError:
                print("Error: Por favor, ingrese un número o expresión válida (ej: 2pi, euler).")
            except KeyboardInterrupt:
                print("\nOperación cancelada.")
                raise

    @staticmethod
    def get_int(prompt: str, min_val: Optional[int] = None, max_val: Optional[int] = None) -> int:
        """Obtiene un número entero del usuario, opcionalmente con validación de rango."""
        while True:
            try:
                value = int(input(f"{prompt}: "))
                if min_val is not None and value < min_val:
                    print(f"Error: El valor debe ser mayor o igual a {min_val}.")
                    continue
                if max_val is not None and value > max_val:
                    print(f"Error: El valor debe ser menor o igual a {max_val}.")
                    continue
                return value
            except ValueError:
                print("Error: Por favor, ingrese un número entero válido.")
            except KeyboardInterrupt:
                print("\nOperación cancelada.")
                raise

    @staticmethod
    def get_list_of_floats(prompt: str, setup_delimiter: str = ",") -> List[float]:
        """Obtiene una lista de números flotantes, soportando constantes."""
        while True:
            try:
                raw = input(f"{prompt} (separado por '{setup_delimiter}'): ")
                if not raw.strip():
                     print("Error: El valor no puede estar vacío.")
                     continue

                return [InputHandler._parse_math_expression(x) for x in raw.split(setup_delimiter)]
            except ValueError:
                print("Error: Asegúrese de que todos los elementos sean números o constantes válidas.")
            except KeyboardInterrupt:
                print("\nOperación cancelada.")
                raise
