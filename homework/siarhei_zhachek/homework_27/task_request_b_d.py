from datetime import datetime
import mysql.connector as mysql


group_name = input('Enter group name: ')
start_date = input('Enter start date of classes(YYYY.mm.dd): ')
end_date = input('Enter the end date of classes(YYYY.mm.dd): ')
student_name = input('Enter first name: ')
student_second_name = input('Enter second name: ')
book_1 = input('Enter the name of the first book: ')
return_date_book_1 = input('Return date of the book(YYYY.mm.dd): ')
book_2 = input('Enter the name of the second book: ')
return_date_book_2 = input('Return date of the book(YYYY.mm.dd): ')


def task_request_b_d():
    d_b = mysql.connect(
        host='db-mysql-fra1-43438-do-user-7651996-0.b.db.ondigitalocean.com',
        port=25060,
        user='user1',
        passwd='1password1',
        database='QAP'
    )

    cursor = d_b.cursor(dictionary=True)

    my_group = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s) "
    values_group = (group_name, start_date, end_date)
    cursor.execute(my_group, values_group)
    group_id = cursor.lastrowid
    d_b.commit()

    my_student = 'INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)'
    values_student = (student_name, student_second_name, group_id)
    cursor.execute(my_student, values_student)
    student_id = cursor.lastrowid
    d_b.commit()

    my_book1 = 'INSERT INTO books (title, taken_by_student_id, return_date) VALUES (%s, %s, %s)'
    values_book1 = (book_1, student_id, return_date_book_1)
    cursor.execute(my_book1, values_book1)
    d_b.commit()

    my_book2 = 'INSERT INTO books (title, taken_by_student_id, return_date) VALUES (%s, %s, %s)'
    values_book2 = (book_2, student_id, return_date_book_2)
    cursor.execute(my_book2, values_book2)
    d_b.commit()

    cursor.execute(
        f'''
            SELECT s.id, s.name, s.second_name, g.title 'group_name', b.title, b.return_date
                FROM students as s
                JOIN `groups` as g
                ON s.group_id = g.id
                JOIN books b
                ON s.id = b.taken_by_student_id
                WHERE s.id = {student_id}
    '''
    )
    result = cursor.fetchall()
    print()
    print(
        f"Student {result[0]['name']} {result[0]['second_name']} "
        f"studies in {result[0]['group_name']} group \n"
        "and took the following books from the library: \n"
        f"{result[0]['title']} until {datetime.strftime(result[0]['return_date'], '%d %B %Y')},"
        f" {result[1]['title']} until {datetime.strftime(result[1]['return_date'], '%d %B %Y')}."
    )

    d_b.close()


task_request_b_d()
