import os
import time
import psycopg2


def wait_for_postgres():
    print("DB Host:", os.getenv("POSTGRES_HOST"))
    retries = 30 
    while retries > 0:
        try:
            conn = psycopg2.connect(
                host=os.getenv("POSTGRES_HOST", "localhost"),
                port=os.getenv("POSTGRES_PORT", 5432),
                user=os.getenv("POSTGRES_USER", "test_user"),
                password=os.getenv("POSTGRES_PASSWORD", "postgres"),
                dbname=os.getenv("POSTGRES_DB", "testing_db"),
            )
            conn.close()
            print("Postgres is ready.")
            return True
        except psycopg2.OperationalError as e:
            retries -= 1
            print("Postgres not ready:", str(e))
            print("Waiting 2 seconds...")
            time.sleep(2)
    raise Exception("Postgres not ready after 60 seconds!")


def run_migrations():
    wait_for_postgres()
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "localhost"),
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
    print("Migrations completed.")


if __name__ == "__main__":
    run_migrations()
