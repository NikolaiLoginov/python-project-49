import random


GAME_RULE_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def get_question_and_answer():
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def is_even(number):
    return number % 2 == 0
