from datetime import datetime

user_date = input('Enter the date: ')

try:
    date = datetime.strptime(user_date, "%B %d, %Y")
    print(f'You entered the correct date: {date}')
except ValueError:
    print('Enter the date in the format: Month DD, YYYY')
