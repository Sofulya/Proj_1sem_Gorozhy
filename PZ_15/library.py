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
    id_section TEXT
    REFERENCES sections ON DELETE CASCADE ON UPDATE CASCADE,
    id_publishing TEXT
    REFERENCES publishing ON DELETE CASCADE ON UPDATE CASCADE
    );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS sections (
    id_section INTEGER PRIMARY KEY AUTOINCREMENT,
    chapter TEXT
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

with sq.connect('Library.db') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO authors VALUES (?, ?, ?)", info_authors)
    cur.executemany("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?)", info_books)
    cur.executemany("INSERT INTO sections VALUES (?, ?)", info_sections)
    cur.executemany("INSERT INTO publishing VALUES (?, ?, ?)", info_publishing)
    cur.executemany("INSERT INTO author_book VALUES (?, ?, ?)", info_author_book)
