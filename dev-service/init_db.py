import os
import psycopg2

def run_migrations():
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        dbname=os.getenv("POSTGRES_DB"),
    )
    cur = conn.cursor()

    with open("init_db.sql", "r") as f:
        sql = f.read()

    cur.execute(sql)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    run_migrations()
