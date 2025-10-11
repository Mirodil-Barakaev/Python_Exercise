def isPerfect(n: int) -> bool:
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n
print(isPerfect(28))

def GetPerfectNumbers(lst: list[int]) -> list[int]:
    l = []
    for i in lst:
        if isPerfect(i):
           l.append(i)
    return l
print(GetPerfectNumbers([6,28]))

