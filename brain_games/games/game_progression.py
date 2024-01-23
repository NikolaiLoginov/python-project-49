import random


def get_question():
    question_text = 'What number is missing in the progression?'
    progression_length = 10
    hide_position = random.randint(1, progression_length)
    start_number = random.randint(1, 20)
    step_number = random.randint(1, 5)
    question_list = [start_number]  
    question = ''  
    
    for n in range(progression_length - 1):
        question_list.insert(n + 1, question_list[n] + step_number)
    
    correct_answer = question_list.pop(hide_position)
    question_list.insert(hide_position, '..')
    
    question = ' '.join(str(number) for number in question_list)    

    return question_text, question, correct_answer
