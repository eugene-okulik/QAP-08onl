# Обработка исключений

# Попросите пользователя ввести дату
# и попробуйте преобразовать дату в формат питона.
#
# В случае, если пользователь не угадал с форматом ввода даты,
# вы получите исключение.
#
# Обработайте это исключение и подскажите пользователю в каком формате нужно вводить дату

from datetime import datetime

user_date = input('Enter date: ')

try:
    python_date = datetime.strptime(user_date, '%d/%m/%Y')
    print("The date format is correct.")
except ValueError:
    print("Date type is incorrect. Please apply the format: DD/MM/YYYY")
