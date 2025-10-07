def sum_list_recursive(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sum_list_recursive(lst[1:])

print(sum_list_recursive([1, 2, 3, 4]))