import math
z = 1
while z > 0:
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
    try:
        if user_input.lower() == "add" or user_input == "1":
            first = float(input("first number:"))
            second = float(input("second number:"))
            add_operation(first, second)
        elif user_input.lower() == "subtract" or user_input == "2":
            first = float(input("first number:"))
            second = float(input("second number:"))
            subtract_operation(first, second)
        elif user_input.lower() == "multiply" or user_input == "3":
            first = float(input("first number:"))
            second = float(input("second number:"))
            multiply_operation(first, second)
        elif user_input.lower() == "divide" or user_input == "4":
            first = float(input("first number:"))
            second = float(input("second number:"))
            divide_operation(first, second)
        elif user_input.lower() == "power" or user_input == "5":
            first = float(input("first number:"))
            second = float(input("second number:"))
            power_operation(first, second)
        elif user_input.lower() == "modulo" or user_input == "6":
            first = float(input("first number:"))
            second = float(input("second number:"))
            modulo_operation(first, second)
        elif user_input.lower() == "square root" or user_input == "7":
            number = float(input("enter number :"))
            squareroot_operation(number)
        elif user_input.lower() == "cube" or user_input == "8":
            number = float(input("enter number :"))
            cube_operation(number)
        else:
            print("invalid input")
    except ValueError:
        print("invalid input")

    user_again = str(input("Let's do next calculation? (yes/no)"))

    if user_again.lower() == "yes":
        continue
    elif user_again.lower() == "no":
        break
    else:
        print("invalid output")
