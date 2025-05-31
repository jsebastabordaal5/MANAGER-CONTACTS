from src.model.sistema import Sistema
from src.model.usuario import Usuario
from src.model.contacto import Contacto


class AppControlador:
    """Controlador principal para gestionar usuarios y contactos en la aplicación."""

    def __init__(self):
        """Inicializa el sistema y el usuario actual."""
        self.sistema = Sistema(usar_db=True)
        self.usuario_actual: Usuario = None

    def iniciar_sesion(self, nombre: str, contraseña: str):
        """Inicia sesión de un usuario. Retorna el usuario si es exitoso."""
        usuario = self.sistema.gestor_usuarios.iniciar_sesion(nombre, contraseña)
        self.usuario_actual = usuario
        return usuario

    def registrar_usuario(self, nombre: str, contraseña: str):
        """Registra un nuevo usuario en el sistema."""
        usuario = Usuario(nombre, contraseña)
        self.sistema.gestor_usuarios.registrar_usuario(usuario)

    def crear_contacto(self, tipo: str, nombre: str, telefono: str):
        """Crea un nuevo contacto para el usuario actual."""
        contacto = Contacto(tipo, nombre, telefono)
        self.usuario_actual.gestor.registrar_contacto(contacto)

    def obtener_contactos(self):
        """Devuelve la lista de contactos del usuario actual."""
        return self.usuario_actual.gestor.contactos

    def actualizar_contacto(self, contacto_original, datos_actualizados):
        """Actualiza un contacto existente con nuevos datos."""
        nuevo_nombre = datos_actualizados.get("nombre", None)
        nuevo_telefono = datos_actualizados.get("telefono", None)
        nuevo_tipo = datos_actualizados.get("tipo", None)
        self.usuario_actual.gestor.editar_contacto(contacto_original, nuevo_tipo, nuevo_nombre, nuevo_telefono)

    def importar_contactos(self, archivo: str):
        """Importa contactos desde un archivo."""
        self.usuario_actual.gestor.importar_contactos(archivo)

    def exportar_contactos(self, nombre_archivo: str):
        """Exporta los contactos a un archivo."""
        self.usuario_actual.gestor.exportar_contactos(nombre_archivo)
