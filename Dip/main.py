""" Main module for demonstrating the Dependency Inversion Principle (DIP) """

from .interfaces import Computer
from argparse import ArgumentParser

def main(a: float, b: float, computer: Computer, computer_type: str) -> float:
    computed_value = computer.compute(a, b)

    print('Input values:', a, b)
    print('Computer type:', computer_type)
    print('Computed value:', computed_value)

    print('Computer class:', computer.__class__.__name__)
    print('Computer super class:', computer.__class__.__bases__)


if __name__ == "__main__":
    parser = ArgumentParser(description="Demonstration of the Dependency Inversion Principle (DIP).")
    parser.add_argument("--a", type=float, default=10.0, help="First number")
    parser.add_argument("--b", type=float, default=5.0, help="Second number")
    parser.add_argument(
        "--computer_type",
        type=str,
        choices=["sum", "product"], default="sum",
        help="Type of computation (sum or product)"
    )

    args = parser.parse_args()
    print(parser.description)

    # dependency injection
    from .concrete import ComputerFactoryImplementation
    computer_factory = ComputerFactoryImplementation()
    computer = computer_factory.create_computer(args.computer_type)

    # main function
    main(args.a, args.b, computer, args.computer_type)
    print("Main function executed.")
