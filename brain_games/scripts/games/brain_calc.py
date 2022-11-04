from random import randint, choice
from brain_games.common_functions import welcome_user, get_user_name, say_hello, explain_game_rules, ask_question, get_answer
from brain_games.common_functions import check_answer, respond_to_wrong_answer, respond_to_correct_answer, congratulate_user


def main():
    welcome_user()
    name = get_user_name()
    say_hello()
    explain_game_rules('What is the result of the expression?')
    counter = 0
    while counter <= 3:
        number_1 = randint(1, 100)
        number_2 = randint(1, 100)
        operators = [' + ', ' - ', ' * ']
        chosen_operator = choice(operators)
        expression = str(number_1) + chosen_operator + str(number_2)
        expression_result = eval(expression)
        ask_question(expression)
        answer = int(get_answer())
        correctness = check_answer(expression_result, answer)
        if correctness == 'False':
            respond_to_wrong_answer(expression_result, answer, name)
            break
        else:
            respond_to_correct_answer()
            counter += 1
        if counter == 3:
            congratulate_user(name)
            break


if __name__ == '__main__':
    main()
