from brain_games.engine import major_func
from brain_games.games.brain_gcd_func import RULE
from brain_games.games.brain_gcd_func import generate_number
from brain_games.games.brain_gcd_func import find_greatest_common_divisor


def main():
    task = RULE
    a1 = generate_number()
    b1 = generate_number()
    quest1 = str(a1) + ' ' + str(b1)
    r_answ1 = str(find_greatest_common_divisor(a1, b1))
    a2 = generate_number()
    b2 = generate_number()
    quest2 = str(a2) + ' ' + str(b2)
    r_answ2 = str(find_greatest_common_divisor(a2, b2))
    a3 = generate_number()
    b3 = generate_number()
    quest3 = str(a3) + ' ' + str(b3)
    r_answ3 = str(find_greatest_common_divisor(a3, b3))
    major_func(task, quest1, quest2, quest3, r_answ1, r_answ2, r_answ3)


if __name__ == '__main__':
    main()
