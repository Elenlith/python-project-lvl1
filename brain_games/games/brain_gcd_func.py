from random import randint

RULE = 'Find the greatest common divisor of given numbers.'


def generate_numbers():
    nums_l = []
    i = 0
    while i <= 5:
        a = randint(1, 100)
        nums_l.append(a)
        i += 1
    return nums_l


def find_greatest_common_divisor(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    result = a + b
    return result


def prepare_questions(nums_l):
    quest = []
    i = 0
    j = 0
    while i <= 2:
        numbers = str(nums_l[j]) + ' ' + str(nums_l[j + 1])
        quest.append(numbers)
        i += 1
        j += 2
    return quest


def prepare_answers(nums_l):
    r_answ = []
    i = 0
    j = 0
    while i <= 2:
        answ = str(find_greatest_common_divisor(nums_l[j], nums_l[j + 1]))
        r_answ.append(answ)
        i += 1
        j += 2
    return r_answ
