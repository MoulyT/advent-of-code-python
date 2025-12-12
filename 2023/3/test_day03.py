from .day03 import (
    find_number,
    get_adyacent_coordinates,
    get_map,
    input_map,
    is_part_number,
    sum_part_numbers,
)

EXAMPLE_INPUT = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def test_get_map():
    assert get_map(EXAMPLE_INPUT) == (
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    )


def test_find_number():
    assert find_number(get_map(EXAMPLE_INPUT)) == [
        {"number": 467, "row": 0, "column": 0},
        {"number": 114, "row": 0, "column": 5},
        {"number": 35, "row": 2, "column": 2},
        {"number": 633, "row": 2, "column": 6},
        {"number": 617, "row": 4, "column": 0},
        {"number": 58, "row": 5, "column": 7},
        {"number": 592, "row": 6, "column": 2},
        {"number": 755, "row": 7, "column": 6},
        {"number": 664, "row": 9, "column": 1},
        {"number": 598, "row": 9, "column": 5},
    ]


def test_is_part_number():
    assert (
        is_part_number(
            {"number": 467, "row": 0, "column": 0}, get_map(EXAMPLE_INPUT)
        )
        is True
    )
    assert (
        is_part_number(
            {"number": 114, "row": 0, "column": 5}, get_map(EXAMPLE_INPUT)
        )
        is False
    )
    assert (
        is_part_number(
            {"number": 35, "row": 2, "column": 2}, get_map(EXAMPLE_INPUT)
        )
        is True
    )
    assert (
        is_part_number(
            {"number": 633, "row": 2, "column": 6}, get_map(EXAMPLE_INPUT)
        )
        is True
    )
    assert (
        is_part_number(
            {"number": 617, "row": 4, "column": 0}, get_map(EXAMPLE_INPUT)
        )
        is True
    )
    assert (
        is_part_number(
            {"number": 58, "row": 5, "column": 7}, get_map(EXAMPLE_INPUT)
        )
        is False
    )
    assert (
        is_part_number(
            {"number": 592, "row": 6, "column": 2}, get_map(EXAMPLE_INPUT)
        )
        is True
    )
    assert (
        is_part_number(
            {"number": 755, "row": 7, "column": 6}, get_map(EXAMPLE_INPUT)
        )
        is True
    )
    assert (
        is_part_number(
            {"number": 664, "row": 9, "column": 1}, get_map(EXAMPLE_INPUT)
        )
        is True
    )
    assert (
        is_part_number(
            {"number": 598, "row": 9, "column": 5}, get_map(EXAMPLE_INPUT)
        )
        is True
    )
    # Real input edge case
    assert is_part_number({"number": 11, "row": 77, "column": 134}, input_map)


def test_sum_part_numbers():
    assert (
        sum_part_numbers(
            find_number(get_map(EXAMPLE_INPUT)), get_map(EXAMPLE_INPUT)
        )
        == 4361
    )


def test_get_adyacent_coordinates():
    # Test case 1
    row = 2
    column = 3
    length = 2
    rows_of_map = 5
    columns_of_map = 6
    expected_result = [
        [1, 2],
        [1, 3],
        [1, 4],
        [1, 5],
        [2, 2],
        [2, 5],
        [3, 2],
        [3, 3],
        [3, 4],
        [3, 5],
    ]
    assert (
        get_adyacent_coordinates(
            row, column, length, rows_of_map, columns_of_map
        )
        == expected_result
    )

    # Test case 2
    row = 0
    column = 0
    length = 1
    rows_of_map = 3
    columns_of_map = 3
    expected_result = [[0, 1], [1, 0], [1, 1]]
    assert (
        get_adyacent_coordinates(
            row, column, length, rows_of_map, columns_of_map
        )
        == expected_result
    )

    # Test case 3
    row = 4
    column = 5
    length = 2
    rows_of_map = 6
    columns_of_map = 7
    expected_result = [[3, 4], [3, 5], [3, 6], [4, 4], [5, 4], [5, 5], [5, 6]]
    assert (
        get_adyacent_coordinates(
            row, column, length, rows_of_map, columns_of_map
        )
        == expected_result
    )
