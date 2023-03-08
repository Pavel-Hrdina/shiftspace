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

class Main():
    """A class that represents the main application.

    This class is responsible for managing the main application and its features.
    """

    def __init__(self, location: str, folders: list) -> None:
        """Initializes the Main class.

        This method sets up the Main class for use.
        """
        self.location = location
        self.folders = []

    def create_workspace(self):
        """_summary_

        _extended_summary_
        """
        logger.info("create workspace...")
        try:
            os.makedirs(self.location + "\\workspace")
            logger.info("done!")
        except OSError:
            logger.exception("folder: 'workspace' already exists")
            sys.exit()

    def hello(self):
        print("Hello world!")

main = Main()

main.hello()

if __name__ == '__main__ ':
    sys.exit()
