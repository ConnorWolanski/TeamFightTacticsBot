from TeamFightTacticsBot.Utility.BotController import bot_initialize
import TeamFightTacticsBot.Utility.Constants as Constants
from PIL import Image
from TeamFightTacticsBot.Utility.Utils import buy_champions
from TeamFightTacticsBot.Utility.Utils import get_screen
import os


def start():
    if __name__ is not '__main__':
        return

    debugging = True

    if not debugging:
        Constants.variables_initialize(os.path.dirname(__file__))
        bot_initialize()

    if debugging:
        Constants.variables_initialize(os.path.dirname(__file__))
        buy_champions(Image.open("StoreTest.png"), None, None)

        # print(str(get_items_carasel(test)))


start()
