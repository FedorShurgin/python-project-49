from random import randint
import prompt
from brain_games.cli import welcome_user
from math import sqrt


def is_prime(number):
    if number <= 1:
        return 'no'
    number_sqrt = int(sqrt(number))
    divisors = range(2, (number_sqrt + 1))
    for element in divisors:
        if number % element == 0:
            return 'no'
    return 'yes'


def brain_prime():
    number_of_iterations = 0
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while number_of_iterations < 3:
        random_number = randint(1, 25)
        print(f'Question: {random_number}')
        question = prompt.string('Your answer: ')
        if question == is_prime(random_number):
            print('Correct!')
            number_of_iterations += 1
        else:
            print(f"'{question}' is wrong answer ;(. Correct answer was '{is_prime(random_number)}'.")  # noqa: E501
            print(f"Let's try again, {name}!")
            break
    if number_of_iterations == 3:
        print(f'Congratulations, {name}!')
