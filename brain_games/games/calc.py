from random import randint, choice

RULE = 'What is the result of the expression?'


def prepare_question():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    operators = ['+', '-', '*']
    chosen_operator = choice(operators)
    expression = f'{str(number_1)} {chosen_operator} {str(number_2)}'
    return expression


def prepare_answer(expression):
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
