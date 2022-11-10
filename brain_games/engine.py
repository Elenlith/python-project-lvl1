import prompt


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


def congratulate_user(counter, name):
    if counter == 3:
        print(f'Congratulations, {name}!')
    else:
        pass


def major_func(task, quest, r_answ):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(task)
    counter = 0
    while counter < 3:
        question = quest[counter]
        right_answ = r_answ[counter]
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        correctness = check_answer(right_answ, answer)
        if correctness is False:
            respond_to_wrong_answer(right_answ, answer, name)
            break
        else:
            print('Correct!')
            counter += 1
        congratulate_user(counter, name)
