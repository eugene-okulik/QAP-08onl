from datetime import datetime
from datetime import date

print('Введите дату')


def users_date():
    user_date = input()
    user_date_python = datetime.strptime(user_date, '%d.%m.%Y').date()
    if isinstance(user_date_python, date):
        print("Формат даты верный")


while True:
    try:
        users_date()
        break
    except ValueError:
        print("Неверный формат даты. Введите дату в формате: dd.mm.yyyy")
