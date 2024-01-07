from random import randint, choice
import prompt
from brain_games.cli import welcome_user


def brain_progression():
    number_of_iterations = 0
    name = welcome_user()
    print('What number is missing in the progression?')
    while number_of_iterations < 3:
        rn_1 = randint(1, 20)
        rn_2 = randint(30, 45)
        rn_3 = randint(2, 7)
        progression_list = list(range(rn_1, rn_2, rn_3))
        if len(progression_list) == 10:
            rn_elem = choice(progression_list)
            rn_index = progression_list.index(rn_elem)
            progression_list[rn_index] = '..'
            result_str = ''
            for elem in progression_list:
                result_str += str(elem) + ' '
            print(f'Question: {result_str.rstrip()}')
            question = prompt.string('Your answer: ')
            if int(question) == rn_elem:
                print('Correct!')
                number_of_iterations += 1
            else:
                print(f"'{question}' is wrong answer ;(. Correct answer was '{rn_elem}'.")  # noqa: E501
                print(f"Let's try again, {name}!")
                break
        if number_of_iterations == 3:
            print(f'Congratulations, {name}!')
