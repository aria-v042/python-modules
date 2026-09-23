#!/usr/bin/env python3


class Plant:

    def __init__(self,
                 name: str = "",
                 height: float = 0,
                 age_days: int = 0) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height:.1f}cm, "
              f"{self.age_days} days old")

    def grow(self, growth: float) -> None:
        self.height += growth

    def age(self, days: int) -> None:
        self.age_days += days


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
    # age_days = int(input("Age (days): "))
    # print()
    # daily_growth = float(input("Plant's daily growth (cm): "))
    # num_of_days = int(input("Number of days: "))
    # print()

    # Hard coded values
    name: str = "rose"
    height: float = 25.0
    age_days: int = 30
    daily_growth = 0.8
    num_of_days = 7

    # Create Plant instance and set its attributes
    plant = Plant()
    plant.name = name
    plant.height = height
    plant.age_days = age_days

    # Simulate/display growth
    simulate_growth(plant, daily_growth, num_of_days)


if __name__ == "__main__":

    ft_plant_growth()
