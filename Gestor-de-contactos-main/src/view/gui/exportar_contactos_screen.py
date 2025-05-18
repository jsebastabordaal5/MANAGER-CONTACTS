from kivy.uix.screenmanager import Screen
from src.controller.app_controlador import AppControlador
from kivy.lang import Builder

Builder.load_file("src/view/gui/kv/exportar_contactos_screen.kv")

class ExportarContactosScreen(Screen):
    def __init__ (self , controlador : AppControlador, **kwargs):
        super().__init__(**kwargs)
        self.controlador: AppControlador= controlador

    def exportar_contactos(self):
        nombre_archivo = self.ids.nombre_archivo_input.text
        self.controlador.exportar_contactos(nombre_archivo)

    def volver(self):
        self.manager.current = "usuario_screen"