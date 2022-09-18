from datetime import datetime

CODE = "123"
DATE = datetime.now()
K_DATE = DATE.strftime('%B %d, %Y')
_entered_code = (input('Введите номер купона: '))
_expiration_date = (input('Введите дату в формате (Month name DD, YYYY): '))

def check_coupon(_entered_code, _expiration_date):
    if _entered_code == CODE and _expiration_date >= K_DATE:
        return True
    return False


print(check_coupon(_entered_code, _expiration_date))
