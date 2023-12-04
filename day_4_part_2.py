# 2023 Day 4 advent calendar part 2
import re

scratching_cards = './input.txt'

file1 = open(scratching_cards, 'r')
lines = file1.readlines()


def separate_wining_from_numbers():
    cards = {}
    for line in lines:
        parts = line.split(':')
        card_number = parts[0].strip()
        digit_in_card_number = ''.join(re.findall(r'\d', card_number))
        results, numbers = map(str.strip, parts[1].split('|'))

        # Convert the string representations of lists to actual lists of integers
        first_list = list(map(int, results.split()))
        second_list = list(map(int, numbers.split()))

        if not cards.get(digit_in_card_number):
            cards.update({digit_in_card_number: {"results": first_list, "numbers": second_list}})
    return cards


def count_matching_numbers(card_results):
    number_of_matches = {}
    for card in card_results:
        results = set(card_results[card]['results'])
        numbers = set(card_results[card]['numbers'])
        duplicates = results.intersection(numbers)
        if not number_of_matches.get(card):
            number_of_matches.update({card: {'points': len(duplicates), 'card_won': 1}})
    return number_of_matches


def calculate_points(number_of_matches):
    total_points = 0
    for match in number_of_matches:
        number = number_of_matches[match]['points']
        if number == 0:
            final_result = 0
        else:
            final_result = 1
            for digit in range(int(number - 1)):
                final_result *= 2
        total_points += final_result
    return total_points


def repeat_calculation(points, card, number_of_matches, times_repeated):
    for _ in range(times_repeated):
        for following_card in range(1, points + 1):
            next_card = str(int(card) + following_card)
            if next_card in number_of_matches:
                number_of_matches[next_card]['card_won'] += 1
    return number_of_matches[card]['card_won']


def get_cards_won(number_of_matches):
    total_card_won = 0
    for card in number_of_matches:
        points = number_of_matches[card]['points']
        for following_card in range(1, points + 1):
            next_card = str(int(card) + following_card)
            if next_card in number_of_matches:
                number_of_matches[next_card]['card_won'] += 1
        repeat_calculation(points, card, number_of_matches, number_of_matches[card]['card_won'] - 1)
        total_card_won += number_of_matches[card]['card_won']
    return total_card_won


def main():
    card_results = separate_wining_from_numbers()
    number_of_matches = count_matching_numbers(card_results)
    # part 1 print number of matches and points
    total_point = calculate_points(number_of_matches)
    print('total points for matches', total_point)
    # part 2 get all cards won originals and copies
    total_card_won = get_cards_won(number_of_matches)
    print('cards won', total_card_won)


main()
