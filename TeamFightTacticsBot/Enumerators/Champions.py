from enum import Enum
from TeamFightTacticsBot.Structures.Champion import Champion
from TeamFightTacticsBot.Enumerators.Synergies import Synergies


class Champions(Enum):
    # name, cost, health, attack_speed, attack_damage, range, armor, magic_resist
    # 1 Cost
    DARIUS = Champion("Darius", 1, 600, .5, 50, 1, 40, 20, (Synergies.KNIGHT, Synergies.IMPERIAL))
    ELISE = Champion("Elise", 1, 450, .6, 40, 2, 20, 20, (Synergies.DEMON, Synergies.SHAPESHIFTER))
    FIORA = Champion("Fiora", 1, 400, 1, 40, 1, 25, 20, (Synergies.BLADEMASTER, Synergies.NOBLE))
    GAREN = Champion("Garen", 1, 600, .6, 50, 1, 40, 20, (Synergies.NOBLE, Synergies.KNIGHT))
    GRAVES = Champion("Graves", 1, 450, .55, 55, 1, 20, 20, (Synergies.PIRATE, Synergies.GUNSLINGER))
    KASSADIN = Champion("Kassadin", 1, 550, .6, 55, 1, 25, 20, (Synergies.SORCERER, Synergies.VOID))
    KHAZIX = Champion("Khazix", 1, 500, .6, 55, 1, 20, 20, (Synergies.VOID, Synergies.ASSASSIN))
    MORDEKAISER = Champion("Mordekaiser", 1, 550, .5, 50, 1, 40, 20, (Synergies.KNIGHT, Synergies.PHANTOM))
    NIDALEE = Champion("Nidalee", 1, 500, .65, 50, 3, 20, 20, (Synergies.WILD, Synergies.SHAPESHIFTER))
    TRISTANA = Champion("Tristana", 1, 500, .65, 50, 4, 20, 20, (Synergies.GUNSLINGER, Synergies.YORDLE))
    VAYNE = Champion("Vayne", 1, 550, .75, 40, 3, 20, 20, (Synergies.NOBLE, Synergies.RANGER))
    WARWICK = Champion("Warwick", 1, 600, .6, 50, 1, 30, 20, (Synergies.WILD, Synergies.BRAWLER))
    # 2 Cost
    AHRI = Champion("Ahri", 2, 450, .55, 50, 3, 20, 20, (Synergies.WILD, Synergies.SORCERER))
    BLITZCRANK = Champion("Blitzcrank", 2, 600, .5, 50, 1, 35, 20, (Synergies.BRAWLER, Synergies.ROBOT))
    BRAUM = Champion("Braum", 2, 750, .6, 40, 1, 75, 20, (Synergies.GLACIAL, Synergies.GUARDIAN))
    LISSANDRA = Champion("Lissandra", 2, 450, .6, 40, 2, 20, 20, (Synergies.GLACIAL, Synergies.ELEMENTALIST))
    LUCIAN = Champion("Lucian", 2, 600, .65, 65, 3, 25, 20, (Synergies.GUNSLINGER, Synergies.NOBLE))
    LULU = Champion("Lulu", 2, 500, .6, 50, 2, 20, 20, (Synergies.YORDLE, Synergies.SORCERER))
    PYKE = Champion("Pyke", 2, 600, .6, 60, 1, 25, 20, (Synergies.PIRATE, Synergies.ASSASSIN))
    REKSAI = Champion("Reksai", 2, 650, .65, 50, 1, 20, 20, (Synergies.BRAWLER, Synergies.VOID))
    SHEN = Champion("Shen", 2, 650, .7, 65, 1, 30, 20, (Synergies.NINJA, Synergies.BLADEMASTER))
    TWISTED_FATE = Champion("Twisted Fate", 2, 450, .75, 40, 3, 20, 20, (Synergies.PIRATE, Synergies.SORCERER))
    VARUS = Champion("Varus", 2, 500, .7, 50, 4, 25, 20, (Synergies.RANGER, Synergies.DEMON))
    ZED = Champion("Zed", 2, 650, .65, 65, 1, 25, 20, (Synergies.ASSASSIN, Synergies.NINJA))
    # 3 Cost
    AATROX = Champion("Aatrox", 3, 700, .65, 65, 1, 25, 20, (Synergies.DEMON, Synergies.BLADEMASTER))
    ASHE = Champion("Ashe", 3, 550, .7, 65, 4, 20, 20, (Synergies.RANGER, Synergies.GLACIAL))
    EVELYNN = Champion("Evelynn", 3, 550, .6, 70, 1, 20, 20, (Synergies.ASSASSIN, Synergies.DEMON))
    GANGPLANK = Champion("Gangplank", 3, 700, .65, 55, 1, 20, 20, (Synergies.GUNSLINGER, Synergies.BLADEMASTER,
                                                                   Synergies.PIRATE))
    KATARINA = Champion("Katarina", 3, 450, .6, 50, 1, 20, 20, (Synergies.ASSASSIN, Synergies.IMPERIAL))
    KENNEN = Champion("Kennen", 3, 550, .65, 65, 2, 20, 20, (Synergies.YORDLE, Synergies.NINJA, Synergies.ELEMENTALIST))
    MORGANA = Champion("Morgana", 3, 650, .6, 50, 2, 20, 20, (Synergies.DEMON, Synergies.SORCERER))
    POPPY = Champion("Poppy", 3, 800, .5, 50, 2, 40, 20, (Synergies.KNIGHT, Synergies.YORDLE))
    RENGAR = Champion("Rengar", 3, 550, .6, 70, 1, 20, 20, (Synergies.WILD, Synergies.ASSASSIN))
    SHYVANA = Champion("Shyvana", 3, 650, .7, 50, 1, 30, 20, (Synergies.DRAGON, Synergies.SHAPESHIFTER))
    VEIGAR = Champion("Veigar", 3, 500, .55, 45, 3, 20, 20, (Synergies.SORCERER, Synergies.YORDLE))
    VOLIBEAR = Champion("Volibear", 3, 700, .55, 75, 1, 30, 20, (Synergies.BRAWLER, Synergies.GLACIAL))
    # 4 Cost
    AKALI = Champion("Akali", 4, 650, .7, 70, 1, 20, 20, (Synergies.NINJA, Synergies.ASSASSIN))
    AURELION_SOL = Champion("Aurelion Sol", 4, 650, .6, 40, 3, 20, 20, (Synergies.SORCERER, Synergies.DRAGON))
    BRAND = Champion("Brand", 4, 700, .6, 60, 3, 25, 20, (Synergies.DEMON, Synergies.ELEMENTALIST))
    CHOGATH = Champion("Chogath", 4, 1000, .6, 70, 1, 20, 20, (Synergies.BRAWLER, Synergies.VOID))
    DRAVEN = Champion("Draven", 4, 700, .75, 75, 3, 25, 20, (Synergies.IMPERIAL, Synergies.BLADEMASTER))
    GNAR = Champion("Gnar", 4, 750, .7, 50, 2, 30, 20, (Synergies.WILD, Synergies.SHAPESHIFTER, Synergies.YORDLE))
    KINDRED = Champion("Kindred", 4, 600, .65, 60, 3, 20, 20, (Synergies.PHANTOM, Synergies.RANGER))
    LEONA = Champion("Leona", 4, 750, .55, 45, 1, 100, 20, (Synergies.NOBLE, Synergies.GUARDIAN))
    SEJUANI = Champion("Sejuani", 4, 850, .55, 45, 1, 40, 25, (Synergies.KNIGHT, Synergies.GLACIAL))
    # 5 Cost
    ANIVIA = Champion("Anivia", 5, 650, .6, 40, 3, 20, 20, (Synergies.GLACIAL, Synergies.ELEMENTALIST))
    KARTHUS = Champion("Karthus", 5, 850, .65, 65, 3, 25, 20, (Synergies.PHANTOM, Synergies.SORCERER))
    KAYLE = Champion("Kayle", 5, 750, 1.1, 60, 3, 40, 20, (Synergies.KNIGHT, Synergies.NOBLE))
    MISS_FORTUNE = Champion("Miss Fortune", 5, 650, .85, 75, 3, 20, 20, (Synergies.GUNSLINGER, Synergies.PIRATE))
    SWAIN = Champion("Swain", 5, 850, .65, 65, 2, 25, 20, (Synergies.SHAPESHIFTER, Synergies.DEMON, Synergies.IMPERIAL))
    YASUO = Champion("Yasuo", 5, 700, 1, 75, 1, 35, 25, (Synergies.EXILE, Synergies.BLADEMASTER))


def get_list_length():
    return len(Champions.__members__)
