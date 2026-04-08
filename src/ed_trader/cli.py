"""Console script for ed_trader."""

import typer
from rich.console import Console

from ed_trader import utils

app = typer.Typer()
console = Console()


@app.command()
def main() -> None:
    """Console script for ed_trader."""
    console.print("Replace this message by putting your code into "
               "ed_trader.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()
