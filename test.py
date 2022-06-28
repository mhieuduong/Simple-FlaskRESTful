import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'jose', 'asdf')
users = [
    (2, 'rolf', 'adsf'),
    (3, 'hiuu', '123')
]
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()
