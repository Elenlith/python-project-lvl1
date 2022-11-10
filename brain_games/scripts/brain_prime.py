from brain_games.engine import major_func
from brain_games.games.brain_prime_func import RULE
from brain_games.games.brain_prime_func import generate_number
from brain_games.games.brain_prime_func import is_prime_number


def main():
    task = RULE
    quest1 = generate_number()
    r_answ1 = is_prime_number(quest1)
    quest2 = generate_number()
    r_answ2 = is_prime_number(quest2)
    quest3 = generate_number()
    r_answ3 = is_prime_number(quest3)
    major_func(task, quest1, quest2, quest3, r_answ1, r_answ2, r_answ3)


if __name__ == '__main__':
    main()
