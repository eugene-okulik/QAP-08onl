# Попросите пользователя ввести дату и попробуйте преобразовать дату в формат питона.
# В случае, если пользователь не угадал с форматом ввода даты, вы получите исключение.
# Обработайте это исключение и подскажите пользователю в каком формате нужно вводить дату

from datetime import datetime

user_input = input('Please, enter date')

try:
    python_format = datetime.strptime(user_input, '%d/%m/%Y')
    print('This is right date format')

except ValueError:
    print('This is not correct date format. Please, use this one: DD/MM/YYYY')
