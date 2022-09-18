from datetime import datetime, date

while True:
    try:
        user_input = input("Введите дату: ")
        date_python = datetime.strptime(user_input, '%d/%m/%y')
        if isinstance(date_python, date):
            print("Дата верна")
            break
    except ValueError:
        print("Дата не правильная, попробуй в таком формате dd/mm/yy")
