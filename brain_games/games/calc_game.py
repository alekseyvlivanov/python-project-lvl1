# -*- coding: utf-8 -*-

from brain_games import cli

game_desc = 'What is the result of the expression?'
max_number = 100

game_operations = {
    '+': (lambda x, y: x + y),
    '-': (lambda x, y: x - y),
    '*': (lambda x, y: x * y),
}
operators = list(game_operations.keys())


def generate_game_data():
    number_one = cli.get_randint(1, max_number)
    number_two = cli.get_randint(1, max_number)
    operator = operators[cli.get_randint(0, len(operators) - 1)]

    question = '{} {} {}'.format(number_one, operator, number_two)
    answer = str(game_operations[operator](number_one, number_two))

    return (question, answer)


def run():
    cli.run_game(game_desc, generate_game_data)
