#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)

    # Check if the temperature is reasonable for plants
    if temp < 0:
        # Raise an exception if temperature is invalid
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")

    return temp


def test_temperature(data: str) -> None:
    print(f"Input data is '{data}'")
    try:
        temp: int = input_temperature(data)
    except (TypeError, ValueError) as e:
        print(f"Caught input_temperature {e.__class__.__name__}: {e}\n")
    else:
        print(f"Temperature is now {temp}°C\n")


def main() -> int:
    print("=== Garden Temperature Checker ===\n")

    test_temperature("25")      # Valid input
    test_temperature("abc")     # Invalid input -> ValueError
    # test_temperature(None)      # Invalid input -> TypeError
    test_temperature("100")     # Invalid input -> too hot (ValueError)
    test_temperature("-50")     # Invalid input -> too cold (ValueError)

    print("All tests completed - program didn't crash!")
    return 0


if __name__ == "__main__":
    main()
