class Money:
    def __init__(self,a): self.a=a
    def __add__(self,o): return Money(self.a+o.a)
    def __sub__(self,o): return Money(self.a-o.a)
    def __repr__(self): return f"${self.a}"

print(Money(10)+Money(5))
print(Money(10)-Money(3))