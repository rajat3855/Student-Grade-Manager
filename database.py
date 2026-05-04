import sqlite3

def init_db():
    conn = sqlite3.connect("grades.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            subject TEXT,
            grade INTEGER,
            letter TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_student(name, subject, grade, letter):
    conn = sqlite3.connect("grades.db")
    conn.execute(
        "INSERT INTO students (name, subject, grade, letter) VALUES (?, ?, ?, ?)",
        (name, subject, grade, letter)
    )
    conn.commit()
    conn.close()

def get_all_students():
    conn = sqlite3.connect("grades.db")
    rows = conn.execute(
        "SELECT id, name, subject, grade, letter FROM students"
    ).fetchall()
    conn.close()
    return rows

def delete_student(student_id):
    conn = sqlite3.connect("grades.db")
    conn.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )
    conn.commit()
    conn.close()

def get_average(subject):
    conn = sqlite3.connect("grades.db")
    row = conn.execute(
        "SELECT AVG(grade) FROM students WHERE subject = ?",
        (subject,)
    ).fetchone()
    conn.close()
    return round(row[0], 2) if row[0] else 0