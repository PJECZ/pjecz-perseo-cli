"""
Perseo - Municipios - Classes
"""
from pydantic import BaseModel


class Municipio(BaseModel):
    """Municipio"""

    clave: int
    nombre: str
