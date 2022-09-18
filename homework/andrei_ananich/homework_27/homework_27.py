"""modules"""
from datetime import datetime
import mysql.connector as mysql


STUDENT_NAME = 'Ivan'
STUDENT_LAST_NAME = 'Ivanov'
STUDENT_GROUP_NAME = '123'
BOOK1 = 'New book1'
BOOK2 = 'New book2'


def request_in_db():
    """modules"""
    d_b = mysql.connect(
        host='db-mysql-fra1-43438-do-user-7651996-0.b.db.ondigitalocean.com',
        port=25060,
        user='user1',
        passwd='1password1',
        database='QAP'
    )
    cursor = d_b.cursor(dictionary=True)
    new_group = 'INSERT INTO `groups`(title, start_date, end_date) VALUES (%s, %s, %s)'
    values_of_the_group = (STUDENT_GROUP_NAME, '1999-01-09', '2011-05-31')
    cursor.execute(new_group, values_of_the_group)
    group_id = cursor.lastrowid
    d_b.commit()

    new_student = 'INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)'
    values_student = (STUDENT_NAME, STUDENT_LAST_NAME, group_id)
    cursor.execute(new_student, values_student)
    student_id = cursor.lastrowid
    d_b.commit()

    new_book1 = 'INSERT INTO books (title, taken_by_student_id, return_date) VALUES (%s, %s, %s)'
    values_new_book1 = (BOOK1, student_id, '2000-11-12')
    cursor.execute(new_book1, values_new_book1)
    d_b.commit()

    new_book2 = 'INSERT INTO books (title, taken_by_student_id, return_date) VALUES (%s, %s, %s)'
    values_new_book2 = (BOOK2, student_id, '2000-11-12')
    cursor.execute(new_book2, values_new_book2)
    d_b.commit()

    cursor.execute(
        f'''
        SELECT s.id, s.name, s.second_name, g.title 'group_name', b.title, b.return_date
        FROM students as s
        JOIN `groups` as g
        ON s.group_id = g.id
        JOIN books as b
        ON s.id = b.taken_by_student_id
        WHERE s.id = {student_id}
    '''
    )
    result = cursor.fetchall()

    print(f"Student {result[0]['name']} {result[0]['second_name']} "
          f"studies in the {result[0]['title']} group and "
          f"took the following books from the library:"
          f"{result[0]['title']} until {datetime.strftime(result[0]['return_date'], '%B %d, %Y')},"
          f"{result[1]['title']} until {datetime.strftime(result[1]['return_date'], '%B %d, %Y')}"
          )

    d_b.close()


request_in_db()
