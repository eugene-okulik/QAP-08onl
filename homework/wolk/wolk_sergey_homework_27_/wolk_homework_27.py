import mysql.connector as mysql


db = mysql.connect(
    host='db-mysql-fra1-43438-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='user1',
    passwd='1password1',
    database='QAP'
)

cursor = db.cursor(dictionary=True)


def test_connection():
    cursor.execute('select * from students')
    print(cursor.fetchall())


def test_add_group():
    query = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
    values = ('Lemon', '2022-09-0', '2024-09-03')
    cursor.execute(query, values)
    db.commit()


def test_add_student():
    query = 'INSERT INTO `students` (name, second_name, group_id) VALUES (%s, %s, %s)'
    values = ('Apple', 'Green', '80')
    cursor.execute(query, values)
    db.commit()


def test_add_book():
    cursor.execute('''
    select id from students where second_name = 'Green'
    ''')
    result = cursor.fetchone()
    result2 = result['id']
    query = 'INSERT INTO books (title, taken_by_student_id, return_date) VALUES (%s, %s, %s)'
    values = [
        ('Adventure Book', result2, '2022-09-03'),
        ('Detective Book', result2, '2022-09-03'),
    ]
    cursor.executemany(query, values)
    db.commit()


def test_get_data():
    cursor.execute('''select s.name, s.second_name, g.title, g.id, b.title as book, b.return_date
    from students s
    inner join books b on b.taken_by_student_id = s.id 
    inner join `groups` g on g.id = s.group_id
    where s.second_name = 'Green'
    ''')
    result = cursor.fetchall()
    name = result[0]['name']
    surname = result[0]['second_name']
    group = result[0]['title']
    book1 = result[0]['book']
    book2 = result[1]['book']
    time1 = result[0]['return_date']
    time2 = result[1]['return_date']
    print(f"Student - {name} {surname} is in Group - {group}. "
          f"He took: {book1} - due date: {time1}; {book2} - due date: {time2}.")
db.close()
