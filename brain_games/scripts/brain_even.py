from brain_games.engine import major_func
from brain_games.games.brain_even_func import RULE
from brain_games.games.brain_even_func import generate_number
from brain_games.games.brain_even_func import check_parity


def main():
    task = RULE
    quest1 = generate_number()
    r_answ1 = check_parity(quest1)
    quest2 = generate_number()
    r_answ2 = check_parity(quest2)
    quest3 = generate_number()
    r_answ3 = check_parity(quest3)
    major_func(task, quest1, quest2, quest3, r_answ1, r_answ2, r_answ3)


if __name__ == '__main__':
    main()
