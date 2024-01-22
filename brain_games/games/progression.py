from random import randint, choice


DESCRIPTION = 'What number is missing in the progression?'


def generate_round():
    '''
    the function returns two values:
    result_st - "Arithmetic progression" with a missing character,
    str(rn_elem) - a random missing character.
    '''
    result_str = ''
    progression_list = is_list()
    rn_elem = choice(progression_list)
    rn_index = progression_list.index(rn_elem)
    progression_list[rn_index] = '..'
    for elem in progression_list:
        result_str += str(elem) + ' '
    return result_str, str(rn_elem)


def is_list():
    '''
    the function creates a random "Arithmetic progression"
    '''
    start = randint(5, 25)
    step = randint(3, 7)
    length = randint(5, 10)
    progression_list = []
    for elem in range(length):
        progression_list.append(start)
        start += step
    return progression_list
