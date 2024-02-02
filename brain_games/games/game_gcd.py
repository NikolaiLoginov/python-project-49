import random


GAME_RULE_TEXT = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 100


def get_question_and_answer():
    first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{first_number} {second_number}'
    correct_answer = gcd(first_number, second_number)
    return question, correct_answer


def gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1
