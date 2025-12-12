# Advent of code Year 2023 Day 3 solution
# Author = Mouly Taha
# Date = December 2018

import os
import re
from math import prod
from typing import Literal

# Obtener la ruta al directorio actual
dir_path = os.path.dirname(os.path.realpath(__file__))

# Construir la ruta al archivo input.txt en el mismo directorio
file_path = os.path.join(dir_path, "input.txt")

with open(file_path, encoding="utf-8") as input_file:
    input_data = input_file.read()


def get_map(input_string: str):
    """
    Splits a multiline string into individual lines.

    Returns:
        tuple[str, ...]: Tuple of strings representing map rows.

    """
    return tuple(input_string.splitlines())


input_map = get_map(input_data)


def find_number(
    map_of_rows: tuple[str, ...],
) -> list[dict[Literal["number", "row", "column"], int]]:
    """
    Finds all numbers in a map and returns their coordinates.

    Args:
        map_of_rows: Tuple of strings representing map rows.

    Returns:
        List of dicts with keys:
            - "number": Found number (int)
            - "row": Row index (int)
            - "column": Starting column index (int)
    """
    reg_exp_number = r"\d+"
    numbers_coordinates = []
    for row_index, row in enumerate(map_of_rows):
        numbers_in_row = re.finditer(reg_exp_number, row)
        for match in numbers_in_row:
            numbers_coordinates.append(
                {
                    "number": int(match.group()),
                    "row": row_index,
                    "column": match.start(),
                }
            )
    return numbers_coordinates


def is_part_number(
    number_coordinates: dict[Literal["number", "row", "column"], int],
    map_of_rows: tuple[str, ...],
):
    """
    Checks if a number has adjacent non-digit, non-period chars.

    Args:
        number_coordinates: Dict with number, row, and column.
        map_of_rows: Tuple of strings representing map rows.

    Returns:
        bool: True if symbol found adjacent to number.
    """
    row = number_coordinates["row"]
    column = number_coordinates["column"]
    number = number_coordinates["number"]
    length = len(str(number_coordinates["number"]))
    rows_of_map = len(map_of_rows)
    columns_of_map = len(map_of_rows[0])
    # print("Checking if number is in the coordinates:")
    # Obtener el fragmento de la fila que corresponde a las coordenadas dadas
    found_fragment = map_of_rows[row][column : column + length]
    # print(
    #     "In that coordine we have: "
    #     + found_fragment
    #     + " and we are looking for: "
    #     + str(number)
    # )

    # Verify the number is at the given coordinates
    if found_fragment != str(number):
        raise ValueError(
            f"Expected {number} at row {row}, column {column}, "
            f"found '{found_fragment}'."
        )

    targets_coordinates = get_adyacent_coordinates(
        row, column, length, rows_of_map, columns_of_map
    )
    # print(
    #     "Target coordinates input: "
    #     + "number: "
    #     + str(number)
    #     + "row: "
    #     + str(row)
    #     + ", column: "
    #     + str(column)
    #     + ", length: "
    #     + str(length)
    #     + ", rows_of_map: "
    #     + str(rows_of_map)
    #     + ", columns_of_map: "
    #     + str(columns_of_map)
    # )
    # print("In that row we have: " + map_of_rows[row])
    # print("Targets coordinates: " + str(targets_coordinates))
    reg_exp_anything_but_number_or_period = r"[^0-9.]"
    for target_coordinates in targets_coordinates:
        target_row, target_column = target_coordinates
        target = map_of_rows[target_row][target_column]
        if re.search(reg_exp_anything_but_number_or_period, target):
            return True
    return False


def get_adyacent_coordinates(row, column, length, rows_of_map, columns_of_map):
    target_coordinates = []
    for target_row in range(row - 1, row + 2):
        for target_column in range(column - 1, column + length + 1):
            if (
                target_row >= 0
                and target_column >= 0
                and target_row < rows_of_map
                and target_column < columns_of_map
                and not (
                    target_row == row
                    and column <= target_column < column + length
                )
            ):
                target_coordinates.append([target_row, target_column])
    return target_coordinates


