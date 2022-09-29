import pytest
import mysql.connector as mysql


@pytest.fixture(scope='session')
def cursor():
    db_connection = mysql.connect(
       host='db-mysql-fra1-43438-do-user-7651996-0.b.db.ondigitalocean.com',
       port=25060,
       user='user1',
       passwd='1password1',
       database='QAP'
    )
    my_cursor = db_connection.cursor(dictionary=True)
    yield my_cursor
    db_connection.close()
