from brain_games.engine import major_func
from brain_games.games.brain_progression_func import RULE
from brain_games.games.brain_progression_func import create_progression
from brain_games.games.brain_progression_func import find_element_to_hide
from brain_games.games.brain_progression_func import hide_progression_element


def main():
    quest = []
    r_answ = []
    i = 0
    while i <= 2:
        progr = create_progression()
        hid_el = find_element_to_hide(progr)
        question = ' '.join(map(str, hide_progression_element(progr, hid_el)))
        answ = str(hid_el)
        quest.append(question)
        r_answ.append(answ)
        i += 1
    major_func(RULE, quest, r_answ)


if __name__ == '__main__':
    main()
