from random import randint


def find_greatest_common_divisor(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    res = a + b
    return res


def create_progression():
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
    return progression


def find_element_to_hide(progression):
    n = len(progression) - 1
    index = randint(0, n)
    hidden_element = progression[index]
    return hidden_element


def hide_progression_element(progression, hidden_element):
    index = progression.index(hidden_element, 0, len(progression) - 1)
    progression_with_hidden_element = progression
    progression_with_hidden_element[index] = ".."
    return progression_with_hidden_element
