import sqlite3

def get_connection():
    conn = sqlite3.connect("employees.db", check_same_thread=False)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        department TEXT,
        salary INTEGER,
        experience INTEGER,
        performance INTEGER,
        attrition INTEGER
    )
    """)

    conn.commit()
    return conn
