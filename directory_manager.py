import re
import csv
from record import Record
from errors import NotUniquePersonalNumber, RecordDoesNotExist, RecordValidationError
from search_result import SearchResult
from rich.progress import track


class DirectoryManager:
    """
    A class to manage a directory of records.
    """

    def __init__(self, filename: str) -> None:
        """
        Initialize the DirectoryManager instance.

        Args:
            filename (str): The name of the CSV file to manage.

        Returns:
            None
        """
        self.filename: str = filename
        self.data: dict[str, Record] = {}
        self.header: list[str] = []
        self.regexes: dict[str, str] = {}
        self.example: dict[str, str] = {}

    def deserialize_directory(self) -> None:
        """
        Deserialize the directory data from the CSV file.

        Returns:
            None
        """
        with open(self.filename, "r", newline="", encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            raw_data = [row for row in csv_reader]

        self.header = raw_data.pop(0)
        self.regexes = {
            field_name: regex for field_name, regex in zip(self.header, raw_data.pop(0))
        }
        self.example = {
            field_name: regex for field_name, regex in zip(self.header, raw_data[0])
        }

        self.data = self.__wrap_data_in_records(raw_data)

    def serialize_directory(self) -> None:
        """
        Serialize the directory data to the CSV file.

        Returns:
            None
        """
        with open(self.filename, mode="w", newline="", encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(self.header)
            csv_writer.writerow(self.regexes.values())
            for record in track(
                self.data.values(),
                description=f"Saving changes to {self.filename}...",
            ):
                csv_writer.writerow(record)

    def is_field_valid(self, field_name, field_value) -> bool:
        """
        Check if a given field value is valid according to its regex pattern.

        Args:
            field_name (str): The name of the field.
            field_value (str): The value of the field.

        Returns:
            bool: True if the field value is valid, False otherwise.
        """
        field_regex = self.regexes.get(field_name)
        return re.match(field_regex, field_value)

    def get_field_example(self, field_name: str) -> str:
        """
        Get an example value for a specific field.

        Args:
            field_name (str): The name of the field.

        Returns:
            str: An example value for the field.
        """
        return self.example.get(field_name)

    def get_records(self) -> list[Record]:
        """
        Get a sorted list of all records in the directory.

        Returns:
            list[Record]: A list of all records.
        """
        return sorted(self.data.values())

    def get_directory_field_names(self) -> list[str]:
        """
        Get the field names of the directory.

        Returns:
            list[str]: A list of field names.
        """
        return self.header

    def add_record(self, record: Record) -> None:
        """
        Add a new record to the directory.

        Args:
            record (Record): The record to add.

        Returns:
            None
        """
        if self.is_number_already_in_directory(record.personal_phone):
            raise NotUniquePersonalNumber(
                f"Record with that personal number already exist in the directory."
            )

        self.data[record.personal_phone] = record

    def delete_record(self, records_personal_number: str) -> Record:
        """
        Delete a record from the directory.

        Args:
            records_personal_number (str): The personal phone number of the record to delete.

        Returns:
            Record: The deleted record.
        """
        if records_personal_number not in self.data:
            raise RecordDoesNotExist(
                f"Record with that personal number does not exist."
            )

        return self.data.pop(records_personal_number)

    def search_records(self, search_string: str) -> SearchResult:
        """
        Search for records based on a search string.

        Args:
            search_string (str): The search string.

        Returns:
            SearchResult: The search result containing matched records and a search string.
        """
        matched_records = [
            record
            for record in self.data.values()
            if search_string in " ".join(str(value) for value in vars(record).values())
        ]

        return SearchResult(search_string, sorted(matched_records))

    def is_record_valid(self, record: Record) -> bool:
        """
        Check if a record is valid according to its regex patterns.

        Args:
            record (Record): The record to check.

        Returns:
            bool: True if the record is valid, False otherwise.
        """
        for field_name, field_value in zip(self.header, record.__dict__.values()):
            if not re.match(self.regexes[field_name], field_value):
                return False
        return True

    def __wrap_data_in_records(self, data: list[list[str]]) -> dict[str, Record]:
        """
        Wrap raw data in Record objects and perform validation.

        Args:
            data (list[list[str]]): The raw data from the CSV file.

        Returns:
            dict[str, Record]: A dictionary of records.
        """
        wrapped_data: dict[str, Record] = {}
        for row in data:
            record = Record(*row)
            if not self.is_record_valid(record):
                raise RecordValidationError(
                    f"Fields in some records are not valid. Modify record fields in {self.filename} to match the regexes located in the file and restart the application."
                )

            if record.personal_phone in wrapped_data:
                raise NotUniquePersonalNumber(
                    f"Identical personal phone numbers found in {self.filename}. Remove identical numbers and restart the application."
                )

            wrapped_data[record.personal_phone] = record

        return wrapped_data

    def is_number_already_in_directory(self, personal_phone_number: str) -> bool:
        """
        Check if a personal phone number already exists in the directory.

        Args:
            personal_phone_number (str): The personal phone number to check.

        Returns:
            bool: True if the number already exists, False otherwise.
        """
        return personal_phone_number in self.data
