from random import randint, choice

RULE = 'What is the result of the expression?'


def make_expression():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    operators = [' + ', ' - ', ' * ']
    chosen_operator = choice(operators)
    expression = str(number_1) + chosen_operator + str(number_2)
    return expression


def make_calculation(expression):
    result = str(eval(expression))
    return result
