import prompt


def launch_engine(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULE)
    counter = 0
    while counter < 3:
        question = game.prepare_question()
        r_ans = game.prepare_answer(question)
        print(f'Question: {question}')
        ans = prompt.string('Your answer: ')
        if ans == r_ans:
            print('Correct!')
            counter += 1
        else:
            text = f"'{ans}' is wrong answer ;(. Correct answer was '{r_ans}'."
            print(text)
            print(f"Let's try again, {name}!")
            break
        if counter == 3:
            print(f'Congratulations, {name}!')
        else:
            pass
