from enemy import Enemy
import random

class IceDragon(Enemy):
    """
    This is our dragon blueprint 
    """
    def __init__(self, name, color):
        super().__init__(name)
        self.color = "white"
        self.name = "Ice Dragon"
        self.health = 350
        self.attack_power = random.randint(22, 45)
        self.ability = "freeze"
        print(f"Boss {self.name} colored {self.color} has been created with {self.health} health and {self.attack_power} attack power as well as a {self.ability} ability.")
    
    def attack(self):
        if self.health < 150:
            self.attack_power = 40

        return self.attack_power
    
    def Freeze(self):
        if self.health < 175:
            
