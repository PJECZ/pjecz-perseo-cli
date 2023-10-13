"""
Perseo - Dispersiones Bancos
"""
import rich
import typer
from openpyxl import Workbook

from config.settings import get_settings
from lib.exceptions import MyAnyError
from perseo.dispersiones_bancos.searchers import buscar_rfc

app = typer.Typer()


@app.command()
def mostrar():
    """Mostrar dispersiones bancarias"""
    rich.print("Mostrar dispersiones bancarias")


@app.command()
def buscar(rfc: str):
    """Buscar un RFC"""
    rich.print("Buscar un RFC")

    # Obtener configuracion
    settings = get_settings()

    # Buscar RFC
    try:
        dispersion = buscar_rfc(settings=settings, rfc=rfc)
    except MyAnyError as error:
        typer.secho(str(error), fg=typer.colors.RED)
        raise typer.Exit()

    # Mostrar resultado
    rich.print(f"Centro de trabajo: [green]{dispersion.persona.centro_trabajo_clave}[/green]")
    rich.print(f"RFC:               [green]{dispersion.persona.rfc}[/green]")
    rich.print(f"Nombre:            [green]{dispersion.persona.nombre}[/green]")
    rich.print(f"Municipio:         [green]{dispersion.persona.municipio}[/green]")
    rich.print(f"Plaza:             [green]{dispersion.persona.plaza}[/green]")
    rich.print(f"Sexo:              [white]{dispersion.persona.sexo}[/white]")
    rich.print()

    # Mostrar percepciones
    for percepcion in dispersion.percepciones_deducciones:
        if percepcion.concepto.p_d.value == "P":
            rich.print(f"{percepcion.concepto.descripcion}: [green]{percepcion.importe}[/green]")
    rich.print()

    # Mostrar deducciones
    for percepcion in dispersion.percepciones_deducciones:
        if percepcion.concepto.p_d.value == "D":
            rich.print(f"{percepcion.concepto.descripcion}: [red]{percepcion.importe}[/red]")
    rich.print()

    # Mostrar cantidades finales
    rich.print(f"Percepcion:        [blue]{dispersion.percepcion}[/blue]")
    rich.print(f"Deduccion:         [red]{dispersion.deduccion}[/red]")
    rich.print(f"Importe:           [green]{dispersion.importe}[/green]")
    rich.print(f"No. Cheque:        [gray]{dispersion.num_cheque}[/gray]")
    rich.print()


@app.command()
def guardar(rfc: str):
    """Crear un archivo XLSX"""
    rich.print("Crear un archivo XLSX")

    # Obtener configuracion
    settings = get_settings()

    # Buscar RFC
    try:
        dispersion = buscar_rfc(settings=settings, rfc=rfc)
    except MyAnyError as error:
        typer.secho(str(error), fg=typer.colors.RED)
        raise typer.Exit()

    # Crear el libro
    wb = Workbook()
    ws = wb.active

    # Escribir los datos de la persona
    ws.append(["Centro de trabajo", dispersion.persona.centro_trabajo_clave])
    ws.append(["RFC", dispersion.persona.rfc])
    ws.append(["Nombre", dispersion.persona.nombre])
    ws.append(["Municipio", dispersion.persona.municipio])
    ws.append(["Plaza", dispersion.persona.plaza])
    ws.append(["Sexo", dispersion.persona.sexo])

    # Escribir las percepciones
    ws.append(["Percepciones"])
    for percepcion in dispersion.percepciones_deducciones:
        if percepcion.concepto.p_d.value == "P":
            ws.append([percepcion.concepto.descripcion, percepcion.importe])

    # Escribir las deducciones
    ws.append(["Deducciones"])
    for percepcion in dispersion.percepciones_deducciones:
        if percepcion.concepto.p_d.value == "D":
            ws.append([percepcion.concepto.descripcion, percepcion.importe])

    # Escribir las cantidades finales
    ws.append(["Percepcion", dispersion.percepcion])
    ws.append(["Deduccion", dispersion.deduccion])
    ws.append(["Importe", dispersion.importe])
    ws.append(["No. Cheque", dispersion.num_cheque])

    # Guardar el archivo, con el nombre del archivo con el RFC
    wb.save(f"{dispersion.persona.rfc}.xlsx")


@app.command()
def generar():
    """Crear layout para el banco"""
    rich.print("Crear layout para el banco")
