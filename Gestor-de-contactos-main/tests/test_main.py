from src.model.usuario import Usuario
from src.model.gestor_contactos import GestorContactos
from src.model.contacto import Contacto
from src.model.gestor_usuarios import GestorUsuarios

from src.model.errores import ContactoNoEncontradoError, DatosInsuficientesError,  NombreCortoError, CampoVacioError, \
    NombreVacioError, DatosNoNumericosError, ErrorSinContactos, ErrorArchivoInexistente, ErrorFormatoArchivoInvalido, NombreLargoError, NumeroInvalidoError,  TipoContactoError, \
    ErrorCriterioInexistente,  ErrorUsuarioYaExistente, ContraseñaIncorrectaError, ErrorUsuarioInexistente, ErrorTipoInvalidoUsuario, ContraseñaVaciaError, ErrorNombreCaracterInvalido



import pytest

#Requisito 1

#Normales
def test_crear_contacto_1():
    usuario = Usuario("juan", "12345")
    contacto = Contacto("personal", "juan sebastian", "3226130937")
    usuario.gestor.registrar_contacto(contacto)
    assert len(usuario.gestor.contactos) == 1

def test_crear_contacto_2():
    usuario = Usuario("juan", "12345")
    contacto = Contacto("profesional", "tomas henao", "3148122236")
    usuario.gestor.registrar_contacto(contacto)
    assert len(usuario.gestor.contactos) == 1

def test_crear_contacto_3():
    usuario = Usuario("juan", "12345")
    contacto = Contacto("profesional", "daniel olarte", "3148122216")
    usuario.gestor.registrar_contacto(contacto)
    assert len(usuario.gestor.contactos) == 1

#Extremos
def test_nombre_con_mas_de_15_caracteres():
    usuario = Usuario("juan", "12345")
    contacto = Contacto("personal", "Daniel Olarte Pérez Valencia", "3148122216")
    usuario.gestor.registrar_contacto(contacto)
    assert len(usuario.gestor.contactos) == 1

def test_telefono_mas_de_10_digitos():
    usuario = Usuario("juan", "12345")
    contacto = Contacto("personal", "Samuel Flórez", "12345678910")
    usuario.gestor.registrar_contacto(contacto)
    assert len(usuario.gestor.contactos) == 1

def test_nombre_con_solo_1_caracter():
    usuario = Usuario("juan", "12345")
    contacto = Contacto("personal", "y", "33124983127")
    usuario.gestor.registrar_contacto(contacto)
    assert len(usuario.gestor.contactos) == 1

# Errores
def test_tipo_contacto_invalido():
    usuario = Usuario("juan", "12345")
    with pytest.raises(TipoContactoError):
        contacto = Contacto("parcero", "juan gonzalez", "12345678910")
        usuario.gestor.registrar_contacto(contacto)


def test_datos_no_numericos():
    with pytest.raises(DatosNoNumericosError):
        usuario = Usuario("juan", "12345")
        contacto = Contacto("profesional", "juan gonzalez", "3abc2334478")
        usuario.gestor.registrar_contacto(contacto)


def test_campos_vacios():
    usuario = Usuario("juan", "12345")
    with pytest.raises(CampoVacioError):
        contacto1 = Contacto(" ", "juan gonzalez", "33124983127")
        usuario.gestor.registrar_contacto(contacto1)

        # Test para tipo vacío
    with pytest.raises(CampoVacioError):
        contacto2 = Contacto("profesional", " ", "33124983127")
        usuario.gestor.registrar_contacto(contacto2)

        # Test para teléfono vacío
    with pytest.raises(CampoVacioError):
        contacto3 = Contacto("profesional", "juan gonzalez", " ")
        usuario.gestor.registrar_contacto(contacto3)





#Requisito 2

#Normales
def test_editar_tipo_contacto ( ):
    usuario = Usuario("juan","12345")
    contacto=Contacto("personal","samuel","3002223984")
    usuario.gestor.registrar_contacto(contacto)
    usuario.gestor.editar_contacto(contacto, nuevo_tipo="profesional")
    assert usuario.gestor.contactos[0].tipo == "profesional"

