from record import Record
from dataclasses import dataclass


@dataclass
class SearchResult:
    """
    Represents a result of a search operation in the phone directory.

    Attributes:
        search_string (str): The search string used.
        matched_records (list[Record]): List of records that match the search string.

    """

    search_string: str
    matched_records: list[Record]
