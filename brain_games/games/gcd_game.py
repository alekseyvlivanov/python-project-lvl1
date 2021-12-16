# -*- coding: utf-8 -*-

from brain_games import cli

game_desc = 'Find the greatest common divisor of given numbers.'
max_number = 100


def get_gcd(x, y):
    return abs(get_gcd(y, x % y) if y != 0 else x)


def generate_game_data():
    number_one = cli.get_randint(1, max_number)
    number_two = cli.get_randint(1, max_number)

    question = '{} {}'.format(number_one, number_two)
    answer = str(get_gcd(number_one, number_two))

    return (question, answer)


def run():
    cli.run_game(game_desc, generate_game_data)
