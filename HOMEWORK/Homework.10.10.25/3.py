def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

key = int(input("Son kiriting (1=qoshish, 2=ayirish, 3=kopaytirish): "))
a = int(input("a="))
b = int(input("b="))

if key == 1:
    print("Natija:", add(a, b))
elif key == 2:
    print("Natija:", subtract(a, b))
elif key == 3:
    print("Natija:", mul(a, b))
else:
    print("Notogri son kiritdingiz")
