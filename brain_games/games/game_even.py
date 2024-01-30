import random


QUESTION_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question():
    question = random.randint(1, 100)
    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
