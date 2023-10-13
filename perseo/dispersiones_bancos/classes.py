"""
Perseo - Dispersiones Bancos - Classes
"""
from pydantic import BaseModel

from perseo.conceptos.classes import Concepto
from perseo.personas.classes import Persona


class PercepcionDeduccion(BaseModel):
    """Percepcion o Deduccion"""

    concepto: Concepto
    importe: float
    desde: str
    hasta: str


class Dispersion(BaseModel):
    """Dispersion"""

    persona: Persona
    percepcion: float
    deduccion: float
    importe: float
    num_cheque: int
    percepciones_deducciones: list[PercepcionDeduccion] = []
