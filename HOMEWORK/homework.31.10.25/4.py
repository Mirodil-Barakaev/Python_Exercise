class Car:
    def drive(self): print("Drive car")
class Bike:
    def drive(self): print("Ride bike")

for v in [Car(), Bike()]:
    v.drive()