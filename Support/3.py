lst = [3, 7, 10, 69, 41]

def isPrime(n: int) -> bool:
    for i in range (2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def GetPrimeNumbers(lst: list[int]) -> list[int]:
    primes = []
    for i in lst:
        if isPrime(i):
            primes.append(i)
    return primes

print(GetPrimeNumbers(lst))
