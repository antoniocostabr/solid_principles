"""Module to provide concrete implementations of the abstract classes defined in the
abstract module.
"""
from typing import Literal

from .interfaces import (
    Computer,
    ComputerFactory
)

class SumComputer(Computer):
    """Concrete implementation of the Computer class to compute the sum of two numbers."""

    def compute(self, a: float, b: float) -> float:
        """Compute the sum of two numbers."""
        return a + b


class ProductComputer(Computer):
    """Concrete implementation of the Computer class to compute the product of two numbers."""

    def compute(self, a: float, b: float) -> float:
        """Compute the product of two numbers."""
        return a * b


class ComputerFactoryImplementation(ComputerFactory):
    """Concrete implementation of the ComputerFactory class to create computer instances."""

    def create_computer(self, computer_type: Literal["sum", "product"] = "sum") -> Computer:
        """Create a computer instance based on the provided type."""

        if computer_type not in ["sum", "product"]:
            raise ValueError(f"Unknown computer type: {computer_type}")

        if computer_type == "sum":
            return SumComputer()
        if computer_type == "product":
            return ProductComputer()
