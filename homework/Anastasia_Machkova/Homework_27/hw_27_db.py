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
values_new_group = ('Titans', '2022-09-15', '2023-09-15')
cursor.execute(NEW_GROUP, values_new_group)
id_group = cursor.lastrowid
db.commit()

NEW_STUDENT = 'INSERT INTO `students` (name, second_name, group_id) VALUES (%s, %s, %s)'
values_new_student = ('Eren', 'Yeager', id_group)
cursor.execute(NEW_STUDENT, values_new_student)
id_student = cursor.lastrowid
db.commit()

NEW_BOOKS = 'INSERT INTO `books` (title, taken_by_student_id, return_date) VALUES (%s, %s, %s)'
values_new_books = [
   ('Attack on Titan_1', id_student, '2022-10-20'),
   ('Attack on Titan_2', id_student, '2022-11-15')
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
      f'in the group {result[0]["title"]} and'
      f'took these books from the library: '
      f'{result[0]["book"]} until {result[0]["return_date"].strftime("%B %d, %Y")}, and '
      f'{result[1]["book"]} until {result[1]["return_date"].strftime("%B %d, %Y")}')

db.close()
