class R:
    def __init__(s,a,b):
        s.a=a
        s.b=b
    def __int__(s):
        return sum(range(s.a,s.b+1))
    def __str__(s):
        return str(int(s))

r=R(1,5)
print(r)
