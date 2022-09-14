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
values_new_group = ('Group-15', '2022-07-01', '2025-09-14')
cursor.execute(NEW_GROUP, values_new_group)
id_group_15 = cursor.lastrowid
db.commit()

NEW_STUDENT = 'INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)'
values_new_student = ('Arya', 'Stark', id_group_15)
cursor.execute(NEW_STUDENT, values_new_student)
id_student = cursor.lastrowid
db.commit()

NEW_BOOKS = 'INSERT INTO books (title, taken_by_student_id, return_date) VALUES (%s, %s, %s)'
values_new_books = [
    ('"A Game of Thrones"', id_student, '2022-10-01'),
    ('"A Clash of Kings"', id_student, '2022-11-25')
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

result = cursor.fetchall()

print(f'Student {result[0]["name"]} {result[0]["second_name"]} studies '
      f'in the {result[0]["title"]} group and '
      f'took the following books from the library: '
      f'{result[0]["book"]} until {result[0]["return_date"].strftime("%B %d, %Y")}, '
      f'{result[1]["book"]} until {result[1]["return_date"].strftime("%B %d, %Y")}')

db.close()
