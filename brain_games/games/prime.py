from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prepare_question():
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


def prepare_answer(quest):
    if is_prime_number(quest):
        r_answ = 'yes'
    else:
        r_answ = 'no'
    return r_answ
