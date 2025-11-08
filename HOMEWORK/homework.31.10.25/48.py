class Student:
    def __init__(self,l):
         self.l=l
    def __lt__(self,o):
         return self.l<o.l
    
print(Student(2)<Student(3))
