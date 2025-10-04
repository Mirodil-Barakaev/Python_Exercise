import math
n = int(input("n: "))
x = int(input("x: "))
s = 0
for i in range(1,n+1):
    s += math.pow(-1,i)*math.pow(x,i) / i

print(s)    