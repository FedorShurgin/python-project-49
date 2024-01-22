from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    '''
    the function returns two values:
    the question and the result of the function - is_even().
    '''
    random_number = randint(1, 21)
    question = f'{random_number}'
    answer = 'yes' if is_even(random_number) else 'no'
    return question, answer


def is_even(number):
    '''
    the function takes a number and checks whether it is even or not.
    '''
    if number % 2 == 0:
        return True
    else:
        return False
