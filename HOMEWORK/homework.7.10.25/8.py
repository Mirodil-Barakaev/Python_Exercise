def unique_list(lst):
    new = []
    for i in lst:
        if i not in new:
            new.append(i)
    return new

print(unique_list([1, 2, 2, 3, 3, 4]))