#!/usr/bin/env python3


def garden_operations(operation_number: int) -> None:

    if operation_number == 0:
        int("mushi")
    elif operation_number == 1:
        42 / 0
    elif operation_number == 2:
        f = open("FREE_CYBERWEAR!.exe", "r")
        f.close()
    elif operation_number == 3:
        "six" + 7


def test_error_types(operation_numbers: list[int]) -> None:

    for op in operation_numbers:
        print(f"Testing operation {op}...")
        try:
            garden_operations(op)
        except ValueError as e:
            print(f"Caught ValueError: {e}\n")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}\n")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}\n")
        except TypeError as e:
            print(f"Caught TypeError: {e}\n")
        else:
            print("Operation completed successfully!\n")


def main() -> int:

    print("=== Garden Error Types Demo ===\n")

    operation_numbers = [0, 1, 2, 3, 4]
    test_error_types(operation_numbers)

    print("All error types successfully!")
    return 0


if __name__ == "__main__":

    main()
