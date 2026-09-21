def ft_count_harvest_iterative():

    harvest = int(input("Days until harvest: "))

    for day in range(1, harvest + 1):
        print("Day", day)

    # day: int = 1
    # while (day <= harvest):
    #     print("Day", day)
    #     day += 1

    print("Harvest time!")
