import mysql.connector as mysql

db = mysql.connect(
    host='db-mysql-fra1-43438-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='user1',
    passwd='1password1',
    database='QAP'
)

cursor = db.cursor(dictionary=True)

NEW_GROUP = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
values_of_the_group = ('Gryffindor', '1999-01-09', '2011-05-31')
cursor.execute(NEW_GROUP, values_of_the_group)
GRYFFINDOR = cursor.lastrowid
db.commit()

NEW_STUDENT = 'INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)'
values_of_the_new_student = ('Harry', 'Potter', GRYFFINDOR)
cursor.execute(NEW_STUDENT, values_of_the_new_student)
id_student = cursor.lastrowid
db.commit()

NEW_BOOKS = 'INSERT INTO books (title, taken_by_student_id, return_date) VALUES (%s, %s, %s)'
values_new_books = [
    ('"Harry Potter and the Sorcerer stone"', id_student, '1999-10-12'),
    ('"Harry Potter and the Chamber of Secrets"', id_student, '2000-01-01')
]
cursor.executemany(NEW_BOOKS, values_new_books)
db.commit()

cursor.execute(f'''
SELECT s.name, s.second_name, g.title, g.id, b.title as book, b.return_date
FROM students as s
INNER JOIN `groups` as g
ON g.id = s.group_id
INNER JOIN books as b 
ON b.taken_by_student_id = s.id
WHERE s.id = {id_student}
''')

res = cursor.fetchall()

print(f'Student {res[0]["name"]} {res[0]["second_name"]} studies '
      f'in the {res[0]["title"]} group and '
      f'took the following books from the library: '
      f'{res[0]["book"]} until {res[0]["return_date"].strftime("%B %d, %Y")} ,'
      f'{res[1]["book"]} until {res[1]["return_date"].strftime("%B %d, %Y")}')

db.close()
