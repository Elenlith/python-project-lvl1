from random import randint

RULE = 'What number is missing in the progression?'


def create_progression_with_hidden_elem():
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
    hidden_element = progression[index]
    progression[index] = ".."
    question = ' '.join(map(str, progression))
    question_and_answer = [question, hidden_element]
    return question_and_answer


def prep_progr_list():
    progr_l = []
    i = 1
    while i <= 3:
        pr = create_progression_with_hidden_elem()
        progr_l.append(pr)
        i += 1
    return progr_l


def prepare_questions(progr_l):
    quest = []
    i = 0
    while i <= 2:
        question = str(progr_l[i][0])
        quest.append(question)
        i += 1
    return quest


def prepare_answers(progr_l):
    r_answ = []
    i = 0
    while i <= 2:
        answ = str(progr_l[i][1])
        r_answ.append(answ)
        i += 1
    return r_answ
