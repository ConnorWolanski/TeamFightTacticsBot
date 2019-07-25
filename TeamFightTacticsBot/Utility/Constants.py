import ctypes

# Program wide variables
# Final
PERCENTAGE_ACCURACY = .7
PERCENTAGE_VARIANCE_ALLOWED = .2
USER_32 = ctypes.windll.user32

# Not Final
screensize = USER_32.GetSystemMetrics(0), USER_32.GetSystemMetrics(1)
