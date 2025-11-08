class Book:
    def __init__(self,t,a):
         self.t=t
         self.a=a
    def __eq__(self,o): 
        return self.t==o.t and self.a==o.a
print(Book("A","B")==Book("A","B"))