# Advent of code Year 2025 Day 1 solution
# Author = Mouly Taha
# Date = December 2025

from pathlib import Path

input_file_path = Path(__file__).parent / "input.txt"
with open(input_file_path, encoding="utf-8") as input_file:
    input_data = input_file.read()


def extract_rotations(str: str) -> tuple[int, ...]:
    string_rotations = tuple(str.split("\n"))
    rotations = []
    for rotation in string_rotations:
        n = int(rotation.replace("R", "").replace("L", "-"))
        rotations.append(n)
    return tuple(rotations)


def apply_rotation(initial_pos: int, rotation: int) -> tuple[int, int]:
    end_pos_extended = initial_pos + rotation

    if rotation > 0:
        zeros_crossed = end_pos_extended // 100
    else:
        zeros_crossed = (initial_pos - 1) // 100 - (end_pos_extended - 1) // 100

    final_position = end_pos_extended % 100

    return (final_position, zeros_crossed)


def count_times_ends_at_zero(rotations: tuple[int, ...]) -> int:
    count = 0
    actual_pos = 50
    for rotation in rotations:
        actual_pos, _ = apply_rotation(actual_pos, rotation)
        if actual_pos == 0:
            count += 1
    return count


def count_times_pass_by_zero(rotations: tuple[int, ...]) -> int:
    count = 0
    actual_pos = 50
    for rotation in rotations:
        actual_pos, zeros_crossed = apply_rotation(actual_pos, rotation)
        count += zeros_crossed
    return count


part_one = count_times_ends_at_zero(extract_rotations(input_data))
part_two = count_times_pass_by_zero(extract_rotations(input_data))

print("Part One :", str(part_one))

print("Part Two :", str(part_two))
