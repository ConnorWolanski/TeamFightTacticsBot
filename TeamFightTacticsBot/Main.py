from TeamFightTacticsBot.Utility.BotController import bot_initialize
import TeamFightTacticsBot.Utility.Constants as Constants
import TeamFightTacticsBot.Utility.Utils as Utils
import TeamFightTacticsBot.Utility.ConfigFileLoader as ConfigFileLoader
from TeamFightTacticsBot.Structures.LearnedMetaData import LearnedMetaData
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

        # print(str(get_items_carasel(test)))


start()
