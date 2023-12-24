from random import randint
import prompt
from brain_games.cli import welcome_user


def brain_even():
    number_of_iterations = 0
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while number_of_iterations < 3:
        random_number = randint(1, 21)
        print(f'Question: {random_number}')
        the_answer_to_the_question = prompt.string('Your answer: ')
        if random_number % 2 == 0 and the_answer_to_the_question == 'yes':
            print('Correct!')
            number_of_iterations += 1
        elif random_number % 2 != 0 and the_answer_to_the_question == 'no':
            print('Correct!')
            number_of_iterations += 1
        else:
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'. \nLet's try again, {name}!")  # noqa: E501
            break
        if number_of_iterations == 3:
            print(f'Congratulations, {name}!')
