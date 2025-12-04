import os
import psycopg2

def run_migrations():
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "postgres"),
        port=os.getenv("POSTGRES_PORT", 5432),
        user=os.getenv("POSTGRES_USER", "test_user"),
        password=os.getenv("POSTGRES_PASSWORD", "postgres"),
        dbname=os.getenv("POSTGRES_DB", "testing_db"),
    )
    cur = conn.cursor()

    with open("init_db.sql", "r") as f:
        sql = f.read()

    cur.execute(sql)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    run_migrations()
