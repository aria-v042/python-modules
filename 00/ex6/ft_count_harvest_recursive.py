# def ft_count_harvest_recursive():
#
#     harvest = int(input("Days until harvest: "))
#
#     day = 1
#     def count_days(day):
#         print("Day", day)
#         if day == harvest:
#             print("Harvest time!")
#         else:
#             count_days(day + 1)
#     count_days(day)

def ft_count_harvest_recursive(day=1, harvest=0):

    if day == 1:
        harvest = int(input("Days until harvest: "))

    if day <= harvest:
        print("Day", day)

    if day >= harvest:
        print("Harvest time!")
    else:
        ft_count_harvest_recursive(day + 1, harvest)