def test_editar_nombre_contacto ( ):
    usuario = Usuario("juan","12345")
    contacto=Contacto("personal","samuel","3002223984")
    usuario.gestor.registrar_contacto(contacto)
    usuario.gestor.editar_contacto(contacto, nuevo_nombre="juan")
    assert usuario.gestor.contactos[0].nombre == "juan"

def test_editar_numero_contacto ( ):
    usuario = Usuario("juan","12345")
    contacto=Contacto("personal","samuel","3002223984")
    usuario.gestor.registrar_contacto(contacto)
    usuario.gestor.editar_contacto(contacto,nuevo_telefono="3005680588")
    assert usuario.gestor.contactos[0].telefono == "3005680588"


#Extremos
def test_editar_contacto_nombre_extremadamente_corto():
    usuario = Usuario("juan", "12345")
    contacto = Contacto("personal", "samuel", "3002223984")
    usuario.gestor.registrar_contacto(contacto)
    with pytest.raises(NombreCortoError):
        usuario.gestor.editar_contacto(contacto, nuevo_nombre="a")

def test_editar_contacto_numero_extremadamente_largo():
    usuario = Usuario("juan", "12345")
    numero_muy_largo = "1234567898765432123"
    contacto = Contacto("personal", "samuel", "3002223984")
    usuario.gestor.registrar_contacto(contacto)
    with pytest.raises(NumeroInvalidoError):
        usuario.gestor.editar_contacto(contacto, nuevo_telefono=numero_muy_largo)

def test_editar_contacto_numero_invalido():
    usuario = Usuario("juan", "12345")
    numero_corto = "1"
    contacto = Contacto("personal", "samuel", "3002223984")
    usuario.gestor.registrar_contacto(contacto)
    with pytest.raises(NumeroInvalidoError):
        usuario.gestor.editar_contacto(contacto, nuevo_telefono=numero_corto)


#Error

def test_editar_contacto_no_existente():
    usuario = Usuario("juan", "12345")
    contacto = Contacto("personal", "samuel", "3002223984")
    usuario.gestor.registrar_contacto(contacto)

    with pytest.raises(ContactoNoEncontradoError):
        usuario.gestor.editar_contacto("desconocido", nuevo_tipo="profesional")


def test_editar_contacto_sin_valores():
    usuario = Usuario("juan", "12345")
    contacto = Contacto("personal", "samuel", "3002223984")
    usuario.gestor.registrar_contacto(contacto)

    with pytest.raises(DatosInsuficientesError):
        usuario.gestor.editar_contacto(contacto)


def test_editar_contacto_nombre_vacio():
    usuario = Usuario("juan", "12345")
    contacto = Contacto("personal", "samuel", "3002223984")
    usuario.gestor.registrar_contacto(contacto)
    with pytest.raises(NombreVacioError):
        usuario.gestor.editar_contacto(contacto, nuevo_nombre="")


# Requisito 3

# Normales

def test_filtrar_contactos_por_nombre():
    usuario = Usuario("juan", "12345")
    usuario.gestor.contactos = [
        Contacto("personal", "Carlos Pérez", "555123456"),
        Contacto("profesional", "Ana López", "555654321"),
        Contacto("personal", "Carlos Gómez", "555987654"),
    ]
    resultado = usuario.gestor.filtrar_contactos('nombre', 'carlos')

    esperado = [
        Contacto("personal", "Carlos Pérez", "555123456"),
        Contacto("personal", "Carlos Gómez", "555987654")
    ]
    assert resultado == esperado


def test_filtrar_contactos_por_telefono():
    usuario = Usuario("juan", "12345")
    usuario.gestor.contactos = [
        Contacto("personal", "Juan Rodríguez", "3146272068"),
        Contacto("profesional", "Ana López", "555654321"),
        Contacto("profesional", "Carlos Gómez", "309482213"),
    ]
    resultado = usuario.gestor.filtrar_contactos('telefono', '3146272068')

    esperado = [
        Contacto("personal", "Juan Rodríguez", "3146272068")
    ]
    assert resultado == esperado



