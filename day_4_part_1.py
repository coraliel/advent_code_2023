# 2023 Day 4 advent calendar

scratching_cards = './input.txt'

file1 = open(scratching_cards, 'r')
lines = file1.readlines()


def separate_wining_from_numbers():
    cards = {}
    for line in lines:
        parts = line.split(':')
        card_number = parts[0].strip()
        results, numbers = map(str.strip, parts[1].split('|'))

        # Convert the string representations of lists to actual lists of integers
        first_list = list(map(int, results.split()))
        second_list = list(map(int, numbers.split()))

        if not cards.get(card_number):
            cards.update({card_number: {"results": first_list, "numbers": second_list}})
    return cards


def count_matching_numbers(card_results):
    number_of_matches = {}
    for card in card_results:
        results = set(card_results[card]['results'])
        numbers = set(card_results[card]['numbers'])
        duplicates = results.intersection(numbers)
        if not number_of_matches.get(card):
            number_of_matches.update({card: len(duplicates)})
    return number_of_matches


def calculate_points(number_of_matches):
    total_points = 0
    for match in number_of_matches:
        number = number_of_matches[match]
        print('number', int(number))
        if number == 0:
            final_result = 0
        else:
            final_result = 1
            for digit in range(int(number - 1)):
                final_result *= 2
        total_points += final_result
    return total_points


def main():
    card_results = separate_wining_from_numbers()
    number_of_matches = count_matching_numbers(card_results)

    total_point = calculate_points(number_of_matches)
    print('total point', total_point )


main()
