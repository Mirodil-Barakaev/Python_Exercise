class Base: pass
class A(Base):
    def f(self): print("ok")
def test(x):
    if isinstance(x, Base) or hasattr(x,"f"): x.f()
A().f(); test(A())