def test_filtrar_contactos_por_tipo():
    usuario = Usuario("juan", "12345")
    usuario.gestor.contactos = [
        Contacto("personal", "Juan Rodríguez", "3146272068"),
        Contacto("profesional", "Ana López", "555654321"),
        Contacto("profesional", "Carlos Gómez", "309482213")
    ]
    resultado = usuario.gestor.filtrar_contactos('tipo', 'profesional')

    esperado = [
        Contacto("profesional", "Ana López", "555654321"),
        Contacto("profesional", "Carlos Gómez", "309482213")
    ]
    assert resultado == esperado


# Extremos

def ordenar_contactos(contacto):
    return (contacto.tipo, contacto.nombre, contacto.telefono)


def test_filtrar_contacto_por_parte_del_telefono():
    usuario = Usuario("juan", "12345")
    usuario.gestor.contactos = [
        Contacto("personal", "Juan Rodríguez", "3146272068"),
        Contacto("profesional", "Ana López", "555654321"),
        Contacto("profesional", "Carlos Gómez", "314482213")
    ]
    resultado = usuario.gestor.filtrar_contactos('telefono', '314')

    esperado = [
        Contacto("profesional", "Carlos Gómez", "314482213"),
        Contacto("personal", "Juan Rodríguez", "3146272068")
    ]

    assert sorted(resultado, key=ordenar_contactos) == sorted(esperado, key=ordenar_contactos)


def test_filtrar_contacto_por_parte_del_nombre():
    usuario = Usuario("juan", "12345")
    usuario.gestor.contactos = [
        Contacto("personal", "Juan Rodríguez", "3146272068"),
        Contacto("profesional", "Ana López", "555654321"),
        Contacto("profesional", "Carlos Gómez", "314482213")
    ]
    resultado = usuario.gestor.filtrar_contactos('nombre', 'Juan')
    esperado = [
        Contacto("personal", "Juan Rodríguez", "3146272068")
    ]
    assert resultado == esperado


def test_filtrar_contactos_cuando_todos_son_del_mismo_tipo():
    usuario = Usuario("juan", "12345")
    usuario.gestor.contactos = [
        Contacto("profesional", "Juan Pérez", "3146272068"),
        Contacto("profesional", "Ana López", "555654321"),
        Contacto("profesional", "Carlos Gómez", "314482213")
    ]
    resultado = usuario.gestor.filtrar_contactos('tipo', 'profesional')
    esperado = [
        Contacto("profesional", "Juan Pérez", "3146272068"),
        Contacto("profesional", "Ana López", "555654321"),
        Contacto("profesional", "Carlos Gómez", "314482213")
    ]
    assert resultado == esperado


# Errores
def test_filtrar_criterio_inexistente():
    usuario = Usuario("juan", "12345")
    usuario.gestor.contactos = [
        Contacto("personal", "mateo lópez", "329050614"),
        Contacto("profesional", "carlos manuel", "399888765"),
        Contacto("profesional", "juan mecanico", "315665432"),
    ]

    with pytest.raises(ErrorCriterioInexistente):
        usuario.gestor.filtrar_contactos("edad", "37")


def test_filtrar_nombre_caracter_invalido():
    usuario = Usuario("juan", "12345")
    usuario.gestor.contactos = [
        Contacto("personal", "mateo lópez", "329050614"),
        Contacto("profesional", "carlos manuel", "399888765"),
        Contacto("profesional", "juan mecanico", "315665432"),
    ]

    with pytest.raises(ErrorNombreCaracterInvalido):
        usuario.gestor.filtrar_contactos("nombre", "C@rlos")


