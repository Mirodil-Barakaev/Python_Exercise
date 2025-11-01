class X:
    def f(self): print("X")
class Y:
    def f(self): print("Y")
class Z(X, Y): pass
print(Z.__mro__)
Z().f()