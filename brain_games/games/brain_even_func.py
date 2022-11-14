from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_number():
    random_number = randint(1, 100)
    return random_number


def check_parity(number):
    if number % 2 == 0:
        r_answ = True
    else:
        r_answ = False
    return r_answ


def prepare_questions():
    quest = []
    i = 0
    while i <= 2:
        number = generate_number()
        quest.append(number)
        i += 1
    return quest


def prepare_answers(quest):
    r_answ = []
    i = 0
    while i <= 2:
        if check_parity(quest[i]) is True:
            answ = 'yes'
        else:
            answ = 'no'
        r_answ.append(answ)
        i += 1
    return r_answ
