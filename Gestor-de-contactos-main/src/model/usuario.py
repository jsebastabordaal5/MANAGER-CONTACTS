from src.model.gestor_contactos import GestorContactos
from src.model.contacto import Contacto

class Usuario:
    """
    Representa a un usuario del sistema, quien posee un nombre, una contraseña,
    y un gestor de contactos que le permite manejar su propia lista de contactos.
    """

    def __init__(self, nombre: str, contraseña: str, usar_db: bool = False):
        """
        Crea una nueva instancia de usuario y asocia un gestor de contactos.
        El gestor puede trabajar con o sin base de datos, según configuración.
        """
        self.nombre = nombre.strip()
        self.contraseña = contraseña.strip()
        self.gestor = GestorContactos(nombre_usuario=nombre, usar_db=usar_db)

    def __str__(self):
        """
        Devuelve una representación legible del usuario mostrando su nombre y contraseña.
        """
        return f"Nombre: {self.nombre}, Contraseña : {self.contraseña}"
