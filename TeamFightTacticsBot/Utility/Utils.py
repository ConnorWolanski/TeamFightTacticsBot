# Python downloaded libraries
import time
import pytesseract as get_text
import pyautogui as auto_gui
import pyscreenshot as image_grab
from PIL import Image, ImageOps
import math
import copy

# Objects
from TeamFightTacticsBot.Structures.Point import Point

# Constants
from TeamFightTacticsBot.Enumerators.Champions import Champions
from TeamFightTacticsBot.Enumerators.Synergies import Synergies
from TeamFightTacticsBot.Utility.Constants import VARIANCE_THRESHOLD, PERCENTAGE_ACCURACY, USER_32

# Global Variable imports
import TeamFightTacticsBot.Utility.Constants as Constants
import TeamFightTacticsBot.Utility.GameConstants as GameConstants
import TeamFightTacticsBot.Utility.ConfigFileLoader as ConfigFileLoader


# puts one point into level
def level_up():
    auto_gui.press("f")
    GameConstants.PLAYER_XP += 4


# rerolls the shop for the player
def reroll_shop():
    auto_gui.press("d")


# hovers over a champion slot and then sells them
def sell_champion(location_slot_tuple):
    if location_slot_tuple[0] == "bench":
        auto_gui.moveTo(GameConstants.BENCH_SLOT_CLICKABLE_LOCATIONS[location_slot_tuple[1]].x,
                        GameConstants.BENCH_SLOT_CLICKABLE_LOCATIONS[location_slot_tuple[1]].y)
    else:
        auto_gui.moveTo(GameConstants.BOARD_SLOT_CLICKABLE_LOCATIONS[location_slot_tuple[1]].x,
                        GameConstants.BOARD_SLOT_CLICKABLE_LOCATIONS[location_slot_tuple[1]].y)
    auto_gui.press("e")


# benches a champion you have on your board as long as your bench isn't full
def bench_champion(board_slot):
    if is_bench_full():
        return False
    else:
        auto_gui.moveTo(GameConstants.BOARD_SLOT_CLICKABLE_LOCATIONS[board_slot].x,
                        GameConstants.BOARD_SLOT_CLICKABLE_LOCATIONS[board_slot].y)
        auto_gui.press("w")
        return True


# Takes in a tuple of whether they are on bench or board and swaps them with the second same tuple
def swap_champion_location(location_slot_tuple_1, location_slot_tuple_2):
    if location_slot_tuple_1[0] == "bench":
        if location_slot_tuple_2[0] == "bench":
            click_and_drag(GameConstants.BENCH_SLOT_CLICKABLE_LOCATIONS[location_slot_tuple_1[1]],
                           GameConstants.BENCH_SLOT_CLICKABLE_LOCATIONS[location_slot_tuple_1[1]])
        else:
            click_and_drag(GameConstants.BENCH_SLOT_CLICKABLE_LOCATIONS[location_slot_tuple_1[1]],
                           GameConstants.BOARD_SLOT_CLICKABLE_LOCATIONS[location_slot_tuple_1[1]])
    else:
        if location_slot_tuple_2[0] == "bench":
            click_and_drag(GameConstants.BOARD_SLOT_CLICKABLE_LOCATIONS[location_slot_tuple_1[1]],
                           GameConstants.BENCH_SLOT_CLICKABLE_LOCATIONS[location_slot_tuple_1[1]])
        else:
            click_and_drag(GameConstants.BOARD_SLOT_CLICKABLE_LOCATIONS[location_slot_tuple_1[1]],
                           GameConstants.BOARD_SLOT_CLICKABLE_LOCATIONS[location_slot_tuple_1[1]])


# returns if bench is full
def is_bench_full():
    return get_empty_bench_count() == 0


# gets the stage the player is currently on
def get_stage_name():
    for stage in ConfigFileLoader.STAGE_LEVEL_ASSOCIATIONS:
        if GameConstants.PLAYER_LEVEL in ConfigFileLoader.STAGE_LEVEL_ASSOCIATIONS[stage]:
            return stage.upper()


# formates the name_threshold of a synergy to access in the rating dictionary
def get_boost_name(boost_name, level):
    returned = ""

    for synergy in Synergies:
        if boost_name.lower() != synergy.value.name.lower():
            continue

        thresholds = synergy.value.boost_character_thresholds
        if isinstance(thresholds, int):
            # Just one level
            returned = boost_name + "_" + str(thresholds)
        else:
            if level <= 0:
                returned = boost_name + "_" + str(thresholds[0])
            else:
                # Multiple levels
                max_levels = len(thresholds)
                if level > max_levels:
                    returned = boost_name + "_" + str(thresholds[max_levels - 1])
                else:
                    returned = boost_name + "_" + str(thresholds[level - 1])

    return returned.lower()


# Finds and returns you players pixel location at the start of a carousel
def find_carousel_starting_location(tested):
    tested = tested.crop((250, 175, 1600, 1080))
    return find_pixels_of_interest_for_starting_circle(tested)


# Roughly gets the circle you start at in carousel
def find_pixels_of_interest_for_starting_circle(tested_area):
    to_be_averaged = find_points_of_interest_by_color(tested_area, (254, 254, 145), 50)

    x, y = 0, 0
    for point in to_be_averaged:
        x += point.x
        y += point.y

    x /= len(to_be_averaged)
    y /= len(to_be_averaged)

    return Point(int(x), int(y))


