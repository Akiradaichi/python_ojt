import random


def game():
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None
    player_score = 0
    computer_score = 0

    while True:
        player = input("rock, paper, or scissors?: ").lower()
        while player not in choices:
            player = input("pls enter rock, paper, or scissors: ").lower()
        break

    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("Tie!")
        print("player score is ", player_score, "win")
        print("computer score is ", computer_score, "win")
        again()

    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
            computer_score = computer_score + 1
            print("player score is ", player_score, "win")
            print("computer score is ", computer_score, "win")
            again()
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
            player_score += 1
            print("player score is ", player_score, "win")
            print("computer score is ", computer_score, "win")
            again()

    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
            computer_score = computer_score + 1
            print("player score is ", player_score, "win")
            print("computer score is ", computer_score, "win")
            again()
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
            player_score += 1
            print("player score is ", player_score, "win")
            print("computer score is ", computer_score, "win")
            again()

    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
            computer_score = computer_score + 1
            print("player score is ", player_score, "win")
            print("computer score is ", computer_score, "win")
            again()
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
            player_score += 1
            print("player score is ", player_score, "win")
            print("computer score is ", computer_score, "win")
            again()
    return player_score, computer_score


def again():
    user_again = str(input("Let's play next game?? (yes/no)"))
    print(" ")
    if user_again.lower() == "yes":
        game()
    elif user_again.lower() == "no":
        print("bye")
    else:
        print("Pls enter yes or no only ")
        again()


game()