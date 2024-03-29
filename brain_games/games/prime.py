from random import randint
from math import sqrt


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    '''
    the function returns two values:
    the question and the result of the function - is_prime().
    '''
    random_number = randint(1, 25)
    question = f'{random_number}'
    answer = 'yes' if is_prime(random_number) else 'no'
    return question, answer


def is_prime(number):
    '''
    the function takes a number and calculates whether it is prime or not.
    '''
    if number <= 1:
        return False
    for element in range(2, int(sqrt(number)) + 1):
        if number % element == 0:
            return False
    return True
