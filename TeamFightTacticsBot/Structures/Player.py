class Player:
    def __init__(self, name):
        self.hp = 100
        self.name = name

    def __str__(self):
        return "[" + \
                "Name: " + str(self.name) + \
                "Health: " + str(self.hp) + \
               "]"
