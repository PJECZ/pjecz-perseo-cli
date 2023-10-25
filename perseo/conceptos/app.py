"""
Perseo - Conceptos
"""
import rich
import typer

from config.settings import get_settings
from lib.exceptions import MyAnyError
from perseo.conceptos.feeders import feed_conceptos
from perseo.conceptos.loaders import load_conceptos

app = typer.Typer()


@app.command()
def alimentar():
    """Alimentar conceptos a la base de datos"""
    rich.print("Alimentar conceptos en la base de datos")

    # Obtener configuracion
    settings = get_settings()

    # Alimentar conceptos
    try:
        conceptos = load_conceptos()
        feed_conceptos(settings, conceptos)
    except MyAnyError as error:
        typer.secho(str(error), fg=typer.colors.RED)
        raise typer.Exit()

    # Mostrar mensaje de exito
    typer.secho("Conceptos alimentados", fg=typer.colors.GREEN)


@app.command()
def mostrar():
    """Mostrar conceptos"""
    rich.print("Mostrar conceptos")

    # Cargar conceptos
    try:
        conceptos = load_conceptos()
    except MyAnyError as error:
        typer.secho(str(error), fg=typer.colors.RED)
        raise typer.Exit()

    # Mostrar tabla con los clientes
    console = rich.console.Console()
    table = rich.table.Table("P/D", "Concepto", "Descripcion")
    for concepto in conceptos:
        table.add_row(
            concepto.p_d.value,
            concepto.concepto,
            concepto.descripcion,
        )
    console.print(table)
