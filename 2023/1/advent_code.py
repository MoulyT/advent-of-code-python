# Advent of code Year 2023 Day 1 solution
# Author = Mouly Taha
# Date = December 2023
from typing import Optional

with open(
    (__file__.rstrip("advent_code.py") + "input.txt"), "r", encoding="utf-8"
) as input_file:
    input = input_file.read()

EXAMPLE_INPUT = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

words = input.split("\n")

type search_result = Optional[dict[str, str]]


def search_first_integer(input_word: str) -> search_result:
    """
    Search the first integer of a word, returns None if no integer is found
    """
    for index, character in enumerate(input_word):
        if character.isdigit():
            return {"number": int(character), "index": index}
    return None


def search_last_integer(input_word: str) -> search_result:
    """
    Search the last integer of a word, returns None if no integer is found
    """
    for index, character in enumerate(reversed(input_word)):
        if character.isdigit():
            return {"number": int(character), "index": len(input_word) - index - 1}
    return None


numbers = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}


def search_first_str_number(input_word: str) -> search_result:
    """
    Searches for the first occurrence of a number (in word form) within a given string and
    returns the corresponding search result.

    This function iterates through a predefined dictionary `numbers`, where each value represents
    a number in word form.
    It checks for the presence of these number words in the input string and returns
      the first one it finds.

    Args:
        input_word (str): The string to be searched for number words.

    Returns:
        search_result: A dictionary containing the numeric value and index of the first found number
                        word in the string.
                       The 'number' key holds the numeric value (as an integer) corresponding
                        to the found number word,and the 'index' key holds the starting index
                        of this number word in the string.
                       Returns None if no number word is found.
    """
    result = None
    for iteration, number in enumerate(numbers.values()):
        index = input_word.find(number)
        if index != -1:
            result = (
                {"number": iteration, "index": index}
                if result is None or result["index"] > index
                else result
            )
    return result


def search_last_str_number(input_word: str) -> search_result:
    """
    Searches for the last occurrence of any number (in word form) in a string and returns a search result.

    Similar to `search_first_str_number`, this function iterates over the `numbers` dictionary to find numbers in word form.
    However, it looks for the last occurrence of these numbers in `input_word`.

    Args:
        input_word (str): The string in which to search for the number.

    Returns:
        search_result: A dictionary containing the number found and its index in the string.
                       The 'number' key holds the numeric value (as an integer) of the found number,
                       and the 'index' key holds the starting index of the number in the string.
                       Returns None if no number is found.
    """
    result = None
    for iteration, number in enumerate(numbers.values()):
        index = input_word.rfind(number)
        if index != -1:
            result = (
                {"number": iteration, "index": index}
                if result is None or result["index"] < index
                else result
            )
    return result


def compare_search_results(
    integer: search_result, str_number: search_result, use_first: bool
) -> search_result:
    """
    Compare two search results and returns the first or last one based on the `use_first` flag.

    Args:
        integer (search_result): The search result containing an integer.
        str_number (search_result): The search result containing a string representation of a number.
        use_first (bool): Flag to determine if the first or last result should be returned.

    Returns:
        search_result: The desired search result based on the comparison.
    """
    if integer is None:
        return str_number
    if str_number is None:
        return integer

    if (integer["index"] < str_number["index"]) == use_first:
        return integer
    else:
        return str_number


def get_first_integer(
    integer: search_result, str_number: search_result
) -> search_result:
    """
    Returns the first integer from the given search results.
    """
    return compare_search_results(integer, str_number, use_first=True)


def get_last_integer(
    integer: search_result, str_number: search_result
) -> search_result:
    """
    Returns the last integer from the given search results.
    """
    return compare_search_results(integer, str_number, use_first=False)


RESULT = 0
for word in words:
    first_integer = get_first_integer(
        search_first_integer(word), search_first_str_number(word)
    )
    last_integer = get_last_integer(
        search_last_integer(word), search_last_str_number(word)
    )
    if first_integer is not None and last_integer is not None:
        concat_of_numbers = first_integer.get(
            "number", "error"
        ) * 10 + last_integer.get("number", "error")
        RESULT = RESULT + concat_of_numbers
    else:
        raise ValueError("first_integer or/and last_integer are NoneType")


print("WIP", "result", RESULT)

# print("Part One : " + str(RESULT))


print("Part Two : " + str(None))
