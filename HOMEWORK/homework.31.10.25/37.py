def start(x): x.run()
class A: 
    def run(self):
        print("A")
class B:
    def run(self):
        print("B")
start(A())
start(B())