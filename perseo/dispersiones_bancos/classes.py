"""
Perseo - Dispersiones Bancos - Classes
"""
from pydantic import BaseModel

from perseo.conceptos.classes import Concepto
from perseo.personas.classes import Persona


class PercepcionDescuento(BaseModel):
    """Percepcion o Descuento"""

    codigo: str
    concepto: Concepto
    importe: float


class Dispersion(BaseModel):
    """Dispersion"""

    persona: Persona
    percepcion: int
    deduccion: int
    importe: int
    num_cheque: int
    percepcion_descuento: PercepcionDescuento
