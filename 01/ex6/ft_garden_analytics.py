#!/usr/bin/env python3


class Plant:

    # Inner class
    class Stats():

        # Constructor
        def __init__(self) -> None:
            self.grow_count: int = 0
            self.age_count: int = 0
            self.show_count: int = 0

        # Stats methods
        def show_stats(self) -> None:
            print(f"Stats: {self.grow_count} grow, "
                  f"{self.age_count} age, "
                  f"{self.show_count} show")

    # Constructor
    def __init__(self,
                 name: str = "",
                 height: float = 0,
                 age: int = 0) -> None:

        # Declare attributes with default values
        self._name: str = ""
        self._height: float = 0
        self._age: int = 0
        self._stats: Plant.Stats = self.Stats()

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
        self._stats.show_count += 1

    def grow(self, growth: float) -> None:
        self.set_height(self.get_height() + growth)
        self._stats.grow_count += 1

    def age(self, days: int) -> None:
        self.set_age(self.get_age() + days)
        self._stats.age_count += 1

    def show_stats(self) -> None:
        self._stats.show_stats()

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

    # Constructor
    def __init__(self,
                 name: str = "",
                 height: float = 0,
                 age: int = 0,
                 color: str = "") -> None:

        # Declare attributes with default values
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
        print(f" Color: {self._color.lower()}")
        if self._bloomed:
            print(f" {self.get_name_pretty().capitalize()} "
                  "is blooming beautifully!")
        else:
            print(f" {self.get_name_pretty().capitalize()} "
                  "has not bloomed yet")

    def bloom(self) -> None:
        self._bloomed = True


class Seed(Flower):

    # Constructor
    def __init__(self,
                 name: str = "",
                 height: float = 0,
                 age: int = 0,
                 color: str = "",
                 bloom_seeds: int = 0) -> None:

        # Declare attributes with default values
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

    # Inner class
    class Stats(Plant.Stats):

        # Constructor
        def __init__(self) -> None:

            super().__init__()
            self.produce_shade_count: int = 0

        # Stats methods
        def show_stats(self) -> None:
            super().show_stats()
            print(f" {self.produce_shade_count} shade")

    # Constructor
    def __init__(self,
                 name: str = "",
                 height: float = 0,
                 age: int = 0,
                 trunk_diameter: float = 0) -> None:

        # Declare attributes and set default values
        self._trunk_diameter: float = 0
        self._shade: bool = False
        self._stats: Tree.Stats = self.Stats()

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
        self._stats.produce_shade_count += 1


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


# Display statistics for any kind of Plant
def show_plant_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name_pretty().capitalize()}]")
    plant.show_stats()


# Exercise demo
def ft_garden_analytics() -> None:

    print("=== Garden Analytics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_year_old(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_year_old(400)}")

    print()

    # Create Flower object and display its information
    print("=== Flower")
    flower1 = Flower("rose", 15.0, 10, "red")
    flower1.show()
    show_plant_stats(flower1)
    # Grow and bloom
    print(f"[asking the {flower1.get_name().lower()} to grow and bloom]")
    flower1.grow(8.0)
    flower1.bloom()
    flower1.show()
    show_plant_stats(flower1)

    print()

    # Create Tree object and display its information
    print("=== Tree")
    tree1 = Tree("oak", 200.0, 365, 5.0)
    tree1.show()
    show_plant_stats(tree1)
    # Produce shade
    print(f"[asking the {tree1.get_name().lower()} to produce shade]")
    tree1.produce_shade()
    show_plant_stats(tree1)

    print()

    # Create Seed object and display its information
    print("=== Seed")
    seed1 = Seed("sunflower", 80.0, 45, "yellow", 42)
    seed1.show()
    # Grow, age and bloom
    print(f"[make {seed1.get_name().lower()} grow, age and bloom]")
    seed1.grow(30.0)
    seed1.age(20)
    seed1.bloom()
    seed1.show()
    show_plant_stats(seed1)

    print()

    # Create "anonymous" Plant object
    print("=== Anonymous")
    anon1 = Plant.anon()
    anon1.show()
    show_plant_stats(anon1)


if __name__ == "__main__":
    ft_garden_analytics()
