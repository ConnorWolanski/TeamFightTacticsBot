from enum import Enum


class ItemEnhancements(Enum):
    ATTACK_DAMAGE = 20
    ATTACK_SPEED = .2
    ABILITY_POWER = 20
    STARTING_MANA = 20
    ARMOR = 20
    MAGIC_RESIST = 20
    HEALTH = 200
    SPATULA = 0


def get_list_length():
    return len(ItemEnhancements.__members__)
