#!/usr/bin/env python


def display_plant_info(name: str, height: float, age: int) -> None:

    print("Plant:", name.capitalize())
    print("Height: ", height, "cm", sep="")
    print("Age:", age, "days")


def ft_garden_intro() -> None:

    print("=== Welcome to My Garden ===")

    # # User input
    # name = input("Plant name: ")
    # height = int(input("Plant height: "))
    # age = int(input("Plant age: "))
    # print()

    # Hard coded
    name = "Rose"
    height = 25
    age = 30

    display_plant_info(name, height, age)

    print()
    print("=== End of Program ===")


if __name__ == "__main__":

    ft_garden_intro()
