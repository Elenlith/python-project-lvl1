import prompt


def generate_task(counter, quest1, quest2, quest3):
    if counter == 0:
        question = quest1
    elif counter == 1:
        question = quest2
    else:
        question = quest3
    return question


def find_right_answer(counter, r_answ1, r_answ2, r_answ3):
    if counter == 0:
        right_answ = r_answ1
    elif counter == 1:
        right_answ = r_answ2
    else:
        right_answ = r_answ3
    return right_answ


def check_answer(right_answ, answer):
    if answer == right_answ:
        correctness = True
    else:
        correctness = False
    return correctness


def respond_to_wrong_answer(right_answ, answer, name):
    text = f"'{answer}' is wrong answer ;(. Correct answer was '{right_answ}'."
    print(text)
    print(f"Let's try again, {name}!")


def major_func(task, quest1, quest2, quest3, r_answ1, r_answ2, r_answ3):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(task)
    counter = 0
    while counter < 3:
        question = generate_task(counter, quest1, quest2, quest3)
        right_answ = find_right_answer(counter, r_answ1, r_answ2, r_answ3)
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        correctness = check_answer(right_answ, answer)
        if correctness is False:
            respond_to_wrong_answer(right_answ, answer, name)
            break
        else:
            print('Correct!')
            counter += 1
        if counter == 3:
            print(f'Congratulations, {name}!')
