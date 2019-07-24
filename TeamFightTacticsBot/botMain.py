import pyautogui as auto_gui
import pyscreenshot as image_grab
from PIL import Image
import time
from TeamFightTacticsBot.Utility.Constants import PERCENTAGE_VARIANCE_ALLOWED
from TeamFightTacticsBot.Utility.Constants import PERCENTAGE_ACCURACY
from TeamFightTacticsBot.Utility.Utils import get_screensize


def click(x, y):
    auto_gui.click(x, y)
    print("Clicked")


def get_screen():
    if __name__ == '__main__':
        image = auto_gui.grab()
        image.save("screen.png")


def compare_pixels(tested, master):
    variance_allowed = (255 * PERCENTAGE_VARIANCE_ALLOWED) * 3
    variance = 0
    red = abs(master[0] - tested[0])
    green = abs(master[1] - tested[1])
    blue = abs(master[2] - tested[2])
    variance += red
    variance += green
    variance += blue
    # print(variance)
    return variance < variance_allowed


def compare_image_to_play_button(tested):
    play_button_image = Image.open("play_button.PNG")
    pixels = tested.load()
    width, height = play_button_image.size
    play_button_image = play_button_image.load()
    total_pixels = width * height
    pixels_wanted = total_pixels * PERCENTAGE_ACCURACY

    # printed = "need: "
    # printed += str(pixelswanted)
    # print(printed)

    pixels_accepted = 0
    for x in range(width):
        for y in range(height):
            if pixels_wanted < pixels_accepted:
                return True

            is_similar = compare_pixels(pixels[x, y], play_button_image[x, y])
            if is_similar:
                pixels_accepted += 1

    # print(str(pixelsaccepted))
    print("Could not find the play button!")
    return False


def compare_images(tested, master):
    width, height = master.size
    search = tested.load()
    search_from = master.load()
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


def check_queue(x, y):
    get_screen()
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

    # Accept queue
    # click(x + 600, y + 540)
    # Decline queue
    click(x + 600, y + 600)
    print("done")


def start_game():
    get_screen()
    screen_image = Image.open("screen.png")
    screen = screen_image.load()

    play_button_image = Image.open("play_button.PNG")
    play_button_image = play_button_image.convert('RGB')
    play_button_image = play_button_image.load()

    found = False
    play_button_location = (0, 0)

    for x in range(get_screensize()[0]):
        for y in range(get_screensize()[1]):
            if play_button_image[0, 0] == screen[x, y]:
                cropped_image = screen_image.crop((x, y, x + 200, y + 50))
                if compare_image_to_play_button(cropped_image):
                    print(str(x) + "   " + str(y))
                    click(x+55, y + 10)
                    found = True
                    play_button_location = (x, y)
                    break

    if not found:
        return

    # At this point we have clicked the play button
    
    # This clicks on the Team Fight Tactics part of game modes
    time.sleep(.02)
    click(play_button_location[0] + 840, play_button_location[1] + 250)

    # This clicks on the confirm for the game mode
    time.sleep(.02)
    click(play_button_location[0] + 500, play_button_location[1] + 666)

    # This clicks on the "Find Match" button once in a TFT lobby.
    time.sleep(3)
    click(play_button_location[0] + 500, play_button_location[1] + 666)

    # This checks if a queue is pops and then clicks on (Accept!/Decline)
    check_queue(play_button_location[0], play_button_location[1])

    print("done")
    print(play_button_image[0, 0])


if __name__ == '__main__':
    start_game()
