import random

while True:
    choice = ['rock', 'paper', 'scissors']
    pc = random.choice(choice)
    player = None

    while player not in choice:
        player = input("rock, paper or scissors?: ").lower()

    print()
    if player == pc:
        print("PC: " + pc)
        print("Player: " + player)
        print("Tie!")
    elif player == "rock":
        if pc == "paper":
            print("PC: " + pc)
            print("Player: " + player)
            print("PC wins!")
        elif pc == "scissors":
            print("PC: " + pc)
            print("Player: " + player)
            print("Player wins!")
    elif player == "paper":
        if pc == "scissors":
            print("PC: " + pc)
            print("Player: " + player)
            print("PC wins!")
        elif pc == "rock":
            print("PC: " + pc)
            print("Player: " + player)
            print("Player wins!")
    elif player == "scissors":
        if pc == "rock":
            print("PC: " + pc)
            print("Player: " + player)
            print("PC wins!")
        elif pc == "paper":
            print("PC: " + pc)
            print("Player: " + player)
            print("Player wins!")
    play_again = input("Would you like to play again? (yes/no):").lower()
    if play_again != "yes":
        break
print("Goodbye!")