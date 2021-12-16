# -*- coding: utf-8 -*-

from brain_games import cli

game_description = 'What number is missing in the progression?'
length_of_progression = 10


def generate_arithmetic_progression(length, first, difference):
    return [first + i * difference for i in range(length)]


def generate_game_data():
    first_term = cli.get_randint(1, 20)
    difference_between_terms = cli.get_randint(1, 30)
    index_of_hidden_term = cli.get_randint(0, length_of_progression - 1)

    progression = generate_arithmetic_progression(
        length_of_progression, first_term, difference_between_terms)

    answer = str(progression[index_of_hidden_term])
    progression[index_of_hidden_term] = '..'

    question = ' '.join(str(e) for e in progression)

    return (question, answer)


def run():
    cli.run_game(game_description, generate_game_data)
