""" Module to provide abstract classes and abstract factories to be used in the main
module directly respecting the DIP design pattern.
"""

from abc import ABC, abstractmethod
from typing import Any


class Computer(ABC):
    """Abstract class to define the interface for all computations."""

    @abstractmethod
    def compute(self, *args: Any, **kwargs: Any) -> Any:
        """Compute the result based on the provided arguments."""
        raise NotImplementedError("Subclasses must implement this method.")


class ComputerFactory(ABC):
    """Abstract class to define the interface for all computation factories."""

    @abstractmethod
    def create_computer(self, computer_type: Any) -> Computer:
        """Create a computer instance based on the provided arguments."""
        raise NotImplementedError("Subclasses must implement this method.")
