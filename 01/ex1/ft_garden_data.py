#!/usr/bin/env python3


class Plant:


    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":


    ## Create Plant instances ##
    rose = Plant("rose", 25, 30) 
    sunflower = Plant("sunflower", 80, 45) 
    cactus = Plant("cactus", 15, 120) 

    ## Welcome message ##
    print("=== Garden Plant Registry ===")

    ## Display each plant's information ##
    rose.show()
    sunflower.show()
    cactus.show()
