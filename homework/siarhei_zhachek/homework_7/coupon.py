from datetime import datetime
CORRECT_CODE = '123'


def check_coupon(entered_code, expiration_date):
    now = datetime.now()
    date = datetime.strptime(expiration_date, "%B %d, %Y")
    if entered_code == CORRECT_CODE:
        if now > date:
            return 'Your coupon has expired'

        period = date - now
        return f'Your coupon is valid {period.days} days left'
    return 'There is no such coupon'


print(check_coupon("123", "July 9, 2022"))
print()
print(check_coupon("123", "June 2, 2022"))
