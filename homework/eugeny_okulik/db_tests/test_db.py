def test_update(cursor):
    cursor.execute("update students set name = 'Joe' where id = 4")
    cursor.execute("select * from students where id = 4")
    assert cursor.fetchone()['name'] == 'Joe'
