"""
Perseo - Municipios
"""
import rich
import typer

from lib.exceptions import MyAnyError
from perseo.municipios.loaders import load_municipios

app = typer.Typer()


@app.command()
def mostrar():
    """Mostrar municipios"""
    rich.print("Mostrar municipios")

    # Cargar municipios
    try:
        municipios = load_municipios()
    except MyAnyError as error:
        typer.secho(str(error), fg=typer.colors.RED)
        raise typer.Exit()

    # Mostrar tabla con los municipios
    console = rich.console.Console()
    table = rich.table.Table("Clave", "Nombre")
    for municipio in municipios:
        table.add_row(
            str(municipio.clave),
            municipio.nombre,
        )
    console.print(table)
