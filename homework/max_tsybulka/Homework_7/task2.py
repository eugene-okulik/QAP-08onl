# У вас интернет магазин, надо написать функцию которая проверяет,
# что введен правильный купон и он еще действителен

from datetime import datetime

CORRECT_CODE = '123'


def check_coupon(entered_code, expiration_date):

    now = datetime.now()
    expiration_date = now.strptime(expiration_date, "%B %d, %Y")
    if entered_code != CORRECT_CODE:
        return "Invalid coupon"
    if expiration_date >= now:
        return 'True'
    return 'False'

print(check_coupon("123", "July 11, 2022"))
print(check_coupon("123", "June 22, 2022"))
