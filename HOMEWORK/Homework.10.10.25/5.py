def apply(func, value):
    return func(value)

def kvadrat(x):
    return x * x

print(apply(kvadrat, 5))
print(apply(lambda x: x + 10, 5))
