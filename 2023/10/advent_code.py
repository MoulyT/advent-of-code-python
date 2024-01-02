# Advent of code Year 2023 Day 10 solution
# Author = Mouly Taha
# Date = December 2018

import os
import sys

# Aumenta el límite de recursión
sys.setrecursionlimit(20000)

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")
with open(file_path, "r", encoding="utf-8") as input_file:
    input_data = input_file.read()

EXAMPLE_INPUT = """............
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

UP = [-1, 0]
DOWN = [1, 0]
LEFT = [0, -1]
RIGHT = [0, 1]

direction_names = {
    tuple(UP): "UP",
    tuple(DOWN): "DOWN",
    tuple(LEFT): "LEFT",
    tuple(RIGHT): "RIGHT",
}


def is_vertex(pipe: str):
    kind_of_vertexes = ["7", "J", "L", "F"]
    return pipe in kind_of_vertexes


def parse_input(input_str: str):
    return [list(row) for row in input_str.splitlines()]


def get_directions(last_move: list[int], next_pipe: str):
    if next_pipe == "S":
        return None
    direction_map = {
        tuple(UP): {"|": UP, "F": RIGHT, "7": LEFT},
        tuple(DOWN): {"|": DOWN, "J": LEFT, "L": RIGHT},
        tuple(RIGHT): {"-": RIGHT, "J": UP, "7": DOWN},
        tuple(LEFT): {"-": LEFT, "F": DOWN, "L": UP},
    }
    last_move_str = direction_names.get(tuple(last_move), "Unknown")
    new_direction = direction_map.get(tuple(last_move), {}).get(next_pipe, None)
    if new_direction is None:
        error_message = (
            f"Error: Invalid movement. Last move was {last_move_str}, "
            f"next pipe is '{next_pipe}'. No valid move found."
        )
        raise ValueError(error_message)
    direction_name = direction_names.get(tuple(new_direction), "Unknown")

    # print(
    #     f"Last move was {last_move_str} and  next pipe is '{next_pipe}', so going {direction_name}"
    # )

    return new_direction


def search_initial_position(grid: list[list[str]]):
    for i, row in enumerate(grid):
        for j, pipe in enumerate(row):
            if pipe == "S":
                return [i, j]


def calculate_area_Gauss_formula(vertexes: list[list[int]]):
    n = len(vertexes)
    area = 0
    for i in range(n - 1):
        area += vertexes[i][0] * vertexes[i + 1][1]
        area -= vertexes[i][1] * vertexes[i + 1][0]

    area += vertexes[n - 1][0] * vertexes[0][1]
    area -= vertexes[n - 1][1] * vertexes[0][0]

    return abs(area / 2)


def calculate_inner_points_Pick_formula(area: int, boundary_points: int):
    return area - (boundary_points / 2) + 1


def search(
    grid: list[list[str]], last_move=None, current_position=None, steps=0, vertexes=None
):
    if vertexes is None:
        vertexes = []
    if current_position is None and last_move is None:
        current_position = search_initial_position(grid)
        last_move = DOWN
        new_i = current_position[0] + last_move[0]
        new_j = current_position[1] + last_move[1]
        return search(grid, last_move, [new_i, new_j], steps + 1)
    i, j = current_position
    direction = get_directions(last_move, grid[i][j])
    if is_vertex(grid[i][j]):
        vertexes.append(current_position)

    if direction is None:
        return steps, vertexes
    return search(
        grid, direction, [i + direction[0], j + direction[1]], steps + 1, vertexes
    )


matrix = parse_input(input_data)


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))


print_matrix(matrix)
print(search(matrix))
steps_walked, list_vertexes = search(matrix)
print("Steps walked :", steps_walked)
print("Vertexes :", list_vertexes)
area = calculate_area_Gauss_formula(list_vertexes)
print("Area :", area)
inner_points = calculate_inner_points_Pick_formula(area, steps_walked)
print("Inner points :", inner_points)

print("Part One :", str(None))

print("Part Two :", str(inner_points))
