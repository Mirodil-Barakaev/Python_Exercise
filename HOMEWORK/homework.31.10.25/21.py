class Flyer: 
    def move(self): print("Fly")
class Swimmer:
    def move(self): print("Swim")
class Duck(Flyer, Swimmer): pass
Duck().move()