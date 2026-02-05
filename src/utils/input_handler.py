from typing import Any, List, Optional, Callable

class InputHandler:
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
        """Obtiene un número flotante del usuario."""
        while True:
            try:
                return float(input(f"{prompt}: "))
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
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
        """Obtiene una lista de números flotantes separados por un delimitador."""
        while True:
            try:
                raw = input(f"{prompt} (separado por '{setup_delimiter}'): ")
                if not raw.strip():
                     print("Error: El valor no puede estar vacío.")
                     continue
                return [float(x.strip()) for x in raw.split(setup_delimiter)]
            except ValueError:
                print("Error: Asegúrese de que todos los elementos sean números válidos.")
            except KeyboardInterrupt:
                print("\nOperación cancelada.")
                raise
