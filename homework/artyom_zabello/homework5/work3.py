def counter(word, char):
    res = word.count(char)
    return print(f"{word}, {char} == {res}")


counter(input(), input())
