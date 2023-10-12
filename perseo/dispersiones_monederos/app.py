"""
Dispersiones Monederos
"""
import rich
import typer

app = typer.Typer()


@app.command()
def mostrar():
    """Mostrar dispersiones monederos electronicos"""
    rich.print("Mostrar dispersiones monederos electronicos")
