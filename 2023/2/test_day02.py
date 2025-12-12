import pytest

from .advent_code import (
    calculate_sum_ids,
    how_many_colors,
    is_game_possible,
    parse_game_data,
)


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([" 1 red", " 2 green", " 6 blue"], {"blue": 6, "green": 2, "red": 1}),
        ([" 3 blue", " 4 red"], {"blue": 3, "green": 0, "red": 4}),
        ([" 2 green"], {"blue": 0, "green": 2, "red": 0}),
        ([" 3 green", " 4 blue", " 1 red"], {"blue": 4, "green": 3, "red": 1}),
    ],
)
def test_how_many_colors(test_input, expected):
    assert how_many_colors(test_input) == expected, (
        f"Input: {test_input}, Expected: {expected}, Got: {how_many_colors(test_input)}"
    )


EXAMPLE_INPUT = """Game 1: 7 red, 14 blue; 2 blue, 3 red, 3 green; 4 green, 12 blue, 15 red; 3 green, 12 blue, 3 red; 11 red, 2 green
Game 2: 16 blue, 9 red, 5 green; 8 red; 8 blue, 5 green, 12 red; 11 blue, 8 green, 17 red
Game 3: 8 green, 1 blue, 7 red; 12 red, 6 blue, 9 green; 2 blue, 1 red, 14 green; 9 green, 4 red; 2 red, 1 blue, 8 green
Game 4: 1 blue, 3 green; 2 green, 1 blue, 1 red; 1 red, 3 green
Game 5: 6 red, 1 blue; 1 green; 5 red, 2 green; 1 red, 1 blue, 3 green
Game 6: 3 green, 4 red, 1 blue; 2 blue, 5 green, 2 red; 12 green, 3 blue, 2 red; 4 blue, 1 green, 4 red; 11 green, 6 red; 5 green, 10 red, 3 blue
Game 7: 2 blue, 3 green, 16 red; 1 blue, 3 red; 2 green, 13 red; 18 red, 2 blue, 1 green; 3 red, 1 blue
Game 8: 4 red, 3 blue, 8 green; 2 red, 16 green; 2 red, 1 blue
Game 9: 4 green, 14 blue, 8 red; 17 blue, 3 red, 5 green; 2 green, 4 red, 6 blue; 7 red, 2 green, 18 blue; 3 red, 19 blue, 4 green; 4 green, 8 red, 6 blue
Game 10: 12 green, 7 red, 1 blue; 6 red, 12 green; 6 red, 7 green, 1 blue; 1 red, 1 blue, 18 green; 11 green, 1 blue
Game 11: 10 green, 3 red, 13 blue; 13 blue, 6 green, 8 red; 12 blue, 4 green, 8 red; 9 green, 9 red, 3 blue; 6 blue, 7 green, 6 red; 11 blue, 13 green
Game 12: 9 green, 2 blue; 4 green, 1 blue, 7 red; 2 green, 1 blue, 5 red
Game 13: 1 green; 7 blue, 1 red, 2 green; 8 blue, 2 green
Game 14: 8 red, 3 green; 1 red, 8 green; 1 blue, 10 green
Game 15: 1 blue, 6 green, 14 red; 3 red, 1 blue, 6 green; 4 green; 1 blue, 5 green, 2 red; 2 blue, 1 green, 6 red; 4 red, 8 green, 1 blue"""

