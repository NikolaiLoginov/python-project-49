import random


def get_question():
    question_text = 'Find the greatest common divisor of given numbers.'
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    question = f'{first_number} {second_number}'
    correct_answer = gcd(first_number, second_number)
    return question_text, question, correct_answer


def gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1
