# У вас интернет магазин, надо написать функцию которая проверяет,
# что введен правильный купон и он еще действителен

from datetime import datetime

CORRECT_CODE = "123"
now = datetime.now()
CORRECT_DATE = now.strftime("%B %d, %Y")

def check_coupon(entered_code, expiration_date):
    if expiration_date == CORRECT_DATE and entered_code == "123":
        return 'You have valid coupon'
    return 'You have invalid coupon'

print(check_coupon(input("Введите код купона "), input("Введите дату - Month  DD, YYYY: ")))
