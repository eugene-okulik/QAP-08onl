from datetime import datetime, date

while True:
    try:
        res = input('Enter date ')
        date1 = datetime.strptime(res, '%b %d, %Y')
        if isinstance(date1, date):
            print("Date is correct")
            break
    except ValueError:
        print("Date type is incorrect, try again in format %b %d, %Y")
