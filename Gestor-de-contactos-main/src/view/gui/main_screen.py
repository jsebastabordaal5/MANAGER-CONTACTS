
from kivy.uix.screenmanager import Screen
from src.controller.app_controlador import AppControlador
from kivy.lang import Builder

Builder.load_file("src/view/gui/kv/main_screen.kv")

class MainScreen(Screen):
    def __init__ (self , controlador : AppControlador, **kwargs):
        super().__init__(**kwargs)
        self.controlador: AppControlador= controlador

    def iniciar_sesion(self):
        self.manager.current = "iniciar_sesion_screen"

    def registrar_usuario(self):
        self.manager.current = "registrar_usuario_screen"


