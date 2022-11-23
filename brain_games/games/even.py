from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def prepare_question():
    random_number = randint(1, 100)
    return random_number


def check_parity(number):
    if number % 2 == 0:
        r_answ = True
    else:
        r_answ = False
    return r_answ


def prepare_answer(quest):
    if check_parity(quest):
        r_answ = 'yes'
    else:
        r_answ = 'no'
    return r_answ
