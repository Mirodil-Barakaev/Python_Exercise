def operate(a, b, op):
    return op(a, b)

print(operate(5, 3, lambda x, y: x + y))
print(operate(5, 3, lambda x, y: x - y))


