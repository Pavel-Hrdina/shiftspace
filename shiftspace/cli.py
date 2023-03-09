import click
from pathlib import Path
from shiftspace.main import Main

HOME_DIR = Path.home()
TEMP = str(HOME_DIR) + "\\temp"
YEAR = ""
ROOT_FOLDERS = ["docs", "projects", "tools"]


@click.command()
@click.option("--path", default=TEMP, help="give path to workspace")
def app(path):
    """Shiftspace CLI

    This command-line interface (CLI) application creates a workspace
    at the given path and generates folders within it.
    """
    main = Main(path, ROOT_FOLDERS)
    main.create_workspace()
    main.generate_folders()


if __name__ == "__main__":
    app()
