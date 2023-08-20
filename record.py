from dataclasses import dataclass


@dataclass
class Record:
    """
    Represents a record with contact information.

    Attributes:
        last_name (str): Last name of the individual.
        first_name (str): First name of the individual.
        middle_name (str): Middle name of the individual.
        organization (str): Name of the organization.
        work_phone (str): Work phone number.
        personal_phone (str): Personal phone number.

    Magic Methods:
        __lt__(self, other): Compare two records based on last name, first name, middle name, and organization.
        __iter__(self): Allow iteration over the values of the record.

    """

    last_name: str
    first_name: str
    middle_name: str
    organization: str
    work_phone: str
    personal_phone: str

    def __iter__(self):
        """
        Allow iteration over the values of the record.

        Returns:
            iterator: An iterator over the attribute values.
        """
        return iter([value for value in self.__dict__.values()])

    def __lt__(self, other):
        """
        Compare two records based on last name, first name, middle name, and organization.

        Args:
            other (Record): Another record to compare with.

        Returns:
            bool: True if self is less than other; False otherwise.
        """
        return (
            self.last_name,
            self.first_name,
            self.middle_name,
            self.organization,
        ) < (
            other.last_name,
            other.first_name,
            other.middle_name,
            other.organization,
        )
