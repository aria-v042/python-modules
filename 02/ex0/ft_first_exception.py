#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    return temp


def test_temperature(data: str) -> None:
    print(f"Input data is '{data}'")
    try:
        temp: int = input_temperature(data)
    # except Exception as e:
    #     print(f"Caught input_temperature error: {e}\n")
    except (TypeError, ValueError) as e:
        # Catch and handle errors
        print(f"Caught input_temperature {e.__class__.__name__}: {e}\n")
    else:
        # If no error occurs
        print(f"Temperature is now {temp}°C\n")


def main() -> int:
    print("=== Garden Temperature ===\n")

    test_temperature("25")      # Valid input
    test_temperature("abc")     # Invalid input -> ValueError
    # test_temperature(None)    # Invalid input -> TypeError

    print("All tests completed - program didn't crash!")
    return 0


if __name__ == "__main__":
    main()
