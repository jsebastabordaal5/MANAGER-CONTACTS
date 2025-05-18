from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.app import App
from kivy.uix.button import Button
from src.controller.app_controlador import AppControlador

Builder.load_file("src/view/gui/kv/ver_contactos_screen.kv")

class VerContactosScreen(Screen):
    modo_edicion = BooleanProperty(False)

    def __init__(self, controlador: AppControlador, **kwargs):
        super().__init__(**kwargs)
        self.controlador: AppControlador = controlador

    def on_enter(self):
        # Mostrar lista según el modo
        if self.modo_edicion:
            self.mostrar_contactos()
        else:
            self.filtrar_contactos()

    def mostrar_contactos(self, contactos=None):
        self.ids.lista_contactos.clear_widgets()

        if contactos is None:
            contactos = self.controlador.obtener_contactos()

        for contacto in contactos:
            btn = self.crear_boton_contacto(contacto)
            self.ids.lista_contactos.add_widget(btn)

    def crear_boton_contacto(self, contacto):
        btn = Button(
            text=f"{contacto.nombre} - {contacto.telefono}",
            size_hint_y=None,
            height=40
        )
        if self.modo_edicion:
            btn.bind(on_release=lambda btn, c=contacto: self.abrir_edicion_contacto(c))
        else:
            btn.bind(on_release=lambda btn: print("Visualización simple"))
        return btn

    def abrir_edicion_contacto(self, contacto):
        pantalla_editar = self.manager.get_screen("editar_contacto_screen")
        pantalla_editar.contacto_original = contacto
        self.modo_edicion = False
        self.manager.current = "editar_contacto_screen"

    def filtrar_contactos(self):
        tipo = self.ids.filtro_tipo.text.lower()
        nombre = self.ids.filtro_nombre.text.lower()
        telefono = self.ids.filtro_telefono.text.lower()

        contactos = self.controlador.obtener_contactos()
        filtrados = [
            c for c in contactos
            if (tipo in c.tipo.lower() if tipo else True)
               and (nombre in c.nombre.lower() if nombre else True)
               and (telefono in c.telefono.lower() if telefono else True)
        ]
        self.mostrar_contactos(filtrados)

