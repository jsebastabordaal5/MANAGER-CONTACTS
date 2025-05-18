from src.model.gestor_usuarios import GestorUsuarios
from src.model.contacto import Contacto
from src.model.gestor_contactos import GestorContactos
from src.model.usuario import Usuario
class Sistema:
    def __init__(self, usar_db=False):
        self.gestor_usuarios= GestorUsuarios(usar_db= usar_db)


