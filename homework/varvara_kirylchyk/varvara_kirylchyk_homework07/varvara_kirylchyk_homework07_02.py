#У вас интернет магазин, надо написать функцию которая проверяет
# что введен правильный купон и он еще действителен

import sys
from datetime import datetime

DATE = str(input('Date: '))
try:
    check = datetime.strptime(DATE, "%B %d, %Y")
except ValueError:
    print("Incorrect format")

CODE = input("Code: ")
CORRECT_CODE = "123"

now = datetime.now()
CORRECT_DATE = now.strftime("%B %d, %Y")
# print(CORRECT_DATE)

def check_coupon(code_x, date_y):
    if code_x == CORRECT_CODE and date_y >= CORRECT_DATE:
        print("True")
    else:
        print("Error")
        sys.exit()

print(check_coupon(CODE, DATE))
