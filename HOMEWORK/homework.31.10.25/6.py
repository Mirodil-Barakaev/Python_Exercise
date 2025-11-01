class Duck:
    def quack(self): print("Quack")
    def walk(self): print("Walk")
class Person:
    def quack(self): print("Imitate")
    def walk(self): print("Walk")

def make_it_quack(o):
    o.quack()
    o.walk()

make_it_quack(Duck())
make_it_quack(Person())