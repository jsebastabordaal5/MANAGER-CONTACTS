from src.Db.conexion_db import Session
from src.Db.db import UsuarioDB, ContactoDB
from sqlalchemy import func

session = Session()

"Consulta de todos los usuarios existentes"
usuarios = session.query(UsuarioDB).all()
for u in usuarios:
    print(u)

"Consulta de todos los contactos existentes"
contactos = session.query(ContactoDB).all()
for c in contactos:
    print(c)

"Consulta de todos los contactos del usuario con el id=1 (juan)"
contactos_user1 = session.query(ContactoDB).filter_by(id_usuario=1).all()
for c in contactos_user1:
    print(c)

"Consulta de todos los contactos cuyo tipo es profesional"
profesionales = session.query(ContactoDB).filter_by(tipo="profesional").all()
for c in profesionales:
    print(c)

"Consulta de los usuarios con mas de 3 contactos"
resultados = (
    session.query(UsuarioDB.nombre, func.count(ContactoDB.id_contacto).label("total"))
    .join(ContactoDB, UsuarioDB.id_usuario == ContactoDB.id_usuario)
    .group_by(UsuarioDB.nombre)
    .having(func.count(ContactoDB.id_contacto) > 3)
    .all()
)

for nombre, total in resultados:
    print(f"{nombre} tiene {total} contactos")


"Consulta de todos los contactos en los que se encuntre Ana en el nombre"
ana = session.query(ContactoDB).filter(ContactoDB.nombre.ilike("%ana%")).all()
for c in ana:
    print(c)

session.close()