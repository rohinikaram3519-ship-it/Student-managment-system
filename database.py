import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
        database="studentdb"
    )

def insert(name, age, course, email):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO student (name, age, course, email) VALUES (%s,%s,%s,%s)",
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
    cur.execute("DELETE FROM student WHERE id=%s", (id,))
    conn.commit()
    conn.close()

def update(id, name, age, course, email):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        UPDATE student
        SET name=%s, age=%s, course=%s, email=%s
        WHERE id=%s
    """, (name, age, course, email, id))
    conn.commit()
    conn.close()