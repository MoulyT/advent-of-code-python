# Advent of code Year 2023 Day 9 solution
# Author = Mouly Taha
# Date = December 2018

import os

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")
with open(file_path, "r", encoding="utf-8") as input_file:
    input_data = input_file.read()

EXAMPLE_INPUT = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def parse_input(input_string: str):
    lines = input_string.splitlines()
    result = []
    for line in lines:
        array_strings = line.split()
        lst = tuple(map(int, array_strings))
        result.append(lst)
    return result


def get_next_number(arr, acc=0):
    differences = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
    if not differences or all(x == 0 for x in differences):
        return acc + (arr[-1] if arr else 0)
    else:
        new_acc = acc + arr[-1]
        return get_next_number(differences, new_acc)


def get_previous_number(arr, original_first_element=None, acc=0, operator=1):
    if original_first_element is None:
        print("Original first element is", arr[0])
        original_first_element = arr[0]
    if not all(x == 0 for x in arr) or len(arr) <= 1:
        differences = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
        new_acc = acc + (differences[0] * operator)
        print(arr, new_acc)
        return get_previous_number(
            differences, original_first_element, new_acc, -operator
        )
    else:
        print(arr, acc)
        print(
            "Previous number is",
            original_first_element,
            -acc,
            "=",
            original_first_element - acc,
            "!",
        )
        return original_first_element - acc


def get_sum_of_next_number(
    arr,
):
    result = 0
    for report in arr:
        result += get_next_number(report)
    return result


def get_sum_of_previous_number(
    arr,
):
    result = 0
    for report in arr:
        result += get_previous_number(report)
    return result


reports = parse_input(input_data)

part_one = get_sum_of_next_number(reports)

part_two = get_sum_of_previous_number(reports)


print("Part One :", str(part_one))

print("Part Two :", str(part_two))
