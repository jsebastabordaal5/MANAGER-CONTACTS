
class Contacto:
    def __init__(self, tipo: str ,nombre: str , telefono : str):
        self.tipo = tipo
        self.nombre = nombre
        self.telefono = telefono


    def __eq__(self, other):
        return (
                isinstance(other, Contacto) and
                self.tipo == other.tipo and
                self.nombre == other.nombre and
                self.telefono == other.telefono
        )


    def __hash__(self):
        return hash((self.nombre, self.telefono, self.tipo))

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Tipo: {self.tipo}"

