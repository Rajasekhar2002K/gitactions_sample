import sqlite3
import os

DB_PATH = os.getenv("DB_PATH", "test.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def get_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM users WHERE id=?", (user_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return {"id": row[0], "name": row[1]}
    return None
