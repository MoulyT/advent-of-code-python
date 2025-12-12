# Advent of code Year 2023 Day 13 solution
# Author = Mouly Taha
# Date = December 2018

import os

file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "input.txt"
)
with open(file_path, encoding="utf-8") as input_file:
    input_data = input_file.read()


EXAMPLE_INPUT = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""


def parse_input(input_str: str):
    mirror_patterns = input_str.split("\n\n")
    return [pattern.splitlines() for pattern in mirror_patterns]


def check_horizontal_symmetry(pattern):
    for i in range(1, len(pattern)):
        top_flipped = pattern[:i][::-1]
        bottom = pattern[i:]

        if (
            sum(
                sum(
                    0 if char_top == char_bottom else 1
                    for char_top, char_bottom in zip(
                        row_top, row_bottom, strict=False
                    )
                )
                for row_top, row_bottom in zip(
                    top_flipped, bottom, strict=False
                )
            )
            == 1
        ):
            return i


def transpose(pattern):
    return ["".join(line) for line in zip(*pattern, strict=False)]


def get_symmetries(patterns):
    horizontal_symmetries = []
    vertical_symmetries = []
    for pattern in patterns:
        horizontal_symmetries.append(check_horizontal_symmetry(pattern))
        vertical_symmetries.append(
            check_horizontal_symmetry(transpose(pattern))
        )
    return horizontal_symmetries, vertical_symmetries


def get_result_part_one(patterns):
    horizontal_symmetries, vertical_symmetries = get_symmetries(patterns)
    vertical_result = sum(filter(None, vertical_symmetries))
    horizontal_result = sum(filter(None, horizontal_symmetries)) * 100
    return vertical_result + horizontal_result


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(cell) for cell in row))


patterns = parse_input(input_data)

print("Part One :", str(get_result_part_one(patterns)))

print("Part One :", str(None))

print("Part Two :", str(None))
