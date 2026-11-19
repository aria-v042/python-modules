#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:

    temp = int(temp_str)
    return temp


def test_temperature(test_inputs: list[str]) -> None:

    for data in test_inputs:
        print(f"Input data is '{data}'")
        try:
            temp: int = input_temperature(data)
        # except Exception as e:
        #     print(f"Caught input_temperature error: {e}\n")
        except (TypeError, ValueError) as e:
            print(f"Caught input_temperature {e.__class__.__name__}: {e}\n")
        else:
            print(f"Temperature is now {temp}°C\n")


def main() -> int:

    print("=== Garden Temperature ===\n")

    test_inputs = [
            "25",
            "abc",
            # None,
            ]
    test_temperature(test_inputs)

    print("All tests completed - program didn't crash!")
    return 0


if __name__ == "__main__":

    main()
