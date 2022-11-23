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


def prepare_question():
    a = randint(1, 100)
    b = randint(1, 100)
    quest = f'{a} {b}'
    return quest


def prepare_answer(quest):
    chars = quest.split()
    a = int(chars[0])
    b = int(chars[1])
    r_answ = str(find_greatest_common_divisor(a, b))
    return r_answ
