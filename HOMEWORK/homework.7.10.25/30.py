def sum_of_digits(n):
    s = 0
    for i in str(n):
        s += int(i)
    return s

print(sum_of_digits(1234))