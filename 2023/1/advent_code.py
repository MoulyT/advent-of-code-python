# Advent of code Year 2023 Day 1 solution
# Author = Mouly Taha
# Date = December 2023
from pathlib import Path

input_file_path = Path(__file__).parent / "input.txt"
with open(input_file_path, encoding="utf-8") as input_file:
    input = input_file.read()

EXAMPLE_INPUT = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

words = input.split("\n")

type search_result = dict[str, int] | None


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
            return {
                "number": int(character),
                "index": len(input_word) - index - 1,
            }
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
    Search for the first occurrence of a number word (e.g., "one", "two").

    Args:
        input_word: String to search for number words.

    Returns:
        Dict with 'number' (int) and 'index' (int) keys,
        or None if not found.
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
    Search for the last occurrence of a number word (e.g., "one", "two").

    Args:
        input_word: String to search for number words.

    Returns:
        Dict with 'number' (int) and 'index' (int) keys,
        or None if not found.
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
    Compare two search results and return first or last based on flag.

    Args:
        integer: Search result from integer search.
        str_number: Search result from number word search.
        use_first: If True, return earliest; if False, return latest.

    Returns:
        The selected search result.
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
        concat_of_numbers = (
            first_integer["number"] * 10 + last_integer["number"]
        )
        RESULT = RESULT + concat_of_numbers
    else:
        raise ValueError("first_integer or/and last_integer are NoneType")


print("WIP", "result", RESULT)

# print("Part One : " + str(RESULT))


print("Part Two : " + str(None))
