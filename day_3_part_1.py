# Day 3 advent calendar part 1
import re

game_file = './input.txt'

file1 = open(game_file, 'r')
lines = file1.readlines()


def transform_txt_to_list():
    multidimensional_list = []
    for line in lines:
        characters = list(line.strip())
        multidimensional_list.append(characters)
    return multidimensional_list


def look_for_special_char(engine_list):
    special_characters_pattern = re.compile(r'[^\w\s.]')
    indexes = []
    for row_index, row in enumerate(engine_list):
        for col_index, item in enumerate(row):
            if special_characters_pattern.search(item):
                indexes.append([row_index, col_index])
    return indexes


def look_for_character_near(engine_list, indexes):
    list_of_index_for_digits = []
    for row, index in indexes:
        above_char = above_left = above_right = None
        below_char = below_left = below_right = None
        left_char = right_char = None

        if row > 0:
            above_char = (row - 1, index) if str(engine_list[row - 1][index]).isdigit() else None
            above_left = (row - 1, index - 1) if str(engine_list[row - 1][index - 1]).isdigit() and index - 1 >= 0 else None
            above_right = (row - 1, index + 1) if str(engine_list[row - 1][index + 1]).isdigit() and index + 1 < len(
                engine_list[row - 1]) else None

        if row < len(engine_list) - 1:
            below_char = (row + 1, index) if str(engine_list[row + 1][index]).isdigit() else None
            below_left = (row + 1, index - 1) if str(engine_list[row + 1][index - 1]).isdigit() and index - 1 >= 0 else None
            below_right = (row + 1, index + 1) if str(engine_list[row + 1][index + 1]).isdigit() and index + 1 < len(
                engine_list[row + 1]) else None

        if index > 0:
            left_char = (row, index - 1) if str(engine_list[row][index - 1]).isdigit() else None

        if index < len(engine_list[row]) - 1:
            right_char = (row, index + 1) if str(engine_list[row][index + 1]).isdigit() else None

        list_of_index_for_digits.append([above_left, above_char, above_right, below_left, below_char, below_right, left_char, right_char])
    return list_of_index_for_digits


def find_whole_number(engine_list, indexes):
    result = []

    for index in indexes:
        for ind in index:
            if ind is not None:
                row, col = ind
                digits = ''
                # Skip consecutive indexes within the same row
                if 'prev_col' in locals() and row == prev_row and col == prev_col + 1:
                    prev_col, prev_row = col, row
                    continue

                # Check left side
                for i in range(col, -1, -1):
                    if i >= 0 and str(engine_list[row][i]).isdigit():
                        digits = str(engine_list[row][i]) + digits
                    else:
                        break

                # Check right side
                for i in range(col + 1, len(engine_list[row])):
                    if i < len(engine_list[row]) and str(engine_list[row][i]).isdigit():
                        digits += str(engine_list[row][i])
                    else:
                        break

                result.append(int(digits))

                # Update prev_col and prev_row
                prev_col, prev_row = col, row

    return result


def main():
    engine_list = transform_txt_to_list()
    indexes = look_for_special_char(engine_list)
    list_of_indexes = look_for_character_near(engine_list, indexes)
    digits = find_whole_number(engine_list, list_of_indexes)
    print(sum(digits))


main()
