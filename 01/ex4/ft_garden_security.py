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
        # Display created instance
        self.show_created()

    # Getters

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    # Setters

    def set_name(self, name: str) -> None:
        if self.get_name() != "":
            print(f"{self.get_name()}: ", end="")
        else:
            print("{unnamed}: ", end="")
        self._name = name.capitalize()
        print(f"Name updated: {self.get_name()}")

    def set_height(self, height: float) -> None:
        if height < 0:
            if self.get_name() != "":
                print(f"{self.get_name()}: ", end="")
            else:
                print("{unnamed}: ", end="")
            print("Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            if self.get_name() != "":
                print(f"{self.get_name()}: ", end="")
            else:
                print("{unnamed}: ", end="")
            print(f"Height updated: {self.get_height()}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            if self.get_name() != "":
                print(f"{self.get_name()}: ", end="")
            else:
                print("{unnamed}: ", end="")
            print("Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            if self.get_name() != "":
                print(f"{self.get_name()}: ", end="")
            else:
                print("{unnamed}: ", end="")
            print(f"Age updated: {self.get_age()} days")

    # Plant methods

    def show(self) -> None:
        if self.get_name() != "":
            print(f"{self.get_name()}: ", end="")
        else:
            print("{unnamed}: ", end="")
        print(f"{self.get_height():.1f}cm, "
              f"{self.get_age()} days old")

    def show_created(self) -> None:
        print("Plant created: ", end="")
        self.show()

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
    plant1 = Plant(init_name, init_height, init_age)
    print()

    # Update attributes with valid values
    plant1.set_name(valid_name)
    plant1.set_height(valid_height)
    plant1.set_age(valid_age)
    print()

    # Update attributes with invalid values
    plant1.set_height(error_height)
    plant1.set_age(error_age)
    print()

    print("Current state: ", end="")
    plant1.show()


def ft_garden_security() -> None:

    # Welcome message
    print("=== Garden Security System ===")

    # Test subject's example
    print("\n--- Test 1 ---\n")
    test_secure_plant("rosee", 15, 10, "rose", 25, 30, -1, -1)

    # Test with default initial values
    print("\n--- Test 2 ---\n")
    test_secure_plant("", 0, 0, "pink lilie", 7, 25, -2, -2)

    # Test with invalid initial values
    print("\n--- Test 3 ---\n")
    test_secure_plant("moonflower", -1, -1, "sunflower", 42, 60, -3, -3)


if __name__ == "__main__":

    ft_garden_security()
