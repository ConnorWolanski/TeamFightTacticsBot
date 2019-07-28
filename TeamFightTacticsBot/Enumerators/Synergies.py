from enum import Enum
from TeamFightTacticsBot.Structures.Synergy import Synergy


class Synergies(Enum):
    # name, champions, numbers, enhancement
    # Origins
    DEMON = Synergy("Demon", ("Aatrox", "Varus", "Morgana", "Swain",
                              "Elise", "Brand", "Evelynn"), (2, 4, 6))
    DRAGON = Synergy("Dragon", ("Shyvana", "Aurelion Sol"), 2)
    EXILE = Synergy("Exile", "Yasuo", 1)
    GLACIAL = Synergy("Glacial", ("Braum", "Ashe", "Sejuani", "Lissandra",
                                  "Volibear", "Anivia"), (2, 4, 6))
    IMPERIAL = Synergy("Imperial", ("Darius", "Draven", "Swain", "Katarina"), (2, 4))
    NINJA = Synergy("Ninja", ("Kennen", "Zed", "Akali", "Shen"), (1, 4))
    NOBLE = Synergy("Noble", ("Vayne", "Kayle", "Garen", "Fiora", "Lucian",
                              "Leona"), (3, 6))
    PIRATE = Synergy("Pirate", ("Graves", "Gangplank", "Twisted Fate", "Miss Fortune",
                                "Pyke"), 3)
    PHANTOM = Synergy("Phantom", ("Mordekaiser", "Kindred", "Karthus"), 2)
    ROBOT = Synergy("Robot", "Blitzcrank", 1)
    WILD = Synergy("Wild", ("Nidalee", "Warwick", "Gnar", "Rengar", "Ahri"),
                   (2, 4))
    VOID = Synergy("Void", ("Khazix", "Reksai", "Kassadin", "Chogath"), 3)
    YORDLE = Synergy("Yordle", ("Veigar", "Tristana", "Kennen", "Gnar", "Poppy",
                                "Lulu"), (3, 6))
    # Classes
    ASSASSIN = Synergy("Assassin", ("Zed", "Khazix", "Evelynn", "Akali", "Pyke",
                                    "Rengar", "Katarina"), (3, 6))
    BLADEMASTER = Synergy("Blademaster", ("Aatrox", "Fiora", "Draven", "Shen",
                                          "Gangplank", "Yasuo"), (3, 6))
    BRAWLER = Synergy("Brawler", ("Blitzcrank", "Volibear", "Reksai", "Warwick",
                                  "Chogath"), (2, 4))
    ELEMENTALIST = Synergy("Elementalist", ("Kennen", "Brand", "Lissandra", "Anivia"), 3)
    GUARDIAN = Synergy("Guardian", ("Leona", "Braum"), 2)
    GUNSLINGER = Synergy("Gunslinger", ("Miss Fortune", "Tristana", "Lucian",
                                        "Gangplank", "Graves"), (2, 4))
    KNIGHT = Synergy("Knight", ("Garen", "Kayle", "Mordekaiser", "Sejuani",
                     "Darius", "Poppy"), (2, 4, 6))
    RANGER = Synergy("Ranger", ("Kindred", "Ashe", "Vayne", "Varus"), (2, 4))
    SHAPESHIFTER = Synergy("Shapeshifter", ("Gnar", "Shyvana", "Nidalee", "Swain",
                                            "Elise"), 3)
    SORCERER = Synergy("Sorcerer", ("Kassadin", "Lulu", "Morgana", "Karthus",
                                    "Ahri", "Veigar", "Aurelion Sol"), (3, 6))