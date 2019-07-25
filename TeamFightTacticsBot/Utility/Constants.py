import ctypes

# Program wide variables
# Final
PERCENTAGE_ACCURACY = .7
PERCENTAGE_VARIANCE_ALLOWED = .2
USER_32 = ctypes.windll.user32


def variables_initialize():
    global in_game
    in_game = False
    global screensize
    screensize = USER_32.GetSystemMetrics(0), USER_32.GetSystemMetrics(1)
