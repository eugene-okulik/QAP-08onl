import random


while True:
    salary = int(input('Enter credits '))
    bonus = random.choice([True, False])
    if bonus is True:
        a = salary * 10
        print(f'You win ', a)
    else:
        print(f'You win ', salary)