def test_filtrar_telefono_con_digitos_no_numericos():
    usuario = Usuario("juan", "12345")
    usuario.gestor.contactos = [
        Contacto("personal", "mateo lópez", "329050614"),
        Contacto("profesional", "carlos manuel", "399888765"),
        Contacto("profesional", "juan mecanico", "315665432"),
    ]

    with pytest.raises(DatosNoNumericosError):
        usuario.gestor.filtrar_contactos("telefono", "abc 123 cde")




       

# Requisito 4

# Normales
def test_exportar_contacto():
    usuario = Usuario("juan", "12345")
    contacto = Contacto("personal", "samuel", "3002223984")
    usuario.gestor.registrar_contacto(contacto)

    usuario.gestor.exportar_contactos("contactos.vcf")

    with open("contactos.vcf", "r") as archivo:
        contenido = archivo.read()

        esperado = """BEGIN:VCARD
FN:samuel
TEL:3002223984
CATEGORIES:personal
END:VCARD"""

        assert esperado in contenido


def test_importar_contacto():
    with open("contactos.vcf", "w") as archivo:
        archivo.write("""BEGIN:VCARD
FN:samuel
TEL:3002223984
CATEGORIES:personal
END:VCARD""")

    usuario = Usuario("juan", "12345")
    usuario.gestor.importar_contactos("contactos.vcf")

    assert len(usuario.gestor.contactos) == 1
    assert usuario.gestor.contactos[0].nombre == "samuel"
    assert usuario.gestor.contactos[0].telefono == "3002223984"
    assert usuario.gestor.contactos[0].tipo == "personal"


def test_exportar_multiples_contactos():
    usuario = Usuario("juan", "12345")
    contacto1 = Contacto("personal", "samuel", "3002223984")
    usuario.gestor.registrar_contacto(contacto1)
    contacto2 = Contacto("profesional", "ana", "3104567890")
    usuario.gestor.registrar_contacto(contacto2)

    usuario.gestor.exportar_contactos("contactos.vcf")

    with open("contactos.vcf", "r") as archivo:
        contenido = archivo.read()

    esperado = """BEGIN:VCARD
FN:samuel
TEL:3002223984
CATEGORIES:personal
END:VCARD
BEGIN:VCARD
FN:ana
TEL:3104567890
CATEGORIES:profesional
END:VCARD"""

    assert esperado in contenido


# Extremos


def test_exportar_contacto_nombre_largo():
    usuario = Usuario("juan", "12345")
    nombre_largo = "a" * 29
    contacto = Contacto("personal", nombre_largo, "3002223984")
    usuario.gestor.registrar_contacto(contacto)
    usuario.gestor.exportar_contactos("contactos.vcf")

    with open("contactos.vcf", "r") as archivo:
        contenido = archivo.read()

    assert f"FN:{nombre_largo}" in contenido


def test_importar_contacto_archivo_vacio():
    with open("contactos_vacio.vcf", "w") as archivo:
        pass  # Crear un archivo vacío

    usuario = Usuario("juan", "12345")
    usuario.gestor.importar_contactos("contactos_vacio.vcf")

    assert len(usuario.gestor.contactos) == 0


def test_exportar_importar_contacto_nombre_largo():
    usuario = Usuario("juan", "12345")
    nombre_largo = "Maximiliano Fernandez Guti"
    telefono_largo = "123456789012"

    contacto = Contacto("personal", nombre_largo, telefono_largo)
    usuario.gestor.registrar_contacto(contacto)
    usuario.gestor.exportar_contactos("contactos_largos.vcf")

    nuevo_usuario = Usuario("carlos", "54321")
    nuevo_usuario.gestor.importar_contactos("contactos_largos.vcf")

    contacto_encontrado = False
    for contacto in nuevo_usuario.gestor.contactos:
        print(f"Nombre importado: {repr(contacto.nombre)}")
        print(f"Nombre esperado: {repr(nombre_largo)}")
        print(f"Teléfono importado: {repr(contacto.telefono)}")
        print(f"Teléfono esperado: {repr(telefono_largo)}")
        print("-" * 50)

        if contacto.nombre == nombre_largo and contacto.telefono == telefono_largo:
            contacto_encontrado = True
            break

    assert contacto_encontrado, "El contacto con nombre largo no fue importado correctamente."


