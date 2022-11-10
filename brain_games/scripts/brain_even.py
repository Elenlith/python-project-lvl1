from brain_games.engine import major_func
from brain_games.games.brain_even_func import RULE
from brain_games.games.brain_even_func import generate_number
from brain_games.games.brain_even_func import check_parity


def main():
    quest = []
    r_answ = []
    i = 0
    while i <= 2:
        number = generate_number()
        quest.append(number)
        answ = check_parity(quest[i])
        r_answ.append(answ)
        i += 1
    major_func(RULE, quest, r_answ)


if __name__ == '__main__':
    main()
