def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:

    if unit.casefold() == "packets":
        print(f"{seed_type.lower().capitalize()} seeds: {quantity} packets "
              "available")
    elif unit.casefold() == "grams":
        print(f"{seed_type.lower().capitalize()} seeds: {quantity} grams "
              "total")
    elif unit.casefold() == "area":
        print(f"{seed_type.lower().capitalize()} seeds: covers {quantity} "
              "square meters")
    else:
        print("Unknown unit type")
