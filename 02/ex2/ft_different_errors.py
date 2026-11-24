#!/usr/bin/env python3


def garden_operations(operation_number: int) -> None:
    if operation_number == 0:       # ValueError
        int("mushi")
    elif operation_number == 1:     # ZeroDivisionError
        42 / 0
    elif operation_number == 2:     # FileNotFoundError
        f = open("FREE_CYBERWEAR!.exe", "r")
        f.close()
    elif operation_number == 3:     # TypeError
        "six" + 7
    else:                           # No error
        1 + 1


def test_error_types() -> None:
    # Raise each type of error and catch it in the same block
    operation_numbers = [0, 1, 2, 3, 4]
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
            # If no error occurs (operation >= 4)
            print("Operation completed successfully!\n")


def main() -> int:
    print("=== Garden Error Types Demo ===\n")

    test_error_types()

    print("All error types successfully!")
    return 0


if __name__ == "__main__":
    main()
