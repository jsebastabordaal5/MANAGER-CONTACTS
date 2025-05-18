from kivy.uix.screenmanager import Screen
from src.controller.app_controlador import AppControlador
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty

Builder.load_file("src/view/gui/kv/usuario_screen.kv")

class UsuarioScreen(Screen):
    contacto = ObjectProperty(None)

    def __init__(self, controlador: AppControlador, **kwargs):
        super().__init__(**kwargs)
        self.controlador: AppControlador = controlador

    def ver_contactos(self):
        self.manager.current = "ver_contactos_screen"

    def mostrar_lista_edicion(self):
        ver_contactos = self.manager.get_screen("ver_contactos_screen")
        ver_contactos.modo_edicion = True
        ver_contactos.mostrar_contactos()
        self.manager.current = "ver_contactos_screen"

    def editar_contacto(self, contacto):
        app = App.get_running_app()
        app.mostrar_editar_contacto(contacto)

    def crear_contacto(self):
        print("Cambiar a crear_contacto_screen")
        self.manager.current = "crear_contacto_screen"

    def importar_contactos(self):
        self.manager.current = "importar_contactos_screen"

    def exportar_contactos(self):
        self.manager.current = "exportar_contactos_screen"