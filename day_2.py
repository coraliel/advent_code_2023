# Day 2 advent calendar

game_file = './input.txt'

file1 = open(game_file, 'r')
lines = file1.readlines()

inputs = {'red': 12, 'green': 13, 'blue': 14}


def build_game_dict():
    games_result = {}
    for line in lines:
        game_number = line.split(":")[0]
        game_party = line.split(":")[1]
        game_rounds = game_party.split(";")
        if game_number not in games_result:
            games_result.update({game_number: {'blue': [], 'red': [], 'green': []}})
        for game_round in game_rounds:
            games_set = game_round.split(",")
            for game in games_set:
                if 'blue' in game:
                    games_result[game_number]['blue'].append(int(game.split()[0]))
                if 'green' in game:
                    games_result[game_number]['green'].append(int(game.split()[0]))
                if 'red' in game:
                    games_result[game_number]['red'].append(int(game.split()[0]))
    return games_result


def get_possible_games(all_games):
    valid_game = 0
    for game in all_games:
        g = all_games[game]
        valid = True
        for colour, number in inputs.items():
            print(colour, number)
            if colour in g and any(number <= int(num) for num in g[colour]):
                valid = False
                continue
        if valid:
            valid_game += int(game.split()[1])

    print(valid_game)


def get_minimum_cubes_for_one_game(all_games):
    sum_of_power = 0
    for game in all_games:
        max_blue = max(all_games[game]['blue'])
        max_green = max(all_games[game]['green'])
        max_red = max(all_games[game]['red'])
        multiply_colours = int(max_blue) * int(max_green) * int(max_red)
        sum_of_power += multiply_colours
    print(sum_of_power)


games = build_game_dict()
get_minimum_cubes_for_one_game(games)
