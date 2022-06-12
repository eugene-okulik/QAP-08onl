# Подсчет букв
# Дано две переменные: строка и буква => "fizbbbuz","b",
# нужно подсчитать сколько раз буква b встречается в заданной строке
# "Hello there", "e" == 3

SOME_STRING = "Hello t h ere"
SOME_LETTER = "h"

if SOME_LETTER != " ":
    print(f"\"{SOME_STRING}\", \"{SOME_LETTER}\" == "
          f"{SOME_STRING.count(SOME_LETTER) + SOME_STRING.count(SOME_LETTER.swapcase())}")
elif SOME_LETTER == " ":
    print(f"\"{SOME_STRING}\", \"{SOME_LETTER}\" == "
          f"{SOME_STRING.count(SOME_LETTER)}")
