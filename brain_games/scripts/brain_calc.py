from random import randint, choice
from operator import add, mul, sub
import prompt
from brain_games.cli import welcome_user


def brain_calc():
    number_of_iterations = 0
    print('brain-even\n')
    name = welcome_user()
    print('What is the result of the expression?')
    while number_of_iterations < 3:
        rn_num_1 = randint(1, 25)
        rn_num_2 = randint(1, 25)
        list_of_operators = ['+', '-', '*']
        random_operators = choice(list_of_operators)
        if random_operators == '+':
            print(f'Question: {rn_num_1} + {rn_num_2}')
            question = prompt.string('Your answer: ')
            if int(question) == add(rn_num_1, rn_num_2):
                print('Correct!')
                number_of_iterations += 1
            else:
                print(f"{question} is wrong answer ;(. Correct answer was {add(rn_num_1, rn_num_2)}.")  # noqa: E501
                print(f"Let's try again, {name}")
                break
        if random_operators == '*':
            print(f'Question: {rn_num_1} * {rn_num_2}')
            question = prompt.string('Your answer: ')
            if int(question) == mul(rn_num_1, rn_num_2):
                print('Correct!')
                number_of_iterations += 1
            else:
                print(f"{question} is wrong answer ;(. Correct answer was {add(rn_num_1, rn_num_2)}.")  # noqa: E501
                print(f"Let's try again, {name}")
                break
        if random_operators == '-':
            print(f'Question: {rn_num_1} - {rn_num_2}')
            question = prompt.string('Your answer: ')
            if int(question) == sub(rn_num_1, rn_num_2):
                print('Correct!')
                number_of_iterations += 1
            else:
                print(f"{question} is wrong answer ;(. Correct answer was {add(rn_num_1, rn_num_2)}.")  # noqa: E501
                print(f"Let's try again, {name}")
                break
    if number_of_iterations == 3:
        print(f'Congratulations, {name}!')
