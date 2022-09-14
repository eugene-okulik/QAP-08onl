import mysql.connector as mysql


db = mysql.connect(
   host='db-mysql-fra1-43438-do-user-7651996-0.b.db.ondigitalocean.com',
   port=25060,
   user='user1',
   passwd='1password1',
   database='QAP'
)

cursor = db.cursor(dictionary=True)

new_group = 'INSERT INTO `groups` (title, start_date, end_date) ' \
            'VALUES (%s, %s, %s)'
values_new_group = ('JUNGLES', '2022-02-02', '2022-09-10')
cursor.execute(new_group, values_new_group)
id_group = cursor.lastrowid
db.commit()

new_student = 'INSERT INTO students (name, second_name, group_id) ' \
            'VALUES (%s, %s, %s)'
values_student = ('Lion', 'King', id_group)
cursor.execute(new_student, values_student)
id_student = cursor.lastrowid
db.commit()

new_book_1 = 'INSERT INTO books (title, taken_by_student_id, return_date) ' \
            'VALUES (%s, %s, %s)'
value_book_1 = [
    ('"Duma-ki"', id_student, '2022-09-17')
]
cursor.execute(new_book_1, value_book_1)
db.commit()

new_book_2 = 'INSERT INTO books (title, taken_by_student_id, return_date) ' \
            'VALUES (%s, %s, %s)'
value_book_2 = [
    ('"Kydjo"', id_student, '2022-10-01')
]
cursor.execute(new_book_2, value_book_2)
db.commit()

cursor.execute(f'''
SELECT s.name, s.second_name, s.id, g.title as book, b.return_date
FROM students as s
JOIN `groups` as g
ON g.id = s.id_group
JOIN books as b
ON b.taken_by_student_id = s.id
WHERE s.id = {id_student}
''')

result = cursor.fetchall()

print(f'Student {result[0]["name"]} {result[0]["second_name"]} studies '
      f'in this group - {result[0]["title"]}, and '
      f'took this books from the library: '
      f'{result[0]["book"]} until {result[0]["return_date"].strftime("%B %d, %Y")}, and'
      f'{result[1]["book"]} until {result[1]["return_date"].strftime("%B %d, %Y")}')

db.close()
