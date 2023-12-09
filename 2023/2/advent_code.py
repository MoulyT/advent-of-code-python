# Advent of code Year 2023 Day 2 solution
# Author = Mouly Taha
# Date = December 2018

from typing import List, Dict, Union, Literal

import os

# Obtener la ruta al directorio actual
dir_path = os.path.dirname(os.path.realpath(__file__))

# Construir la ruta al archivo input.txt en el mismo directorio
file_path = os.path.join(dir_path, "input.txt")

with open(file_path, "r", encoding="utf-8") as input_file:
    input_data = input_file.read()

EXAMPLE_INPUT = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

Color = Literal["blue", "green", "red"]
SetColorCounts = Dict[Color, int]
GameDataType = Dict[str, Union[int, SetColorCounts]]


def how_many_colors(array_cubes: List[str]) -> SetColorCounts:
    """
    Counts the number of occurrences of specified colors in a list of strings.

     Each string in the input list represents a cube, formatted as ' color number'.
     The function counts the number of each color ('blue', 'green', 'red') present in the list.

     Args:
         array_cubes (List[str]): A list of strings, each representing a cube in the format ' color number'.

     Returns:
         dict[str, int]: A dictionary with color keys ('blue', 'green', 'red') and their respective counts as values.
    """
    result = {
        "blue": 0,
        "green": 0,
        "red": 0,
    }
    for cube in array_cubes:
        count, color = cube.strip().split()
        if color in result:
            result[color] += int(count)
    return result


def parse_game_data(string: str) -> List[GameDataType]:
    """
    Parses game data from a string and returns a list of game details.

    Each game is described in a single line, with sets of colors and their counts separated by semicolons.
    The function extracts each game and its sets, then counts the occurrences of each color in the sets.

    Args:
        string (str): A multiline string where each line represents a game with sets of colored cubes.

    Returns:
        List[Dict]: A list of dictionaries, each representing a game. Each game dictionary contains
                    an 'id' key with the game number and keys for each set with the count of colors.
    """
    games_raw = string.split("\n")
    games_to_be_parsed = []
    for game_number, game in enumerate(games_raw):
        games_to_be_parsed.append({"id": game_number + 1})
        semicolon_index = game.find(":")
        game_sets = game[semicolon_index + 1 :: 1].split(";")
        for set_number, game_set in enumerate(game_sets):
            games_to_be_parsed[game_number][f"set {set_number + 1}"] = {}
            cubes = game_set.split(",")
            games_to_be_parsed[game_number][f"set {set_number + 1}"] = how_many_colors(
                cubes
            )
    return games_to_be_parsed


games = parse_game_data(input_data)


def check_color_cubes(game_set: SetColorCounts, color: Color, max_count: int) -> bool:
    """
    Checks if the number of cubes of a specific color in a game set
    is less than the required amount.

    Args:
        game_set (SetColorCounts): A dictionary with color counts.
        color (Color): The color to check.
        required_count (int): The required number of cubes for the color.

    Returns:
        bool: True if the game set has fewer cubes of the specified color than required.
    """
    return game_set.get(color, 0) > max_count


def is_game_possible(game_input: GameDataType) -> bool:
    """
    Determines if a game meets the required number of colored cubes.

    Args:
        game (GameDataType): A game data structure containing sets of colored cubes.

    Returns:
        bool: True if all sets in the game meet the color requirements.
    """
    max_cubes: SetColorCounts = {"blue": 14, "green": 13, "red": 12}
    for key, game_set in game_input.items():
        if "set" in key:
            for color, max_count in max_cubes.items():
                if check_color_cubes(game_set, color, max_count):
                    return False
    return True


def calculate_sum_ids(games):
    result = 0
    for game in games:
        if is_game_possible(game):
            result += game["id"]
    return result


sum_ids = calculate_sum_ids(games)


print("Part One : " + str(sum_ids))


def calculate_power(games: List[GameDataType]):
    result = 0
    for game in games:
        all_red_events = [
            game_set["red"] for key, game_set in game.items() if "set" in key
        ]
        all_green_events = [
            game_set["green"] for key, game_set in game.items() if "set" in key
        ]
        all_blue_events = [
            game_set["blue"] for key, game_set in game.items() if "set" in key
        ]
        power = max(all_red_events) * max(all_green_events) * max(all_blue_events)
        result += power
    return result


print("Part Two : " + str(calculate_power(games)))
