from random import randint

RULE = 'What number is missing in the progression?'


def prepare_q_and_a():
    progression = []
    first_number = randint(1, 100)
    delta = randint(1, 10)
    number_of_items = randint(8, 12)
    number = first_number
    i = 1
    while i <= number_of_items:
        progression.append(number)
        i += 1
        number += delta
    n = len(progression) - 1
    index = randint(0, n)
    r_answ = str(progression[index])
    progression[index] = ".."
    question = ' '.join(map(str, progression))
    return [question, r_answ]
