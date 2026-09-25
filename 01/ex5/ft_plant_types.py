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


class Flower(Plant):

    def __init__(self,
                 name: str = "",
                 height: float = 0,
                 age: int = 0,
                 color: str = "") -> None:

        self._color: str

        super().__init__(name, height, age)
        self._color = color

    # Getters

    def get_color(self) -> str:
        return self._color

    # Setters

    def set_color(self, color: str) -> None:
        self._color = color
        self.show_name_inline()
        print(f"Color updated: {self.get_color()}")

    # Flower methods

    def show(self) -> None:
        super().show()
        print(f" Color: {self.get_color()}")

    def bloom(self) -> None:
        pass


class Tree(Plant):

    def __init__(self,
                 name: str = "",
                 height: float = 0,
                 age: int = 0,
                 trunk_diameter: float = 0) -> None:

        self._trunk_diameter: float

        super().__init__(name, height, age)
        if trunk_diameter < 0:
            self._trunk_diameter = 0
            print("Error, trunk diameter can't be negative")
        else:
            self._trunk_diameter = trunk_diameter

    # Getters

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    # Setters

    def set_trunk_diameter(self, trunk_diameter: float) -> None:
        if trunk_diameter < 0:
            self.show_name_inline()
            print("Error, trunk diameter can't be negative")
            print("Trunk diameter update rejected")
        else:
            self._trunk_diameter = trunk_diameter
            self.show_name_inline()
            print(f"Trunk diameter updated: {self.get_trunk_diameter():.1f}cm")

    # Tree methods

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.get_trunk_diameter():.1f}cm")

    def produce_shade(self) -> None:
        pass


class Vegetable(Plant):

    def __init__(self,
                 name: str = "",
                 height: float = 0,
                 age: int = 0,
                 harvest_season: str = "",
                 nutritional_value: int = 0) -> None:

        self._harvest_season: str
        self._nutritional_value: int

        super().__init__(name, height, age)
        self._harvest_season = harvest_season.capitalize()
        if nutritional_value < 0:
            self._nutritional_value = 0
            print("Error, nutritional value can't be negative")
        else:
            self._nutritional_value = nutritional_value

    # Getters

    def get_harvest_season(self) -> str:
        return self._harvest_season

    def get_nutritional_value(self) -> int:
        return self._nutritional_value

    # Setters

    def set_harvest_season(self, harvest_season: str) -> None:
        self._harvest_season = harvest_season.capitalize()
        self.show_name_inline()
        print(f"Harvest season updated: {self.get_harvest_season()}")

    def set_nutritional_value(self, nutritional_value: int) -> None:
        if nutritional_value < 0:
            self.show_name_inline()
            print("Error, nutritional value can't be negative")
        else:
            self._nutritional_value = nutritional_value
            self.show_name_inline()
            print(f"Nutritional value updated: {self.get_nutritional_value()}")

    # Vegetable methods

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.get_harvest_season()}")
        print(f" Nutritional value: {self.get_nutritional_value()}")


def ft_plant_types() -> None:

    # Welcome message
    print("=== Garden Plant Types ===")

    # Flower instances
    print("=== Flower")
    flower1 = Flower("rose", 15, 10, "red")
    flower1.show()
    print()

    # Tree instances
    print("=== Tree")
    tree1 = Tree("oak", 200, 365, 5)
    tree1.show()
    print()

    # Vegetable instances
    print("=== Vegetable")
    vegetable1 = Vegetable("tomato", 5, 10, "April", 0)
    vegetable1.show()
    print()


if __name__ == "__main__":
    ft_plant_types()
