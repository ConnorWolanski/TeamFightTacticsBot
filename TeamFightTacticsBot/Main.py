from TeamFightTacticsBot.Utility.BotController import bot_initialize
import TeamFightTacticsBot.Utility.Constants as Constants
import TeamFightTacticsBot.Utility.GameConstants as GameConstants
import TeamFightTacticsBot.Utility.Utils as Utils
import TeamFightTacticsBot.Utility.TestingUtils as TestingUtils
from TeamFightTacticsBot.Enumerators.Champions import Champions
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

        GameConstants.PLAYER_BOARD.board_slots[1][1] = Champions.MORDEKAISER.value
        shops = TestingUtils.get_images_from_directory()
        for shop in shops:
            Utils.buy_champions(shop)

        owned = []
        for champion in Utils.get_champions_owned():
            owned.append(champion.name)

        print(owned)


start()
