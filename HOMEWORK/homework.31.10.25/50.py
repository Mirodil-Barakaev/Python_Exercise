class Money:
    def __init__(self,a): self.a=a
    def __add__(self,o): return Money(self.a+o.a)
    def __sub__(self,o): return Money(self.a-o.a)
print((Money(10)+Money(5)).a, (Money(10)-Money(5)).a)