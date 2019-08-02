from TeamFightTacticsBot.Structures.Point import Point

CAROUSEL_CHAMPION_COUNT = 9

BENCH_SLOTS = 9
BENCH_SLOT_CLICKABLE_LOCATIONS = []

BOARD_SIZE_WIDTH = 7
BOARD_SIZE_HEIGHT = 3
BOARD_SLOT_CLICKABLE_LOCATIONS = []

STREAK_BONUS_GOLD_THRESHOLD = [2, 4, 7]

# In game variables
CURRENT_STAGE = 1
CURRENT_ROUND = 0


def variables_initialize():
    global CAROUSEL_CHAMPION_COUNT

    global BENCH_SLOTS
    global BENCH_SLOT_CLICKABLE_LOCATIONS
    BENCH_SLOT_CLICKABLE_LOCATIONS = set_bench_clickable_locations()

    global BOARD_SIZE_WIDTH
    global BOARD_SIZE_HEIGHT
    global BOARD_SLOT_CLICKABLE_LOCATIONS
    BOARD_SLOT_CLICKABLE_LOCATIONS = set_board_clickable_locations()

    global STREAK_BONUS_GOLD_THRESHOLD


def set_bench_clickable_locations():
    points = []
    row_x = 0
    base_x = 430
    base_y = 775
    slot_offset = 120

    for x in range(BENCH_SLOTS):
        points.append(Point(base_x + (slot_offset * row_x), base_y))
        row_x += 1

    return points


def set_board_clickable_locations():
    points = []
    row_x = 0
    row_y = 0
    base_x = 560
    base_y = 490
    slot_offset = Point(140, 85)

    for y in range(BOARD_SIZE_HEIGHT):
        for x in range(BOARD_SIZE_WIDTH):
            if row_y % 2 == 1:
                # Apply offset
                points.append(Point((base_x - 70) + (slot_offset.x * row_x), base_y + (slot_offset.y * row_y)))
            else:
                points.append(Point(base_x + (slot_offset.x * row_x), base_y + (slot_offset.y * row_y)))
            row_x += 1
        row_x = 0
        row_y += 1

    return points
