# -*- coding: utf-8 -*-
import random
from brain_games import cli

game_description = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def generate_game_data():
    random_number = random.SystemRandom().randint(1, 100)

    question = str(random_number)
    answer = 'yes' if is_even(random_number) else 'no'

    return (question, answer)


def run():
    cli.run_game(game_description, generate_game_data)
