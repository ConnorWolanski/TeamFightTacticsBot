# Python downloaded libraries
import time
import pyautogui as auto_gui
import pyscreenshot as image_grab
from PIL import Image

# Objects
from TeamFightTacticsBot.Structures.Point import Point

# Constants
from TeamFightTacticsBot.Utility.Constants import PERCENTAGE_VARIANCE_ALLOWED
from TeamFightTacticsBot.Utility.Constants import PERCENTAGE_ACCURACY
from TeamFightTacticsBot.Utility.Constants import USER_32

# Global Variable imports
import TeamFightTacticsBot.Utility.Constants as Constants


def get_into_game():
    get_screen()
    play_button_location = find_play_button()

    if play_button_location is None:
        print("Could not find league client")
        return

    click_through_to_game(play_button_location)
    Constants.in_game = True


def click_through_to_game(point):
    # x, y is the locations of play button
    x = point.x
    y = point.y

    # This clicks on the play button
    click(x + 55, y + 10)

    # This clicks on the Team Fight Tactics part of game modes
    time.sleep(.5)
    click(x + 840, y + 250)

    # This clicks on the confirm for the game mode
    time.sleep(.5)
    click(x + 500, y + 666)

    # This clicks on the "Find Match" button once in a TFT lobby.
    time.sleep(3)
    click(x + 500, y + 666)

    # This checks if a queue is pops and then clicks on (Accept!/Decline)
    check_queue(point)


def check_queue(point):
    # get_screen()
    x = point.x
    y = point.y

    image = image_grab.grab(bbox=(x + 469, y + 234, x + 744, y + 424))
    image.save("queue_screenshot.png")
    queue_screenshot = Image.open("queue_screenshot.png")
    queue_check = Image.open("queue_check.PNG")

    popped = False
    while not popped:
        popped = compare_images(queue_screenshot, queue_check)
        image = image_grab.grab(bbox=(x + 468, y + 234, x + 743, y + 424))
        image.save("queue_screenshot.png")
        queue_screenshot = Image.open("queue_screenshot.png")
        time.sleep(.5)

    # Accept queue
    # click(x + 600, y + 540)

    # Decline queue
    click(x + 600, y + 600)


def find_play_button():
    screen_image = Image.open("screen.png")
    screen = screen_image.load()
    play_button_location = None

    play_button_image = Image.open("play_button.PNG")
    play_button_pixels = play_button_image.convert('RGB')
    play_button_pixels = play_button_pixels.load()

    for x in range(get_screensize()[0]):
        for y in range(get_screensize()[1]):
            if play_button_pixels[0, 0] == screen[x, y]:
                cropped_image = screen_image.crop((x, y, x + 200, y + 50))
                if compare_images(cropped_image, play_button_image):
                    play_button_location = Point(x, y)
                    break

    return play_button_location


def compare_images(tested, master):
    search = tested.load()
    search_from = master.load()

    width, height = master.size
    pixels_wanted = (width * height) * PERCENTAGE_ACCURACY
    pixels_accepted = 0

    for x in range(width):
        for y in range(height):
            if pixels_wanted < pixels_accepted:
                return True
            is_similar = compare_pixels(search[x, y], search_from[x, y])
            if is_similar:
                pixels_accepted += 1

    return False


def compare_pixels(tested, master):
    # Each input is a pixel with array values as such: [R, G, B, A]
    variance_allowed = (255 * PERCENTAGE_VARIANCE_ALLOWED) * 3

    # Variance for red component
    variance = abs(master[0] - tested[0])
    # Variance for green component
    variance += abs(master[1] - tested[1])
    # Variance for blue component
    variance += abs(master[2] - tested[2])

    return variance < variance_allowed


def get_screensize():
    return USER_32.GetSystemMetrics(0), USER_32.GetSystemMetrics(1)


def get_screen():
    screenshot_name = "screen.png"

    image = auto_gui.grab()
    image.save(screenshot_name)

    return Image.open(screenshot_name)


def click(x, y):
    auto_gui.click(x, y)
    print("Clicked at (" + str(x) + ", " + str(y) + ")")

