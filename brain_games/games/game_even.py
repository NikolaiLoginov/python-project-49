import random


def get_question():
    question_text = 'Answer "yes" if the number is even, otherwise answer "no".'
    question = random.randint(1, 100)
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question_text, question, correct_answer

