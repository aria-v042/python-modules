def ft_water_reminder():

    days = int(input("Days since the last watering: "))

    print("Water the plants!" if days > 2 else "Plants are fine")
