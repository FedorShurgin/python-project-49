from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    random_number = randint(1, 21)
    question = f'{random_number}'
    answer = 'yes' if is_even(random_number) else 'no'
    return question, answer


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
