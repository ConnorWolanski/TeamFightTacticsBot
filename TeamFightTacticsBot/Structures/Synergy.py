class Synergy:
    def __init__(self, name, champions, boost_character_thresholds):
        self.name = name
        self.champions = champions
        self.boost_character_thresholds = boost_character_thresholds

    def __str__(self):
        return self.name
