import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 1000
        self.attack_power = random.randint(5, 50)
        self.frozen = 0  # counts rounds the hero is frozen

    def strike(self):
        if self.frozen > 0:
            print(f"{self.name} is frozen solid and cannot attack this round! ❄️")
            self.frozen -= 1
            return 0
        return random.randint(1, self.attack_power)

    def receive_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

    def is_alive(self):
        return self.health > 0
