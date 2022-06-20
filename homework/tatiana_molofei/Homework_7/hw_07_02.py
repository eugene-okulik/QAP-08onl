# У вас интернет магазин, надо написать функцию которая проверяет
# что введен правильный купон и он еще действителен


from datetime import datetime

correct_code = set(range(100, 201))

expiration_date = datetime(2022, 7, 31)
expiration_date = expiration_date.strftime("%B %d, %Y")

curent_day = datetime.now()
curent_day = curent_day.strftime("%B %d, %Y")

# user_code = int(input(f'Enter your coupon number: '))
# user_date = input(f'Enter your coupon expiration date Month name dd, yyyy: ')


def check_coupon(user_code, user_date):
    if expiration_date >= user_date >= curent_day and user_code in correct_code:
        return True
    return False


print(check_coupon(int(input(f'Enter your coupon number: ')),
                   input(f'Enter your coupon expiration date Month name dd, yyyy: ')))