# Returns a list of item box pixel locations on the ground
def get_item_box_location(tested):
    tested = tested.crop((300, 180, 1550, 800))
    # Not sure if this method will work for item boxes
    # return compare_images_and_get_location_strictly(tested, item_box, .99)
    return find_pixels_of_interest_for_item_boxes(tested)


# Gets a list of pixel locations that are possibly item boxes to check
def find_pixels_of_interest_for_item_boxes(tested_area):
    return find_points_of_interest_by_color(tested_area, (162, 254, 254), 25)


# This takes a color and returns a list of points in which that color is present in an area
def find_points_of_interest_by_color(tested_area, master_color_tuple, cooldown_radius):
    interested_locations = []
    # 162, 254, 254
    width, height = tested_area.size
    tested_pixels = tested_area.load()
    data = []

    for y in range(height):
        for x in range(width):
            if not is_a_close_color(tested_pixels[x, y], master_color_tuple):
                data.append((0, 0, 0))
            else:
                data.append((tested_pixels[x, y][0], tested_pixels[x, y][1], tested_pixels[x, y][2]))

    image = Image.new('RGB', (width, height))
    image.putdata(data)

    image_pixels = image.load()
    width, height = image.size

    for y in range(height):
        for x in range(width):
            # Stay away from out of bounds errors
            if x == 0 or x == width-1 or y == 0 or y == height-1:
                continue

            # Check if close to already existing POI
            if is_in_radius(Point(x, y), interested_locations, cooldown_radius):
                continue

            if not pixel_is_black(image_pixels[x, y]):
                count = 0
                surrounding = [image_pixels[x, y-1], image_pixels[x-1, y],
                               image_pixels[x+1, y], image_pixels[x, y+1]]
                for surround in surrounding:
                    if is_a_close_color(surround, master_color_tuple):
                        count += 1

                if count > 2:
                    interested_locations.append(Point(x, y))

    return interested_locations


# Checks whether two points are within a certain range of eachother
def is_in_radius(point, point_list, cooldown_radius):
    for p in point_list:
        distance = math.sqrt(math.pow((p.x - point.x), 2) + math.pow(p.y - point.y, 2))
        if distance < cooldown_radius:
            return True

    return False


# Checks whether a pixel is black or not
def pixel_is_black(pixel):
    return pixel == (0, 0, 0)


# Checks if a color is within a certain acceptance(5) of a specific color
def is_a_close_color(pixel, master_tuple):
    # For item box: 162, 254, 254

    acceptance = 5

    # Red Component
    if abs(pixel[0] - master_tuple[0]) > acceptance:
        return False

    # Green Component
    if abs(pixel[1] - master_tuple[1]) > acceptance:
        return False

    # Blue Component
    if abs(pixel[2] - master_tuple[2]) > acceptance:
        return False

    return True


# Searches the carousel and returns all available items
def get_items_carousel(screen):
    carousel = screen.crop((300, 195, 1500, 850))
    locations = find_health_bar_locations(carousel, GameConstants.CAROUSEL_CHAMPION_COUNT)
    items = []

    for loc in locations:
        temp_image = carousel.crop((loc[0], loc[1] + 12, loc[0] + 23, loc[1] + 35))
        items.append(image_to_item(temp_image))

    return items


# Takes an image and determines what item it represents and returns the item
def image_to_item(image):
    count = 0
    while count < len(Constants.ITEM_IMAGE_LIST):
        if compare_images_strictly(image, Constants.ITEM_IMAGE_LIST[count], .90):
            break
        count += 1
    return get_item_from_list_index(count)


# Gets the item from its image index
def get_item_from_list_index(count):
    if count < len(Constants.ITEM_NAMES_LIST):
        return Constants.ITEM_NAMES_LIST[count]
    else:
        return 'Could not parse item'


# This determines if a certain location is a character healthbar in carousel
def check_health_bar_location(image, x, y):
    # checks only if one star need to add or for two and three stars later and for enemy bar
    im = image.load()
    if compare_pixels_strictly(im[x, y], (162, 112, 55), .95):
        if compare_pixels_strictly(im[x+1, y], (8, 20, 33), .95):
            if compare_pixels_strictly(im[x+2, y], (2, 18, 35), .95):
                if compare_pixels_strictly(im[x+3, y], (81, 162, 230), .95):
                    if compare_pixels_strictly(im[x, y-1], (0, 20, 33), .95):
                        return True
    return False


# Finds all locations of champion health bars within the carousel
def find_health_bar_locations(image, number_of_bars):
    y_location = 0
    count = 0
    locations = []

    while count < number_of_bars and y_location < image.size[1]:
        for x_location in range(image.size[0]):
            if check_health_bar_location(image, x_location, y_location):
                locations.append((x_location, y_location))
                count += 1
        y_location += 1

    return locations


