def multiply_list(lst):
    p = 1
    for i in lst:
        p *= i
    return p

print(multiply_list([2, 3, 4]))