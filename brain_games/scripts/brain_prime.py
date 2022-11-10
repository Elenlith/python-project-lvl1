from brain_games.engine import major_func
from brain_games.games.brain_prime_func import RULE
from brain_games.games.brain_prime_func import generate_number
from brain_games.games.brain_prime_func import is_prime_number


def main():
    quest = []
    r_answ = []
    i = 0
    while i <= 2:
        number = generate_number()
        quest.append(number)
        answ = is_prime_number(quest[i])
        r_answ.append(answ)
        i += 1
    major_func(RULE, quest, r_answ)


if __name__ == '__main__':
    main()
