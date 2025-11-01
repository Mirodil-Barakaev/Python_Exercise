class A:
    def f(self): print("A")
class B(A):
    def f(self):
        super().f()
        print("B")
class C(B):
    def f(self):
        super().f()
        print("C")
C().f()