A1 = float(input("A1 = "))
B1 = float(input("B1 = "))
C1 = float(input("C1 = "))
A2 = float(input("A2 = "))
B2 = float(input("B2 = "))
C2 = float(input("C2 = "))
D = A1*B2 - A2*B1
Dx = -C1*B2 + C2*B1
Dy = -A1*C2 + A2*C1
x = Dx / D
y = Dy / D
print("x =", x, "y =", y)
