from brain_games.engine import major_func
from brain_games.games.brain_progression_func import RULE
from brain_games.games.brain_progression_func import prep_progr_list
from brain_games.games.brain_progression_func import prepare_questions
from brain_games.games.brain_progression_func import prepare_answers


def main():
    progressions = prep_progr_list()
    quest = prepare_questions(progressions)
    r_answ = prepare_answers(progressions)
    major_func(RULE, quest, r_answ)


if __name__ == '__main__':
    main()
