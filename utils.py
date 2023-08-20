from table import Table
from record import Record
from rich.prompt import Prompt
from rich.console import Console
from config import RECORDS_PER_PAGE
from search_result import SearchResult
from directory_manager import DirectoryManager


def get_record_from_keyboard(
    console: Console, directory_manager: DirectoryManager
) -> Record:
    """
    Collects user input for creating a new Record.

    Args:
        console (Console): The Rich console for interaction.
        directory_manager (DirectoryManager): The directory manager instance.

    Returns:
        Record: The new Record created from user input.
    """
    record_args = []
    for field_name in directory_manager.get_directory_field_names():
        field_from_keyboard = console.input(
            f"{field_name} (Example: {directory_manager.get_field_example(field_name)}): "
        )

        while not directory_manager.is_field_valid(field_name, field_from_keyboard):
            console.print(f"[red]Invalid input.[/red]")
            console.print()
            field_from_keyboard = console.input(
                f"{field_name} (Example: {directory_manager.get_field_example(field_name)}): "
            )

        record_args.append(field_from_keyboard)

    record = Record(*record_args)
    return record


def edit_record_from_keyboard(
    console: Console, directory_manager: DirectoryManager, record_to_edit: Record
) -> Record:
    """
    Collects user input for editing a Record.

    Args:
        console (Console): The Rich console for interaction.
        directory_manager (DirectoryManager): The directory manager instance.
        record_to_edit (Record): The Record to be edited.

    Returns:
        Record: The edited Record.
    """
    record_args = []

    for field_name, records_old_value in zip(
        directory_manager.get_directory_field_names(), record_to_edit
    ):
        field_from_keyboard = Prompt.ask(
            prompt=f"{field_name}",
            default=records_old_value,
        )

        while not directory_manager.is_field_valid(field_name, field_from_keyboard):
            console.print(f"[red]Invalid input.[/red]")
            console.print()
            field_from_keyboard = Prompt.ask(
                prompt=f"{field_name}",
                default=records_old_value,
            )

        record_args.append(field_from_keyboard)

    record = Record(*record_args)
    return record


def calculate_index_range(current_page: int, items_per_page: int) -> tuple[int, int]:
    """
    Calculates the start and end indices for pagination.

    Args:
        current_page (int): Current page number.
        items_per_page (int): Number of items per page.

    Returns:
        tuple[int, int]: The start and end indices for the current page.
    """
    start_index = (current_page - 1) * items_per_page
    end_index = start_index + items_per_page
    return start_index, end_index


def render_search_result_table(
    console: Console,
    directory_manager: DirectoryManager,
    search_result: SearchResult,
) -> None:
    """
    Renders the search result table.

    Args:
        console (Console): The Rich console for rendering.
        directory_manager (DirectoryManager): The directory manager instance.
        search_result (SearchResult): The search result to display.
    """
    current_page_number = 1
    total_pages = (
        1
        if len(search_result.matched_records) == 0
        else (len(search_result.matched_records) + RECORDS_PER_PAGE - 1)
        // RECORDS_PER_PAGE
    )

    start_index, end_index = calculate_index_range(
        current_page_number, RECORDS_PER_PAGE
    )

    current_page_records = search_result.matched_records[start_index:end_index]

    table = Table(title=f"Results for '{search_result.search_string}' search string")
    table.add_columns(directory_manager.get_directory_field_names())
    table.add_rows(current_page_records)
    console.print(table)
    console.print(f"Page {current_page_number} of {total_pages}")
