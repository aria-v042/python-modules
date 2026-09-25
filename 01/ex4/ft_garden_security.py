#!/usr/bin/env python3


class Plant:

    def __init__(self,
                 name: str = "",
                 height: float = 0,
                 age: int = 0) -> None:
        # Declare attributes
        self._name: str
        self._height: float
        self._age: int
        # Init name
        self._name = name.capitalize()
        # Init height
        if height < 0:
            self._height = 0
            print("Error, height can't be negative")
        else:
            self._height = height
        # Init age
        if age < 0:
            self._age = 0
            print("Error, age can't be negative")
        else:
            self._age = age

    # Getters

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    # Setters

    def set_name(self, name: str) -> None:
        self.show_name_inline()
        self._name = name.capitalize()
        print(f"Name updated: {self.get_name()}")

    def set_height(self, height: float) -> None:
        if height < 0:
            self.show_name_inline()
            print("Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            self.show_name_inline()
            print(f"Height updated: {self.get_height()}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            self.show_name_inline()
            print("Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            self.show_name_inline()
            print(f"Age updated: {self.get_age()} days")

    # Plant methods

    def show(self) -> None:
        self.show_name_inline()
        print(f"{self.get_height():.1f}cm, "
              f"{self.get_age()} days old")

    def show_name_inline(self) -> None:
        if self.get_name() == "":
            print("{unnamed}: ", end="")
        else:
            print(f"{self.get_name()}: ", end="")

    def grow(self, growth: float) -> None:
        self.set_height(self.get_height() + growth)

    def age(self, days: int) -> None:
        self.set_age(self.get_age() + days)


def test_secure_plant(
        init_name: str,
        init_height: float,
        init_age: int,
        valid_name: str,
        valid_height: float,
        valid_age: int,
        error_height: float,
        error_age: int
        ) -> None:

    # Create valid Plant instance
    plant = Plant(init_name, init_height, init_age)
    print("Plant created: ", end="")
    plant.show()
    print()

    # Update attributes with valid values
    plant.set_name(valid_name)
    plant.set_height(valid_height)
    plant.set_age(valid_age)
    print()

    # Update attributes with invalid values
    plant.set_height(error_height)
    plant.set_age(error_age)
    print()

    print("Current state: ", end="")
    plant.show()


def ft_garden_security() -> None:

    # Welcome message
    print("=== Garden Security System ===")

    # Test subject's example
    print("=== Test 1")
    test_secure_plant("rosee", 15, 10, "rose", 25, 30, -1, -1)

    # Test with default initial values
    print("\n=== Test 2")
    test_secure_plant("", 0, 0, "pink lilie", 7, 25, -2, -2)

    # Test with invalid initial values
    print("\n=== Test 3")
    test_secure_plant("moonflower", -1, -1, "sunflower", 42, 60, -3, -3)


if __name__ == "__main__":

    ft_garden_security()
