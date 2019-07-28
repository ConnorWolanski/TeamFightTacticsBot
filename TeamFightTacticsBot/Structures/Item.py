class Item:
    def __init__(self, name, item_1, item_2, enhancement):
        self.name = name
        self.item_1 = item_1
        self.item_2 = item_2
        self.enhancement = enhancement

    def __str__(self):
        return "<" + self.name + ">" + \
            "Item 1: " + self.item_1 + \
            "Item 2: " + self.item_2


def get_enhancements(item):
    # Some recursive function get the base stats
    enhancements_list = []
    if item.item_1 is None and item.item_2 is None:
        return item.enhancement

    enhancements_list += get_enhancements(item.item_1)
    enhancements_list += get_enhancements(item.item_2)

    return enhancements_list


def get_image(item):
    # Some function that compares the item name to the dictionary stored in Constants.py
    return None
