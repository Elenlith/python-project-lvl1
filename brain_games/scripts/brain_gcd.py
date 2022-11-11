from brain_games.engine import major_func
from brain_games.games.brain_gcd_func import RULE
from brain_games.games.brain_gcd_func import generate_numbers
from brain_games.games.brain_gcd_func import prepare_questions
from brain_games.games.brain_gcd_func import prepare_answers


def main():
    numbers = generate_numbers()
    quest = prepare_questions(numbers)
    r_answ = prepare_answers(numbers)
    major_func(RULE, quest, r_answ)


if __name__ == '__main__':
    main()
