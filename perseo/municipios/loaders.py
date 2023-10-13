"""
Perseo - Municipios - Loaders
"""
import csv
from pathlib import Path

from lib.exceptions import MyFileNotFoundError
from perseo.municipios.classes import Municipio


def load_municipios() -> list[Municipio]:
    """Load municipios"""

    # Verificar que exista el archivo data/municipios.csv
    municipios_archivo = Path("data/municipios.csv")
    if not municipios_archivo.exists():
        raise MyFileNotFoundError(f"No existe el archivo {municipios_archivo}")

    # Leer el archivo data/municipios.csv
    municipios = []
    with open(municipios_archivo, newline="", encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            municipios.append(
                Municipio(
                    clave=int(row["Clave"]),
                    nombre=row["Nombre"],
                )
            )

    # Entregar el listado de municipios
    return municipios
