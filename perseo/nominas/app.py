"""
Perseo - Nominas
"""
import locale

import rich
import typer

from config.settings import get_settings
from lib.exceptions import MyAnyError
from perseo.nominas.feeders import feed_nominas
from perseo.nominas.loaders import load_nominas

locale.setlocale(locale.LC_ALL, "es_MX.UTF-8")

app = typer.Typer()


@app.command()
def alimentar():
    """Alimentar nominas a la base de datos"""
    rich.print("Alimentar nominas a la base de datos")

    # Alimentar nominas
    try:
        settings = get_settings()
        nominas = load_nominas(settings)
        cantidad = feed_nominas(settings, nominas)
    except MyAnyError as error:
        typer.secho(str(error), fg=typer.colors.RED)
        raise typer.Exit()

    # Mostrar mensaje de exito
    typer.secho(f"Nominas alimentadas: {cantidad}", fg=typer.colors.GREEN)


@app.command()
def mostrar():
    """Mostrar nominas"""
    rich.print("Mostrar nominas")

    # Cargar nominas
    try:
        settings = get_settings()
        nominas = load_nominas(settings)
    except MyAnyError as error:
        typer.secho(str(error), fg=typer.colors.RED)
        raise typer.Exit()

    # Mostrar tabla con las nominas
    console = rich.console.Console()
    table = rich.table.Table(
        "RFC",
        "Nombres",
        "Apellido primero",
        "Apellido segundo",
        "Centro de Trabajo",
        "Concepto",
        "Plaza",
        "Quincena",
        "Importe",
    )
    for nomina in nominas:
        table.add_row(
            nomina.rfc,
            nomina.nombres,
            nomina.apellido_primero,
            nomina.apellido_segundo,
            nomina.centro_trabajo_clave,
            nomina.concepto_clave,
            nomina.plaza_clave,
            nomina.quincena,
            str(locale.currency(nomina.importe, grouping=True)).ljust(12),
        )
    console.print(table)
