import pyautogui

def click(x,y):
    pyautogui.click(x,y);
    print("Clicked")

click(200,100)