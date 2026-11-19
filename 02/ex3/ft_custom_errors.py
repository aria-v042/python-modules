#!/usr/bin/env python3


# === Custom exception classes === #


class GardenError(Exception):

    def __init__(self, message: str = "Unknown garden error") -> None:

        super().__init__(message)
        self.message = message


class PlantError(GardenError):

    def __init__(self, message: str = "Unknown plant error") -> None:

        super().__init__(message)
        self.message = message


class WaterError(GardenError):

    def __init__(self, message: str = "Unknown water error") -> None:

        super().__init__(message)
        self.message = message


# === Demo functions === #


def raise_error(error_type: str) -> None:

    if error_type == "GardenError":
        raise GardenError
    elif error_type == "PlantError":
        raise PlantError("The tomato plant is wilting!")
    elif error_type == "WaterError":
        raise WaterError("Not enough water in the tank!")
    elif error_type == "PlantError default message":
        raise PlantError
    elif error_type == "WaterError default message":
        raise WaterError


def test_custom_errors(custom_errors: list[str]) -> None:

    # Catching specific error types
    for error_type in custom_errors:
        print(f"Testing {error_type}...")
        try:
            raise_error(error_type)
        except WaterError as e:
            print(f"Caught WaterError: {e}\n")
        except PlantError as e:
            print(f"Caught PlantError: {e}\n")
        except GardenError as e:
            print(f"Caught GardenError: {e}\n")

    # Catching all exceptions that inherit from GardenError
    print("Testing catching all garden errors...")
    for error_type in custom_errors:
        try:
            raise_error(error_type)
        except GardenError as e:
            print(f"Caught GardenError: {e}")
    print()


def main() -> int:

    print("=== Custom Garden Errors Demo ===\n")

    custom_errors = [
            "PlantError",
            "WaterError",
            # "GardenError",
            # "PlantError default message",
            # "WaterError default message",
            ]
    test_custom_errors(custom_errors)

    print("All custom error types work correctly!")
    return 0


if __name__ == "__main__":

    main()
