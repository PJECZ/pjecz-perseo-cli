"""
Perseo - Nominas - Loaders
"""
from pathlib import Path

import xlrd

from config.settings import Settings
from lib.exceptions import MyFileNotFoundError
from lib.fechas import crear_clave_quincena
from lib.safe_string import safe_string
from perseo.nominas.classes import Nomina


def load_nominas(settings: Settings) -> list[Nomina]:
    """Load nominas"""

    # Inicializar el listado que se va a entregar
    nominas = []

    # Crear clave de quincena
    quincena = crear_clave_quincena(settings.FECHA)

    # Validar si existe el archivo
    archivo = Path(settings.EXPLOTACION_BASE_DIR, quincena, "NominaFmt2.XLS")
    if not archivo.exists():
        raise MyFileNotFoundError(f"No existe el archivo {str(archivo)}")

    # Abrir el archivo XLS con xlrd
    libro = xlrd.open_workbook(str(archivo))

    # Obtener la primera hoja
    hoja = libro.sheet_by_index(0)

    # Bucle por cada fila
    for fila in range(1, hoja.nrows):
        # Tomar las columnas
        centro_trabajo_clave = hoja.cell_value(fila, 1)
        rfc = hoja.cell_value(fila, 2)
        nombre_completo = hoja.cell_value(fila, 3)
        plaza_clave = hoja.cell_value(fila, 8)
        # percepcion = int(hoja.cell_value(fila, 12)) / 100.0
        # deduccion = int(hoja.cell_value(fila, 13)) / 100.0
        # importe = int(hoja.cell_value(fila, 14)) / 100.0
        # Separar nombre_completo, en apellido_primero, apellido_segundo y nombres
        separado = nombre_completo.split(" ")
        apellido_primero = separado[0]
        apellido_segundo = separado[1]
        nombres = " ".join(separado[2:])
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
            # desde = hoja.cell_value(fila, col_num + 4)
            # hasta = hoja.cell_value(fila, col_num + 5)
            # Acumular en las nominas
            nominas.append(
                Nomina(
                    rfc=rfc,
                    nombres=nombres,
                    apellido_primero=apellido_primero,
                    apellido_segundo=apellido_segundo,
                    centro_trabajo_clave=centro_trabajo_clave,
                    concepto_clave=f"{tipo}{conc}",
                    plaza_clave=plaza_clave,
                    quincena=quincena,
                    importe=impt,
                )
            )
            # Incrementar col_num en SEIS
            col_num += 6
            # Romper el ciclo cuando se llega a la columna
            if col_num > 236:
                break

    # Entregar
    return nominas
