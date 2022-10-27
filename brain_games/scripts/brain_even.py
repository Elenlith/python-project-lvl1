from random import randint
import prompt


def get_user_name():
    name = prompt.string('May I have your name? ')
    return name


def check_answer(number, answ):
    if (number % 2 == 0 and answ == 'yes') or (number % 2 != 0 and answ == 'no'):
        correctness = 'True'
    else:
        correctness = 'False'
    return correctness


def main():
    print('Welcome to the Brain Games!')
    name = get_user_name()
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter <= 3:
        random_number = randint(1, 100)
        if random_number % 2 == 0:
            even_number = 'yes'
        else:
            even_number = 'no'
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        correctness = check_answer(random_number, answer)
        if correctness == 'False':
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{even_number}'.\nLet's try again, {name}")
            break
        else:
            print('Correct!')
            counter += 1
        if counter == 3:
            print(f'Congratulations, {name}!')
            break


if __name__ == '__main__':
    main()