# This buys the champions from the shop based on what is best for that round and with what you have
def buy_champions(screen):
    gold = get_gold(screen)
    champion_list = shop_to_champion(screen)
    owned_champions = get_champions_owned()
    champion_and_index_in_shop = []
    total_cost = 0

    index = 1
    for champion in champion_list:
        champion_and_index_in_shop.append((champion, index))
        total_cost += champion.cost
        index += 1
    print("Owned: ")
    for champion in owned_champions:
        print(str(champion.name))

    # print("Gold: " + str(gold))
    # First three minion rounds
    if GameConstants.CURRENT_STAGE is 1:
        # for early games buys all 5 if can afford and has the slots
        if total_cost <= gold and get_empty_bench_count() >= 5:
            to_be_bought = [1, 2, 3, 4, 5]
            if buy_list(to_be_bought):
                for shop_index in to_be_bought:
                    add_champion_to_board(champion_list[shop_index - 1], owned_champions)
                    owned_champions = get_champions_owned()
        else:
            # First Prioritizes champions then puts duplicates in the front
            champion_priority = prioritize_champions(champion_list, owned_champions)
            champion_priority.sort(key=lambda x: x[1], reverse=True)
            champion_priority = check_duplicates(champion_priority, owned_champions)

            break_out = False
            for champion_and_rating_tuple in champion_priority:
                for champion_and_index_tuple in champion_and_index_in_shop:
                    if (champion_and_index_tuple[0] is champion_and_rating_tuple[0]) and \
                            gold >= champion_and_index_tuple[0].cost:
                        if is_bench_full():
                            break_out = True
                            break

                        if buy(champion_and_index_tuple[1]):
                            champion_and_index_in_shop.remove(champion_and_index_tuple)
                            gold = gold - champion_and_index_tuple[0].cost
                            add_champion_to_board(champion_and_index_tuple[0], owned_champions)
                            owned_champions = get_champions_owned()
                        break

                if gold is 0 or break_out:
                    break

    # First rounds of going against people
    # elif GameConstants.CURRENT_STAGE is 2:

    # rounds after Golems
    # elif GameConstants.CURRENT_STAGE is 3:

    # rounds after Wolves
    # elif GameConstants.CURRENT_STAGE is 4:

    # rounds after Raptors
    # else


# Adds a champion to your board either from carousel or shop and combines if nessecary
def add_champion_to_board(champion, owned_champions):

    if (champion not in owned_champions) or owned_champions.count(champion) < 2:
        GameConstants.PLAYER_BOARD.bench_slots[get_first_empty_bench_slot()] = copy.copy(champion)
    elif owned_champions.count(champion) is 2:
        combine_champions_on_board(champion)
        temp_copy = copy.copy(champion)
        temp_copy.level += 1
        owned_champions_after_combined = get_champions_owned()
        # if two 2 stars are already owns
        if owned_champions_after_combined.count(temp_copy) is 3:
            combine_champions_on_board(temp_copy)
    else:
        return False
    return True


# Combines a champion into its first spot and levels it up
def combine_champions_on_board(champion):
    print("Combining " + str(champion))
    temp_champion = copy.copy(champion)
    temp_champion.level += 1
    first_of_champion_index = get_first_of_champion(champion)
    if isinstance(first_of_champion_index, int):
        GameConstants.PLAYER_BOARD.bench_slots[first_of_champion_index] = temp_champion
        remove_champion_from_board(champion)
    else:
        GameConstants.PLAYER_BOARD.board_slots[first_of_champion_index[0]][first_of_champion_index[1]] = \
            temp_champion
        remove_champion_from_board(champion)


# Removes all instances of a champion from your board
def remove_champion_from_board(champion):
    row_index = 0
    for row in GameConstants.PLAYER_BOARD.board_slots:
        col_index = 0
        for col in row:
            if col is not None:
                if col == champion:
                    GameConstants.PLAYER_BOARD.board_slots[row_index][col_index] = None
            col_index += 1
        row_index += 1
    bench_index = 0
    for slot in GameConstants.PLAYER_BOARD.bench_slots:
        if slot is not None:
            if slot == champion:
                GameConstants.PLAYER_BOARD.bench_slots[bench_index] = None
        bench_index += 1
    return True


# Returns the index first instance of a champion on your board
def get_first_of_champion(champion):
    row_index = 0
    for row in GameConstants.PLAYER_BOARD.board_slots:
        col_index = 0
        for col in row:
            if col is not None:
                if col == champion:
                    return tuple((row_index, col_index))
            col_index += 1
        row_index += 1
    bench_index = 0
    for slot in GameConstants.PLAYER_BOARD.bench_slots:
        if slot is not None:
            if slot == champion:
                return bench_index
        bench_index += 1
    return False


# This reorders a list of champions based on their priority to buy
def prioritize_champions(champions, owned_champions):
    synergies = []
    all_champions = []
    all_champions.extend(owned_champions)
    all_champions.extend(champions)

    for champion in remove_duplicates(all_champions):
        if champion is None:
            continue

        for synergy in champion.synergies:
            synergies.append(synergy.value)

    ordered_synergies = order_synergies(synergies)
    champion_and_rating_tuples = []

    for champion in champions:
        champion_and_rating_tuples.append((champion, get_champion_buy_rating(champion, ordered_synergies)))

    return champion_and_rating_tuples


# returns a champions rating in which you want to buy it based on its synergies and its own rating
def get_champion_buy_rating(champion, ordered_synergies):
    index = 0
    total = 0

    for synergies in champion.synergies:
        for syn in ordered_synergies:
            if synergies.value is syn[1]:
                total += syn[0]
                index += 1

    if index is not 0:
        return total/index
    else:
        return 0


