from TeamFightTacticsBot.Utility.Utils import get_into_game
import TeamFightTacticsBot.Utility.Constants as Constants


def bot_initialize():
    start_game()
    print("Now playing TFT!")


def start_game():
    while not Constants.in_game:
        get_into_game()

    print("Started the game!")
