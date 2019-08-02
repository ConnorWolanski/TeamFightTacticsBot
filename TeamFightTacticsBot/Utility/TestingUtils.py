from PIL import Image
import glob
import TeamFightTacticsBot.Utility.Constants as Constants


def get_images_from_directory():
    images = []

    for testing_image in glob.glob(Constants.MAIN_FILE_LOCATION + "/Testing/*.png"):
        images.append(Image.open(testing_image))

    return images
