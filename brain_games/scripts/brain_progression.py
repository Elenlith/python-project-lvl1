from brain_games.engine import major_func
from brain_games.games.brain_progression_func import RULE
from brain_games.games.brain_progression_func import create_progression
from brain_games.games.brain_progression_func import find_element_to_hide
from brain_games.games.brain_progression_func import hide_progression_element


def main():
    task = RULE
    progr1 = create_progression()
    hid_el1 = find_element_to_hide(progr1)
    quest1 = ' '.join(map(str, hide_progression_element(progr1, hid_el1)))
    r_answ1 = str(hid_el1)
    progr2 = create_progression()
    hid_el2 = find_element_to_hide(progr2)
    quest2 = ' '.join(map(str, hide_progression_element(progr2, hid_el2)))
    r_answ2 = str(hid_el2)
    progr3 = create_progression()
    hid_el3 = find_element_to_hide(progr3)
    quest3 = ' '.join(map(str, hide_progression_element(progr3, hid_el3)))
    r_answ3 = str(hid_el3)
    major_func(task, quest1, quest2, quest3, r_answ1, r_answ2, r_answ3)


if __name__ == '__main__':
    main()
