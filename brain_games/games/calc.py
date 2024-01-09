from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'


def generate_round():
    rn_num_1 = randint(1, 25)
    rn_num_2 = randint(1, 25)
    list_of_operators = ['+', '-', '*']
    random_operators = choice(list_of_operators)
    question = f'{rn_num_1} {random_operators} {rn_num_2}'
    answer = is_calc(rn_num_1, rn_num_2, random_operators)
    return question, answer


def is_calc(num_1, num_2, operator):
    if operator == '+':
        return str(num_1 + num_2)
    if operator == '-':
        return str(num_1 - num_2)
    if operator == '*':
        return str(num_1 * num_2)
