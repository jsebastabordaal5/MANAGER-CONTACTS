import re
import os
from src.model.contacto import Contacto
from src.model.errores import (NombreCortoError , NombreVacioError , NumeroInvalidoError , ContactoNoEncontradoError
                     , DatosInsuficientesError , ErrorNombreCaracterInvalido, ErrorCriterioInexistente, ErrorSinContactos, ErrorArchivoInexistente,ErrorFormatoArchivoInvalido,
                     TipoContactoError, NumeroInvalidoError, NombreInvalidoError, DatosNoNumericosError, CampoVacioError
                    )

from src.Db.contactos_db import guardar_contacto , actualizar_contacto , obtener_contactos
from src.Db.conexion_db import Session
from src.Db.contactos_db import ContactoDB


class GestorContactos:
    """
    Clase que administra la lista de contactos de un usuario. 
    Permite ver, registrar, editar, importar, exportar y filtrar contactos.
    """

    def __init__(self, nombre_usuario=None, usar_db=False):
        """
        Inicializa el gestor de contactos, cargando los contactos del usuario desde base de datos si está habilitado.
        """
        self.nombre_usuario = nombre_usuario
        self.usar_db = usar_db
        if usar_db and nombre_usuario:
            self.contactos = obtener_contactos(nombre_usuario)
        else:
            self.contactos : list[Contacto]= []
  

    def ver_contactos(self):
        """
        Muestra por consola todos los contactos almacenados y los retorna en una lista auxiliar.
        """
        if not self.contactos:
            print("No hay contactos guardados.")
            return

        lista_aux = []

        print("\nLista de Contactos:")

        for i, contacto in enumerate(self.contactos, start=1):
            print(f"{i}. {contacto.tipo} - {contacto.nombre} ({contacto.telefono})")
            lista_aux.append(contacto)

        return lista_aux
    

    def registrar_contacto(self, contacto:Contacto):
        """
        Registra un nuevo contacto si sus datos son válidos. 
        Si está habilitada la base de datos, también lo guarda allí.
        """
        if contacto.nombre.strip() == "" or contacto.tipo.strip() == "" or contacto.telefono.strip() == "":
            raise CampoVacioError()

        if not contacto.telefono.isdigit():
            raise DatosNoNumericosError(contacto.telefono)

        if len(contacto.nombre) < 30 and len(contacto.nombre) > 0:
            if len(contacto.telefono) >= 10 and len(contacto.telefono) <= 12:
                if contacto.tipo.lower() == "profesional" or contacto.tipo.lower() == "personal":
                    self.contactos.append(contacto)  
                    if self.usar_db:
                        guardar_contacto(self.nombre_usuario, contacto) 
                    return contacto
                else:
                    raise TipoContactoError(contacto.tipo)
            else:
                raise NumeroInvalidoError()
        else:
            raise NombreInvalidoError()


    def editar_contacto(self, contacto: Contacto, nuevo_tipo: str = None , nuevo_nombre : str= None , nuevo_telefono: str = None ):
        """
        Edita los datos de un contacto existente. Funciona tanto en base de datos como en memoria.
        """
        if nuevo_nombre is not None and nuevo_nombre.strip() == "":
            raise NombreVacioError()

        if not nuevo_nombre and not nuevo_tipo and not nuevo_telefono:
            raise DatosInsuficientesError()

        if self.usar_db:
            from src.Db.usuario_db import obtener_usuario_por_nombre
            session=Session()

            usuario= obtener_usuario_por_nombre(self.nombre_usuario)
            if not usuario:
                session.close()
                return
            
            contacto_db = session.query(ContactoDB).filter_by(
                nombre=contacto.nombre,
                telefono=contacto.telefono,
                tipo=contacto.tipo,
                id_usuario=usuario.id_usuario
            ).first()

            if not contacto_db:
                raise ContactoNoEncontradoError(contacto)

            if nuevo_nombre:
                if len(nuevo_nombre.strip()) < 3:
                    raise NombreCortoError()
                contacto_db.nombre = nuevo_nombre.strip()
                contacto.nombre= nuevo_nombre

            if nuevo_telefono:
                if not nuevo_telefono.isdigit() or not 10 <= len(nuevo_telefono.strip()) <= 12:
                    raise NumeroInvalidoError()
                contacto_db.telefono = nuevo_telefono.strip()
                contacto.telefono = nuevo_telefono

            if nuevo_tipo:
                if nuevo_tipo.strip().lower() not in ["profesional", "personal"]:
                    print("⚠️ El tipo debe ser 'profesional' o 'personal'")
                else:
                    contacto_db.tipo = nuevo_tipo.strip()
                    contacto.tipo= nuevo_tipo
            
            session.commit()
            session.close()
            return

        if contacto not in self.contactos:
            raise ContactoNoEncontradoError(contacto)

        if nuevo_nombre:
            if len(nuevo_nombre.strip()) < 3:
                raise NombreCortoError()
            contacto.nombre = nuevo_nombre.strip()

        if nuevo_telefono:
            if not nuevo_telefono.isdigit() or not 10 <= len(nuevo_telefono.strip()) <= 12:
                raise NumeroInvalidoError()
            contacto.telefono = nuevo_telefono.strip()

        if nuevo_tipo:
            if nuevo_tipo.strip().lower() not in ["profesional", "personal"]:
                print("⚠️ El tipo debe ser 'profesional' o 'personal'")
            else:
                contacto.tipo = nuevo_tipo.strip()

        return contacto


    def importar_contactos(self, archivo):
        """
        Importa contactos desde un archivo .vcf y los agrega a la lista.
        Valida formato del archivo y evita duplicados.
        """
        archivo = archivo.strip().strip('"').strip("'")
        
        if not os.path.isabs(archivo):
            archivo = os.path.abspath(archivo)

        if not os.path.exists(archivo):
            raise ErrorArchivoInexistente(archivo)

        with open(archivo, "r", encoding="utf-8") as file:
            contenido = file.read().strip()

        if not contenido:
            return

        if "FN:" not in contenido or "TEL:" not in contenido or "CATEGORIES:" not in contenido:
            raise ErrorFormatoArchivoInvalido(archivo)

        with open(archivo, "r", encoding="utf-8") as file:
            contactos_temporales = []
            nombre = telefono = tipo = None

            for linea in file:
                linea = linea.strip()
                if linea.startswith("BEGIN:VCARD"):
                    nombre = telefono = tipo = None
                elif linea.startswith("FN:"):
                    nombre = linea[3:]
                elif linea.startswith("TEL:"):
                    telefono = linea[4:]
                elif linea.startswith("CATEGORIES:"):
                    tipo = linea[11:]
                elif linea.startswith("END:VCARD"):
                    if nombre and telefono and tipo:
                        contacto = Contacto(tipo, nombre, telefono)
                        contactos_temporales.append(contacto)

            for contacto in contactos_temporales:
                if contacto not in self.contactos:
                    self.contactos.append(contacto)
                    if self.usar_db:
                        guardar_contacto(self.nombre_usuario , contacto)

            print(f"Se importaron {len(self.contactos)} contactos correctamente.")


    def exportar_contactos(self,nombre_archivo: str):
        """
        Exporta los contactos existentes a un archivo con formato .vcf.
        Lanza error si no hay contactos disponibles.
        """
        if not self.contactos:
            raise ErrorSinContactos()

        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            for contacto in self.contactos:
                vcard = (
                    f"BEGIN:VCARD\n"
                    f"FN:{contacto.nombre}\n"
                    f"TEL:{contacto.telefono}\n"
                    f"CATEGORIES:{contacto.tipo}\n"
                    f"END:VCARD\n"
                )
                archivo.write(vcard)


    def filtrar_contactos(self, criterio: str, valor: str) -> list[Contacto]:
        """
        Filtra la lista de contactos según nombre, teléfono o tipo.
        También valida que el valor a buscar sea adecuado para el campo indicado.
        """
        criterios_validos = ["nombre", "telefono", "tipo"]
        if criterio not in criterios_validos:
            raise ErrorCriterioInexistente(
                f"El criterio '{criterio}' no es válido. Debe ser 'nombre', 'telefono' o 'tipo'.")

        if criterio == "nombre" and not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", valor):
            raise ErrorNombreCaracterInvalido(f"El nombre '{valor}' contiene caracteres no permitidos.")

        if criterio == "telefono" and not valor.isdigit():
            raise DatosNoNumericosError(f"El teléfono '{valor}' contiene caracteres no numéricos.")

        contactos_filtrados = []

        for contacto in self.contactos:
            if criterio == "tipo" and contacto.tipo.lower() == valor.lower():
                contactos_filtrados.append(contacto)
            elif criterio == "nombre" and valor.lower() in contacto.nombre.lower():
                contactos_filtrados.append(contacto)
            elif criterio == "telefono" and valor in contacto.telefono:
                contactos_filtrados.append(contacto)

        return contactos_filtrados
