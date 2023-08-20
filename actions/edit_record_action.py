from table import Table
from record import Record
from .action import Action
from rich.console import Console
from utils import edit_record_from_keyboard
from directory_manager import DirectoryManager
from errors import RecordDoesNotExist, NotUniquePersonalNumber


class EditRecordAction(Action):
    """
    Action to edit a record in the directory.

    This action prompts the user to enter the personal phone number of the record
    they want to edit. It retrieves the old record, displays it for reference, and
    prompts the user to edit the record fields. The edited record is then added back
    to the directory. If the personal number is not unique, the old record's personal
    number is retained.

    Args:
        Action: The base class for actions.

    Methods:
        run(console, directory_manager): Execute the action to edit a record.
    """

    def run(
        self, console: Console, directory_manager: DirectoryManager
    ) -> list[Record]:
        """
        Execute the action to edit a record.

        Args:
            console (Console): The console object for input and output.
            directory_manager (DirectoryManager): The directory manager instance.

        Returns:
            list[Record]: The updated list of records in the directory.
        """
        records_personal_number = console.input(
            "\nEnter personal phone number of the record you want to edit: "
        )

        try:
            old_record_to_edit = directory_manager.delete_record(
                records_personal_number
            )
        except RecordDoesNotExist as e:
            error_message = e.args[0]
            console.print(f"[red]{error_message}[/red]")
            console.input("Press ENTER to get back to the directory...")
            return

        console.clear()

        table = Table(title="Selected for editing record")
        table.add_columns(directory_manager.get_directory_field_names())
        table.add_rows([old_record_to_edit])
        console.print(table)
        console.print("\nEdit record, ENTER to keep old field value:")
        console.print()

        new_edited_record = edit_record_from_keyboard(
            console, directory_manager, old_record_to_edit
        )

        try:
            directory_manager.add_record(new_edited_record)
        except NotUniquePersonalNumber:
            console.print(
                "[yellow]\nPersonal phone number already exist in the directory. Saving record with old personal number.[/yellow]"
            )
            console.input("Press ENTER to get back to the directory...")
            new_edited_record.personal_phone = old_record_to_edit.personal_phone
            directory_manager.add_record(new_edited_record)
            return directory_manager.get_records()

        console.print("\n[green]Record edited successfully.[green]")
        console.input("Press ENTER to get back to the directory...")

        return directory_manager.get_records()
