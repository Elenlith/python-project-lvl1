from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_number():
    random_number = randint(1, 100)
    return random_number


def is_prime_number_cycle(number):
    right_answer = 'yes'
    i = 2
    while i < number:
        if number % i == 0:
            right_answer = 'no'
            break
        else:
            i += 1
    return right_answer


def is_prime_number(number):
    if number == 1:
        right_answer = 'no'
    elif number == 2:
        right_answer = 'yes'
    else:
        right_answer = is_prime_number_cycle(number)
    return right_answer
