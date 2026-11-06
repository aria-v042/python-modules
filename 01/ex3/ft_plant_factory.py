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


def ft_plant_factory() -> None:

    # Create plant instances, initializing them at instantiation
    plant1 = Plant("rose", 25.0, 30)
    plant2 = Plant("oak", 200.0, 365)
    plant3 = Plant("cactus", 5.0, 90)
    plant4 = Plant("sunflower", 80.0, 45)
    plant5 = Plant("fern", 15.0, 120)

    # Display Plant instances created
    print(f"Created: ", end="")
    plant1.show()
    print("Created: ", end="")
    plant2.show()
    print("Created: ", end="")
    plant3.show()
    print("Created: ", end="")
    plant4.show()
    print("Created: ", end="")
    plant5.show()


if __name__ == "__main__":

    ft_plant_factory()
