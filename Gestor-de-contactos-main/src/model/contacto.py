"""
Define la clase Contacto que representa un contacto personal o profesional.
"""

class Contacto:
    """
    Representa un contacto con nombre, teléfono y tipo (profesional/personal).
    """

    def __init__(self, tipo: str, nombre: str, telefono: str):
        """
        Inicializa un nuevo contacto.

        Args:
            tipo (str): Tipo de contacto (profesional/personal).
            nombre (str): Nombre del contacto.
            telefono (str): Número de teléfono del contacto.
        """
        self.tipo = tipo
        self.nombre = nombre
        self.telefono = telefono

    def __eq__(self, other):
        """Compara dos contactos por igualdad."""
        return (
            isinstance(other, Contacto) and
            self.tipo == other.tipo and
            self.nombre == other.nombre and
            self.telefono == other.telefono
        )

    def __hash__(self):
        """Permite usar la clase en estructuras hash como conjuntos o claves de diccionarios."""
        return hash((self.nombre, self.telefono, self.tipo))

    def __str__(self):
        """Devuelve una representación legible del contacto."""
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Tipo: {self.tipo}"


