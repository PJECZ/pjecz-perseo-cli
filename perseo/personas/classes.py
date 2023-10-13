"""
Perseo - Personas - Classes
"""
from pydantic import BaseModel

from perseo.municipios.classes import Municipio


class Persona(BaseModel):
    """Persona"""

    centro_trabajo_clave: str
    rfc: str
    nombre: str
    municipio: Municipio
    plaza: str
    sexo: str
