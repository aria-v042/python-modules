#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:

    temp_int = int(temp_str)
    return temp_int


def test_temperature(temp_str: str) -> None:

    print(f"Input data is '{temp_str}'")
    try:
        temp_int = input_temperature(temp_str)
    except (TypeError, ValueError) as e:
        print(f"Caught input_temperature {type(e).__name__}: {e}")
    else:
        print(f"Temperature is now {temp_int}°C")


def main() -> None:

    print("=== Garden Temperature ===")
    print()

    # No error
    test_temperature("25")
    print()

    # ValueError
    test_temperature("abc")
    print()

    # TypeError
    test_temperature(None)  # type: ignore[arg-type]
    print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":

    main()
