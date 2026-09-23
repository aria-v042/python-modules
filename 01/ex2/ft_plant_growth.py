#!/usr/bin/env python3


class Plant:

    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height:.1f}cm, "
              f"{self.plant_age} days old")

    def grow(self, growth: float) -> None:
        self.height += growth

    def age(self, days: int) -> None:
        self.plant_age += days


def simulate_growth(plant: Plant, daily_growth: float,
                    num_of_days: int) -> None:

    for day in range(1, num_of_days + 1):
        if (day != 1):
            plant.grow(daily_growth)
            plant.age(1)
        print(f"=== Day {day} ===")
        plant.show()

    total_growth: float = daily_growth * num_of_days
    print(f"Total growth: {total_growth:.1f}cm")


def ft_plant_growth() -> None:

    # # User input values
    # name = input("Plant name: ")
    # height = float(input("Height (cm): "))
    # plant_age = int(input("Age (days): "))
    # print()
    # daily_growth = float(input("Plant's daily growth (cm): "))
    # num_of_days = int(input("Number of days: "))
    # print()

    # Hard coded values
    name: str = "rose"
    height: float = 25.0
    plant_age: int = 30
    daily_growth = 0.8
    num_of_days = 7

    # Create Plant instance
    plant = Plant(name, height, plant_age)

    # Simulate/display growth
    simulate_growth(plant, daily_growth, num_of_days)


if __name__ == "__main__":

    ft_plant_growth()
