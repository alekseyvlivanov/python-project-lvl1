# -*- coding: utf-8 -*-
import random
from brain_games import cli

game_description = 'What is the result of the expression?'
max_number = 100

game_operations = {
    '+': (lambda x, y: x + y),
    '-': (lambda x, y: x - y),
    '*': (lambda x, y: x * y),
}
operators = list(game_operations.keys())


def generate_game_data():
    print(operators)

    number_one = random.SystemRandom().randint(1, max_number)
    number_two = random.SystemRandom().randint(1, max_number)
    operator = operators[random.SystemRandom().randint(0, len(operators) - 1)]

    question = '{} {} {}'.format(number_one, operator, number_two)
    answer = str(game_operations[operator](number_one, number_two))

    return (question, answer)


def run():
    cli.run_game(game_description, generate_game_data)
