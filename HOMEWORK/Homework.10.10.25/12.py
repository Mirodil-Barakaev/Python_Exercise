def make_multiplier(n):
    return lambda x: x * n

m2 = make_multiplier(2)
m3 = make_multiplier(3)
m5 = make_multiplier(5)

print(m2(10))
print(m3(10))
print(m5(10))
