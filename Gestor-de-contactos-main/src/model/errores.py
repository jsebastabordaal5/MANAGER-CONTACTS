"""
Define excepciones personalizadas para errores relacionados con usuarios y contactos.
"""

class ContactoNoEncontradoError(Exception):
    """Excepción para contactos no encontrados."""
    def __init__(self, contacto):
        super().__init__(f"El contacto '{contacto}' no fue encontrado")

class DatosInsuficientesError(Exception):
    """Excepción cuando no se proporciona ningún dato al editar un contacto."""
    def __init__(self):
        super().__init__("Debe proporcionar al menos un dato para modificar el contacto.")

class NumeroInvalidoError(Exception):
    """Excepción por número telefónico fuera del rango permitido."""
    def __init__(self, mensaje="El número de teléfono debe tener entre 10 a 12 dígitos"):
        super().__init__(mensaje)

class NombreInvalidoError(Exception):
    """Excepción por nombre inválido."""
    def __init__(self, mensaje="El nombre de contacto es inválido"):
        super().__init__(mensaje)

class CampoVacioError(Exception):
    """Excepción por campos vacíos obligatorios."""
    def __init__(self, mensaje="El campo se encuentra vacío"):
        super().__init__(mensaje)

class NombreVacioError(Exception):
    """Excepción por nombre vacío."""
    def __init__(self, mensaje="El nombre no puede estar vacío"):
        super().__init__(mensaje)

class NombreCortoError(Exception):
    """Excepción por nombre demasiado corto."""
    def __init__(self, mensaje="El nombre es demasiado corto. Debe tener al menos 3 caracteres."):
        super().__init__(mensaje)

class ContraseñaVaciaError(Exception):
    """Excepción por contraseña vacía."""
    def __init__(self, mensaje="Contraseña Vacía"):
        super().__init__(mensaje)

class ErrorSinContactos(Exception):
    """Excepción cuando no hay contactos para exportar."""
    def __init__(self, mensaje="No hay contactos para exportar."):
        super().__init__(mensaje)

class ErrorArchivoInexistente(Exception):
    """Excepción por archivo no existente."""
    def __init__(self, archivo: str):
        super().__init__(f"El archivo '{archivo}' no existe. Verifique la ruta y el nombre del archivo.")

class ErrorFormatoArchivoInvalido(Exception):
    """Excepción por archivo con formato no válido."""
    def __init__(self, archivo: str):
        super().__init__(f"El archivo '{archivo}' no tiene un formato VCF válido. Verifique el contenido y la estructura.")

class ErrorUsuarioNulo(Exception):
    """Excepción cuando se intenta registrar un usuario nulo."""
    def __init__(self):
        super().__init__("No se puede registrar un usuario nulo. Verifique los datos de entrada.")

class ErrorUsuarioYaExistente(Exception):
    """Excepción cuando un usuario ya existe."""
    def __init__(self, nombre_usuario):
        super().__init__(f"El usuario '{nombre_usuario}' ya está registrado. Elija un nombre diferente.")

class ErrorLimiteCaracteres(Exception):
    """Excepción cuando el nombre supera los 30 caracteres."""
    def __init__(self):
        super().__init__(f"El nombre no puede superar los 30 dígitos")

class NombreLargoError(Exception):
    """Excepción cuando el nombre excede los 15 caracteres."""
    def __init__(self, nombre):
        super().__init__(f"El nombre '{nombre}' excede los 15 caracteres")

class ErrorNombreCaracterInvalido(Exception):
    """Excepción por caracteres inválidos en el nombre."""
    def __init__(self, nombre):
        super().__init__(f"nombre: {nombre} es inválido")

class ErrorUsuarioInexistente(Exception):
    """Excepción por usuario inexistente."""
    def __init__(self, mensaje="El usuario no está registrado"):
        super().__init__(mensaje)

class TipoContactoError(Exception):
    """Excepción por tipo de contacto inválido."""
    def __init__(self, tipo):
        super().__init__(f"El tipo de contacto: {tipo} es inválido")

class DatosNoNumericosError(Exception):
    """Excepción por número de teléfono con caracteres no numéricos."""
    def __init__(self, telefono):
        super().__init__(f"El teléfono: {telefono} no es válido")

class ErrorCriterioInexistente(Exception):
    """Excepción por criterio de búsqueda inexistente."""
    def __init__(self, criterio):
        super().__init__(f"El criterio: {criterio} es inexistente")

class ErrorTipoInvalidoUsuario(Exception):
    """Excepción cuando el objeto no es del tipo Usuario."""
    def _init_(self, mensaje="Debes proporcionar un objeto de tipo Usuario"):
        super()._init_(mensaje)

class ErrorLimiteDigitosTelefono(Exception):
    """Excepción cuando el teléfono excede los 12 caracteres."""
    def __init__(self, telefono):
        super().__init__(f"El teléfono: {telefono} excede los 12 caracteres")

class ErrorUsuarioExistente(Exception):
    """Excepción cuando se detecta un usuario duplicado."""
    def __init__(self):
        super().__init__(f"El usuario ya existe")

class ContraseñaIncorrectaError(Exception):
    """Excepción cuando la contraseña no coincide."""
    def __init__(self, mensaje="La contraseña ingresada es incorrecta."):
        super().__init__(mensaje)

