import prompt


def launch_game(get_question, question_text):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(question_text)

    for _ in range(3):
        question, correct_answer = get_question()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if str(user_answer) == str(correct_answer):
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
