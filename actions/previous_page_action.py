from .action import Action


class PreviousPageAction(Action):
    """
    Action to navigate to the previous page in a paginated view.

    This action decreases the current page number by 1 if it's greater than 1.
    If the current page is already the first page, the current page number remains unchanged.

    Args:
        Action: The base class for actions.

    Methods:
        run(current_page, total_pages): Execute the action to navigate to the previous page.

    """

    def run(self, current_page: int, total_pages: int) -> int:
        """
        Execute the action to navigate to the previous page.

        Args:
            current_page (int): The current page number.
            total_pages (int): The total number of pages.

        Returns:
            int: The updated current page number.
        """
        if current_page > 1:
            return current_page - 1
        return current_page
