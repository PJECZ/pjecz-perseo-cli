"""
Perseo - Conceptos - Classes
"""
from enum import Enum

from pydantic import BaseModel


class TipoPercepcionDeduccion(Enum):
    """Tipo de percepción o deducción"""

    PERCEPCION = "P"
    DEDUCCION = "D"


class Concepto(BaseModel):
    """Concepto"""

    p_d: TipoPercepcionDeduccion
    concepto: str
    descripcion: str
