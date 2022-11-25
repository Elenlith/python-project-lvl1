from random import randint

RULE = 'Find the greatest common divisor of given numbers.'


def find_greatest_common_divisor(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    result = a + b
    return result


def prepare_q_and_a():
    a = randint(1, 100)
    b = randint(1, 100)
    quest = f'{a} {b}'
    r_answ = str(find_greatest_common_divisor(a, b))
    return [quest, r_answ]
