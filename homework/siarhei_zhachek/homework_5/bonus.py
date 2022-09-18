import random


while True:
    salary = int(input('Enter credits '))
    bonus = random.choice([True, False])
    if bonus is True:
        a = salary * 10
        print('You win ', a)
    else:
        print('You win ', salary)
