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


def test_error_types() -> None:

    print("=== Garden Error Types Demo ===\n")

    operation_numbers = [0, 1, 2, 3, 4]

    for op in operation_numbers:
        print(f"Testing operation {op}...")
        try:
            garden_operations(op)
        except (ValueError, ZeroDivisionError, 
                FileNotFoundError, TypeError) as e:
            print(f"Caught {e.__class__.__name__}: {e}\n")
        else:
            print("Operation completed successfully!\n")

    print("All error types successfully!")


def main() -> int:

    test_error_types()
    return 0


if __name__ == "__main__":

    main()
