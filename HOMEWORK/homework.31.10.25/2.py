def animal_sound(a):
    a.sound()

class Dog: 
     def sound(self): 
        print("Woof")
class Cat:
     def sound(self):
         print("Meow")

animal_sound(Dog())
animal_sound(Cat())