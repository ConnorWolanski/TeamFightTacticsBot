import pyautogui as AutoGUI
import pyscreenshot as ImageGrab
import pytesseract as Tesseract
from PIL import Image, ImageFilter, ImageEnhance

# Program wide variables
percentageaccuracy = .8
percentagevarianceallowed = .3


def click(x, y):
    AutoGUI.click(x, y)
    print("Clicked")


def getscreen():
    if __name__ == '__main__':
        im = ImageGrab.grab(bbox=(200, 200, 365, 243))
        im.show()
        im.save("screen.png")
        return getimage()


def getimage():
    return Image.open("screen.png")


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
    playbuttonimage = Image.open("play_button.png")
    pixels = input.load()
    width, height = playbuttonimage.size
    playbuttonimage = playbuttonimage.load()
    totalpixels = width * height
    pixelswanted = totalpixels * percentageaccuracy

    printed = "need: "
    printed += str(pixelswanted)
    print(printed)

    pixelsaccepted = 0
    for x in range(width):
        for y in range(height):
            if(pixelswanted < pixelsaccepted):
                return True

            isSimilar = comparepixels(playbuttonimage[x, y], pixels[x, y])
            if isSimilar:
                pixelsaccepted += 1

    print(str(pixelsaccepted))
    return False


val = getscreen()

if val is not None:
    info = "With accuracy: "
    info += str(percentageaccuracy)
    info += "\nWith variance allowed: "
    info += str(percentagevarianceallowed)
    print(info)
    print(compareimagetoplaybutton(val))
