import prompt


def welcome_user():
    print('Welcome to the Brain Games!')


def get_user_name():
    global name
    name = prompt.string('May I have your name? ')
    return name


def say_hello():
    print(f'Hello, {name}!')


def explain_game_rules(task):
    print(task)


def ask_question(question):
    print(f'Question: {question}')


def get_answer():
    answer = prompt.string('Your answer: ')
    return answer


def check_answer(right_answer, answer):
    if answer == right_answer:
        correctness = True
    else:
        correctness = False
    return correctness


def respond_to_wrong_answer(right_answer, answer, name):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.\nLet's try again, {name}!")


def respond_to_correct_answer():
    print('Correct!')


def congratulate_user(name):
    print(f'Congratulations, {name}!')
