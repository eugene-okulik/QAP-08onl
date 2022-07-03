# Обработка исключений
# Попросите пользователя ввести дату и попробуйте преобразовать дату
# в формат питона. В случае, если пользователь не угадал с форматом
# ввода даты, вы получите исключение. Обработайте это исключение и
# подскажите пользователю в каком формате нужно вводить дату

from datetime import datetime
from datetime import date

print('Enter any date')


def users_date():
    user_date = input()
    user_date_python = datetime.strptime(user_date, '%d.%m.%Y').date()
    if isinstance(user_date_python, date):
        print("Date format is correct")


while True:
    try:
        users_date()
        break
    except ValueError:
        print("Date type is incorrect. Enter any date in the format: dd.dd.yyyy")
