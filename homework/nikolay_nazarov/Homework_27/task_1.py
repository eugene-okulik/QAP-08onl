from datetime import datetime
import mysql.connector as mysql


STUDENT_NAME = 'Nikolay'
STUDENT_LAST_NAME = 'Nazarov'
STUDENT_GROUP_NAME = 'TPR52313'

db = mysql.connect(
    host='db-mysql-fra1-43438-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='user1',
    passwd='1password1',
    database='QAP'
)


def bd_req():
    cursor = db.cursor(dictionary=True)
    query = 'INSERT INTO `groups` (title, start_date , end_date) VALUES (%s, %s, %s)'
    values = (STUDENT_GROUP_NAME, '1999-01-09', '2011-05-31')
    cursor.execute(query, values)
    group_id = cursor.lastrowid
    db.commit()

    query = 'INSERT INTO students(name, second_name, group_id) VALUES (%s, %s, %s)'
    values = (STUDENT_NAME, STUDENT_LAST_NAME, group_id)
    cursor.execute(query, values)
    student_id = cursor.lastrowid
    db.commit()

    query = 'INSERT INTO books (title, taken_by_student_id, return_date) VALUES (%s, %s, %s)'
    values = ('Captain Jack', student_id, '2011-03-06')
    cursor.execute(query, values)
    db.commit()

    query = 'INSERT INTO books (title, taken_by_student_id, return_date) VALUES (%s, %s, %s)'
    values = ('Captain Sparrow', student_id, '2011-02-05')
    cursor.execute(query, values)
    db.commit()

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
    print(f"Студент {result[0]['name']} учится в группе {result[0]['group_name']} "
          f"и взял в библиотеке следующие книги:"
          f" {result[0]['title']} до "
          f"{datetime.strftime(result[0]['return_date'], '%d %B %Y')} года, "
          f"{result[1]['title']} до {datetime.strftime(result[1]['return_date'], '%d %B %Y')} года")

    db.close()


bd_req()
