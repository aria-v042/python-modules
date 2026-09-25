#!/usr/bin/env python3


class Plant:

    def __init__(self,
                 name: str = "",
                 height: float = 0,
                 age: int = 0) -> None:

        # Declare attributes and initialize default values
        self._name: str = ""
        self._height: float = 0
        self._age: int = 0

        # Set attributes
        self.set_name(name)
        self.set_height(height)
        self.set_age(age)

    # Getters

    def get_name(self) -> str:
        return self._name

    def get_name_pretty(self) -> str:
        if self.get_name() == "":
            return "{unnamed}"
        else:
            return self.get_name()

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    # Setters

    def set_name(self, name: str) -> None:
        self._name = name

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.get_name_pretty().capitalize()}: "
                  "Error, height can't be negative")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.get_name_pretty().capitalize()}: "
                  "Error, age can't be negative")
        else:
            self._age = age

    # Plant methods

    def show(self) -> None:
        print(f"{self.get_name_pretty().capitalize()}: "
              f"{self.get_height():.1f}cm, "
              f"{self.get_age()} days old")

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

        # Declare attributes and set default values
        self._color: str = ""
        self._bloomed: bool = False

        # Set attributes
        super().__init__(name, height, age)
        self.set_color(color)

    # Getters

    def get_color(self) -> str:
        return self._color

    # Setters

    def set_color(self, color: str) -> None:
        self._color = color

    # Flower methods

    def show(self) -> None:
        super().show()
        print(f" Color: {self.get_color()}")
        if self._bloomed:
            print(f" {self.get_name_pretty().capitalize()} "
                  "is blooming beautifully!")
        else:
            print(f" {self.get_name_pretty().capitalize()} "
                  "has not bloomed yet")

    def bloom(self) -> None:
        self._bloomed = True


class Tree(Plant):

    def __init__(self,
                 name: str = "",
                 height: float = 0,
                 age: int = 0,
                 trunk_diameter: float = 0) -> None:

        # Declare attributes and set default values
        self._trunk_diameter: float = 0
        self._shade: bool = False

        # Set attributes
        super().__init__(name, height, age)
        self.set_trunk_diameter(trunk_diameter)

    # Getters

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    # Setters

    def set_trunk_diameter(self, trunk_diameter: float) -> None:
        if trunk_diameter < 0:
            print(f"{self.get_name_pretty().capitalize()}: "
                  "Error, trunk diameter can't be negative")
        else:
            self._trunk_diameter = trunk_diameter

    # Tree methods

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.get_trunk_diameter():.1f}cm")

    def produce_shade(self) -> None:
        self._shade = True
        print(f"{self.get_name_pretty().capitalize()} "
              "tree now produces a shade "
              f"{self.get_height():.1f}cm long and "
              f"{self.get_trunk_diameter():.1f}cm wide.")


class Vegetable(Plant):

    def __init__(self,
                 name: str = "",
                 height: float = 0,
                 age: int = 0,
                 harvest_season: str = "") -> None:

        # Declare attributes and set default values
        self._harvest_season: str = ""
        self._nutritional_value: float = 0

        # Set attributes
        super().__init__(name, height, age)
        self.set_harvest_season(harvest_season)

    # Getters

    def get_harvest_season(self) -> str:
        return self._harvest_season

    def get_nutritional_value(self) -> float:
        return self._nutritional_value

    # Setters

    def set_harvest_season(self, harvest_season: str) -> None:
        self._harvest_season = harvest_season.capitalize()

    def set_nutritional_value(self, nutritional_value: float) -> None:
        if nutritional_value < 0:
            print(f"{self.get_name_pretty()}: "
                  "Error, nutritional value can't be negative")
        else:
            self._nutritional_value = nutritional_value

    # Vegetable methods

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.get_harvest_season()}")
        print(f" Nutritional value: {int(self.get_nutritional_value())}")

    def grow(self, growth: float) -> None:
        super().grow(growth)
        self.set_nutritional_value(
                self.get_nutritional_value()
                + growth / 2.1 * 0.5)

    def age(self, days: int) -> None:
        super().age(days)
        self.set_nutritional_value(self.get_nutritional_value() + days * 0.5)


def ft_plant_types() -> None:

    # Welcome message
    print("=== Garden Plant Types ===")

    # Flower instances
    print("=== Flower")
    flower1 = Flower("rose", 15, 10, "red")
    flower1.show()
    print(f"[asking the {flower1.get_name_pretty().lower()} to bloom]")
    flower1.bloom()
    flower1.show()
    print()

    # Tree instances
    print("=== Tree")
    tree1 = Tree("oak", 200, 365, 5)
    tree1.show()
    print(f"[asking the {tree1.get_name_pretty().lower()} to produce shade]")
    tree1.produce_shade()
    print()

    # Vegetable instances
    print("=== Vegetable")
    vegetable1 = Vegetable("tomato", 5, 10, "April")
    vegetable1.show()
    print(f"[make {vegetable1.get_name_pretty().lower()} "
          "grow and age for 20 days]")
    vegetable1.grow(2.1 * 20)
    vegetable1.age(20)
    vegetable1.show()


if __name__ == "__main__":
    ft_plant_types()
