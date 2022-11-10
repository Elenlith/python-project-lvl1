from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_number():
    random_number = randint(1, 100)
    return random_number


def check_parity(number):
    if number % 2 == 0:
        r_answ = 'yes'
    else:
        r_answ = 'no'
    return r_answ