# Errores

def test_exportar_sin_contactos():
    usuario = Usuario("juan", "12345")

    with pytest.raises(ErrorSinContactos):
        usuario.gestor.exportar_contactos("contactos.vcf")


def test_importar_archivo_no_existente():
    usuario = Usuario("juan", "12345")

    with pytest.raises(ErrorArchivoInexistente):
        usuario.gestor.importar_contactos("archivo_inexistente.vcf")


def test_importar_archivo_formato_invalido():
    with open("formato_invalido.vcf", "w") as archivo:
        archivo.write("CONTACTO: samuel, 3002223984")  #

    usuario = Usuario("juan", "12345")

    with pytest.raises(ErrorFormatoArchivoInvalido):
        usuario.gestor.importar_contactos("formato_invalido.vcf")



#Requisito 5

#Normales

def test_registrar_usuario():
    gestor = GestorUsuarios()
    usuario_nuevo = Usuario("juan", "password123")
    gestor.registrar_usuario(usuario_nuevo)
    assert usuario_nuevo in gestor.usuarios

def test_registrar_multiples_usuarios():
    gestor = GestorUsuarios()
    usuario1 = Usuario("juan", "password123")
    usuario2 = Usuario("maria", "password321")

    gestor.registrar_usuario(usuario1)
    gestor.registrar_usuario(usuario2)

    assert usuario1 in gestor.usuarios
    assert usuario2 in gestor.usuarios

def test_registrar_usuarios_similares():
    gestor = GestorUsuarios()
    usuario1 = Usuario("juan1", "password123")
    usuario2 = Usuario("juan", "password123")

    gestor.registrar_usuario(usuario1)
    gestor.registrar_usuario(usuario2)

    assert len(gestor.usuarios) == 2


# Extremos

def test_registrar_usuario_nombre_contraseña_largos():
    gestor = GestorUsuarios()
    nombre_largo = "a" * 500  # Nombre 100 caracteres
    contraseña_larga = "b" * 500  # Contraseña de 100 caracteres
    usuario = Usuario(nombre_largo, contraseña_larga)

    gestor.registrar_usuario(usuario)

    assert len(gestor.usuarios) == 1
    assert gestor.usuarios[0].nombre == nombre_largo
    assert gestor.usuarios[0].contraseña == contraseña_larga

def test_registrar_usuario_caracteres_especiales():
    gestor = GestorUsuarios()
    usuario = Usuario("J@hn_Doe 123", "P@ssw0rd!")

    gestor.registrar_usuario(usuario)

    assert len(gestor.usuarios) == 1
    assert gestor.usuarios[0].nombre == "J@hn_Doe 123"
    assert gestor.usuarios[0].contraseña == "P@ssw0rd!"

def test_registrar_usuario_con_espacios_limpiados():
    gestor = GestorUsuarios()
    nombre_original = "  usuario con espacios  "
    contraseña_original = "  contraseña con espacios  "
    usuario = Usuario(nombre_original, contraseña_original)

    gestor.registrar_usuario(usuario)

    nombre_esperado = "usuario con espacios"
    contraseña_esperada = "contraseña con espacios"

    assert len(gestor.usuarios) == 1
    assert gestor.usuarios[0].nombre == nombre_esperado
    assert gestor.usuarios[0].contraseña == contraseña_esperada


# Errores

def test_registrar_usuario_nulo():
    gestor = GestorUsuarios()
    usuario_incorrecto = "Éste es un string, no un Objeto Usuario"

    with pytest.raises(ErrorTipoInvalidoUsuario):
        gestor.registrar_usuario(usuario_incorrecto)


