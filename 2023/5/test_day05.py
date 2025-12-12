from .day05 import EXAMPLE_INPUT, parse_input


def test_parse_input_and_mapping_functions():
    seeds, mapping_functions = parse_input(EXAMPLE_INPUT)

    assert seeds == [79, 14, 55, 13], f"Semillas incorrectas: {seeds}"

    #'seed_to_soil_map'
    seed_to_soil_map = mapping_functions["seed_to_soil_map"]
    assert seed_to_soil_map(50) == 52, (
        f"Error en seed_to_soil_map con 50: {seed_to_soil_map(50)}"
    )
    assert seed_to_soil_map(51) == 53, (
        f"Error en seed_to_soil_map con 51: {seed_to_soil_map(51)}"
    )
    assert seed_to_soil_map(52) == 54, (
        f"Error en seed_to_soil_map con 52: {seed_to_soil_map(52)}"
    )
    assert seed_to_soil_map(99) == 51, (
        f"Error en seed_to_soil_map con 99: {seed_to_soil_map(99)}"
    )  # Fuera de rango

    #'soil_to_fertilizer_map'
    soil_to_fertilizer_map = mapping_functions["soil_to_fertilizer_map"]
    assert soil_to_fertilizer_map(15) == 0, (
        f"Error en soil_to_fertilizer_map con 15: {soil_to_fertilizer_map(15)}"
    )
    assert soil_to_fertilizer_map(52) == 37, (
        f"Error en soil_to_fertilizer_map con 52: {soil_to_fertilizer_map(52)}"
    )
    assert soil_to_fertilizer_map(0) == 39, (
        f"Error en soil_to_fertilizer_map con 0: {soil_to_fertilizer_map(0)}"
    )
    assert soil_to_fertilizer_map(100) == 100, (
        f"Error en soil_to_fertilizer_map con 100: {soil_to_fertilizer_map(100)}"
    )  # Fuera de rango

    #'fertilizer_to_water_map'
    fertilizer_to_water_map = mapping_functions["fertilizer_to_water_map"]
    assert fertilizer_to_water_map(53) == 49, (
        f"Error en fertilizer_to_water_map con 53: {fertilizer_to_water_map(53)}"
    )
    assert fertilizer_to_water_map(11) == 0, (
        f"Error en fertilizer_to_water_map con 11: {fertilizer_to_water_map(11)}"
    )
    assert fertilizer_to_water_map(0) == 42, (
        f"Error en fertilizer_to_water_map con 0: {fertilizer_to_water_map(0)}"
    )
    assert fertilizer_to_water_map(7) == 57, (
        f"Error en fertilizer_to_water_map con 7: {fertilizer_to_water_map(7)}"
    )
    assert fertilizer_to_water_map(1000) == 1000, (
        f"Error en fertilizer_to_water_map con 1000: {fertilizer_to_water_map(1000)}"
    )  # Fuera de rango

    # 'water_to_light_map'
    water_to_light_map = mapping_functions["water_to_light_map"]
    assert water_to_light_map(18) == 88, (
        f"Error en water_to_light_map con 18: {water_to_light_map(18)}"
    )
    assert water_to_light_map(25) == 18, (
        f"Error en water_to_light_map con 25: {water_to_light_map(25)}"
    )
    assert water_to_light_map(1000) == 1000, (
        f"Error en water_to_light_map con 1000: {water_to_light_map(1000)}"
    )  # Fuera de rango

    #'light_to_temperature_map'
    light_to_temperature_map = mapping_functions["light_to_temperature_map"]
    assert light_to_temperature_map(77) == 45, (
        f"Error en light_to_temperature_map con 77: {light_to_temperature_map(77)}"
    )
    assert light_to_temperature_map(45) == 81, (
        f"Error en light_to_temperature_map con 45: {light_to_temperature_map(45)}"
    )
    assert light_to_temperature_map(64) == 68, (
        f"Error en light_to_temperature_map con 64: {light_to_temperature_map(64)}"
    )
    assert light_to_temperature_map(1000) == 1000, (
        f"Error en light_to_temperature_map con 1000: {light_to_temperature_map(1000)}"
    )  # Fuera de rango

    #'temperature_to_humidity_map'
    temperature_to_humidity_map = mapping_functions[
        "temperature_to_humidity_map"
    ]
    assert temperature_to_humidity_map(69) == 0, (
        f"Error en temperature_to_humidity_map con 69: {temperature_to_humidity_map(69)}"
    )
    assert temperature_to_humidity_map(0) == 1, (
        f"Error en temperature_to_humidity_map con 0: {temperature_to_humidity_map(0)}"
    )
    assert temperature_to_humidity_map(1000) == 1000, (
        f"Error en temperature_to_humidity_map con 1000: {temperature_to_humidity_map(1000)}"
    )  # Fuera de rango

    #'humidity_to_location_map'
    humidity_to_location_map = mapping_functions["humidity_to_location_map"]
    assert humidity_to_location_map(56) == 60, (
        f"Error en humidity_to_location_map con 56: {humidity_to_location_map(56)}"
    )
    assert humidity_to_location_map(93) == 56, (
        f"Error en humidity_to_location_map con 93: {humidity_to_location_map(93)}"
    )
    assert humidity_to_location_map(1000) == 1000, (
        f"Error en humidity_to_location_map con 1000: {humidity_to_location_map(1000)}"
    )  # Fuera de rango
