from random import randint


GAME_RULE_TEXT = 'What is the result of the expression?'
TASK_MIN = 1
TASK_MAX = 3
OPERAND_MIN = 1
OPERAND_MAX = 20


def get_question_and_answer():
    task_index = randint(TASK_MIN, TASK_MAX)
    first_operand = randint(OPERAND_MIN, OPERAND_MAX)
    second_operand = randint(OPERAND_MIN, OPERAND_MAX)
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
