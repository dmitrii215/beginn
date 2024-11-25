import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(  
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER
)
''')

for i in range(1, 11):
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)",
                   (f"Users{i}", f"example{i}@mail.com", f"i*10", 1000))

    cursor.execute("SELECT id, username, email, age, balance FROM Users")
    users = cursor.fetchall()

for i, user in enumerate(users):
    if (i + 1)% 2 !=0:
        cursor.execute("UPDATE users SET balance = ? WHERE id = ?", (500, user[0]))

for i, user in enumerate(users):
    if (i + 1)% 3 == 1:
        cursor.execute("DELETE FROM Users WHERE id = ?",( user[0],))

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age !=60")
remaining_user = cursor.fetchall()
for user in remaining_user:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

connection.commit()
connection.close()


