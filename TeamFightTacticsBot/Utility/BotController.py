from TeamFightTacticsBot.Utility.Utils import get_into_game


def initialize():
    start_game()
    print("Now playing TFT!")


def start_game():
    get_into_game()
    print("Started the game!")
