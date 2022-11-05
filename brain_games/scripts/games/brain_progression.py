from brain_games.common_functions import welcome_user, get_user_name, say_hello
from brain_games.common_functions import explain_game_rules, ask_question, get_answer
from brain_games.common_functions import check_answer, respond_to_wrong_answer
from brain_games.common_functions import respond_to_correct_answer, congratulate_user
from brain_games.special_functions import create_progression, find_element_to_hide
from brain_games.special_functions import hide_progression_element


def main():
    welcome_user()
    name = get_user_name()
    say_hello()
    explain_game_rules('What number is missing in the progression?')
    counter = 0
    while counter <= 3:
        progression = create_progression()
        hidden_element = find_element_to_hide(progression)
        what_to_show = ' '.join(map(str, hide_progression_element(progression, hidden_element)))
        ask_question(what_to_show)
        answer = int(get_answer())
        correctness = check_answer(hidden_element, answer)
        if correctness is False:
            respond_to_wrong_answer(hidden_element, answer, name)
            break
        else:
            respond_to_correct_answer()
            counter += 1
        if counter == 3:
            congratulate_user(name)
            break


if __name__ == '__main__':
    main()
