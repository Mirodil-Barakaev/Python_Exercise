class Box:
    def __init__(s,a):
        s.a=a
    def __contains__(s,x):
        return x in s.a

b=Box(["x","y","z"])
print("x"in b)