def test_registrar_usuario_duplicado():
    gestor = GestorUsuarios()
    usuario1 = Usuario("usuarioRepetido", "contraseña123")
    usuario2 = Usuario("usuarioRepetido", "otraContraseña")

    gestor.registrar_usuario(usuario1)

    with pytest.raises(ErrorUsuarioYaExistente):
        gestor.registrar_usuario(usuario2)


def test_registrar_usuario_tipo_incorrecto():
    gestor = GestorUsuarios()
    usuario_incorrecto = "Este es un string, no un objeto Usuario"

    with pytest.raises(ErrorTipoInvalidoUsuario):
        gestor.registrar_usuario(usuario_incorrecto)




# Requisito 6

# Normales
def test_credenciales_correctas():
    gestor = GestorUsuarios()
    usuario = Usuario("juan", "12345")
    gestor.registrar_usuario(usuario)
    resultado = gestor.iniciar_sesion("juan", "12345")
    assert isinstance(resultado, Usuario)


def test_iniciar_sesion_despues_de_registrar():
    gestor = GestorUsuarios()
    usuario = Usuario("juan", "12345")
    gestor.registrar_usuario(usuario)
    resultado = gestor.iniciar_sesion("juan", "12345")
    assert isinstance(resultado, Usuario)


def test_volver_iniciar_sesion_despues_de_cerrar_sesion():
    gestor = GestorUsuarios()
    usuario = Usuario("juan", "12345")
    gestor.registrar_usuario(usuario)
    resultado1 = gestor.iniciar_sesion("juan", "12345")
    assert isinstance(resultado1, Usuario)
    gestor.cerrar_sesion()
    resultado2 = gestor.iniciar_sesion("juan", "12345")
    assert isinstance(resultado2, Usuario)


# Extremos
def test_iniciar_sesion_con_credenciales_extremadamente_largas():
    gestor = GestorUsuarios()
    usuario = Usuario("juan garzón garzón villa sanchez", "124346gsuyh2tn_@")
    gestor.registrar_usuario(usuario)
    resultado = gestor.iniciar_sesion("juan garzón garzón villa sanchez", "124346gsuyh2tn_@")
    assert isinstance(resultado, Usuario)


def test_iniciar_sesion_con_mayusculas_y_minusculas():
    gestor = GestorUsuarios()
    usuario = Usuario("Juan", "ClaveSegura123")
    gestor.registrar_usuario(usuario)

    resultado1 = gestor.iniciar_sesion("Juan", "ClaveSegura123")
    assert isinstance(resultado1, Usuario)

    resultado2 = gestor.iniciar_sesion("juan", "ClaveSegura123")
    assert isinstance(resultado2, Usuario)

    with pytest.raises(ContraseñaIncorrectaError):
        gestor.iniciar_sesion("Juan", "clavesegura123")


def test_iniciar_sesion_en_multiples_dispositivos():
    gestor = GestorUsuarios()
    usuario = Usuario("juan", "12345")
    gestor.registrar_usuario(usuario)
    resultado1 = gestor.iniciar_sesion("juan", "12345")
    assert isinstance(resultado1, Usuario)
    resultado2 = gestor.iniciar_sesion("juan", "12345")
    assert isinstance(resultado2, Usuario)


# Error
def test_iniciar_sesion_usuario_no_existente():
    gestor = GestorUsuarios()
    # Intentar iniciar sesión con un usuario que no existe
    with pytest.raises(ErrorUsuarioInexistente):
        gestor.iniciar_sesion("usuario_inexistente", "clave123")

def test_iniciar_sesion_con_contraseña_vacia():
    gestor = GestorUsuarios()
    usuario = Usuario("juan", "12345")
    gestor.registrar_usuario(usuario)
    with pytest.raises(ContraseñaVaciaError):
        gestor.iniciar_sesion("carlos", "")

def test_iniciar_sesion_con_nombre_vacio():
    gestor = GestorUsuarios()
    usuario = Usuario("juan", "12345")
    gestor.registrar_usuario(usuario)

    with pytest.raises(NombreVacioError):
        gestor.iniciar_sesion("", "12345")

