import prompt


def welcome_user():
    '''
    The function implements a greeting.
    '''
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
