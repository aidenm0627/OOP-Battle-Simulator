from enemy import Enemy

class BabyElf(Enemy):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        self.name = name
        print(f"Baby Elf {self.name} of color {self.color} has been created with {self.health} health and {self.attack_power} attack power.")

    def take_damage(self, damage):
        self.health -= damage
        print("Cry!! how could you hit a baby 😭, YOU MONSTER!")