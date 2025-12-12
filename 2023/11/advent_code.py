# Advent of code Year 2023 Day 11 solution
# Author = Mouly Taha
# Date = December 2018

import os

file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "input.txt"
)
with open(file_path, encoding="utf-8") as input_file:
    input_data = input_file.read()

EXAMPLE_INPUT = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


def parse_input(input_str: str):
    return [list(row) for row in input_str.splitlines()]


def find_rows_to_expand(universe):
    return [i for i, row in enumerate(universe) if all(x == "." for x in row)]


def find_columns_to_expand(universe):
    num_columns = len(universe[0])
    return [
        j
        for j in range(num_columns)
        if all(universe[i][j] == "." for i in range(len(universe)))
    ]


def expand_rows(universe, rows, num_new_rows=1):
    num_columns = len(universe[0])
    new_row = [num_new_rows] * num_columns
    sorted_rows = sorted(rows, reverse=True)

    for row_index in sorted_rows:
        universe.insert(row_index + 1, new_row.copy())


def expand_columns(universe, columns, num_new_columns=1):
    for col_index in sorted(columns, reverse=True):
        for row in universe:
            row.insert(col_index + 1, num_new_columns)


def expand_universe(universe, num_new_rows=1, num_new_columns=1):
    rows_to_expand = find_rows_to_expand(universe)
    columns_to_expand = find_columns_to_expand(universe)
    expand_rows(universe, rows_to_expand, num_new_rows)
    expand_columns(universe, columns_to_expand, num_new_columns)

    return universe


def search_galaxies(universe):
    galaxies = []
    row_expansion = 0
    for i, row in enumerate(universe):
        if isinstance(row[0], int):
            row_expansion += row[0] - 1
            continue
        col_expansion = 0
        for j, cell in enumerate(row):
            if isinstance(cell, int):
                col_expansion += cell - 1
                continue
            if cell == "#":
                galaxies.append((i + row_expansion, j + col_expansion))
    return galaxies


def get_galaxy_distance(galaxy1, galaxy2):
    return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])


def calculate_all_galaxy_distances(galaxies):
    distances = {}
    num_galaxies = len(galaxies)

    for i in range(num_galaxies):
        for j in range(i + 1, num_galaxies):
            distance = get_galaxy_distance(galaxies[i], galaxies[j])
            distances[(i, j)] = distance

    return distances


def get_sum_galaxy_distance(galaxies):
    distances = calculate_all_galaxy_distances(galaxies)
    return sum(distances.values())


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(cell) for cell in row))


time1 = 1
expanded_universe = expand_universe(parse_input(input_data), time1, time1)
list_of_galaxies = search_galaxies(expanded_universe)
min_distance = get_sum_galaxy_distance(list_of_galaxies)


print("Part One :", str(min_distance))

time2 = 999999
expanded_universe_2 = expand_universe(parse_input(input_data), time2, time2)
print_matrix(expanded_universe_2)
min_distance_2 = get_sum_galaxy_distance(search_galaxies(expanded_universe_2))

print("Part Two :", str(min_distance_2))