# This orders a list of synergies based on their ratings
def order_synergies(synergies):
    synergy_rating_pair = []

    for synergy in synergies:
        temp_pair = (ConfigFileLoader.SYNERGY_LEARNED_RATINGS[get_stage_name().lower()].
                     get(get_boost_name(synergy.name, 1)).rating, synergy)

        if temp_pair not in synergy_rating_pair:
            synergy_rating_pair.append(temp_pair)
        else:
            list_location = synergy_rating_pair.index(temp_pair)

            if isinstance(synergy_rating_pair[list_location][1].boost_character_thresholds, int):
                threshold = synergy_rating_pair[list_location][1].boost_character_thresholds
            else:
                threshold = synergy_rating_pair[list_location][1].boost_character_thresholds[0]

            synergy_rating_pair[list_location] = (int((synergy_rating_pair[list_location][0] +
                                                       (1/threshold*3))), synergy)

    synergy_rating_pair.sort(key=lambda x: x[0], reverse=True)
    return synergy_rating_pair


# This checks a list of champions and puts all duplicates to the front
def check_duplicates(champions, owned_champions):
    list_duplicates = []
    not_duplicated = []

    for champion in champions:
        if champion[0] in owned_champions:
            list_duplicates.append(champion)
            continue

        if champions.count(champion) >= 2:
            list_duplicates.append(champion)
            continue

        not_duplicated.append(champion)

    list_duplicates.extend(not_duplicated)
    return list_duplicates


# This returns a list in which the duplicates are made to be only one
def remove_duplicates(any_list):
    list_without_duplicates = []

    for elements in any_list:
        if elements not in list_without_duplicates:
            list_without_duplicates.append(elements)

    return list_without_duplicates


# This buys a list of slots from the shop and returns true if it was done
def buy_list(to_be_bought):
    for slot in to_be_bought:
        if not buy(slot):
            return False

    return True


# This buysa a single slot from the list and returns true if it was done
def buy(slot):
    if slot is 1:
        click(GameConstants.SHOP_SLOT_CLICKABLE_LOCATIONS[0])
    elif slot is 2:
        click(GameConstants.SHOP_SLOT_CLICKABLE_LOCATIONS[1])
    elif slot is 3:
        click(GameConstants.SHOP_SLOT_CLICKABLE_LOCATIONS[2])
    elif slot is 4:
        click(GameConstants.SHOP_SLOT_CLICKABLE_LOCATIONS[3])
    elif slot is 5:
        click(GameConstants.SHOP_SLOT_CLICKABLE_LOCATIONS[4])
    else:
        print("Invalid slot")
        return False
    # Might have to be changed later to slow the bot inbetween buying MULTIPLE champions
    time.sleep(.1)
    print("Bought slot " + str(slot))
    return True


# This returns the index of the first empty slot on your bench
def get_first_empty_bench_slot():
    index = 0
    for slot in GameConstants.PLAYER_BOARD.bench_slots:
        if slot is None:
            return index
        index += 1
    return False


# This returns how many empty spots you have on your bench
def get_empty_bench_count():
    occupied = 0
    for slot in GameConstants.PLAYER_BOARD.bench_slots:
        if slot is not None:
            occupied += 1
    return GameConstants.BENCH_SLOTS - occupied


# This returns a list of champions that are on your board and bench
def get_champions_owned():
    champions = []

    for row in GameConstants.PLAYER_BOARD.board_slots:
        for col in row:
            if col is None:
                continue
            else:
                champions.append(col)

    for slot in GameConstants.PLAYER_BOARD.bench_slots:
        if slot is None:
            continue
        else:
            champions.append(slot)

    return champions


# This crops the slots from the shop in order to be checked
def crop_shop(screen):
    return [screen.crop((479, 927, 674, 1073)),
            screen.crop((680, 927, 875, 1073)),
            screen.crop((881, 927, 1076, 1073)),
            screen.crop((1083, 927, 1278, 1073)),
            screen.crop((1284, 927, 1479, 1073))]


# This takes the screen and crops the shop and returns a list of champions in the shop
def shop_to_champion(screen):
    champion_slots = []
    shop_slots = crop_shop(screen)
    for slot in shop_slots:
        value = image_to_champion(slot)
        champion_slots.append(value)
    return champion_slots


# This takes a picture of a champion and returns what champion enum from the shop images it matches
def image_to_champion(champion_image):
    # Loop through CHARACTER_IMAGE_LIST until accuracy reaches > 90%
    champion_image_pixels = champion_image.load()
    cost = get_cost(champion_image_pixels[170, 140])
    index_start = search_by_cost(cost)
    is_found = False
    while (not is_found) and (index_start < len(Constants.CHARACTER_IMAGE_LIST)):
        is_found = compare_images_exact(champion_image, Constants.CHARACTER_IMAGE_LIST[index_start])
        if is_found:
            break
        index_start += 1

    if is_found:
        return get_champion_from_list_index(index_start)
    else:
        return None


# This returns the cost of a champion in the shop to know what images to seacrh
def get_cost(pixel):
    if pixel == Constants.COST_CARD_BORDER_COLOR[0]:
        return 1
    if pixel == Constants.COST_CARD_BORDER_COLOR[1]:
        return 2
    if pixel == Constants.COST_CARD_BORDER_COLOR[2]:
        return 3
    if pixel == Constants.COST_CARD_BORDER_COLOR[3]:
        return 4
    if pixel == Constants.COST_CARD_BORDER_COLOR[4]:
        return 5


# This returns the index at which the images of a certain champion cost start
def search_by_cost(cost):
    if cost is 1:
        return Constants.CHARACTER_TIER_INDEXES[0]
    elif cost is 2:
        return Constants.CHARACTER_TIER_INDEXES[1]
    elif cost is 3:
        return Constants.CHARACTER_TIER_INDEXES[2]
    elif cost is 4:
        return Constants.CHARACTER_TIER_INDEXES[3]
    elif cost is 5:
        return Constants.CHARACTER_TIER_INDEXES[4]
    return 0


