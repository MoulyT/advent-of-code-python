from advent_code import (
    search_first_integer,
    search_last_integer,
    search_first_str_number,
    search_last_str_number,
    get_first_integer,
    get_last_integer,
)


EXAMPLE_INPUT = """1two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
input_lines = EXAMPLE_INPUT.split("\n")
input_line1 = input_lines[0]
input_line2 = input_lines[1]
input_line3 = input_lines[2]
input_line4 = input_lines[3]
input_line5 = input_lines[4]
input_line6 = input_lines[5]
input_line7 = input_lines[6]


def test_search_first_integer():
    assert search_first_integer(input_line1) == {"number": 1, "index": 0}
    assert search_first_integer(input_line2) == None
    assert search_first_integer(input_line3) == {"number": 2, "index": 6}
    assert search_first_integer(input_line4) == {"number": 3, "index": 6}
    assert search_first_integer(input_line5) == {"number": 4, "index": 0}
    assert search_first_integer(input_line6) == {"number": 2, "index": 8}
    assert search_first_integer(input_line7) == {"number": 7, "index": 0}


def test_search_last_integer():
    assert search_last_integer(input_line1) == {"number": 1, "index": 4}
    assert search_last_integer(input_line2) == None
    assert search_last_integer(input_line3) == {"number": 2, "index": 6}
    assert search_last_integer(input_line4) == {"number": 3, "index": 6}
    assert search_last_integer(input_line5) == {"number": 2, "index": 15}
    assert search_last_integer(input_line6) == {"number": 4, "index": 10}
    assert search_last_integer(input_line7) == {"number": 7, "index": 0}


def test_search_first_str_number():
    result = search_first_str_number(input_line1)
    expected = {"number": 2, "index": 1}
    assert (
        result == expected
    ), f"Failed for input '{input_line1}'. Expected {expected}, but got {result}"

    result = search_first_str_number(input_line2)
    expected = {"number": 8, "index": 0}
    assert (
        result == expected
    ), f"Failed for input '{input_line2}'. Expected {expected}, but got {result}"

    result = search_first_str_number(input_line3)
    expected = {"number": 1, "index": 3}
    assert (
        result == expected
    ), f"Failed for input '{input_line3}'. Expected {expected}, but got {result}"

    result = search_first_str_number(input_line4)
    expected = {"number": 2, "index": 1}
    assert (
        result == expected
    ), f"Failed for input '{input_line4}'. Expected {expected}, but got {result}"

    result = search_first_str_number(input_line5)
    expected = {"number": 9, "index": 1}
    assert (
        result == expected
    ), f"Failed for input '{input_line5}'. Expected {expected}, but got {result}"

    result = search_first_str_number(input_line6)
    expected = {"number": 1, "index": 1}
    assert (
        result == expected
    ), f"Failed for input '{input_line6}'. Expected {expected}, but got {result}"

    result = search_first_str_number(input_line7)
    expected = {"number": 6, "index": 6}
    assert (
        result == expected
    ), f"Failed for input '{input_line7}'. Expected {expected}, but got {result}"


def test_search_last_str_number():
    result = search_last_str_number(input_line1)
    expected = {"number": 9, "index": 5}
    assert (
        result == expected
    ), f"Failed for input '{input_line1}'. Expected {expected}, but got {result}"

    result = search_last_str_number(input_line2)
    expected = {"number": 3, "index": 7}
    assert (
        result == expected
    ), f"Failed for input '{input_line2}'. Expected {expected}, but got {result}"

    result = search_last_str_number(input_line3)
    expected = {"number": 3, "index": 7}
    assert (
        result == expected
    ), f"Failed for input '{input_line3}'. Expected {expected}, but got {result}"

    result = search_last_str_number(input_line4)
    expected = {"number": 4, "index": 7}
    assert (
        result == expected
    ), f"Failed for input '{input_line4}'. Expected {expected}, but got {result}"

    result = search_last_str_number(input_line5)
    expected = {"number": 7, "index": 10}
    assert (
        result == expected
    ), f"Failed for input '{input_line5}'. Expected {expected}, but got {result}"

    result = search_last_str_number(input_line6)
    expected = {"number": 8, "index": 3}
    assert (
        result == expected
    ), f"Failed for input '{input_line6}'. Expected {expected}, but got {result}"

    result = search_last_str_number(input_line7)
    expected = {"number": 6, "index": 6}
    assert (
        result == expected
    ), f"Failed for input '{input_line7}'. Expected {expected}, but got {result}"


def test_get_first_integer():
    result = get_first_integer(
        search_first_integer(input_line1), search_first_str_number(input_line1)
    )
    expected = {"number": 1, "index": 0}
    assert (
        result == expected
    ), f"Failed for input '{input_line1}'. Expected {expected}, but got {result}"

    result = get_first_integer(
        search_first_integer(input_line2), search_first_str_number(input_line2)
    )
    expected = {"number": 8, "index": 0}
    assert (
        result == expected
    ), f"Failed for input '{input_line2}'. Expected {expected}, but got {result}"

    result = get_first_integer(
        search_first_integer(input_line3), search_first_str_number(input_line3)
    )
    expected = {"number": 1, "index": 3}
    assert (
        result == expected
    ), f"Failed for input '{input_line3}'. Expected {expected}, but got {result}"

    result = get_first_integer(
        search_first_integer(input_line4), search_first_str_number(input_line4)
    )
    expected = {"number": 2, "index": 1}
    assert (
        result == expected
    ), f"Failed for input '{input_line4}'. Expected {expected}, but got {result}"

    result = get_first_integer(
        search_first_integer(input_line5), search_first_str_number(input_line5)
    )
    expected = {"number": 4, "index": 0}
    assert (
        result == expected
    ), f"Failed for input '{input_line5}'. Expected {expected}, but got {result}"

    result = get_first_integer(
        search_first_integer(input_line6), search_first_str_number(input_line6)
    )
    expected = {"number": 1, "index": 1}
    assert (
        result == expected
    ), f"Failed for input '{input_line6}'. Expected {expected}, but got {result}"

    result = get_first_integer(
        search_first_integer(input_line7), search_first_str_number(input_line7)
    )
    expected = {"number": 7, "index": 0}
    assert (
        result == expected
    ), f"Failed for input '{input_line7}'. Expected {expected}, but got {result}"


def test_get_last_integer():
    result = get_last_integer(
        search_last_integer(input_line1), search_last_str_number(input_line1)
    )
    expected = {"number": 9, "index": 5}
    assert (
        result == expected
    ), f"Failed for input '{input_line1}'. Expected {expected}, but got {result}"

    result = get_last_integer(
        search_last_integer(input_line2), search_last_str_number(input_line2)
    )
    expected = {"number": 3, "index": 7}
    assert (
        result == expected
    ), f"Failed for input '{input_line2}'. Expected {expected}, but got {result}"

    result = get_last_integer(
        search_last_integer(input_line3), search_last_str_number(input_line3)
    )
    expected = {"number": 3, "index": 7}
    assert (
        result == expected
    ), f"Failed for input '{input_line3}'. Expected {expected}, but got {result}"

    result = get_last_integer(
        search_last_integer(input_line4), search_last_str_number(input_line4)
    )
    expected = {"number": 4, "index": 7}
    assert (
        result == expected
    ), f"Failed for input '{input_line4}'. Expected {expected}, but got {result}"

    result = get_last_integer(
        search_last_integer(input_line5), search_last_str_number(input_line5)
    )
    expected = {"number": 2, "index": 15}
    assert (
        result == expected
    ), f"Failed for input '{input_line5}'. Expected {expected}, but got {result}"

    result = get_last_integer(
        search_last_integer(input_line6), search_last_str_number(input_line6)
    )
    expected = {"number": 4, "index": 10}
    assert (
        result == expected
    ), f"Failed for input '{input_line6}'. Expected {expected}, but got {result}"

    result = get_last_integer(
        search_last_integer(input_line7), search_last_str_number(input_line7)
    )
    expected = {"number": 6, "index": 6}
    assert (
        result == expected
    ), f"Failed for input '{input_line7}'. Expected {expected}, but got {result}"
