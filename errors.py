class NotUniquePersonalNumber(Exception):
    """
    Exception raised when a personal number is not unique in the directory.
    """

    pass


class RecordDoesNotExist(Exception):
    """
    Exception raised when a record does not exist in the directory.
    """

    pass


class RecordValidationError(Exception):
    """
    Exception raised when a record validation fails.
    """

    pass
