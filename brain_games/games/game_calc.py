import prompt
import random
from brain_games.games.game_even import welcome_user


def question():
    expression = ''
    expression_index = random.randint(1, 3)
    first_operand = random.randint(1,100)
    second_operand = random.randint(1,100)
    answer = 0

    if expression_index == 1:
        expression = f'{first_operand} + {second_operand}'
        answer = first_operand + second_operand
    elif expression_index == 2:
        expression = f'{first_operand} - {second_operand}' 
        answer = first_operand - second_operand
    else:
        expression = f'{first_operand} * {second_operand}'
        answer = first_operand * second_operand
    print(f'Question: {expression}')
    return answer

def game_calc(name):
    print('What is the result of the expression?')    
    for _ in range(3):
        correct_answer = question()
        user_answer = int(prompt.string('Your answer:'))
        if correct_answer == user_answer:
            print(f'Correct!')
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')

    





