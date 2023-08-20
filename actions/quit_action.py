from .action import Action
from rich.console import Console
from directory_manager import DirectoryManager


class QuitAction(Action):
    """
    Action to quit the application.

    This action saves the directory changes, displays a success message,
    and exits the application.

    Args:
        Action: The base class for actions.

    Methods:
        run(console, directory_manager): Execute the action to quit the application.
    """

    def run(self, console: Console, directory_manager: DirectoryManager) -> None:
        """
        Execute the action to quit the application.

        Args:
            console (Console): The console object for output.
            directory_manager (DirectoryManager): The directory manager instance.

        Returns:
            None
        """
        console.print()
        directory_manager.serialize_directory()
        console.print("[green]Changes saved successfully.[/green]")
        console.print("Exiting...")
        exit()
