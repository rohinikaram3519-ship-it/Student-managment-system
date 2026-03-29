import sqlite3

def connect():
    return sqlite3.connect("students.db")

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        course TEXT,
        email TEXT
    )
    """)
    conn.commit()
    conn.close()

def insert(name, age, course, email):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO student (name, age, course, email) VALUES (?,?,?,?)",
                (name, age, course, email))
    conn.commit()
    conn.close()

def view():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (id,))
    conn.commit()
    conn.close()

create_table()