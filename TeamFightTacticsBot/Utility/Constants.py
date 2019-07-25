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
CHARACTER_IMAGE_LIST = []


def variables_initialize(main_file):
    global MAIN_FILE_LOCATION
    MAIN_FILE_LOCATION = main_file
    global CHARACTER_IMAGE_LIST
    CHARACTER_IMAGE_LIST = load_resources()
    global in_game
    in_game = False
    global screensize
    screensize = USER_32.GetSystemMetrics(0), USER_32.GetSystemMetrics(1)


def load_resources():
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
