#!/usr/bin/env python3


class Plant:


    class Stats():

        def __init__(self,
                     grow_count: int = 0,
                     age_count: int = 0,
                     show_count: int = 0) -> None:
            
            self.grow_count: int = 0
            self.age_count: int = 0
            self.show_count: int = 0

        def show_stats(self) -> None:
            print(f"Stats: {self.grow_count} grow, "
                  f"{self.age_count} age, "
                  f"{self.show_count} show")


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
        Stats.show_count += 1

    def grow(self, growth: float) -> None:
        self.set_height(self.get_height() + growth)
        Stats.grow_count += 1

    def age(self, days: int) -> None:
        self.set_age(self.get_age() + days)
        Stats.age_count += 1

    @staticmethod
    def check_year_old(age_in_days: int) -> bool:
        if age_in_days > 365:
            return True
        else:
            return False

    @classmethod
    def anon(cls) -> "Plant":
        return cls("Unknown plant", 0, 0)


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


class Seed(Flower):

    def __init__(self,
                 name: str = "",
                 height: float = 0,
                 age: int = 0,
                 color: str = "",
                 bloom_seeds: int = 0) -> None:

        self._bloom_seeds: int = 0

        super().__init__(name, height, age, color)
        self.set_bloom_seeds(bloom_seeds)

    # Getters

    def get_bloom_seeds(self) -> int:
        return self._bloom_seeds

    # Setters

    def set_bloom_seeds(self, bloom_seeds: int) -> None:
        if bloom_seeds < 0:
            print(f"{self.get_name_pretty().capitalize()}: "
                  "Error, number of seeds can't be negative")
        else:
            self._bloom_seeds = bloom_seeds

    # Seed methods

    def show(self) -> None:
        super().show()
        if self._bloomed:
            print(f" Seeds: {self.get_bloom_seeds()}")
        else:
            print(" Seeds: 0")


class Tree(Plant):

    class Stats(Plant.Stats):
        # TODO
        pass

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


def ft_garden_analytics() -> None:

    print("=== Garden Analytics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_year_old(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_year_old(400)}")
    print()

    print("=== Anonymous")
    anon = Plant.anon()
    anon.show()


if __name__ == "__main__":
    ft_garden_analytics()
