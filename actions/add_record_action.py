from .action import Action
from record import Record
from rich.console import Console
from errors import NotUniquePersonalNumber
from utils import get_record_from_keyboard
from directory_manager import DirectoryManager


class AddRecordAction(Action):
    """
    Action to add a new record to the directory.

    This action prompts the user to enter a new record's information and
    attempts to add the record to the directory. If the personal number
    is not unique, an error message is displayed.

    Args:
        Action: The base class for actions.

    Methods:
        run(console, directory_manager): Execute the action to add a record.

    """

    def run(
        self, console: Console, directory_manager: DirectoryManager
    ) -> list[Record]:
        """
        Execute the action to add a new record.

        Args:
            console (Console): The console object for input and output.
            directory_manager (DirectoryManager): The directory manager instance.

        Returns:
            list[Record]: The updated list of records in the directory.
        """
        console.clear()
        console.print("Enter new record (some fields can be left with '-'): \n")
        record = get_record_from_keyboard(console, directory_manager)

        try:
            directory_manager.add_record(record)
        except NotUniquePersonalNumber as e:
            error_message = e.args[0]
            console.print(f"\n[red]{error_message}[/red]")
            console.input("Press ENTER to get back to the directory...")
            return

        console.print("\n[green]Record successfully added.[/green]")
        console.input("Press ENTER to get back to the directory...")

        return directory_manager.get_records()
