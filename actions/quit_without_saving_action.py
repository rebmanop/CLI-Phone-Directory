from .action import Action
from rich.console import Console
from directory_manager import DirectoryManager


class QuitWithoutSavingAction(Action):
    """
    Action to quit the application without saving changes.

    This action displays an exit message and terminates the application
    without saving any changes made to the directory.

    Args:
        Action: The base class for actions.

    Methods:
        run(console, directory_manager): Execute the action to quit without saving changes.
    """

    def run(self, console: Console, directory_manager: DirectoryManager) -> None:
        """
        Execute the action to quit the application without saving changes.

        Args:
            console (Console): The console object for output.
            directory_manager (DirectoryManager): The directory manager instance.

        Returns:
            None
        """
        console.print()
        console.print("[red]Exiting without saving...[/red]")
        exit()
