from random import randint, choice

RULE = 'What is the result of the expression?'


def prepare_q_and_a():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    operators = ['+', '-', '*']
    chosen_operator = choice(operators)
    expression = f'{str(number_1)} {chosen_operator} {str(number_2)}'
    if chosen_operator == '+':
        result = str(number_1 + number_2)
    elif chosen_operator == '-':
        result = str(number_1 - number_2)
    else:
        result = str(number_1 * number_2)
    return [expression, result]
