def find_index(lst, n):
    for i in range(len(lst)):
        if lst[i] == n:
            return i
    return -1

print(find_index([10, 20, 30, 40], 30))