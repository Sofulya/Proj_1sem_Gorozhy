import sqlite3 as sq
from new_values import *

with sq.connect('library.db') as con:  # Подключеие к БД
    con.execute("PRAGMA foreing_keys = ON;")
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS authors;")
    cur.execute("DROP TABLE IF EXISTS books;")
    cur.execute("DROP TABLE IF EXISTS sections;")
    cur.execute("DROP TABLE IF EXISTS publishing;")
    cur.execute("DROP TABLE IF EXISTS author_book;")

    cur.execute("""CREATE TABLE IF NOT EXISTS authors (
    id_author INTEGER PRIMARY KEY AUTOINCREMENT,
    surname TEXT NOT NULL,
    name TEXT
    );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS books (
    id_book INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    year_publishing TEXT,
    storage TEXT,
    id_section INTEGER
    REFERENCES sections ON DELETE CASCADE ON UPDATE CASCADE,
    id_publishing INTEGER
    REFERENCES publishing ON DELETE CASCADE ON UPDATE CASCADE
    );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS sections (
    id_section INTEGER PRIMARY KEY AUTOINCREMENT,
    section TEXT
    );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS publishing (
    id_publishing INTEGER PRIMARY KEY AUTOINCREMENT,
    publishing TEXT,
    city TEXT
    );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS author_book (
    id_author_book INTEGER PRIMARY KEY AUTOINCREMENT,
    id_book INTEGER
    REFERENCES books ON DELETE CASCADE ON UPDATE CASCADE,
    id_author INTEGER
    REFERENCES authors ON DELETE CASCADE ON UPDATE CASCADE
    );""")

with sq.connect('library.db') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO authors VALUES (?, ?, ?)", info_authors)
    cur.executemany("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?)", info_books)
    cur.executemany("INSERT INTO sections VALUES (?, ?)", info_sections)
    cur.executemany("INSERT INTO publishing VALUES (?, ?, ?)", info_publishing)
    cur.executemany("INSERT INTO author_book VALUES (?, ?, ?)", info_author_book)

# SELECTS (SQL-запросы на выборку данных из БД)
with sq.connect('library.db') as con:
    cur = con.cursor()

    print('\n1.')
    for result_1 in cur.execute("SELECT name, year_publishing FROM books ORDER BY year_publishing"):
        print(*result_1)

    print('\n2.')
    for result_2 in cur.execute("""SELECT books.name FROM books JOIN author_book ON books.id_book = author_book.id_book
            JOIN authors ON author_book.id_author = authors.id_author WHERE authors.surname = ? AND authors.name = ?""",
                                ('Толстой', 'Лев')):
        print(*result_2)

    print('\n3.')
    for result_3 in cur.execute("""SELECT name FROM books JOIN sections ON books.id_section = sections.id_section
        WHERE sections.section = ?""", ('Роман',)):
        print(*result_3)

    print('\n4.')
    for result_4 in cur.execute("""SELECT name FROM books JOIN publishing ON books.id_publishing = 
    publishing.id_publishing WHERE publishing.publishing = ?""", ('Эксмо',)):
        print(*result_4)

    print('\n5.')
    for result_5 in cur.execute("SELECT surname, name FROM authors ORDER BY surname, name"):
        print(*result_5)

    print('\n6.')  # поработать над ним
    for result_6 in cur.execute("SELECT name, year_publishing FROM books ORDER BY name, year_publishing"):
        print(*result_6)

    print('\n7.')
    for result_7 in cur.execute("""SELECT books.name, year_publishing FROM books JOIN
        author_book ON books.id_book = author_book.id_book JOIN authors ON author_book.id_author = authors.id_author
        WHERE authors.surname = ? AND authors.name = ? ORDER BY year_publishing""", ('Петров', 'Александр')):
        print(*result_7)

    print('\n8.')
    for result_8 in cur.execute("SELECT name FROM books WHERE year_publishing='2010 г.'"):
        print(*result_8)

    print('\n9.')
    for result_9 in cur.execute("""SELECT authors.surname, authors.name FROM authors JOIN
       author_book ON authors.id_author = author_book.id_author JOIN
       books ON author_book.id_book = books.id_book JOIN
       publishing ON books.id_publishing = publishing.id_publishing WHERE publishing.publishing = ?""", ('Эксмо',)):
        print(*result_9)

    print('\n10.')
    for result_10 in cur.execute("SELECT name FROM books WHERE name LIKE ?", ('%Волшебник%',)):
        print(*result_10)

