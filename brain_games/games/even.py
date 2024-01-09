from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    random_number = randint(1, 21)
    question = f'{random_number}'
    answer = ''
    if random_number % 2 == 0:
        answer = 'yes'
    if random_number % 2 != 0:
        answer = 'no'
    return question, answer
