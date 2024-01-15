import prompt
import random


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def game_even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    status = 0
    while status < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer:')
        if answer == 'yes':
            if is_even:
                print('Correct!')
                status += 1
            else:
                print('"yes" is wrong answer ;(. Correct answer was "no".')
                status = 4
        else:
            if not is_even:
                print('Correct!')
                status += 1
            else:
                print('"no" is wrong answer ;(. Correct answer was "yes".')
                status = 4
    
        
    if status == 3:
        print(f'Congratulations, {name}!')
    elif status == 4:
        print(f"Let's try again, {name}!")
