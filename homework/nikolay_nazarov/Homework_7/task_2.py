"""Программа проверяет что введен правильный купон"""
import datetime

CORRECT_CODE = '123'


def date_encoder(some_date):
    encoded_date = datetime.datetime.strptime(some_date, '%B %d, %Y')
    return encoded_date


def check_coupon(entered_code, expiration_date):
    if date_encoder(expiration_date) > datetime.datetime.now() and entered_code == CORRECT_CODE:
        return True
    return False


print(check_coupon("123", "July 9, 2022"))
print(check_coupon("123", "June 2, 2022"))
