from datetime import datetime
CORRECT_CODE = '123'


def check_coupon(entered_code, expiration_date):
    now = datetime.now()
    date = datetime.strptime(expiration_date, "%B %d, %Y")
    if entered_code == CORRECT_CODE:
        if now > date:
            print('Your coupon has expired')
            return False
        else:
            period = date - now
            print(f'Your coupon is valid {period.days} days left')
            return True


print(check_coupon("123", "July 9, 2022"))
print(check_coupon("123", "June 2, 2022"))
