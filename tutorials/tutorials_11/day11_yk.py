import random

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
    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
            computer_score = computer_score + 1
            print("player score is ", player_score, "win")
            print("computer score is ", computer_score, "win")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
            player_score += 1
            print("player score is ", player_score, "win")
            print("computer score is ", computer_score, "win")
    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
            computer_score = computer_score + 1
            print("player score is ", player_score, "win")
            print("computer score is ", computer_score, "win")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
            player_score += 1
            print("player score is ", player_score, "win")
            print("computer score is ", computer_score, "win")
    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
            computer_score = computer_score + 1
            print("player score is ", player_score, "win")
            print("computer score is ", computer_score, "win")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
            player_score += 1
            print("player score is ", player_score, "win")
            print("computer score is ", computer_score, "win")
    restart = input("Play Again!(Yes,No) ")
    while restart.lower() != "yes" and restart.lower() != "no":
        restart = input("Invalid Input.Please input Yes or No only :  ")
        if restart.lower() == 'n':
            print("Bye Bye")
            break