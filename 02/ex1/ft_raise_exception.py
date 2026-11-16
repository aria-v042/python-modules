#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:

    temp = int(temp_str)

    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")

    return temp


def test_temperature() -> None:

    print("=== Garden Temperature Checker ===\n")

    test_inputs = [
            "25",
            "abc",
            None,
            "100",
            "-50",
            ]

    for input in test_inputs:
        print(f"Input data is '{input}'")
        try:
            temp: int = input_temperature(input)    # type: ignore[arg-type]
        except (TypeError, ValueError) as e:
            print(f"Caught input_temperature {type(e).__name__}: {e}\n")
        else:
            print(f"Temperature is now {temp}°C\n")

    print("All tests completed - program didn't crash!")


def main() -> None:

    test_temperature()


if __name__ == "__main__":

    main()
