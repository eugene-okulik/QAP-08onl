# У вас интернет магазин, надо написать функцию которая проверяет,
# что введен правильный купон и он еще действителен

from datetime import datetime

CORRECT_CODE = "123"

def check_coupon(entered_code, expiration_date):
    now = datetime.now()
    expiration_date = now.strptime(expiration_date, "%B %d, %Y")
    if entered_code is not CORRECT_CODE:
        return 'You have invalid coupon'
    if expiration_date >= now:
        return 'You have valid coupon'
    return 'You have invalid coupon'

print(check_coupon("123", "July 21, 2022"))
print(check_coupon("123", "June 2, 2022"))
