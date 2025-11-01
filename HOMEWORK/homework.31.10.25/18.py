class Student:
    def __init__(self,lvl): self.lvl=lvl
    def __lt__(self,o): return self.lvl<o.lvl

print(Student(2)<Student(5))