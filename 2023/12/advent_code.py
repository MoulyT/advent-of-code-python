# Advent of code Year 2023 Day 12 solution
# Author = Mouly Taha
# Date = December 2018

import os
import time
from functools import cache

file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "input.txt"
)
with open(file_path, encoding="utf-8") as input_file:
    input_data = input_file.read()

EXAMPLE_INPUT = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def parse_input(input_str: str):
    rows = input_str.splitlines()
    result = []
    for row in rows:
        springs = row.split(" ")[0]
        instructions = tuple(map(int, row.split(" ")[1].split(",")))
        result.append((springs, instructions))
    return result


def unfold_springs(input_list: list[tuple[str, tuple[int, ...]]]):
    unfolded = []
    for springs, instructions in input_list:
        unfolded_springs = "?".join([springs] * 5)
        unfolded_instructions = instructions * 5
        unfolded.append((unfolded_springs, unfolded_instructions))
    return unfolded


def is_possible_springs(springs: str, instructions: tuple[int, ...]):
    damaged_springs = list(filter(None, springs.split(".")))
    result = True
    if len(damaged_springs) != len(instructions):
        return False
    for spring, instruction in zip(damaged_springs, instructions, strict=False):
        if len(spring) != instruction:
            result = False
            break
    return result


@cache
def how_many_possible_springs(
    spring: str,
    instructions: tuple[int, ...],
    index=0,
    block_index=0,
    current_block_length=0,
):
    if index == len(spring):
        if (
            block_index == len(instructions)
            and current_block_length == 0
            or (
                block_index == len(instructions) - 1
                and instructions[block_index] == current_block_length
            )
        ):
            return 1
        else:
            return 0

    ans = 0
    if spring[index] == "." or spring[index] == "?":
        if current_block_length == 0:
            ans += how_many_possible_springs(
                spring, instructions, index + 1, block_index, 0
            )
        elif (
            current_block_length > 0
            and block_index < len(instructions)
            and instructions[block_index] == current_block_length
        ):
            ans += how_many_possible_springs(
                spring, instructions, index + 1, block_index + 1, 0
            )

    if spring[index] == "#" or spring[index] == "?":
        ans += how_many_possible_springs(
            spring,
            instructions,
            index + 1,
            block_index,
            current_block_length + 1,
        )

    return ans


def sum_of_all_possible_springs(
    input_parsed: list[tuple[str, tuple[int, ...]]],
):
    result = 0
    for springs, instructions in input_parsed:
        result += how_many_possible_springs(springs, instructions)
    return result


time1 = time.time()
parsed_input = parse_input(input_data)
print(f"Tiempo para parsear la entrada: {time.time() - time1} segundos")

time2 = time.time()
unfolded_input = unfold_springs(parsed_input)
print(f"Tiempo para desplegar los springs: {time.time() - time2} segundos")

time3 = time.time()
part_one = sum_of_all_possible_springs(unfolded_input)
time4 = time.time()
print("Part One :", str(part_one), "Time :", time4 - time3)

print("Part Two :", str(None))
