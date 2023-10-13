"""
Perseo - Personas - Classes
"""
from pydantic import BaseModel


class Persona(BaseModel):
    """Persona"""

    centro_trabajo_clave: str
    rfc: str
    nombre: str
    municipio: int
    plaza: str
    sexo: str
