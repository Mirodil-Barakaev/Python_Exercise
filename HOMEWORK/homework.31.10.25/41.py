class Warrior: 
    def attack(self): print("Sword")
class Mage: 
    def attack(self): print("Magic")
class Archer:
    def attack(self): print("Arrow")
for x in [Warrior(), Mage(), Archer()]: x.attack()