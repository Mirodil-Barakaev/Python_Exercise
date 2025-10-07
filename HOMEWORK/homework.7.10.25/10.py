def even_numbers(lst):
    new = []
    for i in lst:
        if i % 2 == 0:
            new.append(i)
    return new

print(even_numbers([1, 2, 3, 4, 5, 6]))