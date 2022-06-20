from datetime import datetime
CORRECT_CODE = '123'


def check_coupon(entered_code, expiration_date):
    now = datetime.now()
    date = datetime.strptime(expiration_date, "%B %d, %Y")
    if entered_code == CORRECT_CODE:
        if now > date:
            print('Your coupon has expired')
        else:
            period = date - now
            print(f'Your coupon is valid {period.days} days left')
    else:
        print('There is no such coupon')


print(check_coupon(input('Enter the coupon: '), input('Enter the date(Month dd,YYYY): ')))
