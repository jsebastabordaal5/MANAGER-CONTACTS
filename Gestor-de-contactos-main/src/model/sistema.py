from src.model.gestor_usuarios import GestorUsuarios
from src.model.contacto import Contacto
from src.model.gestor_contactos import GestorContactos
from src.model.usuario import Usuario

class Sistema:
    """
    Clase principal del sistema. Se encarga de inicializar el gestor de usuarios.
    Permite definir si se trabajará en modo con base de datos o en memoria.
    """

    def __init__(self, usar_db=False):
        """
        Crea una instancia del sistema con la opción de activar o no el uso de base de datos.
        Inicializa el gestor de usuarios bajo esa configuración.
        """
        self.gestor_usuarios = GestorUsuarios(usar_db=usar_db)

