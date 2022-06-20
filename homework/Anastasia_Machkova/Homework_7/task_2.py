from datetime import datetime
CORRECT_CODE = '123'


def check_coupon(entered_code, expiration_date):
    now = datetime.now()
    expiration_date = now.strptime(expiration_date, "%B %d, %Y")
    if entered_code is not CORRECT_CODE:
        return "Your coupon is expired"
    if expiration_date >= now:
        return "Your coupon is valid"
    return "Your coupon is expired"


print(check_coupon("123", "July 1, 2022"))
print(check_coupon("123", "June 2, 2022"))
