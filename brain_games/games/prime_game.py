# -*- coding: utf-8 -*-

from brain_games import cli

game_desc = 'Answer "yes" if the given number is prime. Otherwise answer "no".'


def is_prime(num):
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return num > 1


def generate_game_data():
    random_number = cli.get_randint(1, 100)

    question = str(random_number)
    answer = 'yes' if is_prime(random_number) else 'no'

    return (question, answer)


def run():
    cli.run_game(game_desc, generate_game_data)
