def is_armstrong(n):
    s = 0
    for i in str(n):
        s += int(i) ** len(str(n))
    return s == n

print(is_armstrong(153))