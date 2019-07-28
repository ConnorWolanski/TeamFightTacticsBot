from enum import Enum
from TeamFightTacticsBot.Structures.Item import Item
from TeamFightTacticsBot.Enumerators.ItemEnhancements import ItemEnhancements


class Items(Enum):
    BFSWORD = Item("BFSword", None, None, ItemEnhancements.ATTACK_DAMAGE)
    ...
    SPATULA = Item("Spatula", None, None, ItemEnhancements.SPATULA)
    ...
    FORCE_OF_NATURE = Item("ForceOfNature", SPATULA, SPATULA, None)
