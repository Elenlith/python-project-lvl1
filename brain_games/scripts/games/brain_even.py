from random import randint
from brain_games.common_functions import welcome_user, get_user_name, say_hello, explain_game_rules, ask_question, get_answer
from brain_games.common_functions import check_answer, respond_to_wrong_answer, respond_to_correct_answer, congratulate_user
from brain_games.special_functions import check_parity


def main():
    welcome_user()
    name = get_user_name()
    say_hello()
    explain_game_rules('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        random_number = randint(1, 100)
        right_answer = check_parity(random_number)
        ask_question(random_number)
        answer = get_answer()
        correctness = check_answer(right_answer, answer)
        if correctness is False:
            respond_to_wrong_answer(right_answer, answer, name)
            break
        else:
            respond_to_correct_answer()
            counter += 1
        if counter == 3:
            congratulate_user(name)


if __name__ == '__main__':
    main()
