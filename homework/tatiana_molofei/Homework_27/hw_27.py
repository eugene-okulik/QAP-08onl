import mysql.connector as mysql


db = mysql.connect(
   host='db-mysql-fra1-43438-do-user-7651996-0.b.db.ondigitalocean.com',
   port=25060,
   user='user1',
   passwd='1password1',
   database='QAP'
)

cursor = db.cursor(dictionary=True)

# Создает группу (даты в запросе можно указывать как строки, т.е. '2022-04-03')

CREATE_NEW_GROUP = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
values_new_group = ('TOM-22', '2022-01-01', '2024-08-10')
cursor.execute(CREATE_NEW_GROUP, values_new_group)
id_tom_22 = cursor.lastrowid
db.commit()

# Создает студента с именем и фамилией, такими как вы придумаете
# и group_id той группы, что вы создали

CREATE_NEW_STUDENT = 'INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)'
values_new_student = ('Lionel', 'Messi', id_tom_22)
cursor.execute(CREATE_NEW_STUDENT, values_new_student)
id_student = cursor.lastrowid
db.commit()


# Создает 2 книги. В колонку taken_by_student_id записывает id вашего студента и
# записывает дату когда книгу нужно вернуть (в колонку return_date)

CREATE_NEW_BOOKS = 'INSERT INTO books (title, taken_by_student_id, return_date) VALUES (%s, %s, %s)'
values_new_books = [
    ('"Cat in the bag"', id_student, '2022-09-15'),
    ('"The Witches"', id_student, '2022-10-12')
]
cursor.executemany(CREATE_NEW_BOOKS, values_new_books)
db.commit()

#
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
