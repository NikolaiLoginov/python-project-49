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
        if answer == 'yes' and is_even(number):
            print('Correct!')
            status += 1
        elif answer == 'no' and not is_even(number):
            print('Correct!')
            status += 1
        elif answer == 'yes' and not is_even(number):
            print('"yes" is wrong answer ;(. Correct answer was "no".')
            status = 4
        elif answer == 'no' and is_even(number):
            print('"no" is wrong answer ;(. Correct answer was "yes".')
            status = 4
        else:
            status = 4
    if status == 3:
        print(f'Congratulations, {name}!')
    elif status == 4:
        print(f"Let's try again, {name}!")
