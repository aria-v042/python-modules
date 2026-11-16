#!/usr/bin/env python3 


def garden_operations(operation_number: int) -> None:

    if operation_number == 0:
        num = int("abc")
    elif operation_number == 1:
        num = 42 / 0
    elif operation_number == 2:
        f = open("free_iphone.sh", "r")
        f.close()
    elif operation_number == 3:
        6 + "seven"


def test_error_types() -> None:

    print("=== Garden Error Types Demo ===")

    operation_numbers = [0, 1, 2, 3]

    for op in operation_numbers:
        print(f"Testing operation {op}...")
        try:
            garden_operations(op)
        except ValueError, ZeroDivisionError, 
                FileNotFoundError, TypeError as e:
            print(e)
