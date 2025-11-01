class Dog: 
    def action(self): print("Bark")
class Car: 
    def action(self): print("Run")
class Robot: 
    def action(self): print("Move")
for o in [Dog(), Car(), Robot()]: o.action()