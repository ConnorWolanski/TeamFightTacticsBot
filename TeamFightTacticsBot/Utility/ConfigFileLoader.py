import configparser as config_parser_master
from TeamFightTacticsBot.Structures.LearnedMetaData import LearnedMetaData

# Global Variables
STAGE_LEVEL_ASSOCIATIONS = {}
CHAMPION_LEARNED_RATINGS = {}
SYNERGY_LEARNED_RATINGS = {}


def load_configs(relative_path):
    global STAGE_LEVEL_ASSOCIATIONS
    STAGE_LEVEL_ASSOCIATIONS = load_game_stage_to_level_associations(relative_path + "GameStageToLevelAssociations.cfg")
    global CHAMPION_LEARNED_RATINGS
    CHAMPION_LEARNED_RATINGS = load_character_learned_ratings(relative_path + "ChampionLearnedRating.cfg")
    global SYNERGY_LEARNED_RATINGS
    SYNERGY_LEARNED_RATINGS = load_synergy_learned_ratings(relative_path + "SynergyLearnedRating.cfg")


def load_game_stage_to_level_associations(path):
    config_parser = config_parser_master.RawConfigParser()
    config_parser.read(path)
    dictionary = dict(config_parser.items("STAGES"))
    dictionary_created = {}

    for sec in dictionary:
        range_string = dictionary.get(sec).split(",")
        low = int(range_string[0])
        high = int(range_string[1])
        level_list = []

        for x in range(low, high + 1):
            level_list.append(x)

        dictionary_created[sec] = level_list

    return dictionary_created


def load_character_learned_ratings(path):
    return make_dictionary_hell(path)


def load_synergy_learned_ratings(path):
    return make_dictionary_hell(path)


def make_dictionary_hell(path):
    config_parser = config_parser_master.RawConfigParser()
    config_parser.read(path)
    stage_dictionary = {}

    for stage in STAGE_LEVEL_ASSOCIATIONS:
        dictionary = dict(config_parser.items(stage.upper()))
        custom_dictionary = {}
        for learned_data in dictionary:
            data_string = dictionary.get(learned_data)
            custom_dictionary[learned_data] = get_rating_and_games_played(data_string)

        stage_dictionary[stage] = custom_dictionary

    return stage_dictionary


def get_rating_and_games_played(string_input):
    string_input = string_input.split(":")
    rating = int(string_input[0])
    games_played = int(string_input[1])
    return LearnedMetaData(rating, games_played)
