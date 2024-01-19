import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def launch_game(get_qustion, check_answer):
    name = welcome_user()
    print(get_qustion()[2])

    for _ in range(3):
        question, correct_answer, _ = get_qustion()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if check_answer(user_answer, correct_answer):
            print('Correct!')
        else:
            print(f'{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.')
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')





    
