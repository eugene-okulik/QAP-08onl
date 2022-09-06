"""System module."""
import mysql.connector as mysql


db = mysql.connect(
    host='db-mysql-fra1-43438-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='user1',
    passwd='1password1',
    database='QAP'
)

cursor = db.cursor(dictionary=True)


def test_check_connection():
    """A dummy docstring."""
    cursor.execute('select * from students')
    print(cursor.fetchall())


# Создает группу (даты в запросе можно указывать как строки, т.е. '2022-04-03')
def test_add_group():
    """A dummy docstring."""
    query = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
    values = ('Lemon', '2022-01-01', '2024-10-01')
    cursor.execute(query, values)
    db.commit()


# Создает студента с именем и фамилией,
# такими как вы придумаете и group_id той группы, что вы создали
def test_add_student():
    """A dummy docstring."""
    query = 'INSERT INTO `students` (id, name, second_name, group_id) VALUES (%s, %s, %s, %s)'
    values = ('98', 'Grapes', 'Purple', '40')
    cursor.execute(query, values)
    db.commit()


# Создает 2 книги. В колонку taken_by_student_id записывает id вашего студента
# и записывает дату когда книгу нужно вернуть (в колонку return_date)
def test_add_book():
    """A dummy docstring."""
    cursor.execute('select id from students where id = 98')
    result = cursor.fetchone()
    result2 = result['id']
    query = 'INSERT INTO books (title, taken_by_student_id, return_date) VALUES (%s, %s, %s)'
    values = [
        ('Adventure Book', result2, '2022-11-01'),
        ('Detective Book', result2, '2022-11-01'),
    ]
    cursor.executemany(query, values)
    db.commit()


# Получает из базы данных данные для студента, которого вы добавили.
# Желательно одним запросом получить и студента и группы и книги (с помощью Join).
# Выводит следующий текст на основании полученных данных:
# Студент Ivan Ivanov учится в группе GPN-001 и взял в библиотеке следующие книги:
# SQL essentials до 15 мая 2022 года, Python for dummies до 1 июня 2022 года

def test_get_data():
    """A dummy docstring."""
    cursor.execute('''select s.name, s.second_name, g.title, g.id, b.title as book, b.return_date
    from students s
    inner join books b on b.taken_by_student_id = s.id 
    inner join `groups` g on g.id = s.group_id
    where s.id = 98
    ''')
    result = cursor.fetchall()
    # print(result)
    name = result[0]['name']
    surname = result[0]['second_name']
    group = result[0]['title']
    book1 = result[0]['book']
    book2 = result[1]['book']
    time1 = result[0]['return_date']
    time2 = result[1]['return_date']
    print(f"Student - {name} {surname} is in Group - {group}. "
          f"He took: {book1} - due date: {time1}; {book2} - due date: {time2}.")
