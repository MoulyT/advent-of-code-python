# Advent of code Year 2023 Day 2 solution
# Author = Mouly Taha
# Date = December 2018

import os
from typing import Literal

# Obtener la ruta al directorio actual
dir_path = os.path.dirname(os.path.realpath(__file__))

# Construir la ruta al archivo input.txt en el mismo directorio
file_path = os.path.join(dir_path, "input.txt")

with open(file_path, encoding="utf-8") as input_file:
    input_data = input_file.read()

EXAMPLE_INPUT = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

Color = Literal["blue", "green", "red"]
SetColorCounts = dict[Color, int]
GameDataType = dict[str, int | SetColorCounts]


def how_many_colors(array_cubes: list[str]) -> SetColorCounts:
    """
    Counts color occurrences in a list of cube strings.

    Each string represents a cube in format ' color number'.

    Args:
        array_cubes: List of cube strings in format ' color number'.

    Returns:
        Dictionary with color counts for 'blue', 'green', 'red'.
    """
    result: SetColorCounts = {
        "blue": 0,
        "green": 0,
        "red": 0,
    }
    for cube in array_cubes:
        count, color = cube.strip().split()
        if color in ("blue", "green", "red"):
            result[color] += int(count)  # type: ignore
    return result


def parse_game_data(string: str) -> list[GameDataType]:
    """
    Parses game data from a multiline string.

    Each line describes a game with semicolon-separated color sets.

    Args:
        string: Multiline string with game data.

    Returns:
        List of game dictionaries with 'id' and color set counts.
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
            games_to_be_parsed[game_number][f"set {set_number + 1}"] = (
                how_many_colors(cubes)
            )
    return games_to_be_parsed


games = parse_game_data(input_data)


def check_color_cubes(
    game_set: SetColorCounts, color: Color, max_count: int
) -> bool:
    """
    Checks if a color count exceeds the maximum.

    Args:
        game_set: Dictionary with color counts.
        color: Color to check.
        max_count: Maximum allowed count.

    Returns:
        True if count exceeds max_count.
    """
    return game_set.get(color, 0) > max_count


def is_game_possible(game_input: GameDataType) -> bool:
    """
    Checks if game is possible with available cubes.

    Args:
        game_input: Game data with color sets.

    Returns:
        True if all sets meet cube requirements.
    """
    max_cubes: SetColorCounts = {"blue": 14, "green": 13, "red": 12}
    for key, game_set in game_input.items():
        if "set" in key:
            assert isinstance(game_set, dict)  # type narrowing
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


def calculate_power(games: list[GameDataType]):
    result = 0
    for game in games:
        all_red_events = []
        all_green_events = []
        all_blue_events = []
        for key, game_set in game.items():
            if "set" in key:
                assert isinstance(game_set, dict)  # type narrowing
                all_red_events.append(game_set["red"])
                all_green_events.append(game_set["green"])
                all_blue_events.append(game_set["blue"])
        power = (
            max(all_red_events) * max(all_green_events) * max(all_blue_events)
        )
        result += power
    return result


print("Part Two : " + str(calculate_power(games)))