# UPDATES (SQL-запросы на обновление данных из БД)
# with sq.connect('library.db') as con:
#     cur = con.cursor()
#
#     # 1. Обновить год издания всех книг, написанных автором с фамилией "Иванов", установив год издания равным 2022:
#     cur.execute("""UPDATE books SET year_publishing = '2022 г.' WHERE id_book IN (SELECT id_book FROM author_book JOIN
#     authors ON author_book.id_author = authors.id_author WHERE surname = 'Иванов')""")
#
#     # 2. Обновить название и год издания книги, хранящейся в городе "Москва", установив
#     # название "Новая книга" и год издания равным 2023:
#     cur.execute("UPDATE books SET name = 'Новая книга', year_publishing = 2023 WHERE storage = 'Москва'")
#
#     # 3. Обновить название и раздел всех книг, написанных автором с именем "Александр" и фамилией "Петров", установив
#     # название "Новое название" и раздел "Фантастика":
#     cur.execute("""UPDATE books SET name = 'Новое название', id_section = (SELECT id_section FROM sections
#     WHERE section = 'Фантастика') WHERE id_book IN (SELECT id_book FROM author_book JOIN
#     authors ON author_book.id_author = authors.id_author WHERE name = 'Александр' AND surname = 'Петров')""")
#
#     # 4. Обновить название всех книг, которые были опубликованы в годы с 2010 по 2015 включительно, установив
#     # название "Старое название":
#     cur.execute("UPDATE books SET name = 'Старое название' WHERE year_publishing BETWEEN 2010 AND 2015")
#
#     # 5. Обновить место хранения всех книг, написанных автором с кодом 7, установив место хранения "Библиотека №2":
#     cur.execute("""UPDATE books SET storage = 'Библиотека №2' WHERE id_book IN (SELECT id_book FROM author_book
#     WHERE id_author = 7)""")
#
#     # 6. Обновление города из таблицы Издательства по коду города в таблице Книги:
#     cur.execute("""UPDATE publishing SET city = (SELECT city FROM books
#     WHERE books.id_publishing = publishing.id_publishing)""")
#
#     # 7. Обновление кода автора в таблице АвторКниги по коду автора в таблице Авторы:
#     cur.execute("""UPDATE author_book SET id_author = (SELECT id_author FROM authors
#     WHERE authors.id_author = author_book.id_author)""")
#
#     # 8. Обновление названия раздела в таблице Книги по названию раздела в таблице Разделы:
#     cur.execute("""UPDATE books SET id_section = (SELECT id_section FROM sections
#     WHERE sections.section = books.id_section)""")
#
#     # 9. Обновление года издания в таблице books по году издания в таблице author_book:
#     cur.execute("""UPDATE books SET year_publishing = 2022
#                 WHERE id_book IN (SELECT id_book FROM author_book WHERE year_publishing = 2021)""")
#
#     # 10. Обновление места хранения в таблице books по названию издательства в таблице publishing:
#     cur.execute("""UPDATE books SET storage = 'Книжный шкаф 3'
#                 WHERE id_publishing IN (SELECT id_publishing FROM publishing WHERE publishing = 'Эксмо')""")
#
#     # 11. Обновление фамилии автора в таблице authors по коду автора в таблице author_book:
#     cur.execute("""UPDATE authors SET surname = 'Новая фамилия'
#                 WHERE id_author IN (SELECT id_author FROM author_book WHERE id_author = 1)""")
#
#     # 12. Обновить год издания всех книг, изданных в городе "Москва", на 2022 год.
#     cur.execute("""UPDATE books SET year_publishing = '2022 г.'
#                 WHERE id_publishing IN (SELECT id_publishing FROM publishing WHERE city = 'Москва')""")
#
#     # 13. Обновить место хранения всех книг, написанных автором с фамилией "Иванов", на "Книжный шкаф 1".
#     cur.execute("""UPDATE books SET storage = 'Книжный шкаф 1' WHERE id_book IN (SELECT id_book FROM author_book
#     WHERE id_author IN (SELECT id_author FROM authors WHERE surname = 'Иванов'))""")
#
#     # 14. Обновить год издания всех книг, написанных автором с именем "Анна", на 2023 год.
#     cur.execute("""UPDATE books SET year_publishing = '2023 г.' WHERE id_book IN (SELECT id_book FROM author_book
#     WHERE id_author IN (SELECT id_author FROM authors WHERE name = 'Анна'))""")
#
#     # 15. Обновить название раздела всех книг, изданных в городе "Санкт-Петербург", на "Классика".
#     cur.execute("""UPDATE books SET id_section = (SELECT id_section FROM sections WHERE section = 'Классика')
#                 WHERE id_publishing IN (SELECT id_publishing FROM publishing WHERE city = 'Санкт-Петербург')""")
#
#     # 16. Обновить год издания всех книг, написанных автором с фамилией "Петров", на 2024 год.
#     cur.execute("""UPDATE books SET year_publishing = '2024 г.' WHERE id_book IN (SELECT id_book FROM author_book
#                 WHERE id_author IN (SELECT id_author FROM authors WHERE surname = 'Петров'))""")
