from TeamFightTacticsBot.Utility.Constants import USER_32


def get_screensize():
    return USER_32.GetSystemMetrics(0), USER_32.GetSystemMetrics(1)
