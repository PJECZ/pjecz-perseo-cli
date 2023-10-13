"""
Perseo - Dispersiones Monederos
"""
import rich
import typer
from openpyxl import Workbook

from config.settings import get_settings
from lib.exceptions import MyAnyError
from perseo.dispersiones_monederos.loaders import leer

app = typer.Typer()


@app.command()
def generar():
    """Crear layout para el banco"""
    rich.print("Crear layout para el banco")

    # Obtener configuracion
    settings = get_settings()

    # Leer todo el archivo de explotacion
    try:
        dispersiones = leer(settings=settings)
    except MyAnyError as error:
        typer.secho(str(error), fg=typer.colors.RED)
        raise typer.Exit()

    # Crear el libro
    wb = Workbook()
    ws = wb.active

    # Escribir los encabezados en el primer renglon
    ws.append(
        [
            "Centro de trabajo",
            "RFC",
            "Nombre",
            "Municipio",
            "Plaza",
            "Sexo",
            "Percepcion",
            "Deduccion",
            "Importe",
            "No. Cheque",
        ]
    )

    # Bucle para iterar las dispersiones
    for dispersion in dispersiones:
        # Si uno de los conceptos NO es "ME", se salta la dispersion
        tiene_monedero_electronico = False
        for percepcion_deduccion in dispersion.percepciones_deducciones:
            if percepcion_deduccion.concepto.concepto == "ME":
                tiene_monedero_electronico = True
                break
        if not tiene_monedero_electronico:
            continue

        # Escribir los datos de la persona
        ws.append(
            [
                dispersion.persona.centro_trabajo_clave,
                dispersion.persona.rfc,
                dispersion.persona.nombre,
                dispersion.persona.municipio.nombre,
                dispersion.persona.plaza,
                dispersion.persona.sexo,
                dispersion.percepcion,
                dispersion.deduccion,
                dispersion.importe,
                dispersion.num_cheque,
            ]
        )

    # Guardar el archivo, con el nombre TODOS.xlsx
    wb.save("monederos.xlsx")
