import rich.table
from record import Record


class Table(rich.table.Table):
    """
    An extension of the Rich library's Table class for displaying records.

    This class provides additional methods for easier setup and population of columns and rows.

    Args:
        **kwargs: Additional keyword arguments to pass to the base Rich Table class.

    Methods:
        add_columns(column_names: list): Add multiple columns to the table.
        add_rows(records: list[Record]): Add multiple rows to the table using records.

    Attributes:
        Inherited attributes from Rich Table class.

    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def add_columns(self, column_names: list) -> None:
        """
        Add multiple columns to the table.

        Args:
            column_names (list): List of column names to add.

        Returns:
            None

        """
        for column_name in column_names:
            self.add_column(column_name)

    def add_rows(self, records: list[Record]) -> None:
        """
        Add multiple rows to the table using records.

        Args:
            records (list[Record]): List of records to add as rows.

        Returns:
            None

        """
        for record in records:
            self.add_row(*record)
