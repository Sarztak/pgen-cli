import sqlite3

conn = sqlite3.connect("passwords.db")
cursor = conn.cursor()

cursor.execute("""
create table if not exists passwords (
    id integer primary key autoincrement,
    name text unique not null,
    password text not null
) 
""")

cursor.execute("""
create table if not exists master (
    id integer primary key check (id = 1),
    hash text not null
)
""")

conn.commit()