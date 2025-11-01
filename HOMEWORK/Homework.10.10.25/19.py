def repeater(func, n):
    def inner():
        for _ in range(n): 
            func()
    return inner

def func():
    print("Eshmat")

print(repeater(func, 10))
