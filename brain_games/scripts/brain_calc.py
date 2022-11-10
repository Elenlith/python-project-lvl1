from brain_games.engine import major_func
from brain_games.games.brain_calc_func import RULE
from brain_games.games.brain_calc_func import make_expression
from brain_games.games.brain_calc_func import make_calculation


def main():
    task = RULE
    quest1 = make_expression()
    r_answ1 = make_calculation(quest1)
    quest2 = make_expression()
    r_answ2 = make_calculation(quest2)
    quest3 = make_expression()
    r_answ3 = make_calculation(quest3)
    major_func(task, quest1, quest2, quest3, r_answ1, r_answ2, r_answ3)


if __name__ == '__main__':
    main()
