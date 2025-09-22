a = float(input("a ni kiriting: "))
b = float(input("b ni kiriting: "))
A = a if a >= 0 else -a
B = b if b >= 0 else -b
S = A + B
D = A - B
P = A * B
Q = A / B
print("Yig'indi:", S)
print("Ayirma:", D)
print("Ko'paytma:", P)
print("Nisbat:", Q)
