import ctypes
from TeamFightTacticsBot.Utility.Utils import get_screensize

# Program wide variables
# Final
PERCENTAGE_ACCURACY = .7
PERCENTAGE_VARIANCE_ALLOWED = .2
USER_32 = ctypes.windll.user32

# Not Final
screensize = get_screensize()
