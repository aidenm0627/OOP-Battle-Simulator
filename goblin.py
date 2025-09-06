from enemy import Enemy

class Goblin(Enemy):
    """
    This is our goblin blueprint 
    """
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        self.name = name
        print(f"Goblin {self.name} of color {self.color} has been created with {self.health} health and {self.attack_power} attack power.")
  
