import random


QUESTION_TEXT = 'What is the result of the expression?'


def get_question():
    task_index = random.randint(1, 3)
    first_operand = random.randint(1, 20)
    second_operand = random.randint(1, 20)
    if task_index == 1:
        question = f'{first_operand} + {second_operand}'
        correct_answer = first_operand + second_operand
    elif task_index == 2:
        question = f'{first_operand} - {second_operand}'
        correct_answer = first_operand - second_operand
    else:
        question = f'{first_operand} * {second_operand}'
        correct_answer = first_operand * second_operand
    return question, correct_answer
