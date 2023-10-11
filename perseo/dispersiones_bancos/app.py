"""
Dispersiones - Bancos
"""
import rich
import typer

from config.settings import get_settings
from lib.exceptions import MyAnyError

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
        resultado = buscar_rfc(settings=settings, rfc=rfc)
    except MyAnyError as error:
        typer.secho(str(error), fg=typer.colors.RED)
        raise typer.Exit()

    # Mostrar resultado
    rich.print(f"Resultado: [green]{resultado}[/green]")


@app.command()
def generar():
    """Crear layout para el banco"""
    rich.print("Crear layout para el banco")
