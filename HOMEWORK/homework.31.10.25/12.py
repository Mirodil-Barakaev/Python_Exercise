class Shape:
    def perimeter(self): pass
class Circle(Shape):
    def perimeter(self): print("Circle perimeter")
class Square(Shape):
    def perimeter(self): print("Square perimeter")

for s in [Circle(), Square()]:
    s.perimeter()