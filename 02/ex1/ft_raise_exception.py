#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:

    temp = int(temp_str)

    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")

    return temp


def test_temperature(test_inputs: list[str]) -> None:

    for data in test_inputs:
        print(f"Input data is '{data}'")
        try:
            temp: int = input_temperature(data)
        except (TypeError, ValueError) as e:
            print(f"Caught input_temperature {e.__class__.__name__}: {e}\n")
        else:
            print(f"Temperature is now {temp}°C\n")


def main() -> int:

    print("=== Garden Temperature Checker ===\n")

    test_inputs = [
            "25",
            "abc",
            # None,
            "100",
            "-50",
            ]
    test_temperature(test_inputs)

    print("All tests completed - program didn't crash!")
    return 0


if __name__ == "__main__":

    main()
