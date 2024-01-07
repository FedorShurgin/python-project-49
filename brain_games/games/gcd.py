from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_round():
    random_number_1 = randint(1, 50)
    random_number_2 = randint(1, 50)
    question = f'{random_number_1} {random_number_2}'
    answer = calc_gcd(random_number_1, random_number_2)
    return question, answer


def calc_gcd(number_1, number_2):
    while number_1 != number_2:
        if number_1 > number_2:
            number_1 = number_1 - number_2
        else:
            number_2 = number_2 - number_1
    return number_2