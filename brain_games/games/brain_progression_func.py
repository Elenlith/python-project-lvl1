from random import randint

RULE = 'What number is missing in the progression?'


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


def hide_progr_elem(progression, hidden_element):
    index = progression.index(hidden_element)
    progression_with_hidden_element = progression
    progression_with_hidden_element[index] = ".."
    return progression_with_hidden_element


def prep_progr_list():
    progr_l = []
    i = 1
    while i <= 3:
        pr = create_progression()
        hid_el = find_element_to_hide(pr)
        progr_l.append(pr)
        progr_l.append(hid_el)
        i += 1
    return progr_l


def prepare_questions(progr_l):
    quest = []
    i = 0
    j = 0
    while i <= 2:
        progr = progr_l[j]
        hid_el = progr_l[j + 1]
        question = ' '.join(map(str, hide_progr_elem(progr, hid_el)))
        quest.append(question)
        i += 1
        j += 2
    return quest


def prepare_answers(progr_l):
    r_answ = []
    i = 0
    j = 1
    while i <= 2:
        answ = str(progr_l[j])
        r_answ.append(answ)
        i += 1
        j += 2
    return r_answ
