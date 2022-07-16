from datetime import datetime
from datetime import date

print('Please, enter the date:')


def chosen_date():
    user_date = input()
    user_date_format = datetime.strptime(user_date, '%d-%m-%Y').date()
    if isinstance(user_date_format, date):
        print('Correctly! This is the correct format.')


while True:
    try:
        chosen_date()
        break
    except ValueError:
        print('Please enter a date in the following format: %d-%m-%Y')
