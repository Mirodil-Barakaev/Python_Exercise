class Point:
    def __init__(self,x,y): self.x=x; self.y=y
    def __sub__(self,o): return Point(self.x-o.x, self.y-o.y)
    def __repr__(self): return f"({self.x},{self.y})"

print(Point(5,5)-Point(2,1))