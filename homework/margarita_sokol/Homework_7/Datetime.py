# У вас интернет магазин, надо написать функцию которая проверяет,
# что введен правильный купон и он еще действителен.

from datetime import datetime

CORRECT_CODE = "123"
ACTUAL_DATE = datetime.now()
CORRECT_DATE = ACTUAL_DATE.strftime('%B %d, %Y')
_entered_code = (input('Enter coupon code: '))
_expiration_date = (input('Enter the date in the format (Month name DD, YYYY): '))

def check_coupon(_entered_code, _expiration_date):
    if _entered_code == CORRECT_CODE and _expiration_date == CORRECT_DATE:
        return True
    return False


print(check_coupon(_entered_code, _expiration_date))
