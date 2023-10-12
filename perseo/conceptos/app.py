"""
Conceptos
"""
import rich
import typer

from lib.exceptions import MyAnyError
from perseo.conceptos.loaders import load_conceptos

app = typer.Typer()


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
