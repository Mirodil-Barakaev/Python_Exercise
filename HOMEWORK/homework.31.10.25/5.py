class Dog:
    def action(self): print("Bark")
class Car:
    def action(self): print("Move")
class Robot:
    def action(self): print("Work")

for x in [Dog(), Car(), Robot()]:
    x.action()