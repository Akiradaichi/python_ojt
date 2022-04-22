# 1
L = list(range(10))
x = lambda a: a ** 2
square_list = list(map(x, L))
print(square_list)

L = list(range(10))
x = lambda a: a ** 3
square_list = list(map(x, L))
print(square_list)

# 2


def star_function(name):
    for y in range(0, 5):
        print(name*y)


star_function('*')
star_function('?')
