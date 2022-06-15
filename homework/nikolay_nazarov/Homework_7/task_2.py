"""Программа проверяет что введен правильный купон"""
import datetime

CORRECT_CODE = '123'


def date_encoder(some_date):
    """
    Преобразует строку с датой в правильный формат даты
    :param some_date: str
    :return: datetime.datetime
    """
    encoded_date = datetime.datetime.strptime(some_date, '%B %d, %Y')
    return encoded_date


def check_coupon(entered_code, expiration_date):
    """
    Функция проверяет что введен правильный купон и он действителен
    :param entered_code: str
    :param expiration_date: str
    :return: bool
    """
    if date_encoder(expiration_date) > datetime.datetime.now() and entered_code == "123":
        return True
    return False


print(check_coupon("123", "July 9, 2022"))
print(check_coupon("123", "June 2, 2022"))
