x1 = int(input("x1 ni kiriting: "))
y1 = int(input("y1 ni kiriting: "))
x2 = int(input("x2 ni kiriting: "))
y2 = int(input("y2 ni kiriting: "))
ox = abs(x1 - x2)
oy = abs(y1 - y2)

ans = (ox == 2 and oy == 1) or (ox == 1 and oy == 2)

print(ans)