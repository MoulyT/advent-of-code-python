# Advent of code Year 2023 Day 8 solution
# Author = Mouly Taha
# Date = December 2018

import os
import math
from functools import reduce

# Obtener la ruta al directorio actual
dir_path = os.path.dirname(os.path.realpath(__file__))

# Construir la ruta al archivo input.txt en el mismo directorio
file_path = os.path.join(dir_path, "input.txt")
with open(file_path, "r", encoding="utf-8") as input_file:
    input_data = input_file.read()

EXAMPLE_INPUT = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


def parse_input_1(input_string: str):
    network = {}
    steps, _, *rest = input_string.splitlines()
    for line in rest:
        parent, child = line.split(" = ")
        network[parent] = child[1:-1].split(", ")
    return steps, network


def search_exit(directions, network):
    current_positions = [position for position in network if position.endswith("A")]
    steps = []
    max_steps = 1000000
    for current_position in current_positions:
        print("current position", current_position)
        local_directions = directions
        local_steps = 0
        while not current_position.endswith("Z"):
            local_steps += 1
            if local_steps > max_steps:
                raise RuntimeError("Max local_steps reached")
            if local_directions[0] == "L":
                print("going left", local_directions[0])
                print(current_position, "->", network[current_position][0])
                current_position = network[current_position][0]
            else:
                print("going right", local_directions[0])
                print(current_position, "->", network[current_position][1])
                current_position = network[current_position][1]
            local_directions = local_directions[1:] + local_directions[0]
        steps.append(local_steps)

    # while not all(
    #     current_position.endswith("Z") for current_position in current_positions
    # ):
    #     print("current positions", current_positions)

    #     steps += 1
    #     new_current_positions = []
    #     if steps > max_steps:
    #         raise RuntimeError("Max steps reached")

    #     for index, current_position in enumerate(current_positions):
    #         if directions[0] == "L":
    #             print("going left", directions[0])
    #             new_current_positions.append(network[current_position][0])
    #             print(current_position, "->", network[current_position][0])
    #         else:
    #             print("going right", directions[0])
    #             new_current_positions.append(network[current_position][1])
    #             print(current_position, "->", network[current_position][1])
    #     directions = (
    #         directions[1:] + directions[0]
    #     )  # Pones el primero en el final para hacer loop
    #     current_positions = new_current_positions
    return reduce(math.lcm, steps)


instructions, graph = parse_input_1(input_data)
print(search_exit(instructions, graph))

print("Part One : " + str(None))


print("Part Two : " + str(None))
