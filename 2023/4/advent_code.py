# Advent of code Year 2023 Day 4 solution
# Author = Mouly Taha
# Date = December 2018

import os
from typing import Set
import array
import time

# Obtener la ruta al directorio actual
dir_path = os.path.dirname(os.path.realpath(__file__))

# Construir la ruta al archivo input.txt en el mismo directorio
file_path = os.path.join(dir_path, "input.txt")

with open(file_path, "r", encoding="utf-8") as input_file:
    input_data = input_file.read()

EXAMPLE_INPUT = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

type Set_of_ints = Set[int]
type Card = tuple[Set_of_ints, Set_of_ints]
type Cards = tuple[Card, ...]


def parse_input(input_string: str) -> Cards:
    cards = input_string.splitlines()
    parsed_cards = []
    for card in cards:
        _, card_data = card.split(":")
        winning_numbers_str, numbers_you_have_str = card_data.split("|")
        winning_numbers = set(map(int, winning_numbers_str.strip().split()))
        numbers_you_have = set(map(int, numbers_you_have_str.strip().split()))
        parsed_cards.append((winning_numbers, numbers_you_have))
    return tuple(parsed_cards)


def get_how_many_winning_numbers(card: Card) -> int:
    winning_numbers, numbers_you_have = card
    return len(winning_numbers & numbers_you_have)


def get_points(number_of_winning_numbers: int) -> int:
    return 2 ** (number_of_winning_numbers - 1) if number_of_winning_numbers > 0 else 0


def calculate_points(cards: Cards) -> int:
    total = 0
    for card in cards:
        total += get_points(get_how_many_winning_numbers(card))
    return total


print("Part One : " + str(calculate_points(parse_input(input_data))))


def calculate_number_of_scratch_cards(cards: Cards) -> int:
    count_of_scratch_cards = array.array("i", [1] * 208)
    for card_number, card in enumerate(cards):
        winning_numbers = get_how_many_winning_numbers(card)
        if winning_numbers == 0:
            continue
        for i in range(winning_numbers):
            count_of_scratch_cards[card_number + 1 + i] += count_of_scratch_cards[
                card_number
            ]

    return sum(count_of_scratch_cards)


# Medir el tiempo de Part Two
start_time = time.time()
part_two_result = calculate_number_of_scratch_cards(parse_input(input_data))
end_time = time.time()
print("Part Two : " + str(part_two_result))
print("Tiempo de ejecución de Part Two: " + str(end_time - start_time) + " segundos")
