from random import randint

RULE = 'What number is missing in the progression?'


def prepare_question():
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
    progression[index] = ".."
    question = ' '.join(map(str, progression))
    return question


def prepare_answer(quest):
    global found_index
    progression = quest.split()
    for index, elem in enumerate(progression):
        if elem == "..":
            found_index = index
    if found_index != 0 and found_index != 1:
        delta = int(progression[1]) - int(progression[0])
        hidden_element = int(progression[found_index - 1]) + delta
    else:
        delta = int(progression[4]) - int(progression[3])
        hidden_element = int(progression[found_index + 1]) - delta
    return str(hidden_element)
