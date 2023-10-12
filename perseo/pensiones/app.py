"""
Pensiones
"""
import rich
import typer

app = typer.Typer()


@app.command()
def mostrar():
    """Mostrar pensiones"""
    rich.print("Mostrar pensiones")
