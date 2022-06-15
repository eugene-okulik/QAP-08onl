from datetime import datetime


def check_coupon(entered_code, expiration_date):
    """This function checks coupon's validity"""
    correct = ['123', '543', '7656', '970', '013']
    now = datetime.now()
    date = datetime.strptime(expiration_date, "%B %d, %Y")
    if entered_code not in correct:
        return "Your coupon is not correct"
    if date < now:
        return "Your coupon is expired"
    period = date - now
    return f"Your coupon  will be valid {period.days} days yet"


print(check_coupon(input(), input()))

# print(check_coupon("123", "July 9, 2022"))
# print(check_coupon("123", "June 2, 2022"))
