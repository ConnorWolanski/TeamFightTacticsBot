class LearnedMetaData:
    def __init__(self, rating, games_played):
        self.rating = rating
        self.games_played = games_played

    def __str__(self):
        return "[Rating: " + str(self.rating) + ", Games Played: " + str(self.games_played) + "]"
