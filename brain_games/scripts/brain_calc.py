from brain_games.engine import major_func
from brain_games.games.brain_calc_func import RULE
from brain_games.games.brain_calc_func import make_expression
from brain_games.games.brain_calc_func import make_calculation


def main():
    quest = []
    r_answ = []
    i = 0
    while i <= 2:
        expr = make_expression()
        quest.append(expr)
        answ = make_calculation(quest[i])
        r_answ.append(answ)
        i += 1
    major_func(RULE, quest, r_answ)


if __name__ == '__main__':
    main()
