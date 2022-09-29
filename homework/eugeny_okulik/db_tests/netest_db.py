import mysql.connector as mysql

db = mysql.connect(
   host='db-mysql-fra1-43438-do-user-7651996-0.b.db.ondigitalocean.com',
   port=25060,
   user='user1',
   passwd='1password1',
   database='QAP'
)

cursor = db.cursor(dictionary=True)
# cursor.execute('select * from students')
# result = cursor.fetchall()
# for student in result:
#     print(student['name'])

# cursor.execute('select * from books where id = 1')
# result = cursor.fetchone()
# print(result['title'])


QUERY = 'INSERT INTO students (name, second_name) VALUES (%s, %s)'
values = ('1Vasia1', '1Pupkin1')
cursor.execute(QUERY, values)
db.commit()

# query = '''
# SELECT * FROM students
#    WHERE name = "George"
#    AND surname = "Washington"
#    AND id
#    in(SELECT student
#       FROM library
#       WHERE book_title = "Python for dummies")
# '''

db.close()
