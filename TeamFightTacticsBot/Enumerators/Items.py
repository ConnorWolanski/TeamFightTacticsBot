from enum import Enum
from TeamFightTacticsBot.Structures.Item import Item
from TeamFightTacticsBot.Enumerators.ItemEnhancements import ItemEnhancements


class Items(Enum):
    # Base Items
    BF_SWORD = Item("BFSword", None, None, ItemEnhancements.ATTACK_DAMAGE)
    RECURVE_BOW = Item("RecurveBow", None, None, ItemEnhancements.ATTACK_SPEED)
    NEEDLESSLY_LARGE_ROD = Item("NeedlesslyLargeRod", None, None, ItemEnhancements.ABILITY_POWER)
    TEAR_OF_THE_GODDESS = Item("TearOfTheGoddess", None, None, ItemEnhancements.STARTING_MANA)
    CHAIN_VEST = Item("ChainVest", None, None, ItemEnhancements.ARMOR)
    NEGATRON_CLOAK = Item("NegatronCloak", None, None, ItemEnhancements.MAGIC_RESIST)
    GIANTS_BELT = Item("GiantsBelt", None, None, ItemEnhancements.HEALTH)
    SPATULA = Item("Spatula", None, None, ItemEnhancements.SPATULA)
    # BF Sword Builds
    INFINITY_EDGE = Item("InfinityEdge", BF_SWORD, BF_SWORD, None)
    SWORD_OF_THE_DIVINE = Item("SwordOfTheDivine", BF_SWORD, RECURVE_BOW, None)
    HEXTECH_GUNBLADE = Item("HextechGunblade", BF_SWORD, NEEDLESSLY_LARGE_ROD, None)
    SPEAR_OF_SHOJIN = Item("SpearOfShojin", BF_SWORD, TEAR_OF_THE_GODDESS, None)
    GUARDIANS_ANGEL = Item("GuardiansAngel", BF_SWORD, CHAIN_VEST, None)
    THE_BLOODTHIRSTER = Item("Bloodthirster", BF_SWORD, NEGATRON_CLOAK, None)
    ZEKES_HERALD = Item("ZekesHerald", BF_SWORD, GIANTS_BELT, None)
    YOUMUUS_GHOSTBLADE = Item("YoumuusGhostblade", BF_SWORD, SPATULA, None)
    # Recurve Builds
    RAPID_FIRECANNON = Item("RapidFireCannon", RECURVE_BOW, RECURVE_BOW, None)
    GUINSOOS_RAGEBLADE = Item("GuinsoosRageblade", RECURVE_BOW, NEEDLESSLY_LARGE_ROD, None)
    STATIKK_SHIV = Item("StatikkShiv", RECURVE_BOW, TEAR_OF_THE_GODDESS, None)
    PHANTOM_DANCER = Item("PhantomDancer", RECURVE_BOW, CHAIN_VEST, None)
    CURSED_BLADE = Item("CursedBlade", RECURVE_BOW, NEGATRON_CLOAK, None)
    TITANIC_HYDRA = Item("TitanicHydra", RECURVE_BOW, GIANTS_BELT, None)
    BLADE_OF_THE_RUINED_KING = Item("BladeOfTheRuinedKing", RECURVE_BOW, SPATULA, None)
    # Needlessly Large Rod Builds
    RABADONS_DEATHCAP = Item("RabadonsDeathcap", NEEDLESSLY_LARGE_ROD, NEEDLESSLY_LARGE_ROD, None)
    LUDENS_ECHO = Item("LudensEcho", NEEDLESSLY_LARGE_ROD, TEAR_OF_THE_GODDESS, None)
    LOCKET_OF_THE_IRON_SOLARI = Item("LocketOfTheIronSolari", NEEDLESSLY_LARGE_ROD, CHAIN_VEST, None)
    IONIC_SPARK = Item("IonicSpark", NEEDLESSLY_LARGE_ROD, NEGATRON_CLOAK, None)
    MORELLONOMICON = Item("Morellonomicon", NEEDLESSLY_LARGE_ROD, GIANTS_BELT, None)
    YUUMI = Item("Yuumi", NEEDLESSLY_LARGE_ROD, SPATULA, None)
    # Tear of the goddess Builds
    SERAPHS_EMBRACE = Item("SeraphsEmbrace", TEAR_OF_THE_GODDESS, TEAR_OF_THE_GODDESS, None)
    FROZEN_HEART = Item("FrozenHeart", TEAR_OF_THE_GODDESS, CHAIN_VEST, None)
    HUSH = Item("Hush", TEAR_OF_THE_GODDESS, NEGATRON_CLOAK, None)
    REDEMPTION = Item("Redemption", TEAR_OF_THE_GODDESS, GIANTS_BELT, None)
    DARKIN = Item("Darkin", TEAR_OF_THE_GODDESS, SPATULA, None)
    # Chain Vest Builds
    THORNMAIL = Item("Thornmail", CHAIN_VEST, CHAIN_VEST, None)
    SWORD_BREAKER = Item("SwordBreaker", CHAIN_VEST, NEGATRON_CLOAK, None)
    RED_BUFF = Item("RedBuff", CHAIN_VEST, GIANTS_BELT, None)
    KNIGHTS_VOW = Item("KnightsVow", CHAIN_VEST, SPATULA, None)
    # Negatron Cloak Builds
    DRAGONS_CLAW = Item("DragonsClaw", NEGATRON_CLOAK, NEGATRON_CLOAK, None)
    ZEPHYR = Item("Zephyr", NEGATRON_CLOAK, GIANTS_BELT, None)
    RUNAANS_HURRICANE = Item("RunaansHurricane", NEGATRON_CLOAK, SPATULA, None)
    # Giants Belt Builds
    WARMOGS_ARMOR = Item("WarmogsArmor", GIANTS_BELT, GIANTS_BELT, None)
    FROZEN_MALET = Item("FrozenMalet", GIANTS_BELT, SPATULA, None)
    # Spatula Builds
    FORCE_OF_NATURE = Item("ForceOfNature", SPATULA, SPATULA, None)


def get_list_length():
    return len(Items.__members__)
