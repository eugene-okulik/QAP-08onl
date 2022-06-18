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

def check_coupon(coup_code, corr_code, coup_date, curr_date):
    if corr_code == coup_code and coup_date >= curr_date:
        print("True")
    else:
        print("False")

check_coupon(code, CORRECT_CODE, coupon_date, current_date)
