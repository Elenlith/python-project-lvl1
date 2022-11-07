from brain_games.common_functions import welcome_user, get_user_name, say_hello
from brain_games.common_functions import explain_game_rules, ask_question
from brain_games.common_functions import get_answer, check_answer
from brain_games.common_functions import respond_to_wrong_answer
from brain_games.common_functions import respond_to_correct_answer
from brain_games.common_functions import congratulate_user
from brain_games.special_functions import create_progression
from brain_games.special_functions import find_element_to_hide
from brain_games.special_functions import hide_progression_element


def main():
    welcome_user()
    name = get_user_name()
    say_hello()
    explain_game_rules('What number is missing in the progression?')
    counter = 0
    while counter < 3:
        progr = create_progression()
        hid_el = find_element_to_hide(progr)
        pr_text = ' '.join(map(str, hide_progression_element(progr, hid_el)))
        ask_question(pr_text)
        answer = int(get_answer())
        correctness = check_answer(hid_el, answer)
        if correctness is False:
            respond_to_wrong_answer(hid_el, answer, name)
            break
        else:
            respond_to_correct_answer()
            counter += 1
        if counter == 3:
            congratulate_user(name)


if __name__ == '__main__':
    main()
