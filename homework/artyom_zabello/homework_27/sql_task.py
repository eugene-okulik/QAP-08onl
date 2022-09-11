import mysql.connector as sql


def data_base():
    db_sql = sql.connect(
        host='db-mysql-fra1-43438-do-user-7651996-0.b.db.ondigitalocean.com',
        port=25060,
        user='user1',
        passwd='1password1',
        database='QAP')
    return db_sql


def create_group(db_1):
    cursor = db_1.cursor(dictionary=True)
    query_group = 'Insert into `groups` (title, start_date, end_date) values (%s, %s, %s)'
    val_group = ('Secret', '2022-09-07', '2022-10-07')
    cursor.execute(query_group, val_group)
    db_1.commit()
    cursor.execute("Select * from `groups` WHERE title='Secret'")
    res = cursor.fetchone()['id']
    return res


def create_students(db_1, res_id):
    cursor = db_1.cursor(dictionary=True)
    query_students = 'Insert into students (name,second_name,group_id) values (%s, %s, %s)'
    val_students = ('Alexander', 'Vilka', res_id)
    cursor.execute(query_students, val_students)
    db_1.commit()
    cursor.execute("Select * from students WHERE second_name='Vilka' and name = 'Alexander'")
    res = cursor.fetchone()['id']
    return res


def create_books(db_1, res_id):
    cursor = db_1.cursor(dictionary=True)
    query_books = 'Insert into books(title,taken_by_student_id,return_date) values (%s, %s, %s)'
    val_books = [('Memes', res_id, '2022-11-01'),
                 ('SQL for everybody', res_id, '2022-11-01')]
    cursor.executemany(query_books, val_books)
    db_1.commit()
    cursor.execute("Select * from books WHERE title in ('Mafia','Book2')")


def join_text(db_1, id_student):
    cursor = db_1.cursor(dictionary=True)
    cursor.execute('SELECT st.name , st.second_name , gr.title , bo.title as '
                           'book_title ,bo.return_date from students '
                           'as st join books as bo on st.id  = bo.taken_by_student_id'
                           f' join `groups`as gr on gr.id = st.group_id where st.id = {id_student}')
    result = cursor.fetchall()
    name = result[0]['name'] + " " + result[0]['second_name']
    group = result[0]['title']
    book1 = result[0]['book_title']
    return_book1 = result[0]['return_date']
    book2 = result[1]['book_title']
    return_book2 = result[1]['return_date']
    print(f"Student {name} studies in {group} group and took the following books "
          f"from the library: {book1} until {return_book1} and {book2} until {return_book2}")
    db_1.close()


# create_books(data_base(), create_students(data_base(), create_group(data_base())))
join_text(data_base(), create_students(data_base(), create_group(data_base())))
