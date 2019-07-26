from TeamFightTacticsBot.Utility.BotController import bot_initialize
import TeamFightTacticsBot.Utility.Constants as Constants
from PIL import Image
from TeamFightTacticsBot.Utility.Utils import get_gold
from TeamFightTacticsBot.Utility.Utils import get_player_healths
from TeamFightTacticsBot.Utility.Utils import get_player_names
from TeamFightTacticsBot.Utility.Utils import check_place
import os
import glob


def start():
    if __name__ is not '__main__':
        return

    debugging = True

    if not debugging:
        Constants.variables_initialize(os.path.dirname(__file__))
        bot_initialize()

    if debugging:
        Constants.variables_initialize(os.path.dirname(__file__))
        # for image in Constants.ITEM_IMAGE_LIST:
        #    print(image.size)
        for item_image in glob.glob(Constants.MAIN_FILE_LOCATION + "/*.png"):
            test = Image.open(item_image)
            place = check_place(test)
            print("Names: " + str(get_player_names(test, place)))
            print("Healths: " + str(get_player_healths(test, place)))
            print("Gold: " + str(get_gold(test)))



start()
