# Обработка исключений
# Попросите пользователя ввести дату
# и попробуйте преобразовать дату в формат питона.
# В случае, если пользователь не угадал с форматом ввода даты,
# вы получите исключение.
# Обработайте это исключение и подскажите пользователю
# в каком формате нужно вводить дату.

from datetime import datetime
from datetime import date

def users_date():
    user_date = input("Введите дату: \n")
    user_date_python = datetime.strptime(user_date, '%d.%m.%Y').date()
    if isinstance(user_date_python, date):
        print('Спасибо, формат даты правильный')


while True:
    try:
        users_date()
        break
    except ValueError:
        print('Неверный формат ввода даты. Пожалуйста, введите любую дату в формате: d.m.y')
