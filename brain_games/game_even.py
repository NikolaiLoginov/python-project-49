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
    score = 0
    while score < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer:')
        if answer == 'yes' and is_even(number):
            print('Correct!')
            score += 1
        elif answer == 'no' and not is_even(number):
            print('Correct!')
            score += 1
        elif answer == 'yes' and not is_even(number):
            print('"yes" is wrong answer ;(. Correct answer was "no".')
            score = 4
        elif answer == 'no' and is_even(number):
            print('"no" is wrong answer ;(. Correct answer was "yes".')
            score = 4
        else:
            score = 4
    if score == 3:
        print(f'Congratulations, {name}!')
    elif score == 4:
        print(f"Let's try again, {name}!")
