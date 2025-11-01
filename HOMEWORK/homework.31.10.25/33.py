from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): pass
class Circle(Shape):
    def area(self): print("Circle area")
class Square(Shape):
    def area(self): print("Square area")
for s in [Circle(), Square()]: s.area()