from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_number():
    random_number = randint(1, 100)
    return random_number


def is_prime_number(number):
    if number == 1:
        prime_number = False
    elif number == 2:
        prime_number = True
    else:
        prime_number = True
        i = 2
        while i < number:
            if number % i == 0:
                prime_number = False
                break
            else:
                i += 1
    return prime_number


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
        if is_prime_number(quest[i]) is True:
            answ = 'yes'
        else:
            answ = 'no'
        r_answ.append(answ)
        i += 1
    return r_answ
