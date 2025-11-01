class book:
    
    def __init__(self,name,authors):
        self.name = name
        self.authors = authors

    @classmethod
    def default_book(cls):
        return cls("Unknow","Unknow")



book1 = book("harry poter 1","Eshmat")

print(book1.authors,book1.name)