# Returns a champion enum from a specific index in the images
def get_champion_from_list_index(index):
    list_of_champion_enums = []
    for champ in Champions:
        list_of_champion_enums.append(champ)

    return list_of_champion_enums[index].value


# This reads your gold from your screen and returns it
def get_gold(screen):
    gold_image = screen.crop((868, 880, 910, 913))
    gold = int_from_image(gold_image)
    return gold


# This checks a screenshot and returns whatever place you are currently in
def check_place(screen):
    place = screen.load()
    if compare_pixels_strictly(place[1770, 226], (145, 109, 49), .95):
        return 1
    elif compare_pixels_strictly(place[1770, 300], (145, 109, 49), .95):
        return 2
    elif compare_pixels_strictly(place[1770, 372], (145, 109, 49), .95):
        return 3
    elif compare_pixels_strictly(place[1770, 445], (145, 109, 49), .95):
        return 4
    elif compare_pixels_strictly(place[1770, 518], (145, 109, 49), .95):
        return 5
    elif compare_pixels_strictly(place[1770, 591], (145, 109, 49), .95):
        return 6
    elif compare_pixels_strictly(place[1770, 664], (145, 109, 49), .95):
        return 7
    elif compare_pixels_strictly(place[1770, 737], (145, 109, 49), .95):
        return 8
    else:
        return 8


# This returns a list of all the players healths based on what place you are in
def get_player_healths(screen, place):
    healths = []
    # if you are in 1st
    if place is 1:
        healths.append(safe_get_health(100, screen.crop((1785, 215, 1827, 240))))
        healths.append(safe_get_health(healths[0], screen.crop((1825, 303, 1850, 319))))
        healths.append(safe_get_health(healths[1], screen.crop((1825, 376, 1850, 392))))
        healths.append(safe_get_health(healths[2], screen.crop((1825, 448, 1850, 464))))
        healths.append(safe_get_health(healths[3], screen.crop((1825, 519, 1850, 537))))
        healths.append(safe_get_health(healths[4], screen.crop((1825, 591, 1850, 609))))
        healths.append(safe_get_health(healths[5], screen.crop((1825, 664, 1850, 682))))
        healths.append(safe_get_health(healths[6], screen.crop((1825, 737, 1850, 755))))
    # if you are in 2nd
    elif place is 2:
        healths.append(safe_get_health(100, screen.crop((1825, 205, 1850, 223))))
        healths.append(safe_get_health(healths[0], screen.crop((1785, 285, 1827, 310))))
        healths.append(safe_get_health(healths[1], screen.crop((1825, 373, 1850, 391))))
        healths.append(safe_get_health(healths[2], screen.crop((1825, 446, 1850, 464))))
        healths.append(safe_get_health(healths[3], screen.crop((1825, 519, 1850, 537))))
        healths.append(safe_get_health(healths[4], screen.crop((1825, 591, 1850, 609))))
        healths.append(safe_get_health(healths[5], screen.crop((1825, 664, 1850, 682))))
        healths.append(safe_get_health(healths[6], screen.crop((1825, 737, 1850, 755))))
    # if you are in 3rd
    elif place is 3:
        healths.append(safe_get_health(100, screen.crop((1825, 205, 1850, 223))))
        healths.append(safe_get_health(healths[0], screen.crop((1825, 278, 1850, 296))))
        healths.append(safe_get_health(healths[1], screen.crop((1785, 359, 1827, 384))))
        healths.append(safe_get_health(healths[2], screen.crop((1825, 446, 1850, 464))))
        healths.append(safe_get_health(healths[3], screen.crop((1825, 519, 1850, 537))))
        healths.append(safe_get_health(healths[4], screen.crop((1825, 591, 1850, 609))))
        healths.append(safe_get_health(healths[5], screen.crop((1825, 664, 1850, 682))))
        healths.append(safe_get_health(healths[6], screen.crop((1825, 737, 1850, 755))))
    # if you are in 4th
    elif place is 4:
        healths.append(safe_get_health(100, screen.crop((1825, 205, 1850, 223))))
        healths.append(safe_get_health(healths[0], screen.crop((1825, 278, 1850, 296))))
        healths.append(safe_get_health(healths[1], screen.crop((1825, 351, 1850, 369))))
        healths.append(safe_get_health(healths[2], screen.crop((1785, 432, 1827, 457))))
        healths.append(safe_get_health(healths[3], screen.crop((1825, 519, 1850, 537))))
        healths.append(safe_get_health(healths[4], screen.crop((1825, 591, 1850, 609))))
        healths.append(safe_get_health(healths[5], screen.crop((1825, 664, 1850, 682))))
        healths.append(safe_get_health(healths[6], screen.crop((1825, 737, 1850, 755))))
    # if you are in 5th
    elif place is 5:
        healths.append(safe_get_health(100, screen.crop((1825, 205, 1850, 223))))
        healths.append(safe_get_health(healths[0], screen.crop((1825, 278, 1850, 296))))
        healths.append(safe_get_health(healths[1], screen.crop((1825, 351, 1850, 369))))
        healths.append(safe_get_health(healths[2], screen.crop((1825, 424, 1850, 442))))
        healths.append(safe_get_health(healths[3], screen.crop((1785, 505, 1827, 530))))
        healths.append(safe_get_health(healths[4], screen.crop((1825, 591, 1850, 609))))
        healths.append(safe_get_health(healths[5], screen.crop((1825, 664, 1850, 682))))
        healths.append(safe_get_health(healths[6], screen.crop((1825, 737, 1850, 755))))
    # if you are in 6th
    elif place is 6:
        healths.append(safe_get_health(100, screen.crop((1825, 205, 1850, 223))))
        healths.append(safe_get_health(healths[0], screen.crop((1825, 278, 1850, 296))))
        healths.append(safe_get_health(healths[1], screen.crop((1825, 351, 1850, 369))))
        healths.append(safe_get_health(healths[2], screen.crop((1825, 424, 1850, 442))))
        healths.append(safe_get_health(healths[3], screen.crop((1825, 497, 1850, 515))))
        healths.append(safe_get_health(healths[4], screen.crop((1785, 578, 1827, 603))))
        healths.append(safe_get_health(healths[5], screen.crop((1825, 664, 1850, 682))))
        healths.append(safe_get_health(healths[6], screen.crop((1825, 737, 1850, 755))))
    # if you are in 7th
    elif place is 7:
        healths.append(safe_get_health(100, screen.crop((1825, 205, 1850, 223))))
        healths.append(safe_get_health(healths[0], screen.crop((1825, 278, 1850, 296))))
        healths.append(safe_get_health(healths[1], screen.crop((1825, 351, 1850, 369))))
        healths.append(safe_get_health(healths[2], screen.crop((1825, 424, 1850, 442))))
        healths.append(safe_get_health(healths[3], screen.crop((1825, 497, 1850, 515))))
        healths.append(safe_get_health(healths[4], screen.crop((1825, 570, 1850, 588))))
        healths.append(safe_get_health(healths[5], screen.crop((1785, 651, 1827, 676))))
        healths.append(safe_get_health(healths[6], screen.crop((1825, 737, 1850, 755))))
    # if you are in 8th
    elif place is 8:
        healths.append(safe_get_health(100, screen.crop((1825, 205, 1850, 223))))
        healths.append(safe_get_health(healths[0], screen.crop((1825, 278, 1850, 296))))
        healths.append(safe_get_health(healths[1], screen.crop((1825, 351, 1850, 369))))
        healths.append(safe_get_health(healths[2], screen.crop((1825, 424, 1850, 442))))
        healths.append(safe_get_health(healths[3], screen.crop((1825, 497, 1850, 515))))
        healths.append(safe_get_health(healths[4], screen.crop((1825, 570, 1850, 588))))
        healths.append(safe_get_health(healths[5], screen.crop((1825, 643, 1850, 661))))
        healths.append(safe_get_health(healths[6], screen.crop((1785, 724, 1827, 749))))

    return healths


