import random

son = random.randint(1, 100)  
print("1 dan 100 son oyladim!")

while True:
    taxmin = int(input("Son kiriting: "))
    if taxmin < son:
        print("Sonningiz kichkina")
    elif taxmin > son:
        print("Sonningiz katta")
    else:
        print("Togri! Siz topdingiz.")
        break
