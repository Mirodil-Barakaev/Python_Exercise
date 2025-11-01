class A:
    def run(self): print("A run")
class B: pass

def test(o):
    if isinstance(o, A) or hasattr(o, "run"): o.run()
    else: print("Not runnable")

test(A())
test(B())