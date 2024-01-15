from random import randint
from math import sqrt


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    random_number = randint(1, 25)
    question = f'{random_number}'
    answer = 'yes' if is_prime(random_number) else 'no'
    return question, answer


def is_prime(number):
    if number <= 1:
        return False
    for element in range(2, sqrt(number) + 1):
        if number % element == 0:
            return False
    return True
