# Advent of code Year 2023 Day 7 solution
# Author = Mouly Taha
# Date = December 2018

import math
import os

# Obtener la ruta al directorio actual
dir_path = os.path.dirname(os.path.realpath(__file__))

# Construir la ruta al archivo input.txt en el mismo directorio
file_path = os.path.join(dir_path, "input.txt")
with open(file_path, encoding="utf-8") as input_file:
    input_data = input_file.read()


EXAMPLE_INPUT = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

ranking_of_cards = "AKQT98765432J"


def parse_input_1(input_string: str):
    lines = input_string.splitlines()
    hand_and_bid = []
    for line in lines:
        hand, bid = line.split()
        hand_and_bid.append((hand, int(bid)))
    return hand_and_bid


def count_most_common_card(hand):
    if len(hand) == 0:
        return "J"
    return max(set(hand), key=hand.count)


def calculate_entropy(hand):
    hand_without_jokers = hand.replace("J", "")
    most_common_card = count_most_common_card(hand_without_jokers)
    joker_hand = hand.replace("J", most_common_card)
    print("joker_hand", joker_hand)
    entropy = -sum(
        prob * math.log(prob)
        for prob in (
            joker_hand.count(card) / len(joker_hand) for card in set(joker_hand)
        )
    )
    print("has entropy", entropy)
    return entropy


def calculate_card_rank(card):
    return ranking_of_cards.index(card)


# def calculate_hand_rank_with_joker(hand):
#     hand_without_jokers = hand.replace("J", "")
#     most_common_card = count_most_common_card(hand_without_jokers)
#     joker_hand = hand.replace("J", most_common_card)
#     return tuple(calculate_card_rank(card) for card in joker_hand)


def order_by_hand(games):
    return sorted(
        games,
        key=lambda game: (
            calculate_entropy(hand := game[0]),
            tuple(calculate_card_rank(card) for card in hand),
        ),
        reverse=True,
    )


def calculate_bid(games):
    return sum(bid * (index + 1) for index, (_, bid) in enumerate(games))


games = parse_input_1(input_data)
print(games)
ordered_games = order_by_hand(games)
print(ordered_games)
total_bid = calculate_bid(ordered_games)


print("Part One : " + str(total_bid))


print("Part Two : " + str(None))
