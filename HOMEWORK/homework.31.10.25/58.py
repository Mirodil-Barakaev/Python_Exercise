class Money:
    def __init__(s,a,c):
        s.a=a
        s.c=c
    def __format__(s,f):
        return f"{s.a:.1f}{s.c}"

m=Money(7.5,"$")
print(f"{m:x}")
