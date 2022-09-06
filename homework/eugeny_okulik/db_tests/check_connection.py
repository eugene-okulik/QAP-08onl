import mysql.connector as mysql

db = mysql.connect(
   host='db-mysql-fra1-43438-do-user-7651996-0.b.db.ondigitalocean.com',
   port=25060,
   user='user1',
   passwd='1password1',
   database='QAP'
)

cursor = db.cursor()
cursor.execute('select * from students')
print(cursor.fetchall())

db.close()
