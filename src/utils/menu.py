from typing import Callable, Dict, List, Tuple
from src.utils.input_handler import InputHandler

class Menu:
    def __init__(self, title: str):
        self.title = title
        self.options: List[Tuple[str, Callable[[], None]]] = []
        self.exit_flag = False

    def add_option(self, description: str, action: Callable[[], None]) -> None:
        """Registra una nueva opción de menú."""
        self.options.append((description, action))

    def _display(self) -> None:
        print(f"\n--- {self.title} ---")
        for idx, (desc, _) in enumerate(self.options, 1):
            print(f"{idx}. {desc}")
        print("0. Exit")

    def run(self) -> None:
        """Inicia el bucle principal del menú."""
        while not self.exit_flag:
            self._display()
            choice = InputHandler.get_int("Selecciona una opción", 0, len(self.options))

            if choice == 0:
                print("Saliendo...")
                self.exit_flag = True
                break

            _, action = self.options[choice - 1]
            try:
                print("\n" + "="*30)
                action()
                print("="*30)
            except Exception as e:
                print(f"Ocurrió un error: {e}")

            if not self._ask_continue():
                self.exit_flag = True

    def _ask_continue(self) -> bool:
        """Pregunta al usuario si desea volver al menú."""
        while True:
            resp = input("\n¿Desea continuar? (y/n): ").lower().strip()
            if resp in ['y', 'yes']:
                return True
            if resp in ['n', 'no']:
                return False
