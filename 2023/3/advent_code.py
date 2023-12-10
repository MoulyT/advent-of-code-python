# Advent of code Year 2023 Day 3 solution
# Author = Mouly Taha
# Date = December 2018

import os
import re
from typing import List, Dict, Literal, Union
from math import prod

# Obtener la ruta al directorio actual
dir_path = os.path.dirname(os.path.realpath(__file__))

# Construir la ruta al archivo input.txt en el mismo directorio
file_path = os.path.join(dir_path, "input.txt")

with open(file_path, "r", encoding="utf-8") as input_file:
    input_data = input_file.read()


def get_map(input_string: str):
    """
    Esta función toma una cadena de texto con múltiples líneas (input_string) y la divide en líneas individuales.

    Returns:
        tuple[str, ...]: Una tupla donde cada elemento es una string que representa una fila del mapa.

    """
    return tuple(input_string.splitlines())


input_map = get_map(input_data)


def find_number(
    map_of_rows: tuple[str, ...]
) -> List[Dict[Literal["number", "row", "column"], int]]:
    """
    Encuentra todos los números dentro de un mapa representado como una tupla de strings y devuelve sus coordenadas.

    Esta función busca en cada fila del mapa y encuentra todos los números (secuencias de dígitos).
    Devuelve una lista de diccionarios, donde cada diccionario contiene un número encontrado y sus coordenadas (fila y columna).

    Args:
        map_of_rows (tuple[str, ...]): Una tupla de strings, donde cada string representa una fila del mapa.

    Returns:
        List[Dict[Literal["number", "row", "column"], int]]: Una lista de diccionarios. Cada diccionario contiene las claves:
            - "number": El número encontrado (int).
            - "row": El índice de la fila en la que se encontró el número (int).
            - "column": El índice de la columna en la que inicia el número encontrado en la fila (int).
    """
    REG_EXP_NUMBER = r"\d+"
    numbers_coordinates = []
    for row_index, row in enumerate(map_of_rows):
        numbers_in_row = re.finditer(REG_EXP_NUMBER, row)
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
    number_coordinates: Dict[Literal["number", "row", "column"], int],
    map_of_rows: tuple[str, ...],
):
    """
    La función busca alrededor de las coordenadas dadas de un número para ver si hay caracteres que no son dígitos ni puntos (.).

    Args:
        number_coordinates (Dict[Literal["number", "row", "column"], int]): Un diccionario que contiene el número,
            la fila (row) y la columna (column) donde comienza el número en el mapa.
        map_of_rows (tuple[str, ...]): Una tupla de strings, donde cada string representa una fila del mapa.

    Returns:
        bool: True si se encuentra al menos un carácter que no es un dígito ni un punto alrededor del número especificado,
            False en caso contrario.
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

    # Comprobar si el número proporcionado está efectivamente en las coordenadas dadas
    if found_fragment != str(number):
        raise ValueError(
            f"Se esperaba el número {number} en la fila {row}, columna {column}, "
            f"pero se encontró '{found_fragment}'."
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
    REG_EXP_ANYTHING_BUT_NUMBER_OR_PERIOD = r"[^0-9.]"
    for target_coordinates in targets_coordinates:
        target_row, target_column = target_coordinates
        target = map_of_rows[target_row][target_column]
        # print(
        #     f"Target: {target} at row {target_row} and column {target_column} is part of number {number_coordinates['number']} at row {row} and column {column}?",
        #     re.search(REG_EXP_ANYTHING_BUT_NUMBER_OR_PERIOD, target),
        # )
        if re.search(REG_EXP_ANYTHING_BUT_NUMBER_OR_PERIOD, target):
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
            ):
                if not (
                    target_row == row and column <= target_column < column + length
                ):
                    target_coordinates.append([target_row, target_column])
    return target_coordinates


def sum_part_numbers(
    number_coordinates: List[Dict[Literal["number", "row", "column"], int]],
    map_of_rows: tuple[str, ...],
):
    """
    Suma los números que son parte de la solución.

    Args:
        number_coordinates (List[Dict[Literal["number", "row", "column"], int]]): Una lista de diccionarios.
            Cada diccionario contiene las claves:
                - "number": El número encontrado (int).
                - "row": El índice de la fila en la que se encontró el número (int).
                - "column": El índice de la columna en la que inicia el número encontrado en la fila (int).
        map_of_rows (tuple[str, ...]): Una tupla de strings, donde cada string representa una fila del mapa.

    Returns:
        int: La suma de los números que son parte de la solución.
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
    map_of_rows: tuple[str, ...]
) -> List[Dict[Literal["symbol", "row", "column"], Union[int, str]]]:
    """
    Encuentra todos los asteriscos dentro de un mapa representado como una tupla de strings y devuelve sus coordenadas.

    Esta función busca en cada fila del mapa y encuentra todos los asteriscos (secuencias de dígitos).
    Devuelve una lista de diccionarios, donde cada diccionario contiene un número encontrado y sus coordenadas (fila y columna).

    Args:
        map_of_rows (tuple[str, ...]): Una tupla de strings, donde cada string representa una fila del mapa.

    Returns:
        List[Dict[Literal["symbol", "row", "column"], int]]: Una lista de diccionarios. Cada diccionario contiene las claves:
            - "symbol": El número encontrado (int).
            - "row": El índice de la fila en la que se encontró el número (int).
            - "column": El índice de la columna en la que inicia el número encontrado en la fila (int).
    """
    REG_EXP_ASTERISC = r"\*"
    asterisk_coordinates = []
    for row_index, row in enumerate(map_of_rows):
        numbers_in_row = re.finditer(REG_EXP_ASTERISC, row)
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
    asterisk_coordinates: Dict[Literal["symbol", "row", "column"], Union[int, str]],
    map_of_rows: tuple[str, ...],
):
    row = asterisk_coordinates["row"]
    column = asterisk_coordinates["column"]

    # Check if the asterisk is in the coordinates given
    found_fragment = map_of_rows[row][column]
    if found_fragment != str(asterisk_coordinates["symbol"]):
        raise ValueError(
            f"Se esperaba el símbolo * en la fila {row}, columna {column}, "
            f"pero se encontró '{found_fragment}'."
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
