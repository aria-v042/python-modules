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


# def garden_errors() -> None:
#     raise GardenError
#
#
# def plant_errors(error_number: int = 0) -> None:
#
#     if error_number == 0:
#         raise PlantError
#     elif error_number == 1:
#         raise PlantError("The tomato plant is wilting!")
#
#
# def water_errors(error_number: int = 0) -> None:
#
#     if error_number == 0:
#         raise WaterError
#     elif error_number == 1:
#         raise WaterError("Not enough water in the tank!")


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


def test_custom_errors() -> None:

    print("\n=== Custom Garden Errors Demo ===\n")

    custom_errors = [
            "PlantError",
            "WaterError",
            "GardenError",
            "PlantError default message",
            "WaterError default message",
            ]

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

    print("\nAll custom error types work correctly!\n")


def main() -> int:

    test_custom_errors()
    return 0


if __name__ == "__main__":

    main()
