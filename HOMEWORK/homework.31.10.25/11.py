class Warrior:
    def attack(self): print("Sword")
class Mage:
    def attack(self): print("Magic")
class Archer:
    def attack(self): print("Bow")

for p in [Warrior(), Mage(), Archer()]:
    p.attack()