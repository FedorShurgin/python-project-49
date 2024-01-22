import prompt
from brain_games.cli import welcome_user


def start_game(game):
    '''
    accepts the results of other functions (question and answer):
    asks a question and compares the answer with the user's answer.
    '''
    number_of_iterations = 0
    name = welcome_user()
    print(game.DESCRIPTION)
    while number_of_iterations < 3:
        generate_question, generate_answer = game.generate_round()
        print(f'Question: {generate_question}')
        answer = prompt.string('Your answer: ')
        if str(answer) == generate_answer:
            print('Correct!')
            number_of_iterations += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{generate_answer}'.")  # noqa: E501
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
