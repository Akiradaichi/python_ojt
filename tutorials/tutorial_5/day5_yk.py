# 1
f = open("meeting.txt", "w")
f.write("Nice to meet you. I'm Tendo Soji. I'm from Japan.")
f.close

# 2
f = open("meeting.txt", "r")
def count_words():
    read_data = f.read()
    per_word = read_data.split(' ')
    print(read_data)
    print('Total Words:', len(per_word))


count_words()

# 3
user_number = int(input("enter a number"))
if user_number >= 0:
    print(user_number)
else:
    raise Exception("Sorry, the number has to be positive or zero")
