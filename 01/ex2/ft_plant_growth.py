#!/usr/bin/env python3


class Plant:

    def __init__(self,
                 name: str = "",
                 height: float = 0,
                 age: int = 0) -> None:
        self._name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"{self._name.capitalize()}: {self._height:.1f}cm, "
              f"{self._age} days old")

    def grow(self, growth: float) -> None:
        self._height += growth

    def age(self, days: int) -> None:
        self._age += days


def simulate_growth(plant: Plant, daily_growth: float,
                    num_of_days: int) -> None:

    for day in range(1, num_of_days + 1):
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
    # age = int(input("Age (days): "))
    # print()
    # daily_growth = float(input("Plant's daily growth (cm): "))
    # num_of_days = int(input("Number of days: "))
    # print()

    # Hard coded values
    name: str = "rose"
    height: float = 25.0
    age: int = 30
    daily_growth = 0.8
    num_of_days = 7

    # Create Plant instance and set its attributes
    plant = Plant(name, height, age)

    # Simulate/display growth
    print("=== Garden Plant Growth ===")
    plant.show()
    simulate_growth(plant, daily_growth, num_of_days)


if __name__ == "__main__":

    ft_plant_growth()
