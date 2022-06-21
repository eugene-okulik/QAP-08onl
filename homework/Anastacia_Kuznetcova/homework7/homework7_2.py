"""Решение задачи внизу"""
from datetime import datetime

CORRECT_CODE = '123'


def check_coupon(entered_code, expiration_date):
    """Функия проверяет срок годности купона"""
    now = datetime.now()
    expiration_date = now.strptime(expiration_date, "%B %d, %Y")
    if entered_code != CORRECT_CODE:
        return "Купон неверный"
    if expiration_date >= now:
        return "True"
    return "False"


print(check_coupon("123", "June 25, 2022"))
print(check_coupon("123", "June 20, 2022"))
