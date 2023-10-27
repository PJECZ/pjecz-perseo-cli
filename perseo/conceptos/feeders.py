"""
Perseo - Conceptos - Feeders
"""
from sqlalchemy import Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

from config.settings import Settings
from lib.database import get_engine, get_session
from lib.safe_string import safe_string
from lib.universal_mixin import UniversalMixin
from perseo.conceptos.classes import Concepto

Base = declarative_base()


class ConceptoDB(Base, UniversalMixin):
    """Concepto"""

    # Nombre de la tabla
    __tablename__ = "conceptos"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Columnas
    clave = Column(String(16), unique=True, nullable=False)
    descripcion = Column(String(256), nullable=False)


def feed_conceptos(settings: Settings, conceptos: list[Concepto]) -> int:
    """Alimentar conceptos"""

    # Inicializar contador en cero
    contador = 0

    # Cargar el engine de la base de datos para ejecutar comandos SQL
    engine = get_engine(settings)

    # Vaciar la tabla
    with engine.connect() as connection:
        connection.execute(text("TRUNCATE public.conceptos RESTART IDENTITY CASCADE"))

    # Cargar sesion de la base de datos
    session = get_session(settings)

    # Alimentar los conceptos
    for concepto in conceptos:
        session.add(
            ConceptoDB(
                clave=safe_string(f"{concepto.p_d.value}{concepto.concepto}"),
                descripcion=safe_string(concepto.descripcion),
            )
        )

        # Incrementar contador
        contador += 1

    # Cerrar la sesion para que se carguen los datos
    session.commit()
    session.close()

    # Terminar
    return contador
