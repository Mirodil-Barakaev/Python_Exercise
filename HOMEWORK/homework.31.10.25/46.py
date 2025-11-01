class Point:
    def __init__(self,x,y): self.x=x; self.y=y
    def __sub__(self,o): return Point(self.x-o.x,self.y-o.y)
p1=Point(5,4); p2=Point(2,1)
r=p1-p2; print(r.x,r.y)