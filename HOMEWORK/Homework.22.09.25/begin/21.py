x1 = float(input("x1 ni kiriting: "))
y1 = float(input("y1 ni kiriting: "))
x2 = float(input("x2 ni kiriting: "))
y2 = float(input("y2 ni kiriting: "))
x3 = float(input("x3 ni kiriting: "))
y3 = float(input("y3 ni kiriting: "))

a = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
b = ((x3 - x2)**2 + (y3 - y2)**2) ** 0.5
c = ((x1 - x3)**2 + (y1 - y3)**2) ** 0.5
P = a + b + c
p = P / 2
S = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print("Perimetr:", P)
print("Yuza:", S)
