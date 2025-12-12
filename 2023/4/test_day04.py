from .advent_code import (
    get_how_many_winning_numbers,
    get_points,
    parse_input,
)

EXAMPLE_INPUT = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


EXAMPLE_OUTPUT = (
    ({41, 48, 83, 86, 17}, {83, 86, 6, 31, 17, 9, 48, 53}),
    ({13, 32, 20, 16, 61}, {61, 30, 68, 82, 17, 32, 24, 19}),
    ({1, 21, 53, 59, 44}, {69, 82, 63, 72, 16, 21, 14, 1}),
    ({41, 92, 73, 84, 69}, {59, 84, 76, 51, 58, 5, 54, 83}),
    ({87, 83, 26, 28, 32}, {88, 30, 70, 12, 93, 22, 82, 36}),
    ({31, 18, 13, 56, 72}, {74, 77, 10, 23, 35, 67, 36, 11}),
)


def test_parse_input():
    assert parse_input(EXAMPLE_INPUT) == EXAMPLE_OUTPUT


def test_get_how_many_winning_numbers():
    assert get_how_many_winning_numbers(EXAMPLE_OUTPUT[0]) == 4
    assert get_how_many_winning_numbers(EXAMPLE_OUTPUT[1]) == 2
    assert get_how_many_winning_numbers(EXAMPLE_OUTPUT[2]) == 2
    assert get_how_many_winning_numbers(EXAMPLE_OUTPUT[3]) == 1
    assert get_how_many_winning_numbers(EXAMPLE_OUTPUT[4]) == 0
    assert get_how_many_winning_numbers(EXAMPLE_OUTPUT[5]) == 0


def test_get_points():
    assert get_points(4) == 8
    assert get_points(2) == 2
    assert get_points(1) == 1
    assert get_points(0) == 0
