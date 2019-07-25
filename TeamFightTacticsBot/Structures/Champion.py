class Champion:
    def __init__(self, name, cost, health, attack_speed, attack_damage, attack_range, armor, magic_resist):
        self.name = name
        self.cost = cost
        self.health = health
        self.attack_speed = attack_speed
        self.attack_damage = attack_damage
        self.attack_range = attack_range
        self.armor = armor
        self.magic_resist = magic_resist

    def __str__(self):
        return "[Champion: " + self.name + ", Cost: " + str(self.cost) + ", Health: " + str(self.health) + ", Attack Speed: " + \
               str(self.attack_speed) + ", Attack Damage: " + str(self.attack_damage) + ", Attack Range: " + str(self.attack_range) +\
               ", Armor: " + str(self.armor) + ", Magic Resist: " + str(self.magic_resist) + "]"
