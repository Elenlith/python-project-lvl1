from random import randint, choice

RULE = 'What is the result of the expression?'


def make_expression():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    operators = [' + ', ' - ', ' * ']
    chosen_operator = choice(operators)
    expression = f'{str(number_1)} {chosen_operator} {str(number_2)}'
    return expression


def make_calculation(expression):
    result = str(eval(expression))
    return result


def prepare_questions():
    quest = []
    i = 0
    while i <= 2:
        expr = make_expression()
        quest.append(expr)
        i += 1
    return quest


def prepare_answers(quest):
    r_answ = []
    i = 0
    while i <= 2:
        answ = make_calculation(quest[i])
        r_answ.append(answ)
        i += 1
    return r_answ
