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
        persona = buscar_rfc(settings=settings, rfc=rfc)
    except MyAnyError as error:
        typer.secho(str(error), fg=typer.colors.RED)
        raise typer.Exit()

    # Mostrar resultado
    rich.print(f"Centro de trabajo: [green]{persona.centro_trabajo_clave}[/green]")
    rich.print(f"RFC:               [green]{persona.rfc}[/green]")
    rich.print(f"Nombre:            [green]{persona.nombre}[/green]")
    rich.print(f"Municipio:         [green]{persona.municipio}[/green]")
    rich.print(f"Plaza:             [green]{persona.plaza}[/green]")
    rich.print(f"Sexo:              [green]{persona.sexo}[/green]")


@app.command()
def generar():
    """Crear layout para el banco"""
    rich.print("Crear layout para el banco")
