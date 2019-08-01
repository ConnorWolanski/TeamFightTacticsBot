from TeamFightTacticsBot.Utility.BotController import bot_initialize
import TeamFightTacticsBot.Utility.Constants as Constants
import TeamFightTacticsBot.Utility.Utils as Utils
import TeamFightTacticsBot.Utility.ConfigFileLoader as ConfigFileLoader
from TeamFightTacticsBot.Enumerators.Champions import Champions
from TeamFightTacticsBot.Enumerators.Synergies import Synergies
import os


def start():
    if __name__ is not '__main__':
        return

    debugging = True

    if not debugging:
        Constants.variables_initialize(os.path.dirname(__file__))
        bot_initialize()

    if debugging:
        Utils.initialize_resources(os.path.dirname(__file__))

        # buy_champions(Image.open("StoreTest.png"), None, None)
        ConfigFileLoader.edit_rating_in_file("Darius = 50:0", "Darius = 51:0")
        # print(str(get_items_carasel(test)))


start()
