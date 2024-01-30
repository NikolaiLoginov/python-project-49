import random


QUESTION_TEXT = ('Answer "yes" if given number is prime.'
                 ' Otherwise answer "no".')


def get_question():
    question = random.randint(1, 100)
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
