# Advent of code Year 2023 Day 6 solution
# Author = Mouly Taha
# Date = December 2018

from functools import reduce
import os
import math

# Obtener la ruta al directorio actual
dir_path = os.path.dirname(os.path.realpath(__file__))

# Construir la ruta al archivo input.txt en el mismo directorio
file_path = os.path.join(dir_path, "input.txt")
with open(file_path, "r", encoding="utf-8") as input_file:
    input_data = input_file.read()

EXAMPLE_INPUT = """Time:      7  15   30
Distance:  9  40  200"""


def parse_input_1(input_string: str):
    lines = input_string.splitlines()
    time = list(map(int, lines[0].split()[1:]))
    distance = list(map(int, lines[1].split()[1:]))
    return {"times": time, "distances": distance}


def parse_input_2(input_string: str):
    lines = input_string.splitlines()
    time = int(lines[0].split(":")[1].replace(" ", ""))
    distance = int(lines[1].split(":")[1].replace(" ", ""))
    return time, distance


race_record = parse_input_2(input_data)

records = parse_input_1(input_data)


def get_races_1(records):
    how_many_ways = []
    for index, (time, distance) in enumerate(
        zip(records["times"], records["distances"])
    ):
        how_many_ways.append(0)
        for time_charging in range(1, time):
            if time_charging * (time - time_charging) > distance:
                how_many_ways[index] += 1
    print(how_many_ways)
    return how_many_ways


def get_races_2(race_record: (int, int)):
    time, distance = race_record
    first_root = math.ceil((-time + math.sqrt(time**2 - 4 * distance)) / (-2))
    second_root = math.floor((-time - math.sqrt(time**2 - 4 * distance)) / (-2))

    return abs(first_root - second_root) + 1


def get_multiplier_1(good_charging_times: list[int]):
    return reduce(lambda x, y: x * y, good_charging_times)


solution_part_one = get_multiplier_1(get_races_1(records))
solution_part_two = get_races_2(race_record)


print("Part One : " + str(solution_part_one))


print("Part Two : " + str(solution_part_two))
