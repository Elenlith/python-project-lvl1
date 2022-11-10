from brain_games.engine import major_func
from brain_games.games.brain_gcd_func import RULE
from brain_games.games.brain_gcd_func import generate_number
from brain_games.games.brain_gcd_func import find_greatest_common_divisor


def main():
    quest = []
    r_answ = []
    i = 0
    while i <= 2:
        a = generate_number()
        b = generate_number()
        numbers = str(a) + ' ' + str(b)
        quest.append(numbers)
        answ = str(find_greatest_common_divisor(a, b))
        r_answ.append(answ)
        i += 1
    major_func(RULE, quest, r_answ)


if __name__ == '__main__':
    main()
