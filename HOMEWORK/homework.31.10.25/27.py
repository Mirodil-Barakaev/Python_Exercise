class A:
    def m(self): print("A")
class B(A):
    def m(self): print("B")
class C(A):
    def m(self): print("C")
class D(B, C): pass
d = D(); d.m(); print(D.__mro__)