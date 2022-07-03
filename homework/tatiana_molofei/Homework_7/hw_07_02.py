# У вас интернет магазин, надо написать функцию которая проверяет
# что введен правильный купон и он еще действителен


from datetime import datetime
# from datetime import date


correct_code = set(range(100, 201))

current_day = datetime.now()


def check_coupon(user_code, user_date):
    user_date_python = datetime.strptime(user_date, "%B %d, %Y")
    if user_date_python >= current_day and user_code in correct_code:
        return True
    return False


print(check_coupon(int(input('Enter your coupon number: ')),
                   input('Enter your coupon expiration date Month name dd, yyyy: ')))
