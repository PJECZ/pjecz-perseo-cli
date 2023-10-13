"""
Perseo - Dispersiones Bancos - Searchers
"""
from pathlib import Path

import xlrd

from config.settings import Settings
from lib.exceptions import MyFileNotFoundError, MyNoDataWarning, MyNotValidParamError
from lib.fechas import crear_clave_quincena
from lib.safe_string import safe_rfc
from perseo.personas.classes import Persona


def buscar_rfc(settings: Settings, rfc: str) -> Persona:
    """Buscar un RFC"""

    # Validar RFC
    try:
        rfc = safe_rfc(rfc)
    except ValueError as error:
        raise MyNotValidParamError(str(error)) from error

    # Crear clave de quincena
    clave_quincena = crear_clave_quincena(settings.fecha)

    # Validar si existe el archivo
    archivo = Path(settings.explotacion_base_dir, clave_quincena, "NominaFmt2.XLS")
    if not archivo.exists():
        raise MyFileNotFoundError(f"No existe el archivo {str(archivo)}")

    # Abrir el archivo XLS con xlrd
    libro = xlrd.open_workbook(str(archivo))

    # Obtener la primera hoja
    hoja = libro.sheet_by_index(0)

    # Buscar el RFC en la hoja, donde la columna 2 (comienza en 0) es el RFC
    persona = None
    for fila in range(hoja.nrows):
        if hoja.cell_value(fila, 2) == rfc:
            persona = Persona(
                centro_trabajo_clave=hoja.cell_value(fila, 1),
                rfc=hoja.cell_value(fila, 2),
                nombre=hoja.cell_value(fila, 3),
                municipio=int(hoja.cell_value(fila, 4)),
                plaza=hoja.cell_value(fila, 8),
                sexo=hoja.cell_value(fila, 18),
            )
            return persona

    # Si no se encuentra el RFC, levantar excepcion
    raise MyNoDataWarning(f"No se encontro el RFC {rfc}")
