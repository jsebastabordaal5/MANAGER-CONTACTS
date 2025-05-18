from kivy.uix.screenmanager import Screen
from src.controller.app_controlador import AppControlador
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock

from kivy.lang import Builder

Builder.load_file("src/view/gui/kv/registrar_usuario_screen.kv")


class RegistrarUsuarioScreen(Screen):
    def __init__(self, controlador: AppControlador, **kwargs):
        super().__init__(**kwargs)
        self.controlador: AppControlador = controlador

    def registrar_usuario(self):
        usuario = self.ids.usuario_input.text
        contraseña = self.ids.contrasena_input.text

        try:
            self.controlador.registrar_usuario(usuario, contraseña)
            self.mostrar_popup("¡Usuario registrado con éxito!")

            # Esperar 2 segundos antes de cambiar de pantalla
            Clock.schedule_once(lambda dt: self.volver_a_main(), 2)

        except Exception as e:
            self.mostrar_popup(f"Error: {str(e)}")

    def mostrar_popup(self, mensaje):
        popup = Popup(title='Mensaje',
                      content=Label(text=mensaje),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

    def volver_a_main(self):
        self.manager.current = "MainScreen"



