"""Main module."""
import os
import sys
from dataclasses import dataclass

from loguru import logger


@dataclass
class Main(object):
    """A class that represents the main application.

    This class is responsible for managing the main application and its features.
    """

    location: str
    folders: list

    def create_workspace(self) -> None:
        """Create the workspace folder.

        This method creates the 'workspace' folder at the specified location.
        If the folder already exists, an OSError is raised and the program exits.
        """
        logger.info("create workspace...")
        try:
            os.makedirs(self.location + "\\workspace")
            logger.success("done!")
        except OSError:
            logger.exception("folder: 'workspace' already exists")
            sys.exit()

    def generate_folders(self) -> None:
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
