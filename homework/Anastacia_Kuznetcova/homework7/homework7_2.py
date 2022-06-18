"""Решение задачи внизу"""
from datetime import datetime

CORRECT_CODE = "123"
now = datetime.now()
CORRECT_DATE = now.strftime("%B %d, %Y")


def check_coupon(entered_code, user_input_date):
    """Функия проверяет срок годности купона"""
    if user_input_date == CORRECT_DATE and entered_code == "123":
        return True
    return False


print(check_coupon(input("Введите код купона "), input("Введите дату - Month name DD, YYYY: ")))
