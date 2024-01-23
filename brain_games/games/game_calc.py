import random


def get_question():
    question_text = 'What is the result of the expression?'
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
    return question_text, question, correct_answer
