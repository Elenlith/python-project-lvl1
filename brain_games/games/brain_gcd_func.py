from random import randint

RULE = 'Find the greatest common divisor of given numbers.'


def generate_number():
    random_number = randint(1, 100)
    return random_number


def find_greatest_common_divisor(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    result = a + b
    return result
