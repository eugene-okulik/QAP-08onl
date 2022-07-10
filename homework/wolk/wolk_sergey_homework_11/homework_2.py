from datetime import datetime
from datetime import date

print('Введите дату')

def users_date():
    user_date = input()
    user_date_python = datetime.strptime(user_date, '%d.%m.%Y').date()
    if isinstance(user_date_python, date):
        print("Формат даты правильный")


while True:
    try:
        users_date()
        break
    except ValueError:
        print("Неверный тип даты. Введите любую дату в формате: dd.dd.yyyy")
