# 1
number1 = 10
number2 = 50
x = number1 * number2
print(x) if x > 500 else print(number1+number2)

# 2
arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 7, 9, 10]
if list(set(arr1) & set(arr2)):
    print('Two lists are duplicated')
else:
    print('Two lists are not duplicated')
