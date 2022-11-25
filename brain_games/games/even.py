from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def check_parity(number):
    if number % 2 == 0:
        r_answ = True
    else:
        r_answ = False
    return r_answ


def prepare_q_and_a():
    random_number = randint(1, 100)
    if check_parity(random_number):
        r_answ = 'yes'
    else:
        r_answ = 'no'
    return [random_number, r_answ]
