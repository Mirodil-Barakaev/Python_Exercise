class Dog: pass
class Car:
    def move(self): print("Move")

def start(o):
    if hasattr(o, "move"): o.move()
    else: print("No move()")

start(Dog())
start(Car())