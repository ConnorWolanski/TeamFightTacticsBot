from enum import Enum
from TeamFightTacticsBot.Structures.Item import Item
from TeamFightTacticsBot.Enumerators.ItemEnhancements import ItemEnhancements


class Items(Enum):
    # Base Items
    BF_SWORD = Item("BF Sword", None, None, ItemEnhancements.ATTACK_DAMAGE)
    RECURVE_BOW = Item("Recurve Bow", None, None, ItemEnhancements.ATTACK_SPEED)
    NEEDLESSLY_LARGE_ROD = Item("Needlessly Large Rod", None, None, ItemEnhancements.ABILITY_POWER)
    TEAR_OF_THE_GODDESS = Item("Tear Of The Goddess", None, None, ItemEnhancements.STARTING_MANA)
    CHAIN_VEST = Item("Chain Vest", None, None, ItemEnhancements.ARMOR)
    NEGATRON_CLOAK = Item("Negatron Cloak", None, None, ItemEnhancements.MAGIC_RESIST)
    GIANTS_BELT = Item("Giants Belt", None, None, ItemEnhancements.HEALTH)
    SPATULA = Item("Spatula", None, None, ItemEnhancements.SPATULA)
    # BF Sword Builds
    INFINITY_EDGE = Item("Infinity Edge", BF_SWORD, BF_SWORD, None)
    SWORD_OF_THE_DIVINE = Item("Sword Of The Divine", BF_SWORD, RECURVE_BOW, None)
    HEXTECH_GUNBLADE = Item("Hextech Gunblade", BF_SWORD, NEEDLESSLY_LARGE_ROD, None)
    SPEAR_OF_SHOJIN = Item("Spear Of Shojin", BF_SWORD, TEAR_OF_THE_GODDESS, None)
    GUARDIANS_ANGEL = Item("Guardians Angel", BF_SWORD, CHAIN_VEST, None)
    THE_BLOODTHIRSTER = Item("Bloodthirster", BF_SWORD, NEGATRON_CLOAK, None)
    ZEKES_HERALD = Item("Zekes Herald", BF_SWORD, GIANTS_BELT, None)
    YOUMUUS_GHOSTBLADE = Item("Youmuus Ghostblade", BF_SWORD, SPATULA, None)
    # Recurve Builds
    RAPID_FIRECANNON = Item("Rapid Firecannon", RECURVE_BOW, RECURVE_BOW, None)
    GUINSOOS_RAGEBLADE = Item("Guinsoos Rageblade", RECURVE_BOW, NEEDLESSLY_LARGE_ROD, None)
    STATIKK_SHIV = Item("Statikk Shiv", RECURVE_BOW, TEAR_OF_THE_GODDESS, None)
    PHANTOM_DANCER = Item("Phantom Dancer", RECURVE_BOW, CHAIN_VEST, None)
    CURSED_BLADE = Item("Cursed Blade", RECURVE_BOW, NEGATRON_CLOAK, None)
    TITANIC_HYDRA = Item("Titanic Hydra", RECURVE_BOW, GIANTS_BELT, None)
    BLADE_OF_THE_RUINED_KING = Item("Blade Of The Ruined King", RECURVE_BOW, SPATULA, None)
    # Needlessly Large Rod Builds
    RABADONS_DEATHCAP = Item("Rabadons Deathcap", NEEDLESSLY_LARGE_ROD, NEEDLESSLY_LARGE_ROD, None)
    LUDENS_ECHO = Item("Ludens Echo", NEEDLESSLY_LARGE_ROD, TEAR_OF_THE_GODDESS, None)
    LOCKET_OF_THE_IRON_SOLARI = Item("Locket Of The Iron Solari", NEEDLESSLY_LARGE_ROD, CHAIN_VEST, None)
    IONIC_SPARK = Item("Ionic Spark", NEEDLESSLY_LARGE_ROD, NEGATRON_CLOAK, None)
    MORELLONOMICON = Item("Morellonomicon", NEEDLESSLY_LARGE_ROD, GIANTS_BELT, None)
    YUUMI = Item("Yuumi", NEEDLESSLY_LARGE_ROD, SPATULA, None)
    # Tear of the goddess Builds
    SERAPHS_EMBRACE = Item("Seraphs Embrace", TEAR_OF_THE_GODDESS, TEAR_OF_THE_GODDESS, None)
    FROZEN_HEART = Item("Frozen Heart", TEAR_OF_THE_GODDESS, CHAIN_VEST, None)
    HUSH = Item("Hush", TEAR_OF_THE_GODDESS, NEGATRON_CLOAK, None)
    REDEMPTION = Item("Redemption", TEAR_OF_THE_GODDESS, GIANTS_BELT, None)
    DARKIN = Item("Darkin", TEAR_OF_THE_GODDESS, SPATULA, None)
    # Chain Vest Builds
    THORNMAIL = Item("Thornmail", CHAIN_VEST, CHAIN_VEST, None)
    SWORD_BREAKER = Item("Sword Breaker", CHAIN_VEST, NEGATRON_CLOAK, None)
    RED_BUFF = Item("Red Buff", CHAIN_VEST, GIANTS_BELT, None)
    KNIGHTS_VOW = Item("Knights Vow", CHAIN_VEST, SPATULA, None)
    # Negatron Cloak Builds
    DRAGONS_CLAW = Item("Dragons Claw", NEGATRON_CLOAK, NEGATRON_CLOAK, None)
    ZEPHYR = Item("Zephyr", NEGATRON_CLOAK, GIANTS_BELT, None)
    RUNAANS_HURRICANE = Item("Runaans Hurricane", NEGATRON_CLOAK, SPATULA, None)
    # Giants Belt Builds
    WARMOGS_ARMOR = Item("Warmogs Armor", GIANTS_BELT, GIANTS_BELT, None)
    FROZEN_MALET = Item("Frozen Malet", GIANTS_BELT, SPATULA, None)
    # Spatula Builds
    FORCE_OF_NATURE = Item("Force Of Nature", SPATULA, SPATULA, None)


def get_list_length():
    return len(Items.__members__)
