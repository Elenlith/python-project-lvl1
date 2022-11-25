from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


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


def prepare_q_and_a():
    random_number = randint(1, 100)
    if is_prime_number(random_number):
        r_answ = 'yes'
    else:
        r_answ = 'no'
    return [random_number, r_answ]
