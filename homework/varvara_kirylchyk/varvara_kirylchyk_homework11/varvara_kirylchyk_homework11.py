# Обработка исключений

# Попросите пользователя ввести дату
# и попробуйте преобразовать дату в формат питона.
#
# В случае, если пользователь не угадал с форматом ввода даты,
# вы получите исключение.
#
# Обработайте это исключение и подскажите пользователю в каком формате нужно вводить дату

from datetime import datetime
from datetime import date

user_date = input('Enter date: ')
python_date = datetime.strptime(user_date, '%d/%m/%Y')

while True:
    try:
        if isinstance(python_date, date):
            print("Date format is correct")
            break
    except ValueError:
        print("Date type is incorrect. Please apply the format: DD/MM/YYYY")
