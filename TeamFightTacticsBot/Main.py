from TeamFightTacticsBot.Utility.BotController import bot_initialize
import TeamFightTacticsBot.Utility.Constants as Constants
import TeamFightTacticsBot.Utility.GameConstants as GameConstants
import TeamFightTacticsBot.Utility.Utils as Utils
import TeamFightTacticsBot.Utility.TestingUtils as TestingUtils
from TeamFightTacticsBot.Enumerators.Champions import Champions
import os
import copy


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

        print(GameConstants.PLAYER_BOARD)
        '''
        level_2_mord = copy.copy(Champions.MORDEKAISER.value)
        level_2_mord.level += 1
        GameConstants.PLAYER_BOARD.board_slots[2][1] = copy.copy(level_2_mord)
        GameConstants.PLAYER_BOARD.bench_slots[2] = copy.copy(level_2_mord)
        GameConstants.PLAYER_BOARD.bench_slots[3] = copy.copy(Champions.MORDEKAISER.value)
        GameConstants.PLAYER_BOARD.bench_slots[4] = copy.copy(Champions.MORDEKAISER.value)
        print(GameConstants.PLAYER_BOARD)
        owned = Utils.get_champions_owned()
        Utils.add_champion_to_board(Champions.MORDEKAISER.value, owned)
        owned = Utils.get_champions_owned()
        print(GameConstants.PLAYER_BOARD)
         '''


start()
