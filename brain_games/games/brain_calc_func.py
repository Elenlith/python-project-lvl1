from random import randint, choice

RULE = 'What is the result of the expression?'


def make_expression():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    operators = ['+', '-', '*']
    chosen_operator = choice(operators)
    expression = f'{str(number_1)} {chosen_operator} {str(number_2)}'
    return expression


def make_calculation(expression):
    chars = expression.split()
    number_1 = int(chars[0])
    op = chars[1]
    number_2 = int(chars[2])
    if op == '+':
        result = str(number_1 + number_2)
    elif op == '-':
        result = str(number_1 - number_2)
    else:
        result = str(number_1 * number_2)
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
