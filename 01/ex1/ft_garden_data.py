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
        print(f"{self.name.capitalize()}: {self.height}cm, "
              f"{self.age_days} days old")


def ft_garden_data() -> None:

    # Create Plant instances
    plant1 = Plant()
    plant1.name = "rose"
    plant1.height = 25
    plant1.age_days = 30

    plant2 = Plant()
    plant2.name = "sunflower"
    plant2.height = 80
    plant2.age_days = 45

    plant3 = Plant()
    plant3.name = "cactus"
    plant3.height = 15
    plant3.age_days = 120

    # Welcome message
    print("=== Garden Plant Registry ===")

    # Display each plant's information
    plant1.show()
    plant2.show()
    plant3.show()


if __name__ == "__main__":

    ft_garden_data()
