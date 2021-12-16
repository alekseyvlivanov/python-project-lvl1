# -*- coding: utf-8 -*-

import random
import prompt

number_of_attempts = 3


def get_randint(no_less, no_more):
    return random.SystemRandom().randint(no_less, no_more)


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))

    return name


def run_game(game_description, generate_game_data):
    name = welcome_user()
    print(game_description)

    attempt = 1
    while attempt <= number_of_attempts:
        (question, answer) = generate_game_data()

        print('Question: {}'.format(question))

        user_answer = prompt.string('Your answer: ')

        if (user_answer.lower() != answer):
            template = '"{}" is wrong answer ;(. Correct answer was "{}".'
            print(template.format(user_answer, answer))
            print("Let's try again, {}!".format(name))

            return

        print('Correct!')
        attempt += 1

    print('Congratulations, {}!'.format(name))
