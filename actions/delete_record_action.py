from record import Record
from .action import Action
from rich.console import Console
from errors import RecordDoesNotExist
from directory_manager import DirectoryManager


class DeleteRecordAction(Action):
    """
    Action to delete a record from the directory.

    This action prompts the user to enter the personal phone number of the record
    they want to delete. It attempts to delete the record with the given personal
    number from the directory. If the record does not exist, an error message is displayed.

    Args:
        Action: The base class for actions.

    Methods:
        run(console, directory_manager): Execute the action to delete a record.

    """

    def run(
        self, console: Console, directory_manager: DirectoryManager
    ) -> list[Record]:
        """
        Execute the action to delete a record.

        Args:
            console (Console): The console object for input and output.
            directory_manager (DirectoryManager): The directory manager instance.

        Returns:
            list[Record]: The updated list of records in the directory.
        """
        records_personal_number = console.input(
            "\nEnter personal phone number of the record you want to delete: "
        )

        try:
            directory_manager.delete_record(records_personal_number)
        except RecordDoesNotExist as e:
            error_message = e.args[0]
            console.print(f"[red]{error_message}[/red]")
            console.input("Press ENTER to continue...")
            return

        console.print("[green]Record deleted successfully.[/green]")
        console.input("Press ENTER to refresh the table...")

        return directory_manager.get_records()
