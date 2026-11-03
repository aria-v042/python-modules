#!/usr/bin/env python3


class Plant:

    def __init__(self,
                 name: str = "",
                 height: float = 0,
                 age: int = 0) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}cm, "
              f"{self.age} days old")


def ft_garden_data() -> None:

    # Welcome message
    print("=== Garden Plant Registry ===")

    # Create and display Plant instances
    plant1 = Plant()
    plant1.name = "rose"
    plant1.height = 25
    plant1.age = 30
    plant1.show()

    plant2 = Plant()
    plant2.name = "sunflower"
    plant2.height = 80
    plant2.age = 45
    plant2.show()

    plant3 = Plant()
    plant3.name = "cactus"
    plant3.height = 15
    plant3.age = 120
    plant3.show()


if __name__ == "__main__":

    ft_garden_data()