# This gets an int from an image and returns it for health
def safe_get_health(fallback, image):
    """
    health = int_from_image(image)
    if health == -1:
    print("set  ")
    health = fallback
    return int(health)"""
    return int_from_image(image)


# This gets all of the players names depending on what place you are in and returns a list of them
def get_player_names(screen, place):
    players = []
    # if you are in 1st
    if place is 1:
        players.append("Me")
        players.append(string_from_image(screen.crop((1712, 303, 1815, 319))))
        players.append(string_from_image(screen.crop((1712, 376, 1815, 392))))
        players.append(string_from_image(screen.crop((1712, 448, 1815, 464))))
        players.append(string_from_image(screen.crop((1712, 519, 1815, 537))))
        players.append(string_from_image(screen.crop((1712, 591, 1815, 609))))
        players.append(string_from_image(screen.crop((1712, 664, 1815, 682))))
        players.append(string_from_image(screen.crop((1712, 737, 1815, 755))))
    # if you are in 2nd
    elif place is 2:
        players.append(string_from_image(screen.crop((1712, 205, 1815, 223))))
        players.append("Me")
        players.append(string_from_image(screen.crop((1712, 373, 1815, 391))))
        players.append(string_from_image(screen.crop((1712, 446, 1815, 464))))
        players.append(string_from_image(screen.crop((1712, 519, 1815, 537))))
        players.append(string_from_image(screen.crop((1712, 591, 1815, 609))))
        players.append(string_from_image(screen.crop((1712, 664, 1815, 682))))
        players.append(string_from_image(screen.crop((1712, 737, 1815, 755))))
    # if you are in 3rd
    elif place is 3:
        players.append(string_from_image(screen.crop((1712, 205, 1815, 223))))
        players.append(string_from_image(screen.crop((1712, 278, 1815, 296))))
        players.append("Me")
        players.append(string_from_image(screen.crop((1712, 446, 1815, 464))))
        players.append(string_from_image(screen.crop((1712, 519, 1815, 537))))
        players.append(string_from_image(screen.crop((1712, 591, 1815, 609))))
        players.append(string_from_image(screen.crop((1712, 664, 1815, 682))))
        players.append(string_from_image(screen.crop((1712, 737, 1815, 755))))
    # if you are in 4th
    elif place is 4:
        players.append(string_from_image(screen.crop((1712, 205, 1815, 223))))
        players.append(string_from_image(screen.crop((1712, 278, 1815, 296))))
        players.append(string_from_image(screen.crop((1712, 351, 1815, 369))))
        players.append("Me")
        players.append(string_from_image(screen.crop((1712, 519, 1815, 537))))
        players.append(string_from_image(screen.crop((1712, 591, 1815, 609))))
        players.append(string_from_image(screen.crop((1712, 664, 1815, 682))))
        players.append(string_from_image(screen.crop((1712, 737, 1815, 755))))
    # if you are in 5th
    elif place is 5:
        players.append(string_from_image(screen.crop((1712, 205, 1815, 223))))
        players.append(string_from_image(screen.crop((1712, 278, 1815, 296))))
        players.append(string_from_image(screen.crop((1712, 351, 1815, 369))))
        players.append(string_from_image(screen.crop((1712, 424, 1815, 442))))
        players.append("Me")
        players.append(string_from_image(screen.crop((1712, 591, 1815, 609))))
        players.append(string_from_image(screen.crop((1712, 664, 1815, 682))))
        players.append(string_from_image(screen.crop((1712, 737, 1815, 755))))
    # if you are in 6th
    elif place is 6:
        players.append(string_from_image(screen.crop((1712, 205, 1815, 223))))
        players.append(string_from_image(screen.crop((1712, 278, 1815, 296))))
        players.append(string_from_image(screen.crop((1712, 351, 1815, 369))))
        players.append(string_from_image(screen.crop((1712, 424, 1815, 442))))
        players.append(string_from_image(screen.crop((1712, 497, 1815, 515))))
        players.append("Me")
        players.append(string_from_image(screen.crop((1712, 664, 1815, 682))))
        players.append(string_from_image(screen.crop((1712, 737, 1815, 755))))
    # if you are in 7th
    elif place is 7:
        players.append(string_from_image(screen.crop((1712, 205, 1815, 223))))
        players.append(string_from_image(screen.crop((1712, 278, 1815, 296))))
        players.append(string_from_image(screen.crop((1712, 351, 1815, 369))))
        players.append(string_from_image(screen.crop((1712, 424, 1815, 442))))
        players.append(string_from_image(screen.crop((1712, 497, 1815, 515))))
        players.append(string_from_image(screen.crop((1712, 570, 1815, 588))))
        players.append("Me")
        players.append(string_from_image(screen.crop((1712, 737, 1815, 755))))
    # if you are in 8th
    elif place is 8:
        players.append(string_from_image(screen.crop((1712, 205, 1815, 223))))
        players.append(string_from_image(screen.crop((1712, 278, 1815, 296))))
        players.append(string_from_image(screen.crop((1712, 351, 1815, 369))))
        players.append(string_from_image(screen.crop((1712, 424, 1815, 442))))
        players.append(string_from_image(screen.crop((1712, 497, 1815, 515))))
        players.append(string_from_image(screen.crop((1712, 570, 1815, 588))))
        players.append(string_from_image(screen.crop((1712, 643, 1815, 661))))
        players.append("Me")

    return players


