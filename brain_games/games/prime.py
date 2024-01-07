from random import randint
from math import sqrt


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    random_number = randint(1, 25)
    question = f'{random_number}'
    answer = is_prime(random_number)
    return question, answer


def is_prime(number):
    if number <= 1:
        return 'no'
    number_sqrt = int(sqrt(number))
    divisors = range(2, (number_sqrt + 1))
    for element in divisors:
        if number % element == 0:
            return 'no'
    return 'yes'
