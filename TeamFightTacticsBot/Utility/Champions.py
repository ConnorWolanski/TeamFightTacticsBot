from enum import Enum
from TeamFightTacticsBot.Structures.Champion import Champion


class Champions(Enum):
    # name, cost, health, attack_speed, attack_damage, range, armor, magic_resist
    # 1 Cost
    DARIUS = Champion("Darius", 1, 600, .5, 50, 1, 25, 20)
    ELISE = Champion("Elise", 1, 450, .6, 40, 2, 20, 20)
    FIORA = Champion("Fiora", 1, 400, 1, 40, 1, 25, 20)
    GAREN = Champion("Garen", 1, 600, .55, 55, 1, 35, 20)
    GRAVES = Champion("Graves", 1, 450, .5, 55, 1, 20, 20)
    KASSADIN = Champion("Kassadin", 1, 550, .65, 45, 1, 25, 20)
    KHAZIX = Champion("Khazix", 1, 500, .6, 50, 1, 20, 20)
    MORDEKAISER = Champion("Mordekaiser", 1, 550, .5, 50, 1, 35, 20)
    NIDALEE = Champion("Nidalee", 1, 500, .65, 50, 3, 20, 20)
    TRISTANA = Champion("Tristana", 1, 500, .65, 50, 4, 20, 20)
    VAYNE = Champion("Vayne", 1, 550, .65, 45, 3, 20, 20)
    WARWICK = Champion("Warwick", 1, 600, .6, 50, 1, 30, 20)
    # 2 Cost
    AHRI = Champion("Ahri", 2, 450, .55, 50, 3, 20, 20)
    BLITZCRANK = Champion("Blitzcrank", 2, 600, .5, 50, 1, 35, 20)
    BRAUM = Champion("Braum", 2, 750, .6, 40, 1, 25, 20)
    LISSANDRA = Champion("Lissandra", 2, 450, .6, 40, 2, 20, 20)
    LUCIAN = Champion("Lucian", 2, 600, .65, 65, 3, 25, 20)
    LULU = Champion("Lulu", 2, 500, .6, 50, 2, 25, 20)
    PYKE = Champion("Pyke", 2, 600, .6, 60, 1, 25, 20)
    REKSAI = Champion("Reksai", 2, 650, .65, 40, 1, 20, 20)
    SHEN = Champion("Shen", 2, 650, .6, 65, 1, 30, 20)
    TWISTEDFATE = Champion("Twistedfate", 2, 450, .75, 40, 3, 20, 20)
    VARUS = Champion("Varus", 2, 500, .7, 50, 4, 25, 20)
    ZED = Champion("Zed", 2, 650, .65, 65, 1, 25, 20)
    # 3 Cost
    AATROX = Champion("Aatrox", 3, 650, .65, 65, 1, 25, 20)
    ASHE = Champion("Ashe", 3, 550, .7, 60, 4, 20, 20)
    EVELYNN = Champion("Evelynn", 3, 550, .6, 60, 1, 20, 20)
    GANGPLANK = Champion("Gangplank", 3, 700, .65, 55, 1, 20, 20)
    KATARINA = Champion("Katarina", 3, 450, .6, 50, 1, 20, 20)
    KENNEN = Champion("Kennen", 3, 550, .65, 65, 2, 20, 20)
    MORGANA = Champion("Morgana", 3, 650, .6, 50, 2, 20, 20)
    POPPY = Champion("Poppy", 3, 800, .5, 50, 2, 40, 20)
    RENGAR = Champion("Rengar", 3, 550, .55, 65, 1, 20, 20)
    SHYVANA = Champion("Shyvana", 3, 650, .7, 50, 1, 20, 20)
    VEIGAR = Champion("Veigar", 3, 450, .55, 45, 3, 20, 20)
    VOLIBEAR = Champion("Volibear", 3, 700, .55, 75, 1, 30, 20)
    # 4 Cost
    AKALI = Champion("Akali", 4, 650, .7, 70, 1, 20, 20)
    AURELIONSOL = Champion("Aurelionsol", 4, 600, .6, 40, 3, 20, 20)
    BRAND = Champion("Brand", 4, 700, .6, 60, 3, 25, 20)
    CHOGATH = Champion("Chogath", 4, 1000, .55, 70, 1, 20, 20)
    DRAVEN = Champion("Dravem", 4, 700, .75, 75, 3, 25, 20)
    GNAR = Champion("Gnar", 4, 750, .7, 45, 2, 30, 20)
    KINDRED = Champion("Kindred", 4, 600, .65, 55, 3, 20, 20)
    LEONA = Champion("Leona", 4, 750, .55, 45, 1, 55, 20)
    SEJUANI = Champion("Sejuani", 4, 850, .55, 45, 1, 35, 25)
    # 5 Cost
    ANIVIA = Champion("Anivia", 5, 650, .6, 40, 3, 20, 20)
    KARTHUS = Champion("Karthus", 5, 850, .65, 65, 3, 25, 20)
    KAYLE = Champion("Kayle", 5, 800, 1.1, 60, 3, 35, 20)
    MISSFORTUNE = Champion("Missfortune", 5, 650, .85, 75, 3, 20, 20)
    SWAIN = Champion("Swain", 5, 850, .65, 65, 2, 25, 20)
    YASUO = Champion("Yasuo", 5, 700, 1, 65, 1, 35, 25)

