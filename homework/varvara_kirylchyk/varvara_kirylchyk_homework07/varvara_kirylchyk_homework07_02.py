#У вас интернет магазин, надо написать функцию которая проверяет
# что введен правильный купон и он еще действителен

import sys
from datetime import datetime

CORRECT_CODE = "123"

date = input('Enter the date in format - Month DD, YYYY: ')

try:
    coupon_date = datetime.strptime(date, "%B %d, %Y")
except ValueError:
    print("Incorrect date format")
    sys.exit(1)

code = input("Enter the code: ")

current_date = datetime.now()


def check_coupon(coupon_code, correct_code, coupon_date, current_date):
    if correct_code == coupon_code and coupon_date >= current_date:
        return True
    else:
        return False


print(check_coupon(code, CORRECT_CODE, coupon_date, current_date))