import random


GAME_RULE_TEXT = ('Answer "yes" if given number is prime.'
                  ' Otherwise answer "no".')
MIN_NUMBER = 1
MAX_NUMBER = 100


def get_question_and_answer():
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def is_prime(number):
    if number <= 1:
        return False
    for n in range(2, number):
        if number % n == 0:
            return False
    return True
