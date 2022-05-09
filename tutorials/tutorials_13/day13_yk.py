import random


def game():
    print("Welcome from our Number Guessing Game")
    num = random.randint(1, 2)
    while True:
        try:
            guess_number = int(input("Enter number: "))
            break
        except ValueError:
            print("the number has to be integer")
    count = int(2)
    while count > 0:
        if num == guess_number:
            print("You won. The number is {}".format(num))
            break
        else:
            print("Try again. You have {} time left to guess number.".format(count))
            while True:
                try:
                    guess_number = int(input("Enter number: "))
                    break
                except ValueError:
                    print("the number has to be integer")
        count -= 1
    if count == 0 and num != guess_number:
        print("You lost. You have no time left to guess number.")
        print("The number is {}".format(num))
    again()


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