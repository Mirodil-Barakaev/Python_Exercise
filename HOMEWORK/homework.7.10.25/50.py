def sum_matrix(a):
    s = 0
    for row in a:
        for i in row:
            s += i
    return s

print(sum_matrix([[1, 2, 3], [4, 5, 6]]))