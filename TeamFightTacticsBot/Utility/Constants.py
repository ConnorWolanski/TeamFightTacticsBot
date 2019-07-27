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

CHARACTER_TIER_INDEXES = []
CHARACTER_IMAGE_LIST = []
ITEM_IMAGE_LIST = []
ITEM_NAMES_LIST = []
COST_CARD_BORDER_COLOR = []


def variables_initialize(main_file):
    global MAIN_FILE_LOCATION
    MAIN_FILE_LOCATION = main_file

    global CHARACTER_TIER_INDEXES
    global CHARACTER_IMAGE_LIST
    CHARACTER_IMAGE_LIST = load_champion_card_images()

    global ITEM_IMAGE_LIST
    global ITEM_NAMES_LIST
    ITEM_IMAGE_LIST = load_item_images()

    # Must be called AFTER loading the character images
    global COST_CARD_BORDER_COLOR
    COST_CARD_BORDER_COLOR = get_colors()

    # Instanced variables
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
        CHARACTER_TIER_INDEXES.append(index)
        path_to_this_directory = champion_image_folder + directory
        for character_image in glob.glob(path_to_this_directory + "/*.png"):
            image = Image.open(character_image)
            character_image_list.append(image)
            index += 1

    return character_image_list


def load_item_images():
    item_image_list = []
    item_image_folder = MAIN_FILE_LOCATION + '/Resources/Final/AppliedItems/'

    for item_image in glob.glob(item_image_folder + "/*.png"):
        ITEM_NAMES_LIST.append(item_image.split("AppliedItems\\")[1].split('.')[0])
        image = Image.open(item_image)
        item_image_list.append(image)

    return item_image_list


def get_colors():
    return [(CHARACTER_IMAGE_LIST[CHARACTER_TIER_INDEXES[0]].load()[170, 140]),
            CHARACTER_IMAGE_LIST[CHARACTER_TIER_INDEXES[1]].load()[170, 140],
            CHARACTER_IMAGE_LIST[CHARACTER_TIER_INDEXES[2]].load()[170, 140],
            CHARACTER_IMAGE_LIST[CHARACTER_TIER_INDEXES[3]].load()[170, 140],
            CHARACTER_IMAGE_LIST[CHARACTER_TIER_INDEXES[4]].load()[170, 140]]
