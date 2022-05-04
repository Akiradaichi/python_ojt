import math


def calculaton():
    print("""Select operation.
    1.Add
    2.Subtract
    3.Multiply
    4.Divide
    5.power
    6.modulo
    7.square-root
    8.cube""")
    user_input = str(input("Enter choice:"))
    print(" ")

    def add_operation(first, second):
        x = first + second
        print("{} + {}".format(first, second), "=", x)

    def subtract_operation(first, second):
        x = first - second
        print("{} - {}".format(first, second), "=", x)

    def multiply_operation(first, second):
        x = first * second
        print("{} * {}".format(first, second), "=", x)

    def divide_operation(first, second):
        x = first / second
        print("{} / {}".format(first, second), "=", x)

    def power_operation(first, second):
        x = first ** second
        print("{} ** {}".format(first, second), "=", x)

    def modulo_operation(first, second):
        x = first % second
        print("{} % {}".format(first, second), "=", x)

    def squareroot_operation(number):
        x = math.sqrt(number)
        print("Square root =", x)

    def cube_operation(number):
        x = number ** 3
        print("Cube =", x)

    if user_input.lower() == "add" or user_input == "1":
        while True:
            try:
                first = float(input("Enter first number:"))
                print(" ")
                while True:
                    try:
                        second = float(input("Enter second number:"))
                        print(" ")
                        break
                    except ValueError:
                        print(" ")
                        print("Second Number has to be a number !!")
                        print(" ")
                add_operation(first, second)
                break
            except ValueError:
                print(" ")
                print("First number has to be a number !!")
                print(" ")
    elif user_input.lower() == "subtract" or user_input == "2":
        while True:
            try:
                first = float(input("Enter first number:"))
                print(" ")
                while True:
                    try:
                        second = float(input("Enter second number:"))
                        print(" ")
                        break
                    except ValueError:
                        print(" ")
                        print("Second Number has to be a number !!")
                        print(" ")
                subtract_operation(first, second)
                break
            except ValueError:
                print(" ")
                print("First number has to be a number !!")
                print(" ")
    elif user_input.lower() == "multiply" or user_input == "3":
        while True:
            try:
                first = float(input("Enter first number:"))
                print(" ")
                while True:
                    try:
                        second = float(input("Enter second number:"))
                        print(" ")
                        break
                    except ValueError:
                        print(" ")
                        print("Second Number has to be a number !!")
                        print(" ")
                multiply_operation(first, second)
                break
            except ValueError:
                print(" ")
                print("First number has to be a number !!")
                print(" ")
    elif user_input.lower() == "divide" or user_input == "4":
        while True:
            try:
                first = float(input("Enter first number:"))
                print(" ")
                while True:
                    try:
                        second = float(input("Enter second number:"))
                        print(" ")
                        break
                    except ValueError:
                        print(" ")
                        print("Second Number has to be a number !!")
                        print(" ")
                divide_operation(first, second)
                break
            except ValueError:
                print(" ")
                print("First number has to be a number !!")
                print(" ")
    elif user_input.lower() == "power" or user_input == "5":
        while True:
            try:
                first = float(input("Enter first number:"))
                print(" ")
                while True:
                    try:
                        second = float(input("Enter second number:"))
                        print(" ")
                        break
                    except ValueError:
                        print(" ")
                        print("Second Number has to be a number !!")
                        print(" ")
                power_operation(first, second)
                break
            except ValueError:
                print(" ")
                print("First number has to be a number !!")
                print(" ")
    elif user_input.lower() == "modulo" or user_input == "6":
        while True:
            try:
                first = float(input("Enter first number:"))
                print(" ")
                while True:
                    try:
                        second = float(input("Enter second number:"))
                        print(" ")
                        break
                    except ValueError:
                        print(" ")
                        print("Second Number has to be a number !!")
                        print(" ")
                modulo_operation(first, second)
                break
            except ValueError:
                print(" ")
                print("First number has to be a number !!")
                print(" ")
    elif user_input.lower() == "square root" or user_input == "7":
        while True:
            try:
                number = float(input("Enter number :"))
                print(" ")
                squareroot_operation(number)
                break
            except ValueError:
                print(" ")
                print("Number has to be a number !!")
                print(" ")
    elif user_input.lower() == "cube" or user_input == "8":
        while True:
            try:
                number = float(input("Enter number :"))
                print(" ")
                cube_operation(number)
                break
            except ValueError:
                print(" ")
                print("Number has to be a number !!")
                print(" ")
    else:
        print("Pls enter the opreation number or name!!")
        print(" ")
        calculaton()


def again():
    user_again = str(input("Let's do next calculation? (yes/no)"))
    print(" ")
    if user_again.lower() == "yes":
        calculaton()
    elif user_again.lower() == "no":
        print("bye")
    else:
        print("Pls enter yes or no only ")
        again()


calculaton()
again()