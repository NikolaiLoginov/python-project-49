from random import randint


GAME_RULE_TEXT = 'What number is missing in the progression?'
PROGRESSION_LENGHT = 10
INITIAL_TERM_MIN = 1
INITIAL_TERM_MAX = 20
COMMON_DIFF_MIN = 1
COMMON_DIFF_MAX = 5
HIDE_LOWER_BOUND = 0


def get_question_and_answer():
    initial_term = randint(INITIAL_TERM_MIN, INITIAL_TERM_MAX)
    common_difference = randint(COMMON_DIFF_MIN, COMMON_DIFF_MAX)
    progression = make_progression(initial_term, common_difference)
    hide_position = randint(HIDE_LOWER_BOUND, len(progression) - 1)
    question, correct_answer = make_question_and_answer(
        progression, hide_position
    )
    return question, correct_answer


def make_progression(initial_term, common_difference):
    question_list = [initial_term]
    for n in range(PROGRESSION_LENGHT - 1):
        question_list.append(question_list[n] + common_difference)
    return question_list


def make_question_and_answer(question_list, hide_position):
    hidden_number = question_list[hide_position]
    question_list[hide_position] = '..'
    question = ' '.join(str(number) for number in question_list)
    return question, hidden_number
