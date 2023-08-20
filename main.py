from table import Table
from rich.console import Console
from config import RECORDS_PER_PAGE
from utils import calculate_index_range
from directory_manager import DirectoryManager
from actions import NextPageAction, PreviousPageAction
from errors import NotUniquePersonalNumber, RecordValidationError
from key_binding import directory_actions, directory_actions_legend


def main() -> None:
    """
    Entry point for the phone directory program.

    Returns:
        None
    """
    console = Console()
    directory_manager = DirectoryManager("data.csv")

    try:
        directory_manager.deserialize_directory()
    except (NotUniquePersonalNumber, RecordValidationError) as e:
        error_message = e.args[0]
        console.print(f"[red]Deserialization ERROR:[/red]\n{error_message}\nExiting...")
        return

    records = directory_manager.get_records()

    current_page_number = 1
    total_pages = (len(records) + RECORDS_PER_PAGE - 1) // RECORDS_PER_PAGE

    while True:
        console.clear()

        start_index, end_index = calculate_index_range(
            current_page_number, RECORDS_PER_PAGE
        )
        current_page_records = records[start_index:end_index]

        table = Table(title="PHONE DIRECTORY")
        table.add_columns(directory_manager.get_directory_field_names())
        table.add_rows(current_page_records)

        console.print(table)
        console.print(f"Page {current_page_number} of {total_pages}")

        action_key = console.input(directory_actions_legend + ": ").lower()

        if action_key in directory_actions:
            requested_action = directory_actions[action_key]
            if isinstance(requested_action, NextPageAction) or isinstance(
                requested_action, PreviousPageAction
            ):
                current_page_number = requested_action.run(
                    current_page_number, total_pages
                )
            else:
                updated_records = requested_action.run(console, directory_manager)
                records = updated_records if updated_records is not None else records


if __name__ == "__main__":
    main()
