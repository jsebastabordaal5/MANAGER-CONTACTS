
from kivy.uix.screenmanager import Screen
from src.controller.app_controlador import AppControlador
from kivy.lang import Builder
from src.model.errores import ErrorArchivoInexistente
from kivy.app import App
from kivy.properties import StringProperty

Builder.load_file("src/view/gui/kv/importar_contactos_screen.kv")

class ImportarContactosScreen(Screen):
    mensaje_error = StringProperty("")  # Esto permite vincular un mensaje al .kv
    def __init__ (self , controlador : AppControlador, **kwargs):
        super().__init__(**kwargs)
        self.controlador: AppControlador= controlador

    
    def importar_contactos(self):
        ruta=self.ids.ruta_input.text.strip()
        try:
            self.controlador.importar_contactos(ruta)
            self.mensaje_error = "Importación exitosa."
        except ErrorArchivoInexistente as e:
            self.mensaje_error = str(e)
        except Exception as e:
            self.mensaje_error = f"Error inesperado: {e}"
    
    def volver(self):
        self.manager.current= "usuario_screen"