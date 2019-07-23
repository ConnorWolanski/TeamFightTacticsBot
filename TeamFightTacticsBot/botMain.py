import pyautogui as AutoGUI
import pyscreenshot as ImageGrab
from PIL import Image
import time
import ctypes

# Program wide variables
percentageaccuracy = .7
percentagevarianceallowed = .2
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


def click(x, y):
    AutoGUI.click(x, y)
    print("Clicked")


def getscreen():
    if __name__ == '__main__':
        im = ImageGrab.grab()
        im.save("screen.png")


def comparepixels(master, input):
    varianceallowed = (255 * percentagevarianceallowed) * 3
    variance = 0
    red = abs(master[0] - input[0])
    green = abs(master[1] - input[1])
    blue = abs(master[2] - input[2])
    variance += red
    variance += green
    variance += blue
    #print(variance)
    return (variance < varianceallowed)


def compareimagetoplaybutton(input):
    playbuttonimage = Image.open("play_button.PNG")
    pixels = input.load()
    width, height = playbuttonimage.size
    playbuttonimage = playbuttonimage.load()
    totalpixels = width * height
    pixelswanted = totalpixels * percentageaccuracy

    #printed = "need: "
    #printed += str(pixelswanted)
    #print(printed)

    pixelsaccepted = 0
    for x in range(width):
        for y in range(height):
            if(pixelswanted < pixelsaccepted):
                return True

            isSimilar = comparepixels(playbuttonimage[x, y], pixels[x, y])
            if isSimilar:
                pixelsaccepted += 1

    #print(str(pixelsaccepted))
    return False


def compareImages(input, master):
    width, height = master.size
    search = input.load()
    searchFrom = master.load()
    pixelswanted = (width * height) * percentageaccuracy
    pixelsaccepted = 0
    for x in range(width):
        for y in range(height):
            if(pixelswanted < pixelsaccepted):
                print("done1")
                return True
            isSimilar = comparepixels(search[x, y], searchFrom[x, y])
            if isSimilar:
                pixelsaccepted += 1
    return False


def checkQueue(x, y):
    getscreen()
    qSS = Image.open("screen.png")
    im = ImageGrab.grab(bbox=(x + 469, y + 234, x + 744, y + 424))
    im.save("queue_screenshot.png")
    qSS = Image.open("queue_screenshot.png")
    qC = Image.open("queue_check.PNG")
    popped = False
    while (popped == False):
        popped = compareImages(qSS, qC)
        im = ImageGrab.grab(bbox=(x + 468, y + 234, x + 743, y + 424))
        im.save("queue_screenshot.png")
        qSS = Image.open("queue_screenshot.png")
    click(x + 600, y + 540)
    print("done")


def startGame():
    getscreen()
    screenImage = Image.open("screen.png")
    screen = screenImage.load()

    playbuttonimage = Image.open("play_button.PNG")
    playbuttonimage = playbuttonimage.convert('RGB')
    playbuttonimage = playbuttonimage.load()
    playButtonLocation = (0, 0)
    found = False
    for x in range(screensize[0]):
        for y in range(screensize[1]):
            if(playbuttonimage[0, 0] == screen[x, y]):
                croppedImage = screenImage.crop((x, y, x + 200, y + 50))
                if(compareimagetoplaybutton(croppedImage)):
                    print(str(x) + "   " + str(y))
                    click(x+55, y + 10)
                    found = True
                    playButtonLocation = (x, y)
                    break
    time.sleep(.02)
    click(playButtonLocation[0] + 840, playButtonLocation[1] + 250)
    time.sleep(.02)
    click(playButtonLocation[0] + 500, playButtonLocation[1] + 666)
    time.sleep(3)
    click(playButtonLocation[0] + 500, playButtonLocation[1] + 666)
    checkQueue(playButtonLocation[0], playButtonLocation[1])
    print("done")
    print(playbuttonimage[0, 0])


if __name__ == '__main__':
    startGame()
