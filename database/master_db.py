import sqlite3

db = sqlite3.connect('bookshelf.db')

# Creating a Cursor
cursor = db.cursor()


"""Creating a Table - "Read Books"""
# cursor.execute("""CREATE TABLE all_users (
#     id integer PRIMARY KEY,
#     user_name text UNIQUE ,
#     author text DEFAULT 'кто-то'
# )""")


"""Удаление таблицы"""
# cursor.execute("DROP TABLE all_users")

"""Добавление в таблицу"""
# cursor.execute("INSERT INTO read_books VALUES ('Pasternak', 'Михаил Елизаров')")
# cursor.execute("INSERT INTO read_books (title) VALUES ('Мы вышли покурить на 17 лет')")
# cursor.execute("INSERT INTO read_books (author) VALUES ('Михаил Елизаров')")


"""Добавление в конкретную ячейку конкретной строки таблицы"""
# cursor.execute("""UPDATE read_books SET author = 'Михаил Елизаров'
# WHERE title = 'Мы вышли покурить на 17 лет' AND author is null""")

# cursor.execute("""UPDATE read_books SET title = 'Бураттини' WHERE AUTHOR = 'Михаил Елизаров' AND title is null""")

"""Комиттинг в таблицу"""
db.commit()


"""Выводим все даныне из таблицы (а -> генератор) ///"""
# a = cursor.execute('SELECT * FROM read_books')

"""Выборка данных"""
# cursor.execute("SELECT * FROM read_books")
# print(cursor.fetchall())

"""получаем последнее значение"""
# last_input = cursor.execute("""SELECT * FROM read_books ORDER BY id DESC""")
# for i in last_input:
#     print(i)
# print('#'*45)
# получаем значение по ID

# last_id = cursor.execute("""SELECT * FROM read_books ORDER BY id DESC LIMIT 1""")
# print(last_id.fetchall()[0][2])

# if not cursor.fetchall():
#     print('nothing in the table')
# else:
#     print('bubba?')
#     print(cursor.fetchall())
#
# for i in last_id:
#     print(i)

db.close()
