
from kivy.uix.screenmanager import Screen
from src.controller.app_controlador import AppControlador
from src.model.errores import ErrorUsuarioInexistente
from kivy.lang import Builder

Builder.load_file("src/view/gui/kv/iniciar_sesion_screen.kv")

class IniciarSesionScreen(Screen):
    def __init__ (self , controlador : AppControlador, **kwargs):
        super().__init__(**kwargs)
        self.controlador: AppControlador= controlador

    def iniciar_sesion(self):
        usuario= self.ids.usuario_input.text
        contraseña= self.ids.contrasena_input.text
        self.ids.error_label.text = ""

        try:
            user= self.controlador.iniciar_sesion(usuario,contraseña)
            if user:
                self.manager.current = "usuario_screen"
        except ErrorUsuarioInexistente as e:
         self.ids.error_label.text = str(e)  
        except Exception:
            self.ids.error_label.text = "Ocurrió un error inesperado. Intenta de nuevo."



    def volver(self):
        self.ids.error_label.text = ""
        self.manager.current= "MainScreen"

