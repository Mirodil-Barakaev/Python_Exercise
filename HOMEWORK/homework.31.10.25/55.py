class Img:
    def __init__(s,n):
        s.n=n
    def __add__(s,o):
        return Img(s.n+"+"+o.n)
    def __str__(s):
        return s.n

a=Img("bg")
b=Img("fx")
print(a+b)
