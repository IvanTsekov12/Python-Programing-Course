def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print('-------------------------')
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter: (A, B, C or D)!")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses = check_answer(questions.get(key), guess)
        question_num += 1

def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0

def display_score():
    pass

def play_again():
    pass

questions = {"Who created Python? " : 'A',
             "What year was Python created? " : 'B',
             "Python is tributed to which comedy group? " :'C',
             "Is the Earth round? " : 'A'}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
                   ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
                   ["A. Lonley Island", "B. Smosh", "C. Monty Python", "D. SNL"],
                   ["A. True", "B. False", "C. Sometimes", "D. What's Earth?"]]

new_game()