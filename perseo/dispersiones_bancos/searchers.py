"""
Perseo - Dispersiones Bancos - Searchers
"""
from config.settings import Settings
from lib.fechas import crear_clave_quincena


def buscar_rfc(settings: Settings, rfc: str) -> str:
    """Buscar un RFC"""
