from .action import Action
from rich.console import Console
from utils import render_search_result_table
from directory_manager import DirectoryManager


class SearchRecordsAction(Action):
    """
    Action to search for records in the directory.

    This action prompts the user for a search string, searches for records matching
    the search string, and displays the search results in a table.

    Args:
        Action: The base class for actions.

    Methods:
        run(console, directory_manager): Execute the action to search for records.
    """

    def run(self, console: Console, directory_manager: DirectoryManager) -> None:
        """
        Execute the action to search for records in the directory.

        Args:
            console (Console): The console object for output.
            directory_manager (DirectoryManager): The directory manager instance.

        Returns:
            None
        """
        search_string = console.input("\nSearch: ")
        search_result = directory_manager.search_records(search_string)
        console.clear()
        render_search_result_table(console, directory_manager, search_result)
        console.input("Press ENTER to get back to the directory...")
