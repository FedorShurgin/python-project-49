import prompt
from brain_games.cli import welcome_user


def start_game(game):
    number_of_iterations = 0
    name = welcome_user()
    print(game.DESCRIPTION)
    while number_of_iterations < 3:
        generate_question, generate_answer = game.generate_round()
        print(f'Question: {generate_question}')
        answer = prompt.string('Your answer: ')
        if int(answer) == int(generate_answer):
            print('Correct!')
            number_of_iterations += 1
        else:
            print(f"'{int(answer)}' is wrong answer ;(. Correct answer was '{int(generate_answer)}'.")  # noqa: E501
            print(f"Let's try again, {name}!")
            break
    if number_of_iterations == 3:
        print(f'Congratulations, {name}!')
