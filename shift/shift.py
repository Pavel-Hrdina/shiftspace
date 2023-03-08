"""Main module."""
import sys
import os

from pathlib import Path
from loguru import logger

HOME_DIR = Path.home()
TEMP = str(HOME_DIR) + "\\temp"
YEAR = ""
ROOT_FOLDERS = [
    "workspace",
]


class Main:
    """A class that represents the main application.

    This class is responsible for managing the main application and its features.
    """

    def __init__(self, location: str, folders: list) -> None:
        """Initializes the Main class.

        This method sets up the Main class for use.

        Args:
            location (str): location of the root folder
            folders (list): list of folders to generate
        """
        self.location = location
        self.folders = folders

    def create_workspace(self):
        """Create the workspace folder.

        This method creates the 'workspace' folder at the specified location.
        If the folder already exists, an OSError is raised and the program exits.
        """
        logger.info("create workspace...")
        try:
            os.makedirs(self.location + "\\workspace")
            logger.info("done!")
        except OSError:
            logger.exception("folder: 'workspace' already exists")
            sys.exit()

    def generate_folders(self):
        """_Create subfolders

        Create necessary subfolders inside the workspace folder.
        """
        logger.info("create level 2 subfolders...")

        for items in self.folders:
            logger.info(
                f"create subfolder {items} at {self.location}\\workspace\\{items}"
            )
            os.mkdir(f"{self.location}\\workspace\\{items}")

        logger.success("done!")


main = Main(TEMP, ROOT_FOLDERS)

main.create_workspace()
main.generate_folders()

if __name__ == "__main__ ":
    sys.exit()
