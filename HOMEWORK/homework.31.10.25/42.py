class Shape: 
    def perimeter(self): pass
class Circle(Shape):
    def perimeter(self): print("Circle P")
class Square(Shape):
    def perimeter(self): print("Square P")
for s in [Circle(), Square()]: s.perimeter()