from src.model.sistema import Sistema
from src.model.usuario import Usuario
from src.model.contacto import Contacto


class AppControlador:
    def __init__(self):
        self.sistema = Sistema(usar_db=False)
        self.usuario_actual: Usuario = None

    def iniciar_sesion(self, nombre: str, contraseña: str):
        usuario = self.sistema.gestor_usuarios.iniciar_sesion(nombre, contraseña)
        self.usuario_actual = usuario
        return usuario

    def registrar_usuario(self, nombre: str, contraseña: str):
        usuario = Usuario(nombre, contraseña)
        self.sistema.gestor_usuarios.registrar_usuario(usuario)

    def crear_contacto(self, tipo: str, nombre: str, telefono: str):
        contacto = Contacto(tipo, nombre, telefono)
        self.usuario_actual.gestor.registrar_contacto(contacto)

    def obtener_contactos(self):
        return self.usuario_actual.gestor.contactos

    def actualizar_contacto(self, contacto_original, datos_actualizados):
        nuevo_nombre = datos_actualizados.get("nombre", None)
        nuevo_telefono = datos_actualizados.get("telefono", None)
        nuevo_tipo = datos_actualizados.get("tipo", None)

        self.usuario_actual.gestor.editar_contacto(contacto_original, nuevo_tipo, nuevo_nombre, nuevo_telefono)
    
    def importar_contactos(self,archivo: str):
        self.usuario_actual.gestor.importar_contactos(archivo)

    def exportar_contactos(self,nombre_archivo: str):
        self.usuario_actual.gestor.exportar_contactos(nombre_archivo)
        
    



