def sum_odd_numbers(lst):
    s = 0
    for i in lst:
        if i % 2 != 0:
            s += i
    return s

print(sum_odd_numbers([1, 2, 3, 4, 5, 6]))