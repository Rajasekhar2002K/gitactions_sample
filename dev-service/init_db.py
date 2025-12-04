import os
import time
import psycopg2

def wait_for_postgres():
    retries = 10
    while retries > 0:
        try:
            conn = psycopg2.connect(
                host=os.getenv("POSTGRES_HOST", "postgres"),
                port=os.getenv("POSTGRES_PORT", 5432),
                user=os.getenv("POSTGRES_USER", "test_user"),
                password=os.getenv("POSTGRES_PASSWORD", "postgres"),
                dbname=os.getenv("POSTGRES_DB", "testing_db"),
            )
            conn.close()
            return True
        except psycopg2.OperationalError:
            retries -= 1
            print("Postgres not ready, waiting 2s...")
            time.sleep(2)
    raise Exception("Postgres not ready after 20s")

def run_migrations():
    wait_for_postgres()
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "postgres"),
        port=os.getenv("POSTGRES_PORT", 5432),
        user=os.getenv("POSTGRES_USER", "test_user"),
        password=os.getenv("POSTGRES_PASSWORD", "postgres"),
        dbname=os.getenv("POSTGRES_DB", "testing_db"),
    )
    cur = conn.cursor()
    with open("dev-service/init_db.sql") as f:
        cur.execute(f.read())
    conn.commit()
    conn.close()

if __name__ == "__main__":
    run_migrations()
