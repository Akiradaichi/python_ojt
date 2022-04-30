import re

# 1


def string_match(txt):
    x = re.search("a.{2,3}l", txt)
    if x:
        print("Found! Match Sentence")
    else:
        print("Oops! Nothing is match")


string_match("kimi no namae wa Aleel")

# 2


def word_match(txt):
    x = re.search("a+\w", txt)
    print(x.group())


word_match("dwerwe dfdfg asdjf")

# 3


def string_start(txt):
    x = "4"
    print(x + txt)


string_start("Hello world")
