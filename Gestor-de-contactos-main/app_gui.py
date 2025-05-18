from src.model.sistema import Sistema
from src.view.console.menu import Menu
from src.view.gui.gui import ContactosApp
from src.controller.app_controlador import AppControlador

if __name__ == "__main__":
    app_controlador: AppControlador = AppControlador()
    ContactosApp(app_controlador).run()
