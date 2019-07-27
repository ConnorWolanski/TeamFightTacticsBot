import ctypes
import glob
from PIL import Image
import os

# Program wide variables
# Final
PERCENTAGE_ACCURACY = .8
PERCENTAGE_VARIANCE_ALLOWED = .1
USER_32 = ctypes.windll.user32
MAIN_FILE_LOCATION = ''
# 0 - 11 1 Cost Champs
# 12 - 23 2 Cost Champs
# 24 - 35 3 Cost Champs
# 36 - 44 4 Cost Champs
# 45 - 50 5 Cost Champs
CHARACTER_IMAGE_LIST = []
ITEM_IMAGE_LIST = []
COST_CARD_BORDER_COLOR = []


def variables_initialize(main_file):
    global MAIN_FILE_LOCATION
    MAIN_FILE_LOCATION = main_file
    global CHARACTER_IMAGE_LIST
    CHARACTER_IMAGE_LIST = load_champion_card_images()
    global ITEM_IMAGE_LIST
    ITEM_IMAGE_LIST = load_item_images()
    global COST_CARD_BORDER_COLOR
    COST_CARD_BORDER_COLOR = get_colors()
    global in_game
    in_game = False
    global screensize
    screensize = USER_32.GetSystemMetrics(0), USER_32.GetSystemMetrics(1)


def load_champion_card_images():
    character_image_list = []
    index = 0
    champion_image_folder = MAIN_FILE_LOCATION + '/Resources/Final/Champions/'
    directories = os.listdir(champion_image_folder)
    for directory in directories:
        path_to_this_directory = champion_image_folder + directory
        index += 1
        for character_image in glob.glob(path_to_this_directory + "/*.png"):
            image = Image.open(character_image)
            character_image_list.append(image)

    return character_image_list


def load_item_images():
    item_image_list = []
    item_image_folder = MAIN_FILE_LOCATION + '/Resources/Final/AppliedItems/'
    for item_image in glob.glob(item_image_folder + "/*.png"):
        image = Image.open(item_image)
        item_image_list.append(image)

    return item_image_list


def get_colors():
    color_list = []

    color_list.append(CHARACTER_IMAGE_LIST[0].load()[170, 140])
    color_list.append(CHARACTER_IMAGE_LIST[12].load()[170, 140])
    color_list.append(CHARACTER_IMAGE_LIST[24].load()[170, 140])
    color_list.append(CHARACTER_IMAGE_LIST[36].load()[170, 140])
    color_list.append(CHARACTER_IMAGE_LIST[45].load()[170, 140])

    return color_list
