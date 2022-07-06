"""Command-line interface."""

import typer


app = typer.Typer()


@app.command("goodbye", help="Say goodbye to the user.")
def goodbye() -> None:
    """Say goodbye to the user."""
    print("Goodbye!")


@app.command("hello", help="Greet the user.")
def hello() -> None:
    """Greet the user."""
    print("Hello!")


def main() -> None:
    """{{cookiecutter.friendly_name}}."""
    app()


typer_click_object = typer.main.get_command(app)
