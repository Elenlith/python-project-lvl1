import prompt


def launch_engine(task, quest, r_answ):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(task)
    counter = 0
    while counter < 3:
        question = quest[counter]
        r_ans = r_answ[counter]
        print(f'Question: {question}')
        ans = prompt.string('Your answer: ')
        if ans == r_ans:
            correctness = True
        else:
            correctness = False
        if correctness is False:
            text = f"'{ans}' is wrong answer ;(. Correct answer was '{r_ans}'."
            print(text)
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
            counter += 1
        if counter == 3:
            print(f'Congratulations, {name}!')
        else:
            pass
