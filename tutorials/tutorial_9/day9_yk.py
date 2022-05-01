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

    user_input = int(input("Enter choice:"))

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

    if user_input == 1:
        first = int(input("first number:"))
        second = int(input("second number:"))
        add_operation(first, second)
    elif user_input == 2:
        first = int(input("first number:"))
        second = int(input("second number:"))
        subtract_operation(first, second)
    elif user_input == 3:
        first = int(input("first number:"))
        second = int(input("second number:"))
        multiply_operation(first, second)
    elif user_input == 4:
        first = int(input("first number:"))
        second = int(input("second number:"))
        divide_operation(first, second)
    elif user_input == 5:
        first = int(input("first number:"))
        second = int(input("second number:"))
        power_operation(first, second)
    elif user_input == 6:
        first = int(input("first number:"))
        second = int(input("second number:"))
        modulo_operation(first, second)
    elif user_input == 7:
        number = int(input("enter number :"))
        squareroot_operation(number)
    elif user_input == 8:
        number = int(input("enter number :"))
        cube_operation(number)
    else:
        print("invalid input")

    user_again = str(input("Let's do next calculation? (yes/no)"))

    if user_again == "yes":
        continue
    elif user_again == "no":
        break
    else:
        print("invalid output")