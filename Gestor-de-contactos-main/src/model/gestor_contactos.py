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
    def __init__(self, nombre_usuario=None, usar_db=False):
        self.nombre_usuario = nombre_usuario
        self.usar_db = usar_db
        if usar_db and nombre_usuario:
            self.contactos = obtener_contactos(nombre_usuario)
        else:
            self.contactos : list[Contacto]= []
  


    def ver_contactos(self):
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
            
            # Buscar el contacto correspondiente en la base de datos
            contacto_db = session.query(ContactoDB).filter_by(
                nombre=contacto.nombre,
                telefono=contacto.telefono,
                tipo=contacto.tipo,
                id_usuario=usuario.id_usuario
            ).first()

            if not contacto_db:
                raise ContactoNoEncontradoError(contacto)

            # Actualizar valores si se proporcionan
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
            

            session.commit()  # Guardar cambios en la base
            session.close()
            return

        # --- Si no se usa base de datos, trabajar en memoria ---
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
        archivo = archivo.strip().strip('"').strip("'")
        
        if not os.path.isabs(archivo):  # Verifica si la ruta es absoluta
            archivo = os.path.abspath(archivo)  # Convierte a ruta absoluta


        if not os.path.exists(archivo):
            raise ErrorArchivoInexistente(archivo)

        with open(archivo, "r", encoding="utf-8") as file:
            contenido = file.read().strip()

        if not contenido:
            return

            # Verificamos si el contenido sigue el formato VCF esperado
        if "FN:" not in contenido or "TEL:" not in contenido or "CATEGORIES:" not in contenido:
            raise ErrorFormatoArchivoInvalido(archivo)

        with open(archivo, "r", encoding="utf-8") as file:
            contactos_temporales = []
            nombre = telefono = tipo = None

            for linea in file:
                linea = linea.strip()  # Eliminamos espacios innecesarios
                if linea.startswith("BEGIN:VCARD"):
                    nombre = telefono = tipo = None
                elif linea.startswith("FN:"):
                    nombre = linea[3:]  # Tomamos el texto después de "FN:"
                elif linea.startswith("TEL:"):
                    telefono = linea[4:]  # Tomamos el texto después de "TEL:"
                elif linea.startswith("CATEGORIES:"):
                    tipo = linea[11:]  # Tomamos el texto después de "CATEGORIES:"
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
        if not self.contactos:  # Verifica si la lista de contactos está vacía
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
        criterios_validos = ["nombre", "telefono", "tipo"]
        if criterio not in criterios_validos:
            raise ErrorCriterioInexistente(
                f"El criterio '{criterio}' no es válido. Debe ser 'nombre', 'telefono' o 'tipo'.")

        # Validar caracteres en el nombre
        if criterio == "nombre" and not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", valor):
            raise ErrorNombreCaracterInvalido(f"El nombre '{valor}' contiene caracteres no permitidos.")

        # Validar que el teléfono contenga solo dígitos
        if criterio == "telefono" and not valor.isdigit():
            raise DatosNoNumericosError(f"El teléfono '{valor}' contiene caracteres no numéricos.")

        # Filtrar contactos
        contactos_filtrados = []

        for contacto in self.contactos:
            if criterio == "tipo" and contacto.tipo.lower() == valor.lower():
                contactos_filtrados.append(contacto)
            elif criterio == "nombre" and valor.lower() in contacto.nombre.lower():
                contactos_filtrados.append(contacto)
            elif criterio == "telefono" and valor in contacto.telefono:  # Permite búsqueda parcial de teléfono
                contactos_filtrados.append(contacto)

        return contactos_filtrados