import mysql.connector as mysql


db = mysql.connect(
   host='db-mysql-fra1-43438-do-user-7651996-0.b.db.ondigitalocean.com',
   port=25060,
   user='user1',
   passwd='1password1',
   database='QAP'
)

cursor = db.cursor(dictionary=True)
# cursor.execute('select * from `groups`')
# print(cursor.fetchall())


CREATE_NEW_GROUP = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
values_new_group = ('TOM-22', '2022-01-01', '2024-08-10')
cursor.execute(CREATE_NEW_GROUP, values_new_group)
db.commit()

cursor.execute('select * from `groups`')
result = cursor.fetchall()
ID_TOM_22 = None
for groups in result:
    if groups['title'] == 'TOM-22':
        id_tom_22 = groups['id']


CREATE_NEW_STUDENT = 'INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)'
values_new_student = ('Lionel', 'Messi', ID_TOM_22)
cursor.execute(CREATE_NEW_STUDENT, values_new_student)
db.commit()

cursor.execute('select * from students')
result = cursor.fetchall()
ID_STUDENT = None
for student in result:
    if student['group_id'] == ID_TOM_22:
        ID_STUDENT = student['id']


CREATE_NEW_BOOKS = 'INSERT INTO books (title, taken_by_student_id, return_date) VALUES (%s, %s, %s)'
values_new_books = [
    ('Cat in the bag', ID_STUDENT, '2022-09-15'),
    ('The Witches', ID_STUDENT, '2022-10-12')
]
cursor.executemany(CREATE_NEW_BOOKS, values_new_books)
db.commit()

cursor.execute('select * from books')
result = cursor.fetchall()
student_books = []
book_return_date = []
for books in result:
    if books['taken_by_student_id'] == ID_STUDENT:
        student_books.append(books['title'])
        book_return_date.append(books['return_date'])

print(f'Student {student["name"]} {student["second_name"]} studies '
      f'in the {groups["title"]} group and '
      f'took the following books from the library: '
      f'{student_books[0]} until {book_return_date[0].strftime("%B %d, %Y")}, '
      f'{student_books[1]} until {book_return_date[1].strftime("%B %d, %Y")}')

db.close()
