def safe_run(x):
    if hasattr(x,"run"): x.run()
    else: print("No run")
class A: pass
class B: 
    def run(self): print("Run")
safe_run(A()); safe_run(B())