GAMES = [
    {
        "id": 1,
        "set 1": {"blue": 14, "green": 0, "red": 7},
        "set 2": {"blue": 2, "green": 3, "red": 3},
        "set 3": {"blue": 12, "green": 4, "red": 15},
        "set 4": {"blue": 12, "green": 3, "red": 3},
        "set 5": {"blue": 0, "green": 2, "red": 11},
    },
    {
        "id": 2,
        "set 1": {"blue": 16, "green": 5, "red": 9},
        "set 2": {"blue": 0, "green": 0, "red": 8},
        "set 3": {"blue": 8, "green": 5, "red": 12},
        "set 4": {"blue": 11, "green": 8, "red": 17},
    },
    {
        "id": 3,
        "set 1": {"blue": 1, "green": 8, "red": 7},
        "set 2": {"blue": 6, "green": 9, "red": 12},
        "set 3": {"blue": 2, "green": 14, "red": 1},
        "set 4": {"blue": 0, "green": 9, "red": 4},
        "set 5": {"blue": 1, "green": 8, "red": 2},
    },
    {
        "id": 4,
        "set 1": {"blue": 1, "green": 3, "red": 0},
        "set 2": {"blue": 1, "green": 2, "red": 1},
        "set 3": {"blue": 0, "green": 3, "red": 1},
    },
    {
        "id": 5,
        "set 1": {"blue": 1, "green": 0, "red": 6},
        "set 2": {"blue": 0, "green": 1, "red": 0},
        "set 3": {"blue": 0, "green": 2, "red": 5},
        "set 4": {"blue": 1, "green": 3, "red": 1},
    },
    {
        "id": 6,
        "set 1": {"blue": 1, "green": 3, "red": 4},
        "set 2": {"blue": 2, "green": 5, "red": 2},
        "set 3": {"blue": 3, "green": 12, "red": 2},
        "set 4": {"blue": 4, "green": 1, "red": 4},
        "set 5": {"blue": 0, "green": 11, "red": 6},
        "set 6": {"blue": 3, "green": 5, "red": 10},
    },
    {
        "id": 7,
        "set 1": {"blue": 2, "green": 3, "red": 16},
        "set 2": {"blue": 1, "green": 0, "red": 3},
        "set 3": {"blue": 0, "green": 2, "red": 13},
        "set 4": {"blue": 2, "green": 1, "red": 18},
        "set 5": {"blue": 1, "green": 0, "red": 3},
    },
    {
        "id": 8,
        "set 1": {"blue": 3, "green": 8, "red": 4},
        "set 2": {"blue": 0, "green": 16, "red": 2},
        "set 3": {"blue": 1, "green": 0, "red": 2},
    },
    {
        "id": 9,
        "set 1": {"blue": 14, "green": 4, "red": 8},
        "set 2": {"blue": 17, "green": 5, "red": 3},
        "set 3": {"blue": 6, "green": 2, "red": 4},
        "set 4": {"blue": 18, "green": 2, "red": 7},
        "set 5": {"blue": 19, "green": 4, "red": 3},
        "set 6": {"blue": 6, "green": 4, "red": 8},
    },
    {
        "id": 10,
        "set 1": {"blue": 1, "green": 12, "red": 7},
        "set 2": {"blue": 0, "green": 12, "red": 6},
        "set 3": {"blue": 1, "green": 7, "red": 6},
        "set 4": {"blue": 1, "green": 18, "red": 1},
        "set 5": {"blue": 1, "green": 11, "red": 0},
    },
    {
        "id": 11,
        "set 1": {"blue": 13, "green": 10, "red": 3},
        "set 2": {"blue": 13, "green": 6, "red": 8},
        "set 3": {"blue": 12, "green": 4, "red": 8},
        "set 4": {"blue": 3, "green": 9, "red": 9},
        "set 5": {"blue": 6, "green": 7, "red": 6},
        "set 6": {"blue": 11, "green": 13, "red": 0},
    },
    {
        "id": 12,
        "set 1": {"blue": 2, "green": 9, "red": 0},
        "set 2": {"blue": 1, "green": 4, "red": 7},
        "set 3": {"blue": 1, "green": 2, "red": 5},
    },
    {
        "id": 13,
        "set 1": {"blue": 0, "green": 1, "red": 0},
        "set 2": {"blue": 7, "green": 2, "red": 1},
        "set 3": {"blue": 8, "green": 2, "red": 0},
    },
    {
        "id": 14,
        "set 1": {"blue": 0, "green": 3, "red": 8},
        "set 2": {"blue": 0, "green": 8, "red": 1},
        "set 3": {"blue": 1, "green": 10, "red": 0},
    },
    {
        "id": 15,
        "set 1": {"blue": 1, "green": 6, "red": 14},
        "set 2": {"blue": 1, "green": 6, "red": 3},
        "set 3": {"blue": 0, "green": 4, "red": 0},
        "set 4": {"blue": 1, "green": 5, "red": 2},
        "set 5": {"blue": 2, "green": 1, "red": 6},
        "set 6": {"blue": 1, "green": 8, "red": 4},
    },
]


def test_parse_game_data():
    result = parse_game_data(EXAMPLE_INPUT)
    assert result == GAMES, f"Expected {GAMES}, but got {result}"


def test_is_game_possible():
    result = is_game_possible(GAMES[0])
    assert result is False, f"Expected False, but got {result}"

    result = is_game_possible(GAMES[1])
    assert result is False, f"Expected False, but got {result}"

    result = is_game_possible(GAMES[2])
    assert result is False, f"Expected False, but got {result}"

    result = is_game_possible(GAMES[3])
    assert result is True, f"Expected True, but got {result}"

    result = is_game_possible(GAMES[4])
    assert result is True, f"Expected True, but got {result}"

    result = is_game_possible(GAMES[5])
    assert result is True, f"Expected True, but got {result}"

    result = is_game_possible(GAMES[6])
    assert result is False, f"Expected False, but got {result}"

    result = is_game_possible(GAMES[7])
    assert result is False, f"Expected False, but got {result}"

    result = is_game_possible(GAMES[8])
    assert result is False, f"Expected False, but got {result}"

    result = is_game_possible(GAMES[9])
    assert result is False, f"Expected False, but got {result}"

    result = is_game_possible(GAMES[10])
    assert result is True, (
        f"Expected True, but got {result}"
    )  # Game 11 is valid

    result = is_game_possible(GAMES[11])
    assert result is True, f"Expected True, but got {result}"

    result = is_game_possible(GAMES[12])
    assert result is True, f"Expected True, but got {result}"

    result = is_game_possible(GAMES[13])
    assert result is True, f"Expected True, but got {result}"

    result = is_game_possible(GAMES[14])
    assert result is False, f"Expected False, but got {result}"


def test_calculate_sum_ids():
    result = calculate_sum_ids(GAMES)
    assert result == 65, f"Expected 65, but got {result}"  # 4+5+6+11+12+13+14
