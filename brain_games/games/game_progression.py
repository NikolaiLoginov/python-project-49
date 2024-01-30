import random


QUESTION_TEXT = 'What number is missing in the progression?'


def get_question():
    progression = make_progression()
    question, correct_answer = make_question(progression)
    return question, correct_answer


def make_progression():
    progression_length = 10
    start_number = random.randint(1, 20)
    step_number = random.randint(1, 5)
    question_list = [start_number]
    for n in range(progression_length - 1):
        question_list.append(question_list[n] + step_number)
    return question_list


def make_question(question_list):
    hide_position = random.randint(0, len(question_list) - 1)
    hidden_number = question_list[hide_position]
    question_list[hide_position] = '..'
    question = ' '.join(str(number) for number in question_list)
    return question, hidden_number
