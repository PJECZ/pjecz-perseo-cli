"""
Perseo - Dispersiones Bancos
"""
import rich
import typer

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
    rich.print(f"Sexo:              [green]{dispersion.persona.sexo}[/green]")

    rich.print(f"Percepcion:        [blue]{dispersion.percepcion}[/blue]")
    rich.print(f"Deduccion:         [red]{dispersion.deduccion}[/red]")
    rich.print(f"Importe:           [green]{dispersion.importe}[/green]")
    rich.print(f"No. Cheque:        [gray]{dispersion.num_cheque}[/gray]")


@app.command()
def generar():
    """Crear layout para el banco"""
    rich.print("Crear layout para el banco")
