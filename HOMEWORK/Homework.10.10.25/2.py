def add(a,b):
    return (a + b)

def subtract(a,b):
    return (a - b)

operations = [add,subtract]

a = int(input("a="))
b = int(input("b="))
print(operations[0](a,b))
print(operations[1](a,b))
