"""
Conceptos - Loaders
"""
import csv
from pathlib import Path

from lib.exceptions import MyFileNotFoundError
from perseo.conceptos.classes import Concepto


def load_conceptos() -> list[Concepto]:
    """Load conceptos"""

    # Verificar que exista el archivo data/conceptos.csv
    conceptos_archivo = Path("data/conceptos.csv")
    if not conceptos_archivo.exists():
        raise MyFileNotFoundError(f"No existe el archivo {conceptos_archivo}")

    # Leer el archivo data/conceptos.csv
    conceptos = []
    with open(conceptos_archivo, newline="", encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            conceptos.append(
                Concepto(
                    p_d=row["P_D"],
                    concepto=row["Concepto"],
                    descripcion=row["Descripcion"],
                )
            )

    # Entregar el listado de conceptos
    return conceptos
