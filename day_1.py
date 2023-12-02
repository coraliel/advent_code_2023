# Day 1 advent calendar
import re
calibration_values = './input.txt'
letter_to_number = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
file1 = open(calibration_values, 'r')
lines = file1.readlines()


def extract_numbers(text_line):
    number_letter = '|'.join(list(map(lambda s: f'(?:{s})', letter_to_number.keys())))
    return re.findall(fr'(?=(\d|{number_letter}))', text_line)


def map_to_digit(map_value):
    if map_value in letter_to_number:
        return letter_to_number[map_value]
    return map_value


total = 0
for line in lines:
    numbers = extract_numbers(line)
    # numbers = re.findall(r'\d', line)
    length = len(numbers)
    total += (int(map_to_digit(numbers[0]) + map_to_digit(numbers[length - 1])))

print("Sum of all of the calibration values", total)
