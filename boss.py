import random
from enemy import Enemy
from hero import Hero

class IceDragon(Enemy):
    """
    Ice Dragon boss blueprint.
    """

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        self.health = 350
        self.attack_power = random.randint(22, 45)
        self.ability = "freeze"
        self.frozen_once = False  # ensures dragon freezes hero only once
        print(f"Boss {self.name} colored {self.color} has been created with {self.health} health and {self.attack_power} attack power as well as a {self.ability} ability.")

    def attack(self):
        if self.health < 150:
            self.attack_power = 50
        return self.attack_power

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

    def is_alive(self):
        return self.health > 0

    def Freeze(self, hero):
        if self.health < 175 and not self.frozen_once and hero.frozen == 0:
            print(f"{self.name} uses FREEZE BREATH!❄️❄️ {hero.name} is frozen for 1 round!")
            hero.frozen = 1
            self.frozen_once = True

           
            
