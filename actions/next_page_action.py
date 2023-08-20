from .action import Action


class NextPageAction(Action):
    """
    Action to navigate to the next page in a paginated view.

    This action increases the current page number by 1 if it's less than the
    total number of pages. If the current page is already the last page, the
    current page number remains unchanged.

    Args:
        Action: The base class for actions.

    Methods:
        run(current_page, total_pages): Execute the action to navigate to the next page.
    """

    def run(self, current_page: int, total_pages: int) -> int:
        """
        Execute the action to navigate to the next page.

        Args:
            current_page (int): The current page number.
            total_pages (int): The total number of pages.

        Returns:
            int: The updated current page number.
        """
        if current_page < total_pages:
            return current_page + 1
        return current_page
