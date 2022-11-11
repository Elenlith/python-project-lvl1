from brain_games.engine import major_func
from brain_games.games.brain_prime_func import RULE
from brain_games.games.brain_prime_func import prepare_questions
from brain_games.games.brain_prime_func import prepare_answers


def main():
    quest = prepare_questions()
    r_answ = prepare_answers(quest)
    major_func(RULE, quest, r_answ)


if __name__ == '__main__':
    main()
