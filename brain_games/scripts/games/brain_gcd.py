from random import randint
from brain_games.common_functions import welcome_user, get_user_name, say_hello
from brain_games.common_functions import explain_game_rules, ask_question
from brain_games.common_functions import get_answer, check_answer
from brain_games.common_functions import respond_to_wrong_answer
from brain_games.common_functions import respond_to_correct_answer
from brain_games.common_functions import congratulate_user
from brain_games.special_functions import find_greatest_common_divisor


def main():
    welcome_user()
    name = get_user_name()
    say_hello()
    explain_game_rules('Find the greatest common divisor of given numbers.')
    counter = 0
    while counter < 3:
        number_1 = randint(1, 100)
        number_2 = randint(1, 100)
        result = find_greatest_common_divisor(number_1, number_2)
        ask_question(str(number_1) + ' ' + str(number_2))
        answer = int(get_answer())
        correctness = check_answer(result, answer)
        if correctness is False:
            respond_to_wrong_answer(result, answer, name)
            break
        else:
            respond_to_correct_answer()
            counter += 1
        congratulate_user(name) if counter == 3 else None


if __name__ == '__main__':
    main()
