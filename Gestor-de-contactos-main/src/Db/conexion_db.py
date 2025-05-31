"""
Configuración de la conexión a la base de datos usando SQLAlchemy.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de conexión a la base de datos PostgreSQL
DATABASE_URL = "postgresql://Usser:@localhost:5432/contact_manager"

# Crea el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)

# Clase base para los modelos declarativos
Base = declarative_base()
