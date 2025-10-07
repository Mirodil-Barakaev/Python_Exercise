def second_max(lst):
    lst.sort()
    return lst[-2]

print(second_max([10, 50, 20, 40]))