#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:

    temp = int(temp_str)
    return temp


def test_temperature() -> None:

    print("=== Garden Temperature ===\n")

    test_inputs = [
            "25",
            "abc",
            # None,
            ]

    for input in test_inputs:
        print(f"Input data is '{input}'")
        try:
            temp: int = input_temperature(input)
        except (TypeError, ValueError) as e:
            print(f"Caught input_temperature {e.__class__.__name__}: {e}\n")
        else:
            print(f"Temperature is now {temp}°C\n")

    print("All tests completed - program didn't crash!")


def main() -> None:

    test_temperature()


if __name__ == "__main__":

    main()
