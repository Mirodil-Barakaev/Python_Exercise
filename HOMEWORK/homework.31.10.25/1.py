class Dog:
    def sound(self):
        print("Woof")
class Cat:
    def sound(self):
        print("Meow")
class Cow:
    def sound(self):
        print("Moo")

for a in [Dog(), Cat(), Cow()]:
    a.sound()