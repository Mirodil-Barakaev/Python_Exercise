class Duck: 
    def quack(self): print("Quack")
    def walk(self): print("Duck walk")
class Person:
    def quack(self): print("Try quack")
    def walk(self): print("Walk")
def make_it_quack(x): x.quack()
for o in [Duck(), Person()]: make_it_quack(o)