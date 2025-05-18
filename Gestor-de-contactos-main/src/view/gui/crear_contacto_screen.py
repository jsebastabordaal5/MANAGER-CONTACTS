from kivy.uix.screenmanager import Screen
from src.controller.app_controlador import AppControlador
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label



Builder.load_file("src/view/gui/kv/crear_contacto_screen.kv")
class CrearContactoScreen(Screen):

    def __init__(self, controlador: AppControlador, **kwargs):
        super().__init__(**kwargs)
        self.controlador: AppControlador = controlador

    def crear_contacto(self):
        tipo = self.ids.tipo.text.lower()
        nombre = self.ids.nombre.text
        telefono = self.ids.telefono.text

        try:
            self.controlador.crear_contacto(tipo, nombre, telefono)
            self.mostrar_popup("¡Contacto creado con éxito!")

        except Exception as e:
            self.mostrar_popup(f"Error: {str(e)}")

    def mostrar_popup(self, mensaje):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        label = Label(text=mensaje)
        btn = Button(text="OK", size_hint_y=None, height=40)

        layout.add_widget(label)
        layout.add_widget(btn)

        popup = Popup(
            title='Mensaje',
            content=layout,
            size_hint=(0.7, 0.3),
            auto_dismiss=False
        )

        btn.bind(on_release=lambda *args: self.cerrar_popup_y_volver(popup))

        popup.open()

    def cerrar_popup_y_volver(self, popup):
        popup.dismiss()
        self.manager.current = "usuario_screen"

    def volver_a_main(self):
        self.manager.current = "MainScreen"