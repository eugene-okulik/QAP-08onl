# У вас интернет магазин, надо написать функцию которая проверяет
# что введен правильный купон и он еще действителен
#
# def check_coupon(entered_code, expiration_date):
# # Code here!
# check_сoupon("123", "July 9, 2022") == True
# check_сoupon("123", "June 2, 2022") == False


from datetime import date


curent_day = date.today().strftime("%B %d, %Y")
print(curent_day)

CORRECT_CODE = '123'
entered_code = input('Введите код купона: ')
expiration_date = input('Введите срок действия купона дд.мм.гггг: ')

if entered_code == CORRECT_CODE:
    print(True)

