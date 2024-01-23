import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def check_answer(user_answer, correct_answer):
    if str(user_answer) == str(correct_answer):
        return True
    else:
        return False


def launch_game(get_question):
    name = welcome_user()
    print(get_question()[0])

    for _ in range(3):
        _, question, correct_answer = get_question()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if check_answer(user_answer, correct_answer):
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was "
                f"'{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