def sum_part_numbers(
    number_coordinates: list[dict[Literal["number", "row", "column"], int]],
    map_of_rows: tuple[str, ...],
):
    """
    Sums numbers that are part numbers.

    Args:
        number_coordinates: List of dicts with number coordinates.
        map_of_rows: Tuple of strings representing map rows.

    Returns:
        int: Sum of part numbers.
    """
    result = 0
    part_numbers = []
    not_part_numbers = []
    for number_coordinate in number_coordinates:
        if is_part_number(number_coordinate, map_of_rows):
            result += number_coordinate["number"]
            part_numbers.append(number_coordinate["number"])

        else:
            not_part_numbers.append(number_coordinate)

    # print("Part numbers: " + str(part_numbers))
    # sum_part_numbers = sum(part_numbers)
    # print("Sum of part numbers: " + str(sum_part_numbers))
    # print("Not part numbers: ", not_part_numbers)
    # print("Result: " + str(result))
    # print(
    #     "is part number 11?",
    #     is_part_number({"number": 11, "row": 77, "column": 71}, map_of_rows),
    #     is_part_number({"number": 11, "row": 81, "column": 106}, map_of_rows),
    # )
    return result


solution_part_one = sum_part_numbers(find_number(input_map), input_map)

print("Part One : " + str(solution_part_one))


def find_asterisk(
    map_of_rows: tuple[str, ...],
) -> list[dict[Literal["symbol", "row", "column"], int | str]]:
    """
    Finds all asterisks in a map and returns their coordinates.

    Args:
        map_of_rows: Tuple of strings representing map rows.

    Returns:
        List of dicts with keys:
            - "symbol": The asterisk symbol (str)
            - "row": Row index (int)
            - "column": Column index (int)
    """
    reg_exp_asterisk = r"\*"
    asterisk_coordinates = []
    for row_index, row in enumerate(map_of_rows):
        numbers_in_row = re.finditer(reg_exp_asterisk, row)
        for match in numbers_in_row:
            asterisk_coordinates.append(
                {
                    "symbol": match.group(),
                    "row": row_index,
                    "column": match.start(),
                }
            )
    return asterisk_coordinates


def is_gear(
    asterisk_coordinates: dict[Literal["symbol", "row", "column"], int | str],
    map_of_rows: tuple[str, ...],
):
    row: int = asterisk_coordinates["row"]  # type: ignore
    column: int = asterisk_coordinates["column"]  # type: ignore

    # Check if the asterisk is in the coordinates given
    found_fragment = map_of_rows[row][column]
    if found_fragment != str(asterisk_coordinates["symbol"]):
        raise ValueError(
            f"Expected * at row {row}, column {column}, "
            f"found '{found_fragment}'."
        )

    adjacent_numbers = set()
    pattern = re.compile(r"\d+")

    # Revisa todas las posiciones adyacentes incluyendo diagonales
    for r in range(row - 1, row + 2):
        for c in range(column - 1, column + 2):
            if r == row and c == column:
                continue  # Salta la posición del asterisco
            if 0 <= r < len(map_of_rows) and 0 <= c < len(map_of_rows[r]):
                for match in pattern.finditer(map_of_rows[r]):
                    if match.start() <= c < match.end():
                        adjacent_numbers.add(int(match.group()))

    return adjacent_numbers if len(adjacent_numbers) == 2 else None


def calculate_gear_ratio(asterisk_coordinates, map_of_rows):
    result = 0
    for asterisk_coordinate in asterisk_coordinates:
        gear_numbers = is_gear(asterisk_coordinate, map_of_rows)
        if gear_numbers:
            result += prod(gear_numbers)

    return result


gear_ratio = calculate_gear_ratio(find_asterisk(input_map), input_map)

print("Part Two : " + str(gear_ratio))
