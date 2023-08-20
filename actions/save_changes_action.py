from .action import Action
from rich.console import Console
from directory_manager import DirectoryManager


class SaveChangesAction(Action):
    """
    Action to save changes made to the directory.

    This action serializes the directory to save any changes and displays a success message.

    Args:
        Action: The base class for actions.

    Methods:
        run(console, directory_manager): Execute the action to save changes.
    """

    def run(self, console: Console, directory_manager: DirectoryManager) -> None:
        """
        Execute the action to save changes made to the directory.

        Args:
            console (Console): The console object for output.
            directory_manager (DirectoryManager): The directory manager instance.

        Returns:
            None
        """
        console.print()
        directory_manager.serialize_directory()
        console.print("[green]Changes saved successfully.[/green]")
        console.input("Press ENTER to continue...")