# This takes an image and parses and returns a string from it
def string_from_image(image):
    image = make_image_readable(image)
    config_args = "-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    name = get_text.image_to_string(image, lang='eng', config=config_args)
    return name


# This takes an image and parses and returns an int from it
def int_from_image(image):
    image = make_image_readable(image)
    num = get_text.image_to_string(image, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    if num == '':
        num = 0
    return int(num)


# This takes an image and makes it more clearly readable for pytesseract
def make_image_readable(image):
    image = image.convert('L')

    image = ImageOps.invert(image)
    image_pixels = image.load()
    data = []

    for y in range(image.size[1]):
        for x in range(image.size[0]):
            pixel = image_pixels[x, y]
            if pixel < 128:
                data.append(0)
            else:
                data.append(255)

    image = Image.new('1', (image.size[0], image.size[1]))
    image.putdata(data)

    # This is the old resizable before we fixed the gold finding
    # resizable = tuple(2*x for x in image.size)

    resizable = 2*image.size[0], 3*image.size[1]
    image = image.resize(resizable)

    width, height = image.size
    image_pixels = image.load()

    data = []

    for y in range(height):
        for x in range(width):
            if x == 0 or x == width-1 or y == 0 or y == height-1:
                data.append(image_pixels[x, y])
                continue

            surrounding_black = [image_pixels[x, y - 1], image_pixels[x - 1, y],
                                 image_pixels[x + 1, y], image_pixels[x, y + 1]]
            count = 0
            for pixel in surrounding_black:
                if pixel == 0:
                    count += 1

            if count > 1:
                data.append(0)
            else:
                data.append(255)

    image = Image.new('1', (width, height))
    image.putdata(data)

    new_size = tuple(2*x for x in image.size)
    image.resize(new_size)

    return image


# This finds the play button and puts you in a game from it
def get_into_game():
    play_button_location = find_play_button()

    if play_button_location is None:
        print("Could not find league client")
        return

    click_through_to_game(play_button_location)
    Constants.in_game = True


# This takes a  point in the play button and then clicks you accordingly into game based on it
def click_through_to_game(point):
    # x, y is the locations of play button
    x = point.x
    y = point.y

    # This clicks on the play button
    click(Point(x + 55, y + 10))

    # This clicks on the Team Fight Tactics part of game modes
    time.sleep(.5)
    click(Point(x + 840, y + 250))

    # This clicks on the confirm for the game mode
    time.sleep(.5)
    click(Point(x + 500, y + 666))

    # This clicks on the "Find Match" button once in a TFT lobby.
    time.sleep(3)
    click(Point(x + 500, y + 666))

    # This checks if a queue is pops and then clicks on (Accept!/Decline)
    check_queue(point)


# This loops and checks queue until it pops and then accepts or declines it
def check_queue(point):
    # get_screen()
    x = point.x
    y = point.y

    image = image_grab.grab(bbox=(x + 469, y + 234, x + 744, y + 424))
    image.save(get_analyzable_relative_path() + "queue_screenshot.png")
    queue_screenshot = Image.open(get_analyzable_relative_path() + "queue_screenshot.png")
    queue_check = Image.open(get_button_relative_path() + "queue_check.PNG")

    popped = False
    while not popped:
        popped = compare_images(queue_screenshot, queue_check)
        image = image_grab.grab(bbox=(x + 468, y + 234, x + 743, y + 424))
        image.save(get_analyzable_relative_path() + "queue_screenshot.png")
        queue_screenshot = Image.open(get_analyzable_relative_path() + "queue_screenshot.png")
        time.sleep(.5)

    # Accept queue
    # click(Point(x + 600, y + 540))

    # Decline queue
    click(Point(x + 600, y + 600))


# This searches you screen and finds the play button and returns its first pixel location
def find_play_button():
    get_screen()
    screen = Image.open(get_analyzable_relative_path() + "screen.png")
    play_button_image = Image.open(get_button_relative_path() + "play_button.PNG")

    return compare_images_and_get_location_strictly(screen, play_button_image, 25)


# This compares two images and then returns the location of the tested image
def compare_images_and_get_location_strictly(tested, master, variance):
    tested_pixels = tested.load()
    master_pixels = master.load()

    index = 0
    for x in range(tested.size[0]):
        print("still going... at " + str(index))
        index += 1
        for y in range(tested.size[1]):
            if compare_pixels_strictly(tested_pixels[x, y], master_pixels[0, 0], variance):
                cropped_image = tested.crop((x, y, x + master.size[0], y + master.size[1]))
                if compare_images(cropped_image, master):
                    cropped_image.show()
                    return Point(x, y)

    return None


# This compares to image to a specific percent accuracy
def compare_images(tested, master):
    return compare_images_strictly(tested, master, PERCENTAGE_ACCURACY)


# This compares to images with a specified percent accuracy
def compare_images_strictly(tested, master, variance_allowed):
    search = tested.load()
    search_from = master.load()

    width, height = master.size
    pixels_wanted = (width * height) * variance_allowed
    pixels_accepted = 0

    for x in range(width):
        for y in range(height):
            if pixels_wanted < pixels_accepted:
                return True
            is_similar = compare_pixels(search[x, y], search_from[x, y])
            if is_similar:
                pixels_accepted += 1

    return False


# This compares to perfect accuracy
def compare_images_exact(tested, master):
    search = tested.load()
    search_from = master.load()
    width, height = master.size
    for x in range(width):
        for y in range(height):
            if compare_pixels(search[x, y], search_from[x, y]):
                continue
            else:
                return False
    return True


# This compares two pixels to a specified variance allowed
def compare_pixels(tested, master):
    return compare_pixels_strictly(tested, master, VARIANCE_THRESHOLD)


# This compares two pixels with a specified variance allowed
def compare_pixels_strictly(tested, master, variance_threshold):
    # Each input is a pixel with array values as such: [R, G, B, A]
    # Get the limit of variance by RGB values
    variance_allowed = (255 - (255 * variance_threshold)) * 3

    # Variance for red component
    variance = compare_pixels_red(tested, master)
    # Variance for green component
    variance += compare_pixels_green(tested, master)
    # Variance for blue component
    variance += compare_pixels_blue(tested, master)

    return variance < variance_allowed


# This compares two pixels red values
def compare_pixels_red(tested, master):
    return abs(master[0] - tested[0])


# This compares two pixels green values
def compare_pixels_green(tested, master):
    return abs(master[1] - tested[1])


# This compares two pixels blue values
def compare_pixels_blue(tested, master):
    return abs(master[2] - tested[2])


# This gets the relative path for the analyzable folder
def get_analyzable_relative_path():
    return Constants.MAIN_FILE_LOCATION + "/Resources/Analyzable/"


# This gets the relative path for the config folder
def get_config_relative_path():
    return Constants.MAIN_FILE_LOCATION + "/Resources/Config/"


# This gets the relative path for the misc folder
def get_misc_relative_path():
    return Constants.MAIN_FILE_LOCATION + "/Resources/Final/Misc/"


# This gets the relative path for the buttons folder
def get_button_relative_path():
    return Constants.MAIN_FILE_LOCATION + "/Resources/Final/Buttons/"


# This gets a screenshot of your screen
def get_screen():
    screenshot_name = get_analyzable_relative_path() + "screen.png"

    image = auto_gui.grab()
    image.save(screenshot_name)

    return Image.open(screenshot_name)


# This gets the users screensize
def get_screensize():
    return USER_32.GetSystemMetrics(0), USER_32.GetSystemMetrics(1)


# This clicks a specified point on your screen
def click(point):
    auto_gui.click(point.x, point.y)


# This clicks a specified point on your screen and drags to another point
def click_and_drag(initial_point, final_point):
    auto_gui.moveTo(initial_point.x, initial_point.y)
    auto_gui.dragTo(final_point.x, final_point.y, .2, button='left')


# This initializes your constants and config files
def initialize_resources(main_file_path):
    Constants.variables_initialize(main_file_path)
    ConfigFileLoader.load_configs(get_config_relative_path())
