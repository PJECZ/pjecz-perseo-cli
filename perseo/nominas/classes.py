"""
Perseo - Nominas - Classes
"""
from pydantic import BaseModel


class Nomina(BaseModel):
    """Nomina"""

    rfc: str
    nombres: str
    apellido_primero: str
    apellido_segundo: str
    centro_trabajo_clave: str
    concepto_clave: str
    plaza_clave: str
    quincena: str
    importe: float
