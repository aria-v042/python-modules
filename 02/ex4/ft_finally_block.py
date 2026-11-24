#!/usr/bin/env python3


# === Custom exception classes === #


class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)
        self.message = message


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


# === Demo functions === #


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(plants: list[str]) -> None:
    # Open the watering system
    print("Opening watering system")
    try:
        # Water several plants
        for p in plants:
            water_plant(p)
    except PlantError as e:
        # If a plant can't be watered, end tests and exit
        print(f"Caught {e.__class__.__name__}: {e}")
        print(".. ending tests and returning to main")
    finally:
        # Always close the watering system
        print("Closing watering system\n")


def main() -> int:
    print("=== Garden Watering System ===\n")

    print("Testing valid plants...")
    valid_plants = [
            "Tomato",
            "Lettuce",
            "Carrots",
            ]
    test_watering_system(valid_plants)

    print("Testing invalid plants...")
    invalid_plants = [
            "Tomato",
            "lettuce",  # Invalid plant name
            "carrots",  # Invalid plant name
            ]
    test_watering_system(invalid_plants)

    print("Cleanup always happens, even with errors!")
    return 0


if __name__ == "__main__":
    main()
