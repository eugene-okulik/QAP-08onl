"""Внизу решение задания"""
import sys


number_names = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
    5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
    15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
}

numbers = input("numbers>> ")
numbers_list = numbers.split(" ")

if len(numbers_list) > 100:
    print("Error!")
    sys.exit()

names = []

for i in numbers_list:
    if int(i) > 19:
        print("Error!")
        sys.exit()

    word = number_names[int(i)]
    names.append(word)
names.sort()
result = []

for i in names:
    values = list(number_names.values())
    index = values.index(i)
    keys = list(number_names.keys())
    result.append(keys[index])

for i in result:
    print(i, end=" ")
