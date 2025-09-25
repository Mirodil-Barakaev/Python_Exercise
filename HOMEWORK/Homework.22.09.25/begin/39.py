import math
A = float(input("A = "))
B = float(input("B = "))
C = float(input("C = "))
D = B**2 - 4*A*C
if D < 0:
    print("Yechim yo'q")
elif D == 0:
    x = -B / (2*A)
    print("Bitta yechim:", x)
else:
    x1 = (-B + math.sqrt(D)) / (2*A)
    x2 = (-B - math.sqrt(D)) / (2*A)
    print("Ikkita yechim:", x1, x2)

