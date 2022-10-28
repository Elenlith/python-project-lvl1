from random import randint
from brain_games.common_functions import welcome_user, get_user_name, say_hello, explain_game_rules, ask_question, get_answer
from brain_games.common_functions import check_answer, respond_to_wrong_answer, respond_to_correct_answer, congratulate_user


def main():
    welcome_user()
    name = get_user_name()
    say_hello()
    explain_game_rules('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter <= 3:
        random_number = randint(1, 100)
        if random_number % 2 == 0:
            even_number = 'yes'
        else:
            even_number = 'no'
        ask_question(random_number)
        answer = get_answer()
        correctness = check_answer(even_number, answer)
        if correctness == 'False':
            respond_to_wrong_answer(even_number, answer, name)
            break
        else:
            respond_to_correct_answer()
            counter += 1
        if counter == 3:
            congratulate_user(name)
            break


if __name__ == '__main__':
    main()
