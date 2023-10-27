"""
Perseo - Dispersiones Monederos - Loaders
"""
from pathlib import Path

import xlrd

from config.settings import Settings
from lib.exceptions import MyFileNotFoundError, MyNoDataWarning
from lib.fechas import crear_clave_quincena
from lib.safe_string import safe_string
from perseo.conceptos.loaders import load_conceptos
from perseo.dispersiones_bancos.classes import Dispersion, PercepcionDeduccion
from perseo.municipios.loaders import load_municipios
from perseo.personas.classes import Persona


def leer(settings: Settings) -> list[Dispersion]:
    """Leer todo el archivo de nomina"""

    # Crear clave de quincena
    clave_quincena = crear_clave_quincena(settings.FECHA)

    # Validar si existe el archivo
    archivo = Path(settings.EXPLOTACION_BASE_DIR, clave_quincena, "NominaFmt2.XLS")
    if not archivo.exists():
        raise MyFileNotFoundError(f"No existe el archivo {str(archivo)}")

    # Cargar los conceptos
    conceptos = load_conceptos()

    # Cargar los municipios
    municipios = load_municipios()

    # Abrir el archivo XLS con xlrd
    libro = xlrd.open_workbook(str(archivo))

    # Obtener la primera hoja
    hoja = libro.sheet_by_index(0)

    # Preparar listados de dispersiones
    dispersiones = []

    # Bucle por cada fila
    for fila in range(1, hoja.nrows):
        # Tomar el municipio
        municipio = None
        for item in municipios:
            if item.clave == int(hoja.cell_value(fila, 4)):
                municipio = item
                break
        # Si no encuentra el municipio, levantar excepcion
        if municipio is None:
            raise MyNoDataWarning(f"No se encontro el municipio {hoja.cell_value(fila, 4)}")
        # Tomar los datos de la persona
        persona = Persona(
            centro_trabajo_clave=hoja.cell_value(fila, 1),
            rfc=hoja.cell_value(fila, 2),
            nombre=hoja.cell_value(fila, 3),
            municipio=municipio,
            plaza=hoja.cell_value(fila, 8),
            sexo=hoja.cell_value(fila, 18),
        )
        # Tomar los datos de la dispersion
        dispersion = Dispersion(
            persona=persona,
            percepcion=int(hoja.cell_value(fila, 12)) / 100.0,
            deduccion=int(hoja.cell_value(fila, 13)) / 100.0,
            importe=int(hoja.cell_value(fila, 14)) / 100.0,
            num_cheque=int(hoja.cell_value(fila, 15)),
        )
        # Buscar percepciones y deducciones
        col_num = 26
        while True:
            # Tomar el tipo, primero
            tipo = safe_string(hoja.cell_value(fila, col_num))
            # Si el tipo es un texto vacio, se rompe el ciclo
            if tipo == "":
                break
            # Tomar las cinco columnas
            conc = safe_string(hoja.cell_value(fila, col_num + 1))
            try:
                impt = int(hoja.cell_value(fila, col_num + 3)) / 100.0
            except ValueError:
                impt = 0.0
            desde = hoja.cell_value(fila, col_num + 4)
            hasta = hoja.cell_value(fila, col_num + 5)
            # Buscar el concepto
            concepto = None
            for item in conceptos:
                if item.p_d.value == tipo and item.concepto == conc:
                    concepto = item
                    break
            # Si no encuentra el concepto, levantar excepcion
            if concepto is None:
                concepto = conceptos[0]  # raise MyNoDataWarning(f"No se encontro el concepto {tipo}{conc}")
            # Acumular la percepcion o la deduccion en dispersion
            dispersion.percepciones_deducciones.append(
                PercepcionDeduccion(
                    concepto=concepto,
                    importe=impt,
                    desde=desde,
                    hasta=hasta,
                )
            )
            # Incrementar col_num en SEIS
            col_num += 6
            # Romper el ciclo cuando se llega a la columna
            if col_num > 236:
                break
        # Acumular la dispersion en dispersiones
        dispersiones.append(dispersion)

    # Si no se encuentran dispersiones, levantar excepcion
    if len(dispersiones) == 0:
        raise MyNoDataWarning("No hay dispersiones")

    # Entregar dispersiones
    return dispersiones
