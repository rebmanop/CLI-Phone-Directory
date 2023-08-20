from typing import Any
from abc import ABC, abstractmethod


class Action(ABC):
    """
    Abstract base class for defining actions within the program.

    Attributes:
        name (str): The name of the action.

    Methods:
        run(): Abstract method that must be implemented by subclasses.
    """

    def __init__(self, name) -> None:
        """
        Initialize the action with a name.

        Args:
            name (str): The name of the action.
        """
        self.name = name

    @abstractmethod
    def run(self) -> Any:
        """
        Abstract method to be implemented by subclasses.

        Returns:
            Any: The result of the action.
        """
        pass
