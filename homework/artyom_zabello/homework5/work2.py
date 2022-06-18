import random


LST = [True, False]
SALARY = random.randint(10000, 100000)
BONUS = random.choice(LST)
if BONUS is True:
    NEW_SALARY = SALARY * 10
else:
    NEW_SALARY = SALARY

print(f"{SALARY},{BONUS} == ${NEW_SALARY}")
