# Advent of code Year 2023 Day 5 solution
# Author = Mouly Taha
# Date = December 2018

import os
from typing import List, Callable, Dict, Tuple
import time

start_time = time.time()
# Obtener la ruta al directorio actual
dir_path = os.path.dirname(os.path.realpath(__file__))

# Construir la ruta al archivo input.txt en el mismo directorio
file_path = os.path.join(dir_path, "input.txt")
with open(file_path, "r", encoding="utf-8") as input_file:
    input_data = input_file.read()

EXAMPLE_INPUT = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def create_mapping_function(input_list: List[str]) -> Callable[[int], int]:
    ranges = []
    for item in input_list[1:]:
        end, start, offset = map(int, item.split())
        source_range = range(start, start + offset)
        destination_range = range(end, end + offset)
        ranges.append((source_range, destination_range, end - start))

    def mapping_function(n: int) -> int:
        for source_range, destination_range, shift in ranges:
            if n in source_range:
                return n + shift
        return n

    return mapping_function


def create_mapping_function_reversed(input_list: List[str]) -> Callable[[int], int]:
    ranges = []
    for item in input_list[:-1]:
        end, start, offset = map(int, item.split())
        source_range = range(start, start + offset)
        destination_range = range(end, end + offset)
        ranges.append((source_range, destination_range, end - start))

    def mapping_function(n: int) -> int:
        for source_range, destination_range, shift in ranges:
            if n in destination_range:
                return n - shift
        return n

    return mapping_function


def get_end_points(input_list: List[str]) -> List[int]:
    """
    Obtiene los puntos críticos de una lista de especificaciones.

    Parámetros:
    input_list (List[str]): Una lista donde el primer elemento es una etiqueta descriptiva
                            y los elementos siguientes son strings que representan rangos de mapeo.
                            Cada string de rango tiene el formato 'end start offset', donde
                            'start' y 'end' definen los rangos de inicio y final, y 'offset' es la longitud del rango.

    Retorna:
    List[int]: Una lista de los puntos críticos de la lista de especificaciones.
    """
    end_points = []
    for item in input_list[:-1]:
        end, start, offset = map(int, item.split())
        end_points.append(end - 1)
        end_points.append(end)
        end_points.append(end + offset)
        end_points.append(end + offset + 1)
    return end_points


def parse_input(input_string: str) -> Tuple[List[str], Dict[str, Callable[[int], int]]]:
    """
    Procesa un string de entrada y crea funciones de mapeo basadas en las especificaciones dadas.

    Esta función divide el string de entrada en bloques de texto separados por líneas vacías,
    interpreta cada bloque como una lista de especificaciones para una función de mapeo,
    y crea un diccionario de estas funciones.

    Parámetros:
    input_string (str): El string de entrada que contiene las especificaciones de mapeo.

    Retorna:
    Tuple[List[str], Dict[str, Callable[[int], int]]]: Un tuple conteniendo:
        - Una lista de semillas.
        - Un diccionario de funciones de mapeo.
    """
    raw_list = input_string.splitlines()
    buffer = []
    mappings = {}
    for line in raw_list[1:]:
        if line == "":
            if buffer:
                mapping_function = create_mapping_function(buffer)
                function_name = (
                    buffer[0].replace("-", "_").replace(" ", "_").replace(":", "")
                )
                mappings[function_name] = mapping_function
                buffer = []
        else:
            buffer.append(line)
    if buffer:
        mapping_function = create_mapping_function(buffer)
        function_name = buffer[0].replace("-", "_").replace(" ", "_").replace(":", "")
        mappings[function_name] = mapping_function
    seeds = list(map(int, raw_list[0].split(":")[1].split()))
    print(seeds)
    print(mappings)

    return seeds, mappings


def parse_input_part_2(
    input_string: str,
) -> Tuple[List[str], Dict[str, Callable[[int], int]]]:
    raw_list = input_string.splitlines()
    buffer = []
    mappings = {}
    end_points = []
    for line in raw_list[::-1]:
        if line == "":
            if buffer:
                mapping_function = create_mapping_function_reversed(buffer)
                critical_points_in_wrong_domain = get_end_points(buffer)
                end_points.extend(critical_points_in_wrong_domain)
                end_points = [mapping_function(point) for point in end_points]
                function_name = (
                    buffer[len(buffer) - 1]
                    .replace("-", "_")
                    .replace(" ", "_")
                    .replace("_reverse_", "")
                )
                mappings[function_name] = mapping_function
                buffer = []
        else:
            buffer.append(line)
    seed_values = raw_list[0].split(":")[1].split()
    seeds = [
        range(int(seed_values[i]), int(seed_values[i]) + int(seed_values[i + 1]) + 1)
        for i in range(0, len(seed_values), 2)
    ]
    end_points = sorted(list(set(end_points)))

    def is_in_seeds(point):
        return any(point in seed_range for seed_range in seeds)

    filtered_end_points = list(filter(is_in_seeds, end_points))
    # print("seeds:", seeds)
    # print("mappings:", mappings.keys())
    # print("end points:", end_points)
    # print("filtered end points:", filtered_end_points)

    return seeds, mappings, filtered_end_points


def get_location(seed: int, mappings: Dict[str, Callable[[int], int]]) -> int:
    print("En get_location recibimos:", seed)
    print("y mappings:", mappings)
    soil = mappings["seed_to_soil_map"](seed)
    fertilizer = mappings["soil_to_fertilizer_map"](soil)
    water = mappings["fertilizer_to_water_map"](fertilizer)
    light = mappings["water_to_light_map"](water)
    temperature = mappings["light_to_temperature_map"](light)
    humidity = mappings["temperature_to_humidity_map"](temperature)
    location = mappings["humidity_to_location_map"](humidity)
    return location


def get_seed(location: int, mappings: Dict[str, Callable[[int], int]]) -> int:
    humidity = mappings["humidity_to_location_reverse_map"](location)
    temperature = mappings["temperature_to_humidity_reverse_map"](humidity)
    light = mappings["light_to_temperature_reverse_map"](temperature)
    water = mappings["water_to_light_reverse_map"](light)
    fertilizer = mappings["fertilizer_to_water_reverse_map"](water)
    soil = mappings["soil_to_fertilizer_reverse_map"](fertilizer)
    seed = mappings["seed_to_soil_reverse_map"](soil)
    return seed


def get_seed_minimum_location(
    seeds: List[int], mappings: Dict[str, Callable[[int], int]]
) -> int:
    seed_locations = [get_location(seed, mappings) for seed in seeds]
    return min(seed_locations)


seed_part_one, mapping_dict = parse_input(input_data)
seed_list, mapping_dict_reversed, critical_points = parse_input_part_2(input_data)

# solution_part_one = get_seed_minimum_location(seed_list, mapping_dict)

solution_part_two = get_seed_minimum_location(critical_points, mapping_dict)
print("Part One : " + str(None))

end_time = time.time()
print("Part Two : " + str(solution_part_two), "in", end_time - start_time, "seconds